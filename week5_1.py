############1###############33

def d_alani():
    r=int(input("yarıçap giriniz"))
    pi = int(input("pi değerini giriniz"))

    alan = pi*(r**2)
    return print(alan)

d_alani()


#############ödev 2##############3

def faktoriyel(a):

    i=a
    fak = 1
    while i>=1 :
        fak = fak*i
        i -= 1
    return fak

print(faktoriyel(5))

##################ödev3##################3

def yas_bul():
    dy=int(input("doğum yılınızı giriniz"))
    yas = 2024 - dy
    return yas

print(yas_bul())


#####################Ödev4##################33

def emekli_tespit():
    isim = input("isminizi giriniz")
    dogum_yili  = int(input("doğum yılınızı giriniz"))

    if 2024 - dogum_yili >= 65 :
        print("emekli oldunuz")

    else:
        print(f"emekli olmanıza {65-(2024- dogum_yili)} yıl kaldı")

emekli_tespit()