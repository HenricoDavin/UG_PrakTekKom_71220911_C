print ("===========================")
print ("Operasi Matematika")
print (" 1. Jumlah [+]")
print (" 2. Kurang [-]")
print (" 3. Kali   [*]")
print (" 4. Bagi   [/]")
print ("===========================")

kalkulasi = input("Pilih Operasi (1/2/3/4): ")
print ("===========================")

bilpertama = int (input("Masukkan bilangan pertama: "))
bilkedua = int (input("Masukkan bilangan kedua: "))

def penjumlahan(penjumlahan):
    penjumlahan = bilpertama + bilkedua
    return penjumlahan

def pengurangan(pengurangan):
    pengurangan = bilpertama - bilkedua
    return pengurangan

def perkalian(perkalian):
    perkalian = bilpertama * bilkedua
    return perkalian

def pembagian(pembagian):
    pembagian = bilpertama / bilkedua
    return pembagian

if kalkulasi == ("1"):
    print ("Hasil operasi dari", bilpertama, ("+"), bilkedua, ("="), penjumlahan(penjumlahan))

elif kalkulasi == ("2"):
    print ("Hasil operasi dari", bilpertama, ("-"), bilkedua, ("="), pengurangan(pengurangan))

elif kalkulasi == ("3"):
    print ("Hasil operasi dari", bilpertama, ("*"), bilkedua, ("="), perkalian(perkalian))

elif kalkulasi == ("4"):
    print ("Hasil operasi dari", bilpertama, ("/"), bilkedua, ("="), pembagian(pembagian))
