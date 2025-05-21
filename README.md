# 🔐 Quantum Random Password Generator

A futuristic password generator that uses **real quantum randomness** instead of pseudo-random numbers — ensuring ultra-secure, high-entropy passwords. Powered by the **ANU Quantum Random Number Generator** and built with a stylish **cyberpunk-themed web UI**.

![Cyberpunk Demo Screenshot](path/to/screenshot.png) <!-- Replace with actual screenshot path -->

---

## 🚀 Live Demo

👉 [Try it now](https://your-deployed-app-link.com)  
*(Powered by quantum randomness from ANU)*

---

## 🧠 Why Quantum?

Traditional password generators use pseudo-random number generators (PRNGs), which can be statistically predictable. This project fetches randomness from **real quantum phenomena** — true randomness from light particle behavior — via the [ANU Quantum Random Numbers API](https://qrng.anu.edu.au/).

---

## 🎯 Features

- ✅ **Quantum entropy** (ANU QRNG API)
- ✅ Selectable password strength: `Weak`, `Medium`, `Strong`
- ✅ Stylish **cyberpunk interface** with glitch effects
- ✅ One-click copy, regenerate, and optional password saving
- ✅ Built with Python and Streamlit (or Flask)

---

## 🛠️ Tech Stack

| Layer      | Tech Used                      |
|------------|--------------------------------|
| Backend    | Python 3, ANU QRNG API         |
| Web UI     | Streamlit / Flask              |
| Styling    | Custom CSS (Cyberpunk Theme)   |
| Hosting    | Streamlit Cloud / Render / Heroku |

---

## ⚙️ Installation (Local)

```bash
git clone https://github.com/your-username/quantum-password-generator.git
cd quantum-password-generator
pip install -r requirements.txt
streamlit run app.py  # or flask run if using Flask
