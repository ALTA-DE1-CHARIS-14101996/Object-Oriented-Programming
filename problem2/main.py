# tulis solusi code disini
class Volume:
    def __init__(self) -> None:
        pass
    
    def Kubus(sisi):
        vol = pow(sisi,3)
        return f'Kubus : {vol}'
    
    def Balok(p,l,t):
        vol = p * l * t
        return f'Balok : {vol}'
    
    def Tabung(r,t):
        pi = 22/7
        vol = pi * (r**2) * t
        return f'Tabung : {int(vol)}'
    
print("Volume")
print(Volume.Kubus(10))
print(Volume.Balok(3,6,10))
print(Volume.Tabung(7,10))