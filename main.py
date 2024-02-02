import random


harfler = "abcdefghijklnopqrstuvwxyz"
buyukharfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayilar = "1234567890"
semboller = "+-/*!&$#?=@"

uzunluk = int(input("şifreniz kaç haneli olsun?"))

sifre=""


for i in range(uzunluk):  



    
    sifre += random.choice(harfler)  



    
print(sifre)
