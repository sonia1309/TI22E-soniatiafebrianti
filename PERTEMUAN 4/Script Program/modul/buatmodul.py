import LuasVolumeBangunRuang 

panjang=int(input('Masukan panjang = '))
tinggi=int(input('Masukan tinggi = '))
lebar=int(input('Masukan lebar = '))
jari_jari=int(input('Masukan jari-jari = '))

print('Luas Balok = ',LuasVolumeBangunRuang.luas_balok(panjang,lebar,tinggi))
print('Luas Tabung = ',LuasVolumeBangunRuang.luas_balok(jari_jari,tinggi))