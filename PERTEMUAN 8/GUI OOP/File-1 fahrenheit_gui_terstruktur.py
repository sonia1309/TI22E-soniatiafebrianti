 class Fahrenheit:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_fahrenheit(self):
        val = self.suhu
        return val

    def get_reamur(self):
        val = (4/9) * (self.suhu - 32)
        return val
    
    def get_celcius(self):
        val = (5/9) * (self.suhu - 32)
        return val

    def get_kelvin(self):
        val= (5/9) * (self.suhu + 32) + 273
        return val

suhu = input ("Masukkan suhu dalam Fahrenheit :")
F = Fahrenheit (float(suhu))
val = F.get_fahrenheit()

R = F.get_reamur()
C = F.get_celcius()
K = F.get_kelvin()

print(str(val) + " Fahrenheit, sama dengan:")
print(str(R) + " Reamur")
print(str(C) + " Celcius")
print(str(K) + " Kelvin")