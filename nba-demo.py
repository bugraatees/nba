import pandas as pd

df = pd.read_csv("nba.csv")

#1- İlk 10 kaydı getir
result = df.head(10)

#2-Toplam Kaç kayıt vardır
result = len(df.index)

#3 Tüm oyuncuların toplam maaşı ne kadardır
result = df["Salary"].mean()

#4-En yüksek maaş ne kadardır
result = df["Salary"].max()

#5 En yüksek maaş alan oyuncu kimdir
result = df[df["Salary"]== df["Salary"].max()]["Name"].iloc[0]

#6 Yaşı 20-25 arası olan oyuncuların isim ve oynadıkları takımları azalan şeklinde sıralı getiriniz.
result = df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name", "Team", "Age"]].sort_values("Age",ascending=True)

#7 "John Holland" isimli oyuncunun oynadığı takım hangisidir
result = df[df["Name"] == "John Holland"]["Team"].iloc[0]

#8 Takımlara göre oyuncuların ortalama maaş bilgisi nedir
result = df.groupby("Team")["Salary"].mean()
 
#9 Kaç farklı takım mevcut
result = len(df.groupby("Team"))
result = df["Team"].nunique()

#10 her takımda kaç oyuncu vardır?
result = df["Team"].value_counts()

#11 -ismi içinde "and" geçen kayıtları bul
df = df.dropna
#result = df[df["Name"].str.contains("and")]
def str_find(name):
    if "and" in name.lower():
        return True
    return False

print (result)