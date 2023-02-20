
pojistenci = []

class pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, vek: {self.vek}, tel: {self.telefon}"


p1 = pojisteny("David", "Krupička", 25, "123456789")
p2 = pojisteny("Elena", "Santini", 30, "987654321")

pojistenci.append(p1)
pojistenci.append(p2)

class EvidencePojistencu:
    def __init__(self):
        self.pojistenci = []

    def pridat_pojisteneho(self, pojisteny):
        self.pojistenci.append(pojisteny)

    def zobrazit_pojistene(self):
        for pojisteny in self.pojistenci:
                print(pojisteny)

    def vyhledat_pojistene(self, kriteria):
            nalezeni_pojistenci = []
            for pojisteny in self.pojistenci:
                if kriteria.lower() in pojisteny.jmeno.lower() or kriteria.lower() in pojisteny.prijmeni.lower():
                    nalezeni_pojistenci.append(pojisteny)
            return nalezeni_pojistenci

evidence = EvidencePojistencu()

while True:

    print("=====================")
    print("Evidence pojistenych")
    print("=====================")
    print("Vyberte si akci")
    print("1 - Pridat noveho pojisteneho")
    print("2 - Vypsat vsechny pojistene")
    print("3 - Vyhledat pojisteneho")
    print("4 - Konec")
    volba = input(" ")

    if volba.lower() == "1":
        jmeno = input("Zadejte jméno pojištěnce: ")
        prijmeni = input("Zadejte příjmení pojištěnce: ")
        vek = int(input("Zadejte věk pojištěnce: "))
        telefon = input("Zadejte telefon pojištěnce: ")
        print("Pojištěnec byl úspěšně přidán do evidence")
        input("Stiskněte libovolnou klávesu pro pokračování")

    elif volba.lower() == "2":
        for pojisteny in pojistenci:
            print(pojisteny)
        input("Stiskněte  libovolnou klávesu pro pokračování")

    elif volba.lower() == "3":
        jmeno = input("Zadejte jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení pojištěného: ")
        nalezeni_pojistenci = []

        for pojisteny in pojistenci:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                nalezeni_pojistenci.append(pojisteny)

        if len(nalezeni_pojistenci) > 0:
            for pojisteny in nalezeni_pojistenci:
                print(
                    f"Jméno: {pojisteny.jmeno}, Příjmení: {pojisteny.prijmeni}, Věk: {pojisteny.vek}, Telefon: {pojisteny.telefon}")
        else:
            print("Osoba není v seznamu")
        input("Stiskněte  libovolnou klávesu pro pokračování")

    elif volba.lower() == "4":
        print("Děkuji za použití evidence")

    else:
        print("Chybná volba")
