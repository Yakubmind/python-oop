from geometri.bangunruang import BangunRuang
from geometri.persegi_panjang import PersegiPanjang
from geometri.segitiga import SegiTiga

print('Menggunakan OOP')
p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

s1 = SegiTiga(10, 2)
print(s1.info())
print(s1.hitung_luas())

b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

#Polymorphism : kemampuan objek untuk meresponse berbeda, terhadap pemanggilan method yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\nPolymorphism')
for BangunRuang in daftar_bangun_ruang:
    print(BangunRuang.info())


