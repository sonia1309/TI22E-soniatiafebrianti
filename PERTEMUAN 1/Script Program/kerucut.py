print("mencari kerucut")
import math
# variabel                              
tinggi_kerucut = 2
jari_jari_lingkaran = 4

#rumus                                     
luas_kerucut = math.pi * jari_jari_lingkaran * (jari_jari_lingkaran + math.sqrt(jari_jari_lingkaran * 2 + tinggi_kerucut * 2))
volume_kerucut = (1/3) * math.pi * jari_jari_lingkaran * tinggi_kerucut * 2

#output 
print("luas kerucut :", luas_kerucut)
print("volume kerucut :", volume_kerucut)