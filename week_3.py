
#######################Ödev1###########################

sayi3 = 4.5
sayi4=6
string1 = "True"
string2 = "5"

print(int(sayi3))
print(float(sayi4))
a=bool(string1)
print(type(a))

print(type(int(string2)))


#############################Ödev2############################

Ela = 22
Ali =26
Lale = 27

if (Ali > Lale and Ali > Ela):

    if (Lale > Ela ):
        print("Ali grubun en büyüğüdür ve Ela en küçüğüdür. Lale Ela'dan büyük Ali'den küçüktür")

    else:
        print("Ali grubun en büyüğüdür ve Lale en küçüğüdür. Ela Lale'den büyük Ali'den küçüktür")

elif(Lale > Ali and Lale > Ela):
    if(Ali > Ela):
        print("Lale grubun en büyüğüdür ve Ela en küçüğüdür. Ali Ela'den büyük Lale'den küçüktür ")


    else:
        print("Lale grubun en büyüğüdür ve Ali en küçüğüdür. Ela Lale'den küçük Ali'den büyüktür")

elif(Ela > Lale and Ela > Ali):
    if(Lale > Ali):
        print("Ela grubun en büyüğüdür ve Ali en küçüğüdür. Lale Ela'dan küçük Ali'den büyüktür")

    else:
        print("Ela grubun en büyüğüdür ve Lale en küçüğüdür. Ali Lale'den büyük Ela'dan küçüktür ")


##################################Ödev3#####################3

sayi1 = float(input("1. sayıyı giriniz"))
sayi2 = float(input("2. sayıyı giriniz"))

toplam = int(sayi1 + sayi2)
fark = int(sayi1-sayi2)
carpim = int(sayi1*sayi2)
bolum = (sayi1/sayi2)

print("girdiğiniz sayıların toplamlar: " + str(toplam))
print("girdiğiniz sayıların farkı: " + str(fark))
print("girdiğiniz sayıların çarpımı: " + str(carpim))
print("girdiğiniz sayıların bölümü: " + str(bolum))


##############################################Ödev4############################

isim = input("isminizi giriniz")
yaş= input("yaşınızı giriniz")
şehir= input("yaşadığınız şehri giriniz")
meslek= input("mesleğinizi giriniz")

print("Bu kullanıcı " + isim + " adında " + yaş + " yaşındadır " + şehir + " şehrinde yaşamaktadır ve mesleği: " + meslek + "'dir" )

#Ödev5

cumle = "Gelecek Hayalim W-code: Veri Bilimi Atolyesi"
print(cumle.split())

print(cumle.upper())
print(cumle.lower())



###################Ödev5##########################################3

sayı = "0123456789"

cift_sayılar = []
tek_sayılar = []


for i in sayı:

    if(int(i) % 2 == 0):
        cift_sayılar.append(i)

    else:
        tek_sayılar.append(i)


print("çift sayılar listesi: " + "" .join(cift_sayılar))
print("tek sayılar listesi: " + "" .join(tek_sayılar))

