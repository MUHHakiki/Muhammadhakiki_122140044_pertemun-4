# main.py

# Cara 1: Import seluruh modul
import math_operations

# Cara 2: Import fungsi tertentu saja
from math_operations import celsius_to_fahrenheit, celsius_to_kelvin

def main():
    print("=== Menggunakan Modul math_operations ===\n")
    
    # Persegi
    sisi = 5
    print(f"Luas Persegi (sisi={sisi}): {math_operations.luas_persegi(sisi)}")
    print(f"Keliling Persegi (sisi={sisi}): {math_operations.keliling_persegi(sisi)}\n")
    
    # Persegi Panjang
    panjang = 8
    lebar = 4
    print(f"Luas Persegi Panjang (p={panjang}, l={lebar}): {math_operations.luas_persegi_panjang(panjang, lebar)}")
    print(f"Keliling Persegi Panjang (p={panjang}, l={lebar}): {math_operations.keliling_persegi_panjang(panjang, lebar)}\n")
    
    # Lingkaran
    jari_jari = 7
    print(f"Luas Lingkaran (r={jari_jari}): {math_operations.luas_lingkaran(jari_jari)}")
    print(f"Keliling Lingkaran (r={jari_jari}): {math_operations.keliling_lingkaran(jari_jari)}\n")
    
    # Konversi Suhu
    celsius = 25
    print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F")
    print(f"{celsius}°C = {celsius_to_kelvin(celsius)}K\n")

    # Menampilkan konstanta
    print(f"Nilai PI dari modul: {math_operations.PI}")

if __name__ == "__main__":
    main()
