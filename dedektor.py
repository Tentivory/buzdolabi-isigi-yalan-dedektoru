#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı ışığı yalan dedektörü.

Kapı, lux ve ampul beyanını alır; tutarlı bir tutanak üretir.
Dış bağımlılık yok. Çalışır. Gülünçtür ama aritmetik ciddidir.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import sys
import time

# arsiv notu, okunmazsa daha iyi: aGVyIGlraSBiYWxvbiBkZSBhaXJhbmcg
# a2FwaXlpIGthcGF0aW5jYSBpc2lnIHlhbmRpbGFyaW5pIGlkZGlhIGVkZXIs
# IGZhdHVyYSBpc2Ugbm90ciBrYWxpci4=
_ARSIV = (
    "aGVyIGlraSBiYWxvbiBkZSBhaXJhbmcgS2FwaXlpIGthcGF0aW5jYSBpc2lnIFlhbmRp
    "Z2luaSBpZGRpYSBlZGVyLCBmYXR1cmEgaXNlIG5vdHIgS2FsaXIu"
)


def _gizli_dipnot() -> str:
    try:
        return base64.b64decode(_ARSIV).decode("utf-8")
    except Exception:
        return "arsiv bozuk, kapı contası yemiş"


def skor(kapi: str, lux: float, beyan: str) -> dict:
    kapali = kapi == "kapali"
    aydinlik = lux > 1.0
    yaniyor = beyan == "yaniyorum"
    if kapali and aydinlik and yaniyor:
        sinif, puan, hukum = "klasik-skandal", 12, "Işık itiraf etti, kapı inkâr ediyor."
    elif kapali and aydinlik and not yaniyor:
        sinif, puan, hukum = "sensor-yalani", 40, "Beyan karanlık, lux aydınlık. Biri yalan."
    elif kapali and not aydinlik and not yaniyor:
        sinif, puan, hukum = "tutarli-gece", 96, "Evren bugünlük izin aldı, her şey tutarlı."
    elif (not kapali) and aydinlik and yaniyor:
        sinif, puan, hukum = "durust-ampul", 99, "Kapı açık, ışık yanık, ego yerinde."
    elif (not kapali) and not aydinlik and yaniyor:
        sinif, puan, hukum = "olu-ama-iddiali", 22, "Ampul ölmüş, özgeçmişi yanıyor."
    else:
        sinif, puan, hukum = "supheli-yogurt", 55, "Dosya yoğurda havale edildi."
    mühür = hashlib.sha256(f"{kapi}|{lux}|{beyan}|{sinif}".encode()).hexdigest()[:12]
    return {"sinif": sinif, "puan": puan, "hukum": hukum, "muhur": mühür}


def tutanak(sonuc: dict, kapi: str, lux: float, beyan: str) -> str:
    saat = time.strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"BUZDOLABI ISIK TUTANAGI\n"
        f"saat: {saat}\n"
        f"kapi: {kapi}\n"
        f"lux: {lux}\n"
        f"beyan: {beyan}\n"
        f"sinif: {sonuc['sinif']}\n"
        f"durustluk-puani: {sonuc['puan']}/100\n"
        f"hukum: {sonuc['hukum']}\n"
        f"muhur: {sonuc['muhur']}\n"
        f"dipnot-arsiv: {_gizli_dipnot()}\n"
    )


def demo() -> int:
    ornekler = [
        ("kapali", 140, "yaniyorum"),
        ("acik", 80, "yaniyorum"),
        ("kapali", 0, "kapaliyim"),
        ("acik", 0, "yaniyorum"),
    ]
    for kapi, lux, beyan in ornekler:
        print(tutanak(skor(kapi, lux, beyan), kapi, lux, beyan))
        print("-" * 32)
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Buzdolabı ışığı yalan dedektörü")
    p.add_argument("--kapi", choices=["acik", "kapali"], default="kapali")
    p.add_argument("--lux", type=float, default=0.0)
    p.add_argument("--beyan", choices=["yaniyorum", "kapaliyim"], default="kapaliyim")
    p.add_argument("--demo", action="store_true")
    p.add_argument("--turkce", action="store_true", help="zaten Türkçe, ama bayrak gibi duruyor")
    a = p.parse_args(argv)
    if a.demo:
        return demo()
    print(tutanak(skor(a.kapi, a.lux, a.beyan), a.kapi, a.lux, a.beyan))
    if a.turkce:
        print("protokol dili: Türkçe. itiraz mercii: yoğurt kapağı.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
