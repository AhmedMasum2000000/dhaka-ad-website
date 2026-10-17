# Dhaka AD

Public static website: https://ahmedmasum2000000.github.io/dhaka-ad-website/

360° outdoor advertising agency site: LED screens, static, expressway, tri-vision and neon billboards, metro, airport, events, activations, inserts, printing, guides and FAQs. Every page is built to send visitors to one action: calling 01840 860 284.

Rates are deliberately not published. Pages explain how pricing works and invite a call for current rates and availability.

## Rebuilding generated pages

The homepage, the `static-billboards/` directory, the newer service pages, `guides/` and `industries/` are generated, and every page's navigation, footer, call rail, FAQ schema, `sitemap.xml`, `llms.txt` and `robots.txt` are refreshed by the same script:

```bash
pip install pillow
python scripts/build/build.py
```

- `scripts/build/data_static.py` – billboard inventory (from the static billboard proposal) and area descriptions
- `scripts/build/data_services.py`, `data_guides.py` – service, guide and industry copy
- `scripts/build/gen_home.py` – homepage story, finder data and FAQs
- `scripts/build/postprocess.py` – sitewide chrome, cross-links, schema, sitemap and `llms.txt`

Images: `assets/field/` (team photography, EXIF/GPS removed) and `assets/billboards/` (placement photos from the proposal), each as WebP at two sizes.
