# Hybrid Dataset‑Driven CLI for PC Build Recommendations

#### Video Demo: <https://youtu.be/HeDKf8h6zsY>
#### Description:

This project is a **Hybrid Dataset‑Driven CLI for PC Build Recommendations** written in Python. It allows users to explore computer builds based on budget or custom configuration. The dataset contains **expanded categories** (Gaming, Office, Student,) with detailed parts, per‑component prices, and direct shopping links.

---

## Features
- **Budget Mode**  
  Enter a budget (₹20,000 – ₹60,000 in ₹5,000 intervals) and usage type to see builds that fit.  
  Each price point includes multiple consumer‑centric builds (Gaming, Office, Student), so users can choose based on their needs.

- **Custom Mode**  
  Guided, interactive flow that explains component choices step‑by‑step:  
  - CPU (Intel vs AMD, series options)  
  - GPU (NVIDIA vs AMD, entry/mid/high tiers)  
  - RAM (8GB/16GB/32GB)  
  - Storage (SSD/HDD/NVMe)  
  - PSU and Motherboard defaults provided  
  Prices and shopping links are fetched from a **custom JSON dataset** (`custom_parts.json`).

- **Expanded Dataset**  
  - `parts.json`: Budget builds for every price point and category.  
  - `custom_parts.json`: Component‑level catalog for Custom Mode.  
  Both include **ComponentPrices** and **Links**.

- **Table Output**  
  Builds are displayed in a neat table format, followed by per‑component prices and shopping links on new lines.

- **Save Option**  
  Users can save builds to `build.json` for later reference.

---

## Files
- **project.py**: Main program with CLI flow (Budget Mode + Custom Mode).
- **test_project.py**: Pytest tests (10 tests covering budget, custom, output, and saving).
- **parts.json**: Expanded dataset with multiple categories and builds for each price point.
- **custom_parts.json**: Component catalog for Custom Mode with prices and links.
- **requirements.txt**: Lists dependencies (`pytest`).
- **README.md**: Documentation describing the project.

---

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
