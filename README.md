# 🎮 Channel Capacity Calculator

**Information Theory - Task #2**

A retro-styled web application for calculating the capacity of a binary communication channel with noise, featuring both frontend (JavaScript) and backend (Python) implementations.

![Retro Style](https://img.shields.io/badge/style-retro%2090s-ff0066)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-3.0-green)

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

## 🚀 Quick Start

### Option 1: GitHub Pages (Frontend Only)

The frontend is deployed at:
**https://streamferow.github.io/information_theory_2/**

Works entirely in your browser with JavaScript calculations!

### Option 2: Local Python Backend

#### Installation

```bash
# Clone repository
git clone https://github.com/streamferow/information_theory_2.git
cd information_theory_2

# Install dependencies
pip install -r requirements.txt
```

#### Running CLI Calculator

```bash
python backend/calculator.py
```

#### Running API Server

```bash
python backend/api.py
```

The API will start on `http://localhost:5000`

## 🎯 Features

### Frontend (index.html)
- 🎨 **Retro 90s pixel art design** - CRT scanlines, pixel font, neon colors
- 📈 **Interactive charts** - Capacity vs flip probability visualization
- 🕹️ **Arcade-style UI** - Press Start 2P font, pixel-perfect borders
- ⚡ **Real-time calculation** - JavaScript computation engine
- 📱 **Responsive design** - Works on mobile and desktop

### Backend (Python)
- 🐍 **Pure Python calculations** - No JavaScript required
- 🔢 **Mathematical accuracy** - Shannon's formulas implemented correctly
- 🌐 **REST API** - Flask-based API for frontend integration
- 📊 **Chart data generation** - Backend-generated chart datasets
- ✅ **Input validation** - Comprehensive parameter checking

## 📡 API Endpoints

### POST `/api/calculate`
Calculate channel capacity

**Request:**
```json
{
  "N": 1000,
  "P": 0.01,
  "M": 0.05
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "H_X": 1.0,
    "H_Y_X": 0.3525,
    "H_Y": 0.9557,
    "I_XY": 0.6032,
    "capacity": 603.21
  }
}
```

### POST `/api/chart`
Generate chart data for visualization

**Request:**
```json
{
  "N": 1000,
  "M": 0.05
}
```

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
│   └── index.html          # Frontend (GitHub Pages)
├── backend/
│   ├── calculator.py       # Core calculation logic
│   └── api.py              # Flask REST API
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## 🔧 Development

### Frontend Development
The frontend is a single HTML file with embedded CSS and JavaScript. No build step required!

### Backend Development
```bash
# Run tests
python -m pytest backend/

# Run with debug mode
FLASK_DEBUG=1 python backend/api.py
```

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
- **Frontend**: Retro 90s pixel art design with HTML/CSS/JS
- **Backend**: Python implementation of Shannon's formulas
- **Font**: [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) by Google Fonts

---

⭐ **Star this repo if it helped you with your information theory studies!**
