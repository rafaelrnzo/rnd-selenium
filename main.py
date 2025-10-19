# main.py
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

def run():
    # Membuat folder untuk menyimpan hasil screenshot
    out_dir = Path("artifacts/screenshots")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "home.png"

    # Mengatur opsi browser Chrome
    opts = webdriver.ChromeOptions()
    opts.add_argument("--start-maximized")  # buka jendela Chrome dengan ukuran penuh

    # Inisialisasi WebDriver (akan membuka Chrome otomatis)
    driver = webdriver.Chrome(options=opts) 
    try:
        # Membuka situs Kopi Kenangan
        driver.get("https://kopikenangan.com")

        # Verifikasi bahwa judul halaman mengandung kata 'Kopi' atau 'Kenangan'
        assert "Kopi" in driver.title or "Kenangan" in driver.title

        # Mencari semua elemen link (<a>) di header atau navigasi halaman
        _ = driver.find_elements(By.CSS_SELECTOR, "header a, nav a")

        # Mengambil screenshot halaman dan menyimpannya ke folder artifacts/screenshots
        driver.save_screenshot(str(out_file))
        print(f"[OK] Screenshot saved to: {out_file.resolve()}")

    finally:
        # Menutup browser setelah proses selesai
        driver.quit()

# Menjalankan fungsi utama jika file ini dijalankan langsung
if __name__ == "__main__":
    run()
