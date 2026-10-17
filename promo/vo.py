"""Voice-over for the reel: Piper neural TTS, one clip per line, placed on the timeline in reel.html.

Usage: [VO_LINES=lines.json VO_DUR=seconds] python promo/vo.py <voice.onnx> <out.wav> [length_scale]
Each line is sped up (max 1.3x) only if it would overrun the start of the next line.
"""
import array, subprocess, sys, tempfile, wave, os
from piper import PiperVoice, SynthesisConfig

SR = 48000
DUR = 28.0
# (start seconds, text) — timed to the cuts in reel.html
LINES = [
    (0.05, "Dhaka is stuck in traffic."),
    (1.50, "And everyone's looking up..."),
    (2.90, "at someone else's brand."),
    (4.33, "Every red light."),
    (5.08, "Every jam."),
    (5.83, "Every flyover."),
    (6.58, "Every terminal."),
    (7.35, "That's a captive audience."),
    (8.58, "Make it yours."),
    (9.60, "This is Dhaka Ad."),
    (11.15, "Forty four billboards."),
    (12.40, "Fifty-six digital screens."),
    (13.78, "Ten cities."),
    (14.90, "Half a million commuters, daily."),
    (16.45, "Billboards. The metro. Airports. Events. And print."),
    (19.72, "One team. One call. Every format."),
    (21.70, "Get your free location shortlist."),
    (23.60, "Call zero one eight four zero, eight six zero, two eight four."),
]

def main(model, out, scale=0.95):
    global LINES, DUR
    if os.environ.get("VO_LINES"):  # another reel: [[start, text], ...] in a JSON file
        import json
        LINES = [tuple(x) for x in json.load(open(os.environ["VO_LINES"]))]
        DUR = float(os.environ.get("VO_DUR", DUR))
    voice = PiperVoice.load(model)
    track = array.array("h", [0] * int(DUR * SR))
    tmp = tempfile.mkdtemp()
    for i, (start, text) in enumerate(LINES):
        raw, fit = os.path.join(tmp, f"{i}.wav"), os.path.join(tmp, f"{i}-fit.wav")
        with wave.open(raw, "wb") as w:
            voice.synthesize_wav(text, w, syn_config=SynthesisConfig(length_scale=scale))
        with wave.open(raw) as w:
            dur = w.getnframes() / w.getframerate()
        nxt = LINES[i + 1][0] if i + 1 < len(LINES) else DUR - .4
        room = nxt - start - .05
        tempo = min(1.3, max(1.0, dur / room))
        # trim Piper's edge silence, fit tempo, resample, light voice polish
        af = f"silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,atempo={tempo:.3f},highpass=f=90,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,aresample={SR}"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", af, "-ac", "1", "-c:a", "pcm_s16le", fit], check=True)
        with wave.open(fit) as w:
            pcm = array.array("h", w.readframes(w.getnframes()))
        i0 = int(start * SR)
        for k, v in enumerate(pcm):
            if i0 + k < len(track):
                track[i0 + k] = max(-32768, min(32767, track[i0 + k] + v))
        print(f"{start:5.2f}s  {len(pcm)/SR:4.2f}s (x{tempo:.2f}, room {room:.2f}s)  {text}")
    with wave.open(out, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(track.tobytes())

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 0.95)
