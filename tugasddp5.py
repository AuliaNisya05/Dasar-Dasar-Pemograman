a = ["B 1234 abc","mio","50cc","merah"]
print (a)

a.append("3.000.000")
print (a)
a.append("2")
print (a)
a.insert(3,"Honda")
print (a)
a.insert(4,"sepeda motor")
print (a)

ket = '''Menghitung luas bangun datar
masukan pilihan:
1. Luas persegi
2. Luas lingkaran
3. Luas segitiga
'''

Pilihan = input (ket)
match Pilihan:
    case "1":
        print ("Kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("masukkan sisi"))
        luasP = sisi * sisi
        print ("luas persegi yang sisiya", sisi,"adalah", luasP)
    case "2":
        print ("Kamu memilih 1 untuk menghitung luas lingkaran")
        jari2 = float(input("masukkan jari2"))
        luasL = 3,14 * jari2 * jari2
        print ("luas lingkaran yang jari2nya", jari2, "adalah", int(luasL))
    case "3":
        print ("Kamu memilih 1 untuk menghitung luas segitiga")
        alas = int(input("masukkan alas"))
        tinggi = int(input("masukkan tinggi"))
        luasS = o,5 * alas * tinggi
        print ("luas segitiga yang alasnya", alas, "dan tingginya", tinggi, "adalah", int(luasS))
    case _:
        print("salah masukkan pilihan")
    