from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def take_element_screenshot(driver, element, filename):
    """
    Mengambil screenshot dari elemen tertentu
    """
    # Scroll ke elemen
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.5)  # Tunggu sebentar agar elemen terlihat jelas
    
    # Periksa ukuran elemen
    size = element.size
    if size['width'] <= 0 or size['height'] <= 0:
        raise ValueError(f"Elemen memiliki ukuran tidak valid: {size}")
    
    # Ambil screenshot elemen
    element.screenshot(filename)
    return os.path.abspath(filename)

def identify_elements():
    """
    Membuka website resmi Kopi Kenangan, mengidentifikasi beberapa elemen,
    dan menyimpan screenshot untuk setiap elemen.
    """
    # Membuat direktori untuk menyimpan screenshot
    out_dir = Path("artifacts/screenshots")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Membuat direktori khusus untuk screenshot elemen
    elements_dir = out_dir / "elements"
    elements_dir.mkdir(parents=True, exist_ok=True)
    
    # Screenshot halaman utuh
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
            
            # Cetak ID dan class dari elemen dan ambil screenshot
            for i, element in enumerate(elements[:5]):  # Batasi hanya 5 elemen per kategori
                element_id = element.get_attribute("id") or f"no-id-{i+1}"
                element_class = element.get_attribute("class")
                
                # Buat nama file yang unik untuk screenshot
                element_type = item["desc"].lower().replace(" ", "_")
                screenshot_filename = f"{element_type}_{element_id}_{i+1}.png"
                screenshot_path = elements_dir / screenshot_filename
                
                try:
                    # Ambil screenshot elemen
                    screenshot_file = take_element_screenshot(driver, element, str(screenshot_path))
                    
                    # Tampilkan informasi elemen
                    print(f"  - Elemen {i+1} ({element_type}):")
                    if element_id and element_id != f"no-id-{i+1}":
                        print(f"    ID: {element_id}")
                    if element_class:
                        print(f"    Class: {element_class}")
                    print(f"    Screenshot: {screenshot_path}")
                except Exception as e:
                    print(f"    Tidak dapat mengambil screenshot: {str(e)}")
        
        # Ambil screenshot halaman penuh
        driver.save_screenshot(str(out_file))
        print(f"\n[OK] Screenshot halaman penuh disimpan di: {out_file.resolve()}")
        print(f"[OK] Screenshot elemen-elemen disimpan di: {elements_dir.resolve()}")
        
    finally:
        # Tutup browser
        driver.quit()

if __name__ == "__main__":
    identify_elements()