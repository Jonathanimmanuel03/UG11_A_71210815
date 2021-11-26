def balik(string): 
    string = "".join(reversed(string)) 
    return string 

def ambil() :
    print("abcde")

def ambil2() :
    print("w")

s = "bcd"
o = "er" 


print (balik(s)) 
ambil()
print (balik(o))
ambil2()

#print(balik("abcdefg",2,4,True))
#print(ambil("abcdefg",1,5,False))
#print(balik("Qwerty",3,4,True))
#print(ambil("Qwerty",2,2,False)