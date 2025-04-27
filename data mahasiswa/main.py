# Program Pengelolaan Data Nilai Mahasiswa

# Membuat list berisi data mahasiswa
mahasiswa = [
    {"nama": "bezzalel", "nim": "122140140", "nilai_uts": 85, "nilai_uas": 90, "nilai_tugas": 80},
    {"nama": "ikoy", "nim": "122140168", "nilai_uts": 75, "nilai_uas": 70, "nilai_tugas": 80},
    {"nama": "ical", "nim": "122140165", "nilai_uts": 60, "nilai_uas": 65, "nilai_tugas": 55},
    {"nama": "boy", "nim": "122140163", "nilai_uts": 50, "nilai_uas": 45, "nilai_tugas": 55},
    {"nama": "Eko", "nim": "122140001", "nilai_uts": 40, "nilai_uas": 35, "nilai_tugas": 45},
]

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(uts, uas, tugas):
    return 0.3 * uts + 0.4 * uas + 0.3 * tugas

# Fungsi untuk menentukan grade
def tentukan_grade(nilai_akhir):
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"

# Menghitung nilai akhir dan grade untuk setiap mahasiswa
for mhs in mahasiswa:
    nilai_akhir = hitung_nilai_akhir(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])
    mhs["nilai_akhir"] = round(nilai_akhir, 2)
    mhs["grade"] = tentukan_grade(nilai_akhir)

# Menampilkan data dalam format tabel
print("\nData Nilai Mahasiswa")
print("-" * 70)
print(f"{'Nama':<10} {'NIM':<10} {'UTS':<5} {'UAS':<5} {'Tugas':<7} {'Nilai Akhir':<12} {'Grade':<5}")
print("-" * 70)

for mhs in mahasiswa:
    print(f"{mhs['nama']:<10} {mhs['nim']:<10} {mhs['nilai_uts']:<5} {mhs['nilai_uas']:<5} {mhs['nilai_tugas']:<7} {mhs['nilai_akhir']:<12} {mhs['grade']:<5}")

print("-" * 70)

# Mencari mahasiswa dengan nilai tertinggi dan terendah
nilai_tertinggi = max(mahasiswa, key=lambda x: x["nilai_akhir"])
nilai_terendah = min(mahasiswa, key=lambda x: x["nilai_akhir"])

print(f"\nMahasiswa dengan nilai tertinggi: {nilai_tertinggi['nama']} ({nilai_tertinggi['nilai_akhir']})")
print(f"Mahasiswa dengan nilai terendah: {nilai_terendah['nama']} ({nilai_terendah['nilai_akhir']})")
