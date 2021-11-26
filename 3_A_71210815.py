def hitung_hapus() : 
    sen = input("Masukan Kalimat : ")
    isn  = int(input("Index Start : ")) + 1
    ist = int(input("Index Stop : ")) + 1
     
    hps = ist - isn + 1 
    hasil = (hps/len(sen)) * 100

    if isn > len(sen) or ist > len(sen) :
        return 0.0
    elif hasil < 0 :
        return 0.0
    else :
        return hasil 

print (hitung_hapus())