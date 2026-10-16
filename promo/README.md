# Instagram brand reel

`dhaka-ad-reel.mp4` — 26 s, 1080×1920, 30 fps, H.264 + AAC, with a synthesized sound bed timed to the cuts.
`dhaka-ad-reel-no-music.mp4` — same picture, no audio, for adding a trending sound inside Instagram.
`cover.jpg` — suggested cover frame.

Rebuild:

```
python promo/prep_images.py <folder with full-size Drive photos in full/>   # 9:16 crops into promo/img
node promo/render.js promo/silent.mp4                                       # needs Playwright
python3 promo/soundtrack.py promo/soundtrack.wav
ffmpeg -i promo/silent.mp4 -i promo/soundtrack.wav -c:v copy -af loudnorm=I=-14:TP=-1.5 -c:a aac -b:a 192k -shortest promo/dhaka-ad-reel.mp4
```

The animation lives in `reel.html`; `seek(t)` draws any moment, so edits can be previewed with
`node promo/render.js x --preview 1.3,9.8,24`.
