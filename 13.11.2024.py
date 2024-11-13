import random

# Úkol 1: Vytvořte nový soubor s alespoň sedmi písmeny ve slovech
def ukol_1(vstupni_soubor, vystupni_soubor):
    with open(vstupni_soubor, 'a+') as f:
        f.seek(0)
        obsah = f.read()
        if not obsah:
            f.write("toto je testovací text s některými velmi dlouhými slovy jako programování, inverzní, slovníček\n")

    with open(vstupni_soubor, 'r') as f:
        obsah = f.read()

    slova = obsah.split()
    dlouha_slova = [slovo for slovo in slova if len(slovo) >= 7]

    with open(vystupni_soubor, 'w') as f:
        for slovo in dlouha_slova:
            f.write(slovo + '\n')

# Úkol 2: Zapište řádky do jiného souboru
def ukol_2(vstupni_soubor, vystupni_soubor):
    with open(vstupni_soubor, 'r') as f:
        radky = f.readlines()

    with open(vystupni_soubor, 'w') as f:
        f.writelines(radky)

# Úkol 3: Inverzní pořadí řádků
def ukol_3(vstupni_soubor, vystupni_soubor):
    with open(vstupni_soubor, 'r') as f:
        radky = f.readlines()

    s_inverznim_poradim = radky[::-1]

    with open(vystupni_soubor, 'w') as f:
        f.writelines(s_inverznim_poradim)

# Úkol 4: Přidat hvězdičky po řádcích bez čárek
def ukol_4(vstupni_soubor, vystupni_soubor):
    with open(vstupni_soubor, 'r') as f:
        radky = f.readlines()

    radky_bez_carek = [radek for radek in radky if ',' not in radek]

    if radky_bez_carek:
        radky_bez_carek[-1] = radky_bez_carek[-1].rstrip('\n') + '\n************\n'
    else:
        radky.append('************\n')

    with open(vystupni_soubor, 'w') as f:
        f.writelines(radky)

# Úkol 5: Počet slov začínající na zadanou znakovou sadu
def ukol_5(vstupni_soubor, znakova_sada):
    with open(vstupni_soubor, 'r') as f:
        text = f.read()

    slova = text.split()
    pocet_slov = sum(1 for slovo in slova if slovo.startswith(znakova_sada))

    return pocet_slov

# Úkol 6: Nahraďte * za & a naopak
def ukol_6(vstupni_soubor, vystupni_soubor):
    with open(vstupni_soubor, 'r') as f:
        text = f.read()

    upraveny_text = text.replace('*', 'TEMP').replace('&', '*').replace('TEMP', '&')

    with open(vystupni_soubor, 'w') as f:
        f.write(upraveny_text)

# Úkol 7: Pole řetězců do souboru na jednotlivé řádky
def ukol_7(pole, vystupni_soubor):
    with open(vystupni_soubor, 'w') as f:
        for prvek in pole:
            f.write(prvek + '\n')

# Úkol 8: Inverzní pořadí pole řetězců do souboru
def ukol_8(pole, vystupni_soubor):
    with open(vystupni_soubor, 'w') as f:
        for prvek in reversed(pole):
            f.write(prvek + '\n')

# Úkol 9: Počet znaků v souboru
def ukol_9(vstupni_soubor):
    with open(vstupni_soubor, 'r') as f:
        text = f.read()

    pocet_znaku = len(text)

    return pocet_znaku

# Úkol 10: Počet řádků v souboru
def ukol_10(vstupni_soubor):
    with open(vstupni_soubor, 'r') as f:
        radky = f.readlines()

    pocet_radku = len(radky)

    return pocet_radku

# Hlavní funkce pro volání jednotlivých úkolů
def main():
    # Testování úkolů
    ukol_1('vstupni_soubor.txt', 'vystupni_soubor_1.txt')
    ukol_2('vstupni_soubor.txt', 'vystupni_soubor_2.txt')
    ukol_3('vstupni_soubor.txt', 'vystupni_soubor_3.txt')
    ukol_4('vstupni_soubor.txt', 'vystupni_soubor_4.txt')
    pocet_slov = ukol_5('vstupni_soubor.txt', 'z')
    print(f'Počet slov začínajících na "z": {pocet_slov}')
    ukol_6('vstupni_soubor.txt', 'vystupni_soubor_6.txt')
    ukol_7(['Ahoj', 'Svět', 'Python'], 'vystupni_soubor_7.txt')
    ukol_8(['Ahoj', 'Svět', 'Python'], 'vystupni_soubor_8.txt')
    pocet_znaku = ukol_9('vstupni_soubor.txt')
    print(f'Počet znaků v souboru: {pocet_znaku}')
    pocet_radku = ukol_10('vstupni_soubor.txt')
    print(f'Počet řádků v souboru: {pocet_radku}')

if __name__ == "__main__":
    main()
