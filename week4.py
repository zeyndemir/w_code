##################Odev1#######################
maas = int(input("lütfen maaşınızı giriniz"))

if maas <= 10000:
    maas = maas - (maas * 0.05)
    print("yeni maaş " + str(maas) )

elif maas < 25000:
    maas = maas - (maas * 0.1)
    print("yeni maaş " + str(maas))

elif maas <= 45000:
    maas = maas - (maas * 0.25)
    print("yeni maaş " + str(maas))

else :
    maas = maas - (maas * 0.3)
    print("yeni maaş " + str(maas))


###############Odev2#################################



kullanici_adi1 = input("lutfen bir kullanıcı adı oluşturunuz")
sifre1 = input("lutfen bir sifre olusturunuz")

if len(sifre1) == 6:
    print("hesabınız oluşturulmuştur")

else:
    print("6 haneli bir şifre oluşturunuz lütfen")



##################Odev3################

kullanici_adi2=input("lutfen bir kullanıcı adı oluşturunuz")
sifre2 = input("lutfen bir sifre olusturunuz")


while not (5 < len(sifre2)  < 10 ):
    sifre = input("Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!")


print("sifreniz oluşturuldu")


###############Odev4######################

sifre3 = "123456"
girdi = input("Şifreyi giriniz")

if girdi == sifre3:
    print("giriş yapıldı")

else:
    print("yanlış ş,fre girildi")
    i=3

    while i>=1 :
        sifre_deneme = input("tekrar deneyiniz")

        if sifre_deneme == girdi:
            print("giriş yapıldı")
            break

        else:
            i -= 1
            print(f"kalan hakkınız" + i)


############### Odev4 ######################

sifre3 = "123456"
girdi = input("Şifreyi giriniz: ")


if girdi == sifre3:
    print("Giriş yapıldı.")

else:
    print("Yanlış şifre girildi!")

    i = 2
    while i > 0:  # İlk giriş yanlış olduğu için hakkı bir eksiltiyoruz
        i -= 1
        sifre_deneme = input("tekrar deneyiniz kalan hakkınız: " + i)

        if sifre_deneme == sifre3:
            print("Giriş yapıldı.")
            break
        else:
            print("Yanlış şifre girildi!")

    if i == 0 :
        print("Şifreyi 3 kez yanlış girdiniz. Giriş hakkınız kalmadı!")





















