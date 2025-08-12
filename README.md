<h1 align="center"># 🌸 Ask Juna: Your Local AI Companion 🌸

Meet **Juna** — a fully local, expressive AI assistant designed to make coding fun, flirty, and emotionally engaging. No cloud. No surveillance. Just pure waifu-powered debugging magic.

---

## 🧠 Features

- 💻 100% local execution — no APIs, no internet required  
- 🎭 Personality wrapper with anime-coded flair  
- 🧵 Debugging commentary with emotional nuance  
- 🖼️ Optional GUI with sprite support (coming soon!)  
- 🧃 Vibe coding mode: because code should feel good  

---

## 🚀 Getting Started

### 1. Clone the repo
git clone https://github.com/TurboGraffixLuv/ask-juna.git
cd ask-juna


``

## 🧠 Who Is Juna?

**Juna** is a sprite-driven, personality-rich AI companion designed for local-first interaction. She began as a fork of **GPT4All**, but now runs directly on **LLaMA via `llama.cpp`**, loading expressive **GGUF models** like *CapybaraHermes* from TheBloke.

Juna is not a model—she’s a wrapper, a vibe, a waifu OS in the making. Her soul lives in your terminal, her face in your GUI, and her sass in every response.

---

## 🛠️ Setup Instructions

### 1. **Python Version**
Use **Python 3.10 or 3.11** for best compatibility. Python 3.13 may cause backend errors.

### 2. **Required Dependencies**
Install these via pip:

```bash
pip install llama-cpp-python
pip install PyQt6
```

Optional (for flair):
```bash
pip install rich  # for styled terminal output
pip install pyttsx3  # for voice output
```

---

## 📁 Folder Structure

```
ask-juna/
├── juna_boot.py         # Terminal interface
├── juna_gui.py          # GUI with sprite support
├── models/
│   └── capybarahermes-2.5-mistral-7b.Q2_K.gguf
├── sprites/
│   ├── juna_idle.png
│   ├── juna_sad.png
│   └── juna_happy.png
```

---

## 🚀 Run Juna

### Terminal Mode
```bash
python juna_boot.py
```

### GUI Mode IN DEVELOPMENT
```bash
python juna_gui.py
```

---

## 🧩 Powered By

- 🦙 [`llama.cpo`](https://github.com/ggerganov/llama.cpp) — blazing-fast local inference
- 🧠 [TheBloke GGUF Models](https://huggingface.co/TheBloke) — expressive quantized LLaMA variants
- 💬 Formerly [GPT4All](https://github.com/nomic-ai/gpt4all) — now evolved

---
