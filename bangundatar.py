def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print('jadi luas persegi yang sisinya', sisi, 'adalah', luas)
    print('jadi keliling persegi yang sisinya', sisi, 'adalah', keliling)

def persegipanjang(panjang,lebar):
    luas = panjang * lebar
    keliling = panjang + lebar * 2
    print('jadi luas persegi panjang yang panjang dan lebarnya', panjang, 'dan', lebar,'adalah', luas)
    print('jadi keliling persegi panjang yang panjang dan lebarnya', panjang, 'dan',lebar , 'adalah', keliling)

def segitiga(sisi,alas,tinggi):
    luas = 1/2 * alas * tinggi
    keliling = 3 * sisi
    print('jadi luas segitiga yang alas dan tingginya',alas, 'dan', tinggi, 'adalah', luas)
    print('jadi keliling segitiga yang sisinya',sisi, 'adalah', keliling)

def belahketupat(d1,d2,sisi):
    luas = 1/2 * d1 * d2
    keliling = 4 * sisi
    print('jadi luas belah ketupat yang diagonal satu dan diagonal duanya',d1, 'dan',d2, 'adalah', luas)
    print('jadi keliling belah ketupat yang sisinya', sisi, 'adalah', keliling)

def lingkaran(r):
    luas = 22/7 * r * r
    keliling = 2 * 22/7 * r
    print('jadi luas lingkaran yang jari-jarinya',r, 'adalah', luas)
    print('jadi keliling lingkaran yang jari-jarinya',r, 'adalah', keliling)

def jajargenjang(alas,tinggi,sisi):
    luas = alas * tinggi
    keliling = 2 * (alas + sisi)
    print('jadi luas jajargenjang yang alas dan tingginya',alas, 'dan',tinggi, 'adalah', luas)
    print('jadi keliling jajargenjang yang alas dan sisinya', alas, 'dan', sisi, 'adalah', keliling)

def layanglayang(d1,d2,sisi1,sisi2):
    luas = 1/2 * d1 * d2
    keliling = 2 * sisi1 * sisi2
    print('jadi luas layang-layang yang diagonal satu dan diagonal duanya', d1, 'dan', d2, 'adalah', luas)
    print('jadi keliling layang-layang yang sisi-sisinya', sisi1, 'dan', sisi2, 'adalah', keliling)


