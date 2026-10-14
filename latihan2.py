nama = input("Masukkan nama :")
npm = int(input("Masukkan NPM :"))
umur = int(input("Masukkan umur :"))
tinggi = float(input("Masukkan tinggi :"))
prodi = input("Masukkan prodi :")

tugas = float(input("Masukkan nilai tugas :"))
uts = float(input("Masukkan nilai UTS :"))
uas = float(input("Masukkan nilai UAS :"))

nilai_akhir = (tugas + uts + uas) / 3

print("\n---Hasil ---")
print("Nama:", nama)
print("NPM:", npm)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Prodi:", prodi)
print("Nilai Tugas:", tugas)
print("Nilai UTS:", uts)
print("Nilai UAS:", uas)
print("Nilai Akhir:", nilai_akhir)

if nilai_akhir >= 75:
    print("Status: Anda Lulus")
else:
    print("Status: Anda Tidak Lulus")