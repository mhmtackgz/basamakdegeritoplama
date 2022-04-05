import  random

rand=(random.randint(1000,10000))
print("Girilen Sayı:",rand)
toplam=0
for i  in range(4):
    toplam+=rand%10
    rand=int(rand/10)
    print(rand)
print("Basamak Değerleri Toplamı :" ,toplam)
