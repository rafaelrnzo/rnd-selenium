# 🚀 How to Run

## 1️⃣ Create and activate environment

```bash
conda create -n envAI python=3.11 -y
conda activate envAI
```

## 2️⃣ Install dependencies

```bash
pip install --upgrade pip
pip install selenium pytest
```

> 💡 *Tip:* Selenium 4.6+ automatically manages ChromeDriver, so you don’t need to download it manually.
## 3️⃣ Project structure

```
rndSelenium/
├── main.py
├── requirements.txt
├── tests/
│   └── test_kopi.py
└── artifacts/
    └── screenshots/
```

## 4️⃣ Run the Selenium script

```bash
python main.py
```

This script will:

* Launch **Google Chrome**
* Open **[https://kopikenangan.com](https://kopikenangan.com)**
* Verify the page title
* Capture a screenshot
* Save it to:
  `artifacts/screenshots/home.png`

**Expected output:**

```
[OK] Screenshot saved to: /absolute/path/artifacts/screenshots/home.png
```

## 5️⃣ Run automated test (optional)

```bash
pytest -q
```

**Expected result:**

```
1 passed in X.XXs
```

A screenshot from the test run will be stored at:

```
artifacts/screenshots/home_pytest.png
```

## ✅ Notes

* Ensure **Google Chrome** is installed on your system.
* No need to manually manage `chromedriver` — Selenium handles it automatically.
* For CI or headless environments, add this option before launching the browser:

```python
options.add_argument("--headless=new")
```
