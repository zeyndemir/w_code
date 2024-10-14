import pandas as pd

sozluk = {
"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],


  "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],


"Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

df = pd.DataFrame(sozluk)

print(df)

print(df.loc[2, "Kategori"])
print(df.loc[2, "Ürün"])

print(df.loc[4:9])
print(df.loc[1:6, "Ürün"])

print(df[df["Kategori"] == "Giyim"])
print(df[df["Kategori"] == "Ayakkabı"])
print(df[(df["Kategori"] == "Giyim") & (df["Fiyat"] > 300)])
print(df[(df["Kategori"] == "Ayakkabı") & (df["Fiyat"] < 600)])
print(df[(df["Kategori"] == "Aksesuar") & (df["Fiyat"] > 100)])


