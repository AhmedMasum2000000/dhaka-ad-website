# Instagram brand reel

`dhaka-ad-reel-voiceover.mp4` — 28 s, 1080×1920, 30 fps, H.264 + AAC: voice-over plus the music bed, ducked under the voice.
`dhaka-ad-reel.mp4` — same picture with the music bed only.
`dhaka-ad-reel-no-music.mp4` — same picture, no audio, for adding a trending sound inside Instagram.
`cover.jpg` — suggested cover frame.
`voiceover.wav` — the voice track on its own (Piper TTS, en_US-ryan-high), lined up to the video.

Rebuild:

```
python promo/prep_images.py <folder with full-size Drive photos in full/>   # 9:16 crops into promo/img
node promo/render.js promo/silent.mp4                                       # needs Playwright
python3 promo/soundtrack.py promo/soundtrack.wav
python promo/vo.py en_US-ryan-high.onnx promo/voiceover.wav   # pip install piper-tts; voice from huggingface.co/rhasspy/piper-voices
ffmpeg -i promo/silent.mp4 -i promo/soundtrack.wav -c:v copy -af loudnorm=I=-14:TP=-1.5 -c:a aac -b:a 192k -shortest promo/dhaka-ad-reel.mp4
ffmpeg -i promo/silent.mp4 -i promo/soundtrack.wav -i promo/voiceover.wav -filter_complex "[1:a]aresample=48000,volume=0.9[m];[2:a]aresample=48000,pan=stereo|c0=c0|c1=c0,asplit=2[v1][v2];[m][v1]sidechaincompress=threshold=0.015:ratio=12:attack=8:release=350[d];[d][v2]amix=inputs=2:normalize=0:weights=0.75 1.5,loudnorm=I=-14:TP=-1.5[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest promo/dhaka-ad-reel-voiceover.mp4
```

Voice lines and their start times are in `vo.py`; a line is sped up (max 1.3x) only if it would run into the next.

The animation lives in `reel.html`; `seek(t)` draws any moment, so edits can be previewed with
`node promo/render.js x --preview 1.3,9.8,24`.
