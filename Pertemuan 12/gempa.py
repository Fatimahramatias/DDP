class Gempa:
    # atribut class
    lokasi = ''
    skala = 0

    # constructor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    # method untuk menampilkan datanya
    def data_gempa(self):
        if self.skala < 2:
         ket = 'maka dampak gempa tidak berasa'
        elif (self.skala >=2  and self.skala <=4):
         ket = 'maka dampak gempa banguna retak-retak'
        elif (self.skala >=4 and self.skala <=6):
         ket = 'maka dampak gempa bangunan roboh'
        elif (self.skala >6):
         ket = 'maka dampak gempa bangunan roboh dan berpotensi tsunami'
        else :
         ket = 'salah memasukan skala'
        print(f'Telah terjadi gempa di {self.lokasi} dengan skala {self.skala} {ket}')