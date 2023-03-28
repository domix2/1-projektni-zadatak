from datetime import date
korisnik = {}
ime = input("Unesite ime korisnika:").capitalize().strip()
prezime = input("Unesite prezime korisnika:").capitalize().strip()
telefon = str(input("Unesite telefon korisnika:")).strip()
email = input("Unesite email korisnika:").strip()
korisnik[ime] = prezime, telefon, email  # Spremam unesene ime,prezime,telefon i email u riječnik korisnik
artikl = {}
naslov = input("Unesite naslov artikla:")
opis = input("Unesite opis artikla:")
cijena = str(input("Unesite cijenu artikla:"))
artikl["naslov"] = opis, cijena
artikl["korisnik"] = korisnik
prodaja = {}
dan = int(input("Unesite dan isteka prodaje:"))
mjesec = int(input("Unesite mjesec isteka prodaje:"))
godina = int(input("Unesite godinu isteka prodaje:"))
datum = date(godina, mjesec, dan)
prodaja["datum"] = datum
prodaja["korisnik"] = korisnik
prodaja["artikl"] = artikl
print("Informacije o artiklu:", "\n\t Naslov:", naslov, "\n\t Opis:", opis, "\n\t Cijena:", cijena)
print("Datum isteka prodaje:", "\n\t Dan:", dan, "\n\t Mjesec:", mjesec, "\n\t Godina:", godina)
print("Informacije o korisniku:", "\n\t", ime,prezime, "\n\t Telefon:", telefon, "\n\t Email:", email)  #Ispisuje informacije