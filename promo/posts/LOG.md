# Instagram posting log

The plan, calendar and status of every post live in the "Dhaka AD Instagram Growth Plan" doc. This file mirrors what has gone out and what is ready.

| Date | Format | Service | Status | Files |
| --- | --- | --- | --- | --- |
| Fri 16 Oct 2026 | Reel (brand intro, voice-over) | All services | Posted | `promo/dhaka-ad-reel-voiceover.mp4` |
| Sat 17 Oct 2026 | Carousel, 9 slides | LED billboards | Ready | `2026-10-17-led-carousel/slide-01..09.png`, `caption.txt` |
| Sun 18 Oct 2026 | Single image | Metro rail advertising | Ready | `2026-10-18-metro-post/post.png`, `caption.txt` |
| Mon 19 Oct 2026 | Reel, 25 s, voice-over | Billboards and artwork | Ready | `2026-10-19-three-second-reel/three-second-test-reel.mp4`, `cover.jpg`, `caption.txt` |
| Tue 20 Oct 2026 | Stories | LED screen rental | To film | `2026-10-20-led-rental-stories/caption.txt` |
| Wed 21 Oct 2026 | Reel | Event management | To film | `2026-10-21-event-reel/caption.txt` |
| Thu 22 Oct 2026 | Carousel | Airport advertising | To design | `2026-10-22-airport-carousel/caption.txt` |
| Fri 23 Oct 2026 | Reel | Expressway billboards | To film | `2026-10-23-expressway-reel/caption.txt` |

Rebuild: carousels and single posts with `node promo/posts/render_slides.js <post dir>`; reels with
`REEL_HTML=<post dir>/reel.html node promo/render.js <out.mp4>`, voice with `VO_LINES=<post dir>/vo_lines.json VO_DUR=<s> python promo/vo.py <voice.onnx> <out.wav>`, then mix as in `promo/README.md`.
