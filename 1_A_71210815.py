def penambahan(a,b):
    return a + b

def pengurangan(a,b):
    return a - b

def perkalian(a,b):
    return a * b

def pembagian(a,b):
    return a / b

def perpangkatan(a,b):
    return a ** b

def calculator():
    print("======== Calculator Sederhana ========")
    print("1. Penambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Perpangkatan")
    print("")

calculator()

pilih = int(input('Masukan Pilihan : '))
A = int(input('Masukan Bilangan 1 : '))
B = int(input('Masukan Bilangan 2 : '))

if pilih == 1 :
    print("Hasilnya : ",penambahan(A,B))
elif pilih == 2 :
    print("Hasilnya : ",pengurangan(A,B))
elif pilih == 3 :
    print("Hasilnya : ",perkalian(A,B))
elif pilih == 4 :
    print("Hasilnya : ",pembagian(A,B))
elif pilih  == 5 :
    print("Hasilnya : ",perpangkatan(A,B))
else:
    print("Hasilnya : Maaf Input Operasi antara 1-5 ")