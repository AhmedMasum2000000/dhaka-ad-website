"""Synthesize the reel's sound bed (no samples, no dependencies), timed to the cuts in reel.html."""
import math, random, struct, sys, wave

SR, DUR = 44100, 28.0
N = int(SR * DUR)
L = [0.0] * N
R = [0.0] * N
random.seed(7)

def add(t0, samples, gain=1.0, pan=0.0):
    i0 = int(t0 * SR)
    gl, gr = gain * (1 - max(0, pan)), gain * (1 + min(0, pan))
    for k, v in enumerate(samples):
        i = i0 + k
        if 0 <= i < N:
            L[i] += v * gl; R[i] += v * gr

def kick(dur=.45, f0=130, f1=42):
    out, ph = [], 0.0
    for k in range(int(dur * SR)):
        t = k / SR
        f = f1 + (f0 - f1) * math.exp(-t * 28)
        ph += 2 * math.pi * f / SR
        out.append(math.sin(ph) * math.exp(-t * 7.5) * (1 if t > .002 else t / .002))
    return out

def noise(dur, shape, cutoff=.15):
    out, y = [], 0.0
    n = int(dur * SR)
    for k in range(n):
        y += cutoff * (random.uniform(-1, 1) - y)
        out.append(y * shape(k / n))
    return out

def whoosh(dur=.35):  # swells into the cut
    return noise(dur, lambda p: p ** 2.2, .22)

def hat(dur=.06):
    return noise(dur, lambda p: (1 - p) ** 4, .9)

def tone(f, dur, decay=3.0, attack=.005):
    return [math.sin(2 * math.pi * f * k / SR) * min(1, k / SR / attack) * math.exp(-k / SR * decay) for k in range(int(dur * SR))]

def riser(dur):
    out, ph = [], 0.0
    n = int(dur * SR); y = 0.0
    for k in range(n):
        p = k / n
        ph += 2 * math.pi * (180 + 1100 * p * p) / SR
        y += .3 * (random.uniform(-1, 1) - y)
        out.append((math.sin(ph) * .5 + y * .6) * p ** 1.8)
    return out

# --- drone pad (A minor), ducked by section ---
def pad_gain(t):
    if t < 2.85: return .22 + .08 * t / 2.85
    if t < 3.4: return 0.0            # silence before the punchline lands
    if t < 8.55: return .26
    if t < 9.45: return .14
    if t < 21.5: return .3
    return .3 * max(0, 1 - (t - 26.6) / 1.4) if t > 26.6 else .3
for i in range(N):
    t = i / SR
    g = pad_gain(t)
    if g:
        trem = .8 + .2 * math.sin(2 * math.pi * 4 * t)
        v = (math.sin(2 * math.pi * 55 * t) + .55 * math.sin(2 * math.pi * 82.41 * t) + .35 * math.sin(2 * math.pi * 110 * t) + .12 * math.sin(2 * math.pi * 164.8 * t)) * g * trem * .5
        L[i] += v; R[i] += v

# --- hits on every cut and headline slam ---
cuts = [0, 1.45, 2.85, 4.3, 5.05, 5.8, 6.55, 7.3, 8.55, 9.45, 11.1, 12.35, 13.6, 14.85, 16.1, 19.7, 21.5]
for c in cuts:
    add(c, kick(), .9)
    if c > 0: add(c - .35, whoosh(), .35, pan=random.choice([-.4, .4]))
for s in [.28, .54, 1.72, 1.97, 3.12, 3.37, 7.55, 7.8, 8.8, 20.2, 20.68]:
    add(s, kick(.3, 160, 60), .5)
add(3.37, tone(73.4, 1.4, 1.8), .5)  # sub drop under "BRAND."
# riser into the logo, then a wide boom
add(8.55, riser(.9), .5)
add(9.45, kick(1.2, 110, 30), 1.0)
add(9.45, tone(220, 1.6, 2.2), .18, -.3); add(9.47, tone(329.6, 1.6, 2.2), .14, .3)
# counter ticks while numbers roll
for i in range(4):
    s = 11.1 + i * 1.25
    for k in range(10):
        add(s + .05 + k * .065, tone(1800 + 90 * k, .03, 60), .06)
# hi-hats driving the 360° montage
t = 16.1
while t < 19.7:
    add(t, hat(), .22, pan=.3); add(t + .225, hat(.04), .12, pan=-.3); t += .45
# phone CTA chime
for f, d in [(880, 0), (1318.5, .12)]:
    add(22.15 + d, tone(f, 1.2, 3.5), .12)

peak = max(max(abs(x) for x in L), max(abs(x) for x in R)) or 1
out = sys.argv[1] if len(sys.argv) > 1 else "soundtrack.wav"
with wave.open(out, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b"".join(struct.pack("<hh", int(a / peak * 30000), int(b / peak * 30000)) for a, b in zip(L, R)))
print("wrote", out)
