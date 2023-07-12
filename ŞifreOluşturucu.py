import random
semboller = "+-/!'^^%&=?_#$qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ."
uzunluk = input("Oluşturmak İstediğiniz Şifrenin Uzunluğunu Giriniz: ")
uzunluk = int(uzunluk)
sifre = ""
for i in range(uzunluk):
    sifre += random.choice(semboller)
print(sifre)    
