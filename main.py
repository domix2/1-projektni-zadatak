from datetime import date
korisnik = {}
ime = input("Unesite ime korisnika:").capitalize()
prezime = input("Unesite prezime korisnika:").capitalize()
telefon = str(input("Unesite telefon korisnika:")).strip()
email = input("Unesite email korisnika:").strip()
korisnik[ime] = prezime, telefon, email  # Spremam unesene ime,prezime,telefon i email u riječnik korisnik
artikl = {}
naslov = input("Naslov:")
opis = input("Opis:")
cijena = str(input("Cijena:"))
artikl["naslov"] = opis, cijena
artikl["korisnik"] = korisnik
prodaja = {}
dan = int(input("Dan:"))
mjesec = int(input("Mjesec:"))
godina = int(input("Godina:"))
datum = date(godina, mjesec, dan)
prodaja["datum"] = datum
prodaja["korisnik"] = korisnik
prodaja["artikl"] = artikl
print("Informacije o artiklu:", "\n\t Naslov:", naslov, "\n\t Opis:", opis, "\n\t Cijena:", cijena)
print("Datum isteka prodaje:", "\n\t Dan:", dan, "\n\t Mjesec:", mjesec, "\n\t Godina:", godina)
print("Informacije o korisniku:", "\n\t", ime, prezime, "\n\t Telefon:", telefon, "\n\t Email:", email)  #Ispisuje informacije