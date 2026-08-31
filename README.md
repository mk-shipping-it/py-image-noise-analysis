# Image Noise Analysis

Python toolkit for estimating and comparing noise between 2K and 4K image crops via Gaussian blur differencing. Ships with sample crops and a one-command matplotlib demo.

## What it does

Estimates noise by blurring a grayscale crop, subtracting from the original, and measuring the standard deviation of the difference. Designed to compare noise characteristics between resolutions — e.g., `your_2k_crop.jpg` vs `your_4k_crop.jpg` — and display both with per-image metrics side-by-side.

## Features

- **Gaussian blur differencing** — blur, subtract, measure stddev for noise score
- **2K vs 4K comparison** — side-by-side matplotlib view with noise levels in titles
- **Zero-config demo** — sample crops included, works out-of-box

## Quick Start

```bash
pip install -r requirements.txt
python compare_two_images_noise.py
```

Edit `image_2k_path` / `image_4k_path` at the top of `compare_two_images_noise.py` to use your own images, or keep the defaults.

## Stack

Python 3, OpenCV (`cv2.GaussianBlur`), Pillow, NumPy, matplotlib

## Structure

```
image-noise-analysis/
├── compare_two_images_noise.py — main script (grayscale load → blur → diff → stddev → plot)
├── requirements.txt — numpy, opencv-python, Pillow, matplotlib
├── your_2k_crop.jpg / your_4k_crop.jpg — sample inputs
├── .github/ISSUE_TEMPLATE/ — bug/feature templates
└── CODE_OF_CONDUCT.md / CONTRIBUTING.md / SECURITY.md
```

## License

Apache 2.0 — see `LICENSE` (Copyright 2026 Mayukh Karmakar). Originally `FalloutGhoulBusta`.
