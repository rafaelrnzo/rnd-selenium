````markdown
# ☕ Selenium WebDriver Test – Kopi Kenangan

## 🚀 How to Run

### 1. Create and activate environment
```bash
conda create -n envAI python=3.11 -y
conda activate envAI
````

### 2. Install dependencies

```bash
pip install --upgrade pip
pip install selenium pytest
```

### 3. Project structure

```
rndSelenium/
├─ main.py
├─ requirements.txt
├─ tests/
│  └─ test_kopi.py
└─ artifacts/
   └─ screenshots/
```

### 4. Run the Selenium script

```bash
python main.py
```

This will:

* Launch Chrome and open **[https://kopikenangan.com](https://kopikenangan.com)**
* Verify the page title
* Capture a screenshot
* Save it to `artifacts/screenshots/home.png`

Expected output:

```
[OK] Screenshot saved to: /absolute/path/artifacts/screenshots/home.png
```

### 5. Run automated test (optional)

```bash
pytest -q
```

Expected result:

```
1 passed in X.XXs
```

Screenshot from the test will be stored at:

```
artifacts/screenshots/home_pytest.png
```

---

✅ **Notes**

* Make sure **Google Chrome** is installed.
* Selenium 4.6+ automatically manages the ChromeDriver, no manual download required.
* For server or CI environments, use headless mode:

```python
options.add_argument("--headless=new")
```

```
```
