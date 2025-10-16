# main.py
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

def run():
    out_dir = Path("artifacts/screenshots")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "home.png"

    opts = webdriver.ChromeOptions()
    opts.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=opts) 
    try:
        driver.get("https://kopikenangan.com")
        assert "Kopi" in driver.title or "Kenangan" in driver.title

        _ = driver.find_elements(By.CSS_SELECTOR, "header a, nav a")

        driver.save_screenshot(str(out_file))
        print(f"[OK] Screenshot saved to: {out_file.resolve()}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run()
