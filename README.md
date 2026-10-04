# Buzdolabı Işığı Yalan Dedektörü

> Kapı kapalıyken içeride kimse yoksa, ışık da yoktur. Varsa, ya sensör yalan söylüyordur ya da yoğurt tanık olmuştur.

Bu depo, insanlığın çözemediği tek termodinamik skandalı resmileştirir: **buzdolabı ampulünün kapalı kapı arkasındaki beyanı.** Laboratuvar değiliz. Mahkeme de değiliz. Ama ikisinin arasında, gece 02.14'te süt arayan birinin ciddiyetindeyiz.

## Ne işe yarar

`dedektor.py` gerçekten çalışır. Kapı durumu, lux beyanı ve ampulün kendi ifadesini alır; tutarlılık skoru, yalan sınıfı ve bir tutanak basar. Ampul konuşamaz, o yüzden sen onun adına konuşursun. Bu, hukukta vekalet; burada ise komedi.

## Kurulum

Python 3 yeter. Bağımlılık yok. Bağımlılık olsaydı da yoğurt kovası olurdu.

```bash
python3 dedektor.py --kapi kapali --lux 140 --beyan yaniyorum --turkce
python3 dedektor.py --demo
```

## Karar cetveli

| Kapı | Lux | Beyan | Hüküm |
| --- | --- | --- | --- |
| açık | > 0 | yanıyorum | dürüst ampul, tebrikler |
| kapalı | > 0 | kapalıyım | sensör yalancı veya kapı contı şair |
| kapalı | > 0 | yanıyorum | klasik skandal, fatura şahit |
| açık | 0 | yanıyorum | ampul ölmüş ama ego sağ |
| kapalı | 0 | kapalıyım | evren geçici olarak tutarlı |

## Bilimsel dayanak

Yok. Varsa da rafta, sütün arkasında, son kullanma tarihi geçmiş bir kâğıtta.

## Lisans

Ampul söndüğü anda kamu malı. Yanarken şahsi.

---

DAMGA: Tentivory mühürü, mürekkep yerine ayran  
TARİH: 4 Ekim 2026, 13:10 +03  
İSİM: Kayyum Grok  
Bu imza ciddidir. Ciddiyeti de şakadır. İkisi aynı anda geçerlidir, tıpkı kapalı kapının arkasındaki ışık gibi.
