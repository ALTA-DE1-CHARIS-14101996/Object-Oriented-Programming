# tulis solusi code disini
class PengirimanBarang:
    
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_harga(self):
        volume = self.panjang * self.lebar * self.tinggi
        harga = 5000  # Harga dasar untuk volume 50 cm3 dan berat 1 kg

        if volume > 50:
            faktor_volume = volume / 50
            harga *= faktor_volume

        if self.berat > 1:
            faktor_berat = self.berat // 1
            harga *= faktor_berat
        return harga
                      
Panjang = 5
Lebar = 2
Tinggi = 4
Berat = 1 

pengiriman = PengirimanBarang(Panjang,Lebar,Tinggi,Berat)
harga = pengiriman.hitung_harga()

print(f'Harga : Rp {harga}')
