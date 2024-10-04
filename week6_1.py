#####Odev1####

sozluk = {"Zeynep": "Matematik", "Akif" : "Fizik", "Halime" : "Kimya"}
ad = input("merak ettiğiniz öğreninin adını giriniz")
print(sozluk[ad])


##########Odev2#############3



sozluk["Zeynep"] = "Tarih" #değiştirme
sozluk["Rabia"] = "Biyoloji" #ekleme

print(sozluk.popitem())

sozluk.update({
    "Beyza" : "İngilizce",
    "Evrim" : "Din Kültürü ve Ahlak Bilgisi",
    "Burhan" : "Coğrafya"
})

sonuc = sozluk
print(sonuc)