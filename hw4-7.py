import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
from scipy.stats.mstats import winsorize
from sklearn.preprocessing import normalize
from scipy.stats import jarque_bera
from scipy.stats import normaltest
import warnings

ogrenciler = pd.read_csv("StudentsPerformance.csv")

#Sınav sonuçları normal dağılımlı mıdır? Değilse normal dağılıma sahip hale getirmek için ne yapabiliriz?

# plt.figure(figsize=(13,5))
#
# sınavlar= ['matematik_notu', 'okuma_notu', 'yazma_notu']
#
# for i in range(3):
#     plt.subplot(1,3,i+1)
#     plt.hist(ogrenciler[sınavlar[i]])
#     plt.title(sınavlar[i])
# plt.show()
#
# pd.options.display.float_format = '{:.5f}'.format
#
# ozellikler = ['matematik_notu', 'okuma_notu', 'yazma_notu']
# dagilim_testleri = pd.DataFrame(columns=['ozellik', 'jarque_bera_stats', 'jarque_bera_p_value',
#                                          'normal_stats', 'normal_p_value'])
#
# for ozellik in ozellikler:
#     jb_stats = jarque_bera(np.log(ogrenciler[ozellik]))
#     norm_stats = normaltest(np.log(ogrenciler[ozellik]))
#     dagilim_testleri = dagilim_testleri.append({"ozellik": ozellik,
#                                                 "jarque_bera_stats" : jb_stats[0] ,
#                                                 "jarque_bera_p_value" : jb_stats[1] ,
#                                                 "normal_stats": norm_stats[0] ,
#                                                 "normal_p_value" : norm_stats[1]
#                                                }, ignore_index=True)
# print(dagilim_testleri)
#
# ogrenciler["norm_matematik_notu"] = normalize(np.array(ogrenciler["matematik_notu"]).reshape(1,-1)).reshape(-1,1)  ###reshape???
# ogrenciler["norm_okuma_notu"] = normalize(np.array(ogrenciler["okuma_notu"]).reshape(1,-1)).reshape(-1,1)
# ogrenciler["norm_yazma_notu"] = normalize(np.array(ogrenciler["yazma_notu"]).reshape(1,-1)).reshape(-1,1)
# normal_ozellikler=["matematik_notu","norm_matematik_notu","okuma_notu","norm_okuma_notu",
#                     "yazma_notu","norm_yazma_notu"]
#
# print('Minimum Değer\n-----------------',)
# print(ogrenciler[normal_ozellikler].min())
# print('\nMaksimum Değer\n-----------------',)
# print(ogrenciler[normal_ozellikler].max())

###---------------------------------------------------------------------------------------------

# sınav sonucunu tek bir değişkende, hedef değişkeni olarak tutmak istiyoruz.
# Bunun için üç sınavın ortalamasını içeren yeni bir değişken tanımlayın.
# Bu yeni değişkenin ortalamasının normal dağılımlı olup olmadığını test edin.
# Eğer normal dağılıma sahip değilse dönüşüm yaparak normal dağılımlı hale getirmeye çalışın ve dönüşümün sonucunu test edin.

# mat_serisi= ogrenciler["matematik_notu"]
# okuma_serisi= ogrenciler["okuma_notu"]
# yazma_serisi = ogrenciler["yazma_notu"]
#
# hedef_seri = mat_serisi.append(okuma_serisi, ignore_index=True)
# hedef_seri = hedef_seri.append((yazma_serisi), ignore_index=True)
# print("Hedef serinin ortalaması:", hedef_seri.mean())
#
#
# plt.hist(hedef_seri)
# plt.show()
#
# jb_stat = jarque_bera(hedef_seri)
# print(jb_stat[1])
#
# normall = normaltest(hedef_seri)
# print(normall)
#
# jb_stat2 = jarque_bera(np.log(hedef_seri))
# print(jb_stat2[1])

#jarque bera ve normaltest olaylarını tam anladığımı söylemem zaten bozuk oluyor

##------------------------------------------------------------------------------------

#Bir önceki soruda oluşturduğumuz hedef değişkeni ile hangi değişkenler ilişkili görünüyor?
# Eğer amacımız sınav başarısını belirleyen etkenleri açıklamak olsaydı hangi değişkenleri veri kümemizde tutmamız gerekirdi?

# mat_serisi= ogrenciler["matematik_notu"]
# okuma_serisi= ogrenciler["okuma_notu"]
# yazma_serisi = ogrenciler["yazma_notu"]
#
# hedef_seri = mat_serisi.append(okuma_serisi, ignore_index=True)
# hedef_seri = hedef_seri.append((yazma_serisi), ignore_index=True)
#
# ogrenciler["hedef"]=hedef_seri
#
# print(ogrenciler.corr())
# print("En çok okuma ve yazma birbiriyle alakalı")
#
# sns.heatmap(ogrenciler.corr(), square=True, annot=True, linewidths=.5, vmin=0, vmax=1, cmap='viridis')
# plt.title("Korelasyon Matrisi ")
# plt.show()

#sorunun amacını anlayamadım. Correlation yaparsak zaten oluşturudğumuz değerleri görürüz.
#diğer değerleri de hw4-6da yaptık zaten.