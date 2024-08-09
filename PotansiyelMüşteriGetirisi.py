import pandas as pd

pd.set_option("display.max_columns", None)
df = pd.read_excel('miuul_gezinomi.xlsx')
pd.set_option('display.float_format', lambda x: '%.2f' % x)

print(df.head())
print(df.shape)
print(df.info())

#Kaç unique şehir vardır? Frekansları nedir?
print(df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

#Kaç unique Concept vardır?
print(df["ConceptName"].nunique())

#Hangi Concept'dan kaçar tane satış gerçekleşmiş?
print(df["ConceptName"].value_counts())

#Şehirlere göre satışlardan toplam ne kadar kazanılmış?
print(df.groupby("SaleCityName").agg({"Price": "sum"}))

#Concept türlerine göre göre ne kadar kazanılmış?
print(df.groupby("ConceptName").agg({"Price": "sum"}))

#Şehirlere göre PRICE ortalamaları nedir?
print(df.groupby(by=['SaleCityName']).agg({"Price": "mean"}))

#Conceptlere göre PRICE ortalamaları nedir?
print(df.groupby(by=['ConceptName']).agg({"Price": "mean"}))

# Şehir-Concept kırılımında PRICE ortalamaları nedir?
print(df.groupby(by=["SaleCityName", 'ConceptName']).agg({"Price": "mean"}))

#satis_checkin_day_diff değişkenini EB_Score adında yeni bir kategorik değişkene çeviriniz.
bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]
df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)

# Şehir, Concept, EB_Score, Sezon, CInday kırılımında ücret ortalamalarına ve frekanslarına bakınız
# Şehir-Concept-EB Score kırılımında ücret ortalamaları
print(df.groupby(by=["SaleCityName", 'ConceptName', "EB_Score"], observed=True).agg({"Price": ["mean", "count"]}))

# Şehir-Concept-Sezon kırılımında ücret ortalamaları
print(df.groupby(by=["SaleCityName", "ConceptName", "Seasons"], observed=True).agg({"Price": ["mean", "count"]}))

# Şehir-Concept-CInday kırılımında ücret ortalamaları
print(df.groupby(by=["SaleCityName", "ConceptName", "CInDay"], observed=True).agg({"Price": ["mean", "count"]}))

#City-Concept-Season kırılımın çıktısını PRICE'a göre sıralayınız.
agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"], observed=True).agg({"Price": "mean"}).sort_values("Price", ascending=False)
print(agg_df.head(20))

#Indekste yer alan isimleri değişken ismine çeviriniz.
agg_df.reset_index(inplace=True)
print(agg_df.head())

#Yeni level based satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
agg_df['sales_level_based'] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)
print(agg_df.head())

#Personaları segmentlere ayırınız.
agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
print(agg_df.head(30))
print(agg_df.groupby("SEGMENT", observed=True).agg({"Price": ["mean", "max", "sum"]}))

#Oluşan son df'i price değişkenine göre sıralayınız.
#"ANTALYA_HERŞEY DAHIL_HIGH" hangi segmenttedir ve ne kadar ücret beklenmektedir?
agg_df = agg_df.sort_values(by="Price")
print(agg_df.head())

new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
print(agg_df[agg_df["sales_level_based"] == new_user])
