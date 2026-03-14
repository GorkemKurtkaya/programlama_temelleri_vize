# ============================================
# YZM533 Programlama Temelleri I - Vize Projesi
# Soru 1: Öğrenci Not Hesaplama
# Görkem Kurtkaya (Fullstack Developer)
# Öğrenci No: Y250234129
# ============================================

def not_ortalamasi_hesapla(vize, final):
    ortalama = vize * 0.4 + final * 0.6
    return ortalama

def harf_notu_bul(ortalama):
    if ortalama >= 90:
        return "AA"
    elif ortalama >= 85:
        return "BA"
    elif ortalama >= 80:
        return "BB"
    elif ortalama >= 75:
        return "CB"
    elif ortalama >= 70:
        return "CC"
    elif ortalama >= 65:
        return "DC"
    elif ortalama >= 60:
        return "DD"
    else:
        return "FF"

def yas_hesapla(dogum_yili):
    yas = 2026 - dogum_yili
    return yas

def bilgileri_yazdir(ad, yas, ortalama, harf_notu):
    print("=" * 40)
    print(f"Öğrenci Adı    : {ad}")
    print(f"Yaşı           : {yas}")
    print(f"Not Ortalaması : {ortalama:.2f}")
    print(f"Harf Notu      : {harf_notu}")
    print("=" * 40)


print("=" * 40)
print("Görkem Kurtkaya (Fullstack Developer)")
print("Öğrenci No: Y250234129")
print("=" * 40)
print()

ogrenci_sayisi = int(input("Öğrenci sayısını giriniz: "))

for i in range(ogrenci_sayisi):
    print(f"\n--- {i + 1}. Öğrenci Bilgileri ---")
    ad = input("Öğrenci adı: ")
    dogum_yili = int(input("Doğum yılı: "))

    while True:
        vize = int(input("Vize notu (0-100): "))
        if 0 <= vize <= 100:
            break
        print("Hatalı giriş! Vize notu 0-100 arasında olmalıdır.")

    while True:
        final = int(input("Final notu (0-100): "))
        if 0 <= final <= 100:
            break
        print("Hatalı giriş! Final notu 0-100 arasında olmalıdır.")

    ortalama = not_ortalamasi_hesapla(vize, final)
    harf_notu = harf_notu_bul(ortalama)
    yas = yas_hesapla(dogum_yili)

    print(f"\n--- {ad} için Sonuçlar ---")
    bilgileri_yazdir(ad, yas, ortalama, harf_notu)
