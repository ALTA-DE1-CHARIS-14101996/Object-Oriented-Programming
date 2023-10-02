# tulis solusi code disini
class Luas:
    def __init__(self) -> None:
        pass
    
    def Persegi(sisi):
        luas = sisi * sisi
        return f"Persegi: {luas}"
    
    def Segitiga(alas,tinggi):
        luas = (alas * tinggi)/2
        return f"Segitiga: {int(luas)}"
    
    def PersegiPanjang(panjang,lebar):
        luas = panjang * lebar
        return f"Persegi Panjang: {luas}"
    
class Keliling:
    def __init__(self) -> None:
        pass
    def Persegi(sisi):
        keliling = 4 * sisi
        return f"Persegi: {keliling}"
    
    def Segitiga(alas,tinggi):
        c = (alas**2 + tinggi**2)**(1/2)
        keliling = alas + tinggi + c
        return f"Segitiga: {int(keliling)}"
    
    def PersegiPanjang(panjang,lebar):
        keliling = (panjang + lebar)
        return f"Persegi Panjang: {keliling}"
 
print("Luas")    
print(Luas.Persegi(4))
print(Luas.Segitiga(3,4))
print(Luas.PersegiPanjang(7,8))
print()
print("Keliling")
print(Keliling.Persegi(4))
print(Keliling.Segitiga(3,4))
print(Keliling.PersegiPanjang(7,8))