alfabe=['a','b' ,'c' , 'd', 'e', 'f', 'g' ,'h' ,'i' ,'j','k' ,'l' ,'m' ,'n' ,'o' ,'p' ,'q','r' ,'s' 
           ,'t' ,'u' ,'v','w','x' ,'y' ,'z']
alfabe2=['A','B' ,'C' , 'D', 'E', 'F', 'G' ,'H' ,'I' ,'J','K' ,'L' ,'M' ,'N' ,'O' ,'P' ,'Q','R' ,'S' 
           ,'T' ,'U' ,'V','W','X' ,'Y' ,'Z']
#fonksiyon, uzunluk hesaplar
def uzunluk(alfabe):
    s=0
    for i in alfabe:
        s=s+1
    return s
    
#fonksiyon, metinin icindeki karakterlerin alfabede kacinci indiste oldugunu bulur
def index(mesaj,i):
    s=0
    s2=0
    if i in alfabe:
        for j in alfabe:
            if i == j:
                return s
                break
            else:
                s=s+1
    elif i in alfabe2:
        for j in alfabe2:
            if i == j:
                return s2
                break
            else:
                s2=s2+1

def yaz(mesaj,anahtarsayi):
    sifre = ""
    indexDegeri =0
    for i in mesaj:
        indexDegeri = index(mesaj,i)
        if i in alfabe:
            sifre+=alfabe[(indexDegeri+anahtarsayi)%uzunluk(alfabe)]
        elif i in alfabe2:
            sifre+=alfabe2[(indexDegeri+anahtarsayi)%uzunluk(alfabe2)]
    print("Mesaj:",mesaj)
    print("Yeni Mesaj:",sifre)
    
def coz(mesaj,anahtarsayi):
    sifre = ""
    indexDegeri =0
    for i in mesaj:
        indexDegeri = index(mesaj,i)
        if i in alfabe:
            sifre+=alfabe[(indexDegeri-anahtarsayi)%uzunluk(alfabe)]
        elif i in alfabe2:
            sifre+=alfabe2[(indexDegeri-anahtarsayi)%uzunluk(alfabe2)]
    print("Mesaj:",mesaj)
    print("Yeni Mesaj:",sifre) 
    

devam = input("Sifreyi yazmak veya gormek istiyor musunuz(e/h):")
while devam == "e" or devam == "E":
    secim = input("Yazmak icin y ye cozmek icin c ye basiniz:")
    anahtarsayi = int(input("Anahtar sayiyi giriniz:"))
    mesaj = input("Mesaj giriniz:")
    if devam == "e" or devam == "E":
        if secim == "y" or secim == "Y":
            yaz(mesaj,anahtarsayi)
            print("İşlem bitmiştir.")
            devam = input("Devam etmek istiyor musunuz(e/h):")
            if devam == "h" or devam == "H":
                break
        elif secim == "c" or secim == "C":
            coz(mesaj,anahtarsayi) 
            print("İşlem bitmiştir.")
            devam = input("Devam etmek istiyor musunuz(e/h):")
            if devam == "h" or devam == "H":
                break
        else:
            print("Lutfen y veya c yi seciniz.")
    elif devam == "h" or devam == "H":
        break
    else:
        print("Lutfen e veya h yi seciniz:")
    

            