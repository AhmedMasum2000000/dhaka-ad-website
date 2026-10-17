"""Synthesized music bed for a reel, driven by a sound.json next to the reel (no samples, no licences).

Usage: python promo/posts/beat.py <post dir> <out.wav>
sound.json keys (times in seconds):
  dur        length of the track
  bpm        tempo of the drum groove
  groove     [[start, end, level], ...] four-on-the-floor kick, off-beat hats and a bass pulse
  pad        [[start, end, level], ...] low drone under everything
  hits       impact times (kick + noise swell into it)
  risers     [[start, end], ...] noise sweeps that build into a drop
  ticks      clock ticks for countdowns
  chimes     two-note bell for reveals
  fade       [start, end] master fade out
"""
import json, os, sys
import numpy as np

SR = 44100
cfg = json.load(open(os.path.join(sys.argv[1], "sound.json")))
N = int(SR * cfg["dur"]); L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(7)
t_all = np.arange(N) / SR


def add(t0, smp, g=1.0, pan=0.0):
    i0 = int(t0 * SR); i1 = min(N, i0 + len(smp))
    if i1 <= i0 or i0 < 0: return
    s = smp[: i1 - i0] * g
    L[i0:i1] += s * (1 - max(0, pan)); R[i0:i1] += s * (1 + min(0, pan))


def kick(d=.42, f0=140, f1=45):
    t = np.arange(int(d * SR)) / SR
    return np.sin(2 * np.pi * np.cumsum(f1 + (f0 - f1) * np.exp(-t * 30)) / SR) * np.exp(-t * 8)


def noise(d, shape, smooth=.25):
    x = rng.uniform(-1, 1, int(d * SR)); y = np.zeros_like(x); acc = 0.0
    for i, v in enumerate(x): acc += smooth * (v - acc); y[i] = acc
    return y * shape(np.linspace(0, 1, len(x)))


def tone(f, d, decay=3.0):
    t = np.arange(int(d * SR)) / SR
    return np.sin(2 * np.pi * f * t) * np.minimum(1, t / .004) * np.exp(-t * decay)


def level(spans, t):
    g = np.zeros_like(t)
    for a, b, v in spans: g[(t >= a) & (t < b)] = v
    return g


beat = 60 / cfg.get("bpm", 120)
HAT = noise(.06, lambda p: (1 - p) ** 6, .95)
for a, b, v in cfg.get("groove", []):
    k = 0
    while a + k * beat < b - 1e-6:
        t0 = a + k * beat
        add(t0, kick(), .85 * v)
        add(t0 + beat / 2, HAT, .22 * v, pan=.3 if k % 2 else -.3)
        k += 1
    m = (t_all >= a) & (t_all < b)
    ph = ((t_all - a) % beat) / beat
    bass = np.sin(2 * np.pi * 55 * t_all) * np.exp(-ph * 5) * v * .35  # pumping A1 under each beat
    L[m] += bass[m]; R[m] += bass[m]
g = level(cfg.get("pad", []), t_all)
pad = (np.sin(2 * np.pi * 55 * t_all) + .5 * np.sin(2 * np.pi * 82.41 * t_all) + .3 * np.sin(2 * np.pi * 110 * t_all)) * .3 * g * (.8 + .2 * np.sin(2 * np.pi * .5 * t_all))
L += pad; R += pad
for h in cfg.get("hits", []):
    add(h, kick(.6, 120, 38), 1.0)
    if h > .3: add(h - .3, noise(.3, lambda p: p ** 2.2), .35, pan=-.3)
for a, b in cfg.get("risers", []):
    add(a, noise(b - a, lambda p: p ** 2.5, .5), .45)
for s in cfg.get("ticks", []):
    add(s, tone(1600, .12, 30), .4); add(s, noise(.05, lambda p: (1 - p) ** 4, .9), .25)
for s in cfg.get("chimes", []):
    add(s, tone(1046.5, 1.2, 3.2), .22); add(s + .12, tone(1568, 1.2, 3.2), .17)
if "fade" in cfg:
    a, b = cfg["fade"]; f = np.clip(1 - (t_all - a) / (b - a), 0, 1); L *= f; R *= f
peak = max(np.abs(L).max(), np.abs(R).max()) or 1
out = (np.stack([L, R], 1) / peak * 30000).astype("<i2")
import wave
with wave.open(sys.argv[2], "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(out.tobytes())
print("wrote", sys.argv[2])
