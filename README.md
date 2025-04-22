

# 🔍 Google Dorking Tool

This Python tool helps you perform **manual Google dorking** to discover potentially sensitive or misconfigured resources exposed online for a given domain. It generates Google search queries based on common dork patterns and saves them with a timestamp.

---

## 🛠 Features

- Automatically generates multiple Google dorking queries
- Provides direct links to manually open in a browser
- Saves all results with a timestamp to `google_results.txt`
- User-friendly terminal interface with ASCII-styled banner

---

## 📦 Requirements

- Python 3.x
- [`rich`](https://pypi.org/project/rich/) for colored terminal output

Install `rich` using pip:

```bash
pip install rich
```

---

## 🚀 Usage

```bash
python google_dorker.py
```

Then enter the target domain when prompted (e.g., `example.com`).

---

## 📁 Output

Results will be saved in a file called:

```
google_results.txt
```

Each result includes:

- Timestamp
- Target domain
- Search query link (manually open in a browser)

---

## ⚠️ Disclaimer

This tool is intended for **educational and ethical use only**. Do not use it to target systems without proper authorization. Misuse of this tool may lead to legal consequences.

---

## 👨‍💻 Author

Made with 💻 by Surya Teja Devi
