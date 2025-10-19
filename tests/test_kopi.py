from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_open_kopikenangan_and_capture(tmp_path):
    out_dir = Path("artifacts/screenshots")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "home_pytest.png"

    opts = webdriver.ChromeOptions()
    # opts.add_argument("--headless=new")
    driver = webdriver.Chrome(options=opts)
    try:
        wait = WebDriverWait(driver, 10)
        driver.get("https://kopikenangan.com")
        wait.until(EC.title_contains("Kopi"))
        assert "Kopi" in driver.title or "Kenangan" in driver.title

        nav_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "header a, nav a")))
        assert len(nav_links) > 0

        driver.save_screenshot(str(out_file))
        assert out_file.exists()
    finally:
        driver.quit()
