# tulis solusi code disini
class Kalkulator:
    def __init__(self) -> None:
        pass
    
    def Penjumlahan(a,b):
        result = a + b
        return f'Penjumlahan : {result}'
    
    def Pengurangan(a,b):
        result = a - b
        return f'Pengurangan : {result}'
    
    def Perkalian(a,b):
        result = a * b
        return f'Perkalian : {result}'
    
    def Pembagian(a,b):
        result = a / b
        return f'Pembagian : {int(result)}'
    
    
print(Kalkulator.Penjumlahan (3,4)) 
print(Kalkulator.Pengurangan (15,4))
print(Kalkulator. Perkalian (10,10))
print(Kalkulator.Pembagian (12,3))
