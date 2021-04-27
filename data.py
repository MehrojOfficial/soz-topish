"""
</>
Date: 04.27.2021
Time: 7:35 AM
Programmer: Mehroj Majidov
Github: https://github.com/MehrojOfficial
Title: "So'z topish o'yini"
</>
"""
from uzwords import words
from random import randint

def tanlamoq():
    tanlangan = words[randint(0,len(words))]
    while "-" in tanlangan or " " in tanlangan :
        tanlangan = words[randint(0,len(words))]
    return tanlangan.upper()

def tekshirish(harf,soz):
    xxarf = ""
    for xarf in soz:
        if xarf.upper() in harf.upper():
            xxarf += xarf
        else:
            xxarf += "-"
    return xxarf.upper()

def play():
    soz = tanlamoq()
    urinish = 0
    harf = ""
    chiziq = "-"*len(soz)
    print(f"Мен {len(soz)} хонали сўз ўйладим. Топа оласизми?")
    while True:
        urinish += 1
        print(chiziq)
        hharf = input("Ҳарф киритинг: ")
        if len(hharf) == 1 and hharf in soz and hharf not in harf:
            harf += hharf
            chiziq = tekshirish(harf,soz)
            print(f"\n{hharf} ҳарфи тўғри.\nШу вақтгача киритган ҳарфларингиз: {harf}")
        elif len(hharf) == 1 and hharf not in soz and hharf not in harf:
            harf += hharf
            chiziq = tekshirish(harf,soz)
            print(f"\nБундай ҳарф йўқ.\nШу вақтгача киритган ҳарфларингиз: {harf}")
        elif hharf in harf:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
        if chiziq == soz:
            break
    print(f"\nТабриклайман! {soz.upper()} сўзини {urinish} та уринишда топдингиз.")

def start(): 
    play()