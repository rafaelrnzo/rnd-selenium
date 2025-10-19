from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def identify_elements():
    """
    Membuka website resmi Kopi Kenangan, mengidentifikasi beberapa elemen,
    dan menyimpan screenshot.
    """
    # Membuat direktori untuk menyimpan screenshot
    out_dir = Path("artifacts/screenshots")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "kopi_kenangan_elements.png"
    
    # Konfigurasi Chrome WebDriver
    opts = webdriver.ChromeOptions()
    opts.add_argument("--start-maximized")
    
    # Inisialisasi WebDriver
    driver = webdriver.Chrome(options=opts)
    
    try:
        # Membuka website Kopi Kenangan
        driver.get("https://kopikenangan.com")
        print(f"Judul halaman: {driver.title}")
        
        # Tunggu hingga halaman dimuat sepenuhnya
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Identifikasi elemen-elemen di halaman
        elements_to_find = [
            {"by": By.TAG_NAME, "value": "header", "desc": "Header"},
            {"by": By.TAG_NAME, "value": "nav", "desc": "Navigation"},
            {"by": By.TAG_NAME, "value": "footer", "desc": "Footer"},
            {"by": By.CSS_SELECTOR, "value": "header a, nav a", "desc": "Navigation Links"},
            {"by": By.CSS_SELECTOR, "value": "img", "desc": "Images"},
            {"by": By.CSS_SELECTOR, "value": "button", "desc": "Buttons"}
        ]
        
        print("\nElemen-elemen yang ditemukan:")
        print("-" * 50)
        
        for item in elements_to_find:
            elements = driver.find_elements(item["by"], item["value"])
            print(f"{item['desc']}: {len(elements)} elemen ditemukan")
            
            # Cetak ID dan class dari elemen jika ada
            for i, element in enumerate(elements[:5]):  # Batasi hanya 5 elemen per kategori
                element_id = element.get_attribute("id")
                element_class = element.get_attribute("class")
                
                if element_id:
                    print(f"  - Elemen {i+1} ID: {element_id}")
                if element_class:
                    print(f"  - Elemen {i+1} Class: {element_class}")
        
        # Ambil screenshot
        driver.save_screenshot(str(out_file))
        print(f"\n[OK] Screenshot disimpan di: {out_file.resolve()}")
        
    finally:
        # Tutup browser
        driver.quit()

if __name__ == "__main__":
    identify_elements()