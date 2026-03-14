# ============================================
# YZM533 Programlama Temelleri I - Vize Projesi
# Soru 2: Menü Tabanlı İşlemler
# Görkem Kurtkaya (Fullstack Developer)
# Öğrenci No: Y250234129
# ============================================

def menu_goster():
    print("\n" + "=" * 45)
    print("(1) Girilen Sayının Tek Yada Çift Olduğunu Bulma")
    print("(2) Girilen 3 Sayıyı Büyükten Küçüğe Sıralama")
    print("(3) Girilen Sayının Asal Sayı Olup Olmadığını Bulma")
    print("Çıkmak için -1'e basınız.")
    print("=" * 45)

def tek_cift_bul(sayi):
    if sayi % 2 == 0:
        print(f"{sayi} sayısı ÇİFT sayıdır.")
    else:
        print(f"{sayi} sayısı TEK sayıdır.")

def buyukten_kucuge_sirala(a, b, c):
    if a >= b and a >= c:
        if b >= c:
            print(f"Büyükten küçüğe sıralama: {a}, {b}, {c}")
        else:
            print(f"Büyükten küçüğe sıralama: {a}, {c}, {b}")
    elif b >= a and b >= c:
        if a >= c:
            print(f"Büyükten küçüğe sıralama: {b}, {a}, {c}")
        else:
            print(f"Büyükten küçüğe sıralama: {b}, {c}, {a}")
    else:
        if a >= b:
            print(f"Büyükten küçüğe sıralama: {c}, {a}, {b}")
        else:
            print(f"Büyükten küçüğe sıralama: {c}, {b}, {a}")

def asal_mi(sayi):
    if sayi < 2:
        print(f"{sayi} sayısı ASAL DEĞİLDİR.")
        return
    for i in range(2, sayi):
        if sayi % i == 0:
            print(f"{sayi} sayısı ASAL DEĞİLDİR.")
            return
    print(f"{sayi} sayısı ASAL sayıdır.")


print("=" * 45)
print("Görkem Kurtkaya (Fullstack Developer)")
print("Öğrenci No: Y250234129")
print("=" * 45)

while True:
    menu_goster()
    secim = int(input("Seçiminizi Giriniz: "))

    if secim == -1:
        print("Programdan çıkılıyor...")
        break
    elif secim == 1:
        sayi = int(input("Bir sayı giriniz: "))
        tek_cift_bul(sayi)
    elif secim == 2:
        sayi1 = int(input("1. sayıyı giriniz: "))
        sayi2 = int(input("2. sayıyı giriniz: "))
        sayi3 = int(input("3. sayıyı giriniz: "))
        buyukten_kucuge_sirala(sayi1, sayi2, sayi3)
    elif secim == 3:
        sayi = int(input("Bir sayı giriniz: "))
        asal_mi(sayi)
    else:
        print("Yanlış değer girdiniz tekrar giriş yapınız")
