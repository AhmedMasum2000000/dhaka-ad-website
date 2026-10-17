"""Sound bed for the 3-second billboard test reel (synthesized, no samples)."""
import math, os, random, struct, sys, wave
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
SR, DUR = 44100, 25.0
N = int(SR * DUR); L = [0.0] * N; R = [0.0] * N; random.seed(11)
def add(t0, smp, g=1.0, pan=0.0):
    i0 = int(t0 * SR); gl, gr = g * (1 - max(0, pan)), g * (1 + min(0, pan))
    for k, v in enumerate(smp):
        i = i0 + k
        if 0 <= i < N: L[i] += v * gl; R[i] += v * gr
def kick(d=.45, f0=130, f1=42):
    out, ph = [], 0.0
    for k in range(int(d * SR)):
        t = k / SR; ph += 2 * math.pi * (f1 + (f0 - f1) * math.exp(-t * 28)) / SR; out.append(math.sin(ph) * math.exp(-t * 7.5))
    return out
def noise(d, shape, c=.2):
    out, y, n = [], 0.0, int(d * SR)
    for k in range(n): y += c * (random.uniform(-1, 1) - y); out.append(y * shape(k / n))
    return out
def tone(f, d, decay=3.0): return [math.sin(2 * math.pi * f * k / SR) * min(1, k / SR / .004) * math.exp(-k / SR * decay) for k in range(int(d * SR))]
def buzz(d=.5): return [(1 if math.sin(2 * math.pi * 110 * k / SR) > 0 else -1) * .5 * math.exp(-k / SR * 5) for k in range(int(d * SR))]
# low pulse bed, ducked during the countdowns so the ticks land
for i in range(N):
    t = i / SR
    g = .05 if (2.8 <= t < 5.8 or 8.6 <= t < 11.6) else .22
    if t > 23.6: g *= max(0, 1 - (t - 23.6) / 1.4)
    v = (math.sin(2 * math.pi * 55 * t) + .5 * math.sin(2 * math.pi * 82.41 * t) + .3 * math.sin(2 * math.pi * 110 * t)) * g * (.75 + .25 * math.sin(2 * math.pi * 2 * t)) * .5
    L[i] += v; R[i] += v
for c in [0, 2.2, 5.8, 7.6, 11.6, 13.4, 15.8, 18.2]:
    add(c, kick(), .9)
    if c: add(c - .3, noise(.3, lambda p: p ** 2.2), .3, pan=random.choice([-.4, .4]))
for s in [2.8, 3.8, 4.8, 8.6, 9.6, 10.6]:  # countdown ticks
    add(s, tone(1600, .12, 30), .35); add(s, noise(.05, lambda p: (1 - p) ** 4, .9), .25)
for s in [5.8, 11.6]: add(s, buzz(), .25)       # time's up
add(16.2, tone(1046.5, 1.2, 3.2), .18); add(16.32, tone(1568, 1.2, 3.2), .14)  # the reveal
add(18.8, tone(880, 1.0, 3.5), .1); add(18.92, tone(1318.5, 1.0, 3.5), .08)    # CTA
peak = max(max(abs(x) for x in L), max(abs(x) for x in R)) or 1
with wave.open(sys.argv[1], "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b"".join(struct.pack("<hh", int(a / peak * 30000), int(b / peak * 30000)) for a, b in zip(L, R)))
print("wrote", sys.argv[1])
