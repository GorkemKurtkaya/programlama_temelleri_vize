# YZM533 Programlama Temelleri I - Vize Projesi

**Görkem Kurtkaya (Fullstack Developer)**
**Öğrenci No:** Y250234129

---

## Proje Hakkında

Bu proje, YZM533 Programlama Temelleri I dersi vize ödevi kapsamında hazırlanmıştır. İki ayrı Python programından oluşmaktadır.

## Soru 1 — Öğrenci Not Hesaplama (`soru1.py`)

Kullanıcıdan öğrenci bilgilerini alarak not ortalaması, harf notu ve yaş hesaplayan program.

**Özellikler:**
- Öğrenci adı, doğum yılı, vize ve final notu girişi
- Not girişlerinde 0–100 aralık kontrolü
- Vize %40 + Final %60 ağırlıklı ortalama hesaplama
- Harf notu dönüşümü (AA, BA, BB, CB, CC, DC, DD, FF)
- Yaş hesaplama ve bilgileri ekrana yazdırma
- Tüm işlemler kullanıcı tanımlı fonksiyonlarla gerçekleştirilmektedir

**Harf Notu Tablosu:**

| Aralık | Harf Notu |
|--------|-----------|
| 90–100 | AA        |
| 85–89  | BA        |
| 80–84  | BB        |
| 75–79  | CB        |
| 70–74  | CC        |
| 65–69  | DC        |
| 60–64  | DD        |
| 0–59   | FF        |

## Soru 2 — Menü Tabanlı İşlemler (`soru2.py`)

Kullanıcıya menü sunan ve seçime göre matematiksel işlemler gerçekleştiren program.

**Menü Seçenekleri:**
1. Girilen sayının tek veya çift olduğunu bulma
2. Girilen 3 sayıyı büyükten küçüğe sıralama
3. Girilen sayının asal olup olmadığını bulma
4. Çıkış için `-1` girişi

**Özellikler:**
- Geçersiz menü girişlerinde uyarı mesajı
- `-1` girilene kadar program çalışmaya devam eder
- Tüm işlemler kullanıcı tanımlı fonksiyonlarla gerçekleştirilmektedir

## Çalıştırma

```bash
python3 soru1.py
```

```bash
python3 soru2.py
```

## Gereksinimler

- Python 3.x
