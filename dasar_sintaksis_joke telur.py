"""
semua sintaksis dasa bahasa pemograman terdiri dari:
1. Sekuensial : langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# sekuensial
print('ibu berkata,"pergi ke toko"')
print('Budi menjawab,"Baik, apa yang harus saya lakukan di toko?"')
print('ibu menjawab,"beli 1 botol susu dan jika ada telor beli 6"')
print('maka Budi berangkat ke toko')
print('Dan mulai berbelanja')

# Percabangan
jumlah_botol_susu = 22
jumlah_telur = 77

print(f"jumlah botol susu {jumlah_botol_susu} botol",)
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu >0:
    print("budi mengecek harganya, dan ternyata uang nya cukup")
    if jumlah_telur <6:
        print("budi membeli 1 botol susu")
    else:
        print("Budi membeli 1 botol susu dan 6 butir telur")

else:
    print("budi tidak jadi membeli 1 botol susu")

print("budi pulang ke rumah")



