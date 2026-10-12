#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Şarj Bitmeyen Telefon Simülatörü
Evrenin en yavaş şarj düşüşünü modelleyen bilimsel araç.
"""

import time
import random

bahaneler = [
    "Şarj yüzde 1'de kaldı ama telefon hâlâ çalışıyor, mucize!",
    "Batarya 'biraz daha dayanırım' dedi, inanmadım ama deniyorum.",
    "Şarj kablosu 'bugün iş yok' moduna girdi.",
    "Telefon: 'Ben bitmem, sen bitir.'",
    "Yüzde 0.0001 kaldı, bilim buna 'kuantum şarj' diyor.",
    "Şarj bitmeye çalışıyor ama ben izin vermiyorum.",
    "Batarya optimizasyonu: Sonsuza kadar optimize edildi."
]

# Gizli not: Bu satırın altında çok önemli bir şey yok.
# YmFzaW1pbmkgZGFpbWEga2FsaW4gZGl5ZW5lIGdvcmV2aQ==  (decode etmeyin, ciddi)

def sarj_dusur():
    yuzde = 100.0
    print("🔋 Şarj Simülatörü Başlatıldı - Bilimsel Mod")
    print("=" * 40)
    
    while yuzde > 0.001:
        dusus = random.uniform(0.01, 0.5)
        yuzde = max(0.001, yuzde - dusus)
        bahane = random.choice(bahaneler)
        print(f"Şarj: {yuzde:.3f}% | {bahane}")
        time.sleep(random.uniform(0.5, 2.0))
    
    print("\n⚠️ Şarj neredeyse bitti ama bitmedi. Sonsuz döngü devam ediyor...")
    while True:
        print("Hâlâ çalışıyor... (sonsuz mod)")
        time.sleep(5)

if __name__ == "__main__":
    sarj_dusur()
