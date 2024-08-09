## Gezinomi Veri Analizi Projesi

Bu, `miuul_gezinomi.xlsx` veri kümesini inceleyen bir Pandas tabanlı veri analizi projesidir.

### Proje Genel Bakışı

Bu projenin temel amaçları şunlardır:

- Veri kümesini temel veri keşfi ve temizleme işlemleri yaparak anlamak.
- Satış verilerini şehir, konsept, rezervasyon davranışı ve mevsimler gibi farklı açılardan analiz etmek.
- Daha derin içgörüler elde etmek için yeni değişkenler ve segmentler oluşturmak.
- En iyi performans gösteren şehir-konsept-sezon kombinasyonlarını ve ilişkili ölçümleri belirlemek.

### Veri Keşfi

Proje, gerekli kütüphanelerin içe aktarılması, veri çerçevesinin kurulması ve ilk birkaç satırın, şekil bilgisinin ve veri çerçevesi hakkındaki bilgilerin görüntülenmesiyle başlar.

Daha sonra analiz şu noktalara odaklanır:

- Benzersiz şehir sayısının ve frekanslarının hesaplanması.
- Benzersiz konsept sayısının ve her konseptin satış sayısının hesaplanması.
- Her şehir ve konsept için toplam gelir ve ortalama fiyatın analizi.
- Her şehir-konsept kombinasyonu için ortalama fiyatın hesaplanması.

### Yeni Değişken Oluşturma

Verileri daha derinlemesine analiz etmek için, `SaleCheckInDayDiff` değişkenine dayalı olarak `EB_Score` adlı yeni bir kategorik değişken oluşturulur. Bu değişken, "Son Dakika Rezervasyoncularını", "Potansiyel Planlamacıları", "Planlamacıları" ve "Erken Rezervasyon Yapanları" gibi farklı rezervasyon davranışı kategorilerini temsil eder.

### Daha Derin Analiz

Daha sonra analiz, aşağıdaki kombinasyonların ortalama fiyatını ve sıklığını incelemektedir:

- Şehir-Konsept-EB_Score
- Şehir-Konsept-Sezon
- Şehir-Konsept-CInDay

### Sıralama ve Segmentasyon

Veriler `Fiyat` değişkenine göre sıralanır ve ilk 20 sonuç görüntülenir. Ek olarak, müşteriler `Fiyat` değişkenine göre segmentlere ayrılır ve her segment için ortalama, maksimum ve toplam fiyat analiz edilir.

### Nihai Sonuçlar

Son adım, verileri `Fiyat` değişkenine göre sıralamak ve `ANTALYA_HERŞEY DAHİL_YÜKSEK` satış seviyesinin ayrıntılarını bulmaktır.

### Kullanım

Bu projeyi çalıştırmak için aşağıdaki bağımlılıkların yüklü olması gerekir:

- Python
- Pandas
- NumPy
- Matplotlib (veri görselleştirmesi için isteğe bağlı)

Sağlanan kodu Jupyter Notebook veya Google Colab gibi bir Python ortamında çalıştırabilirsiniz.

### Sonuç

Bu proje, gerçek dünya veri kümesi üzerinde kapsamlı veri analizi yapmada Pandas'ın gücünü göstermektedir. Bu analizden elde edilen içgörüler, iş stratejilerini ve karar verme süreçlerini iyileştirmek için kullanılabilir.
