# 🎮 Channel Capacity Calculator

**Information Theory - Task #2**

A retro-styled web application for calculating the capacity of a binary communication channel with noise. Works entirely in your browser!

![Retro Style](https://img.shields.io/badge/style-retro%2090s-ff0066)
![Pure JS](https://img.shields.io/badge/pure-javascript-yellow)
![GitHub Pages](https://img.shields.io/badge/deployed-github%20pages-blue)

## 🌐 Live Demo

**https://streamferow.github.io/information_theory_2/**

No installation required! Open in any browser and start calculating.

## 📊 About

This application calculates the **Shannon channel capacity** for a binary communication channel with two types of errors:

- **P (Flip probability)**: Probability that bit 0 becomes 1 or vice versa
- **M (Erasure probability)**: Probability that signal becomes unrecognizable

### Formula

```
C = N × I(X;Y) = N × [H(Y) - H(Y|X)]

Where:
- C = Channel capacity (bits/sec)
- N = Signal transmission rate (signals/sec)
- I(X;Y) = Mutual information
- H(Y) = Receiver entropy
- H(Y|X) = Conditional entropy
```

## 🚀 How to Use

### Online (GitHub Pages)
Simply open: **https://streamferow.github.io/information_theory_2/**

### Local (No Internet Required)
```bash
# Clone repository
git clone https://github.com/streamferow/information_theory_2.git

# Open the file in browser
cd information_theory_2/docs
open index.html  # or double-click the file
```

## 🎯 Features

- 🎨 **Retro 90s pixel art design** - CRT scanlines, pixel font, neon colors
- 📈 **Interactive charts** - Capacity vs flip probability visualization
- 🕹️ **Arcade-style UI** - Press Start 2P font, pixel-perfect borders
- ⚡ **Real-time calculation** - Pure JavaScript computation engine
- 📱 **Responsive design** - Works on mobile and desktop
- 🔢 **Shannon's formulas** - Accurate mathematical calculations
- 📊 **Visual channel model** - ASCII diagram of the communication channel

## 🎨 Design Inspiration

The UI is inspired by classic 90s video games:
- **Super Mario Bros** - Platformer aesthetics
- **Sonic the Hedgehog** - Bright neon colors
- **Arcade machines** - CRT scanline effects, pixel fonts
- **8-bit era** - Limited color palette, sprite-like elements

## 📁 Project Structure

```
.
├── docs/
│   └── index.html          # Single-file web app (GitHub Pages)
├── backend/
│   ├── calculator.py       # Optional: Python calculations (CLI)
│   └── api.py              # Optional: Flask API
├── requirements.txt        # Python dependencies (optional)
└── README.md               # This file
```

## 🐍 Optional Python Backend

For those who prefer Python calculations:

```bash
# Install dependencies
pip install -r requirements.txt

# Run CLI calculator
python backend/calculator.py

# Run API server (if needed for other integrations)
python backend/api.py
```

**Note:** Python backend is completely optional. The web app works without it.

## 📖 Mathematical Background

### Channel Model

For a binary symmetric channel with erasures:

```
Transmitter                    Receiver
   ┌───┐                        ┌───┐
   │ 0 │──┬────────────────────→│ 0 │  prob: 1-P-M
   └───┘  │                      └───┘
          │    ┌──────────┐
          └───→│  NOISE   │←───┐
          │    │ CHANNEL  │    │
   ┌───┐  │    └──────────┘    └──┐┌───┐
   │ 1 │──┤                       ││ 1 │  prob: 1-P-M
   └───┘  │                       │└───┘
          └─────────────────────→[ ? ]  prob: M (erasure)
          └─────────────────────→ ERR   prob: P (flip)
```

### Entropy Calculations

**Conditional entropy H(Y|X):**
```
H(Y|X) = -[(1-P-M)·log₂(1-P-M) + P·log₂(P) + M·log₂(M)]
```

**Receiver entropy H(Y):**
```
P(Y=0) = P(Y=1) = 0.5·(1-M)
P(Y=?) = M
```

**Channel capacity:**
```
C = N × [H(Y) - H(Y|X)]
```

## 📝 License

MIT License - feel free to use for educational purposes!

## 🏆 Credits

Created for Information Theory course - Task #2
- **Design**: Retro 90s pixel art style
- **Font**: [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) by Google Fonts
- **Calculations**: Shannon's Information Theory formulas

---

⭐ **Star this repo if it helped you with your information theory studies!**
