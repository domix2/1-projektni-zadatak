from datetime import date
korisnik = {}
korisnik["ime"] = input("Unesite ime korisnika:").capitalize().strip()
korisnik["prezime"] = input("Unesite prezime korisnika:").capitalize().strip()
korisnik["telefon"] = int(input("Unesite telefon korisnika:"))
korisnik["email"] = input("Unesite email korisnika:").strip()
artikl = {}
artikl["naslov"] = input("Unesite naslov artikla:")
artikl["opis"] = input("Unesite opis artikla:")
artikl["cijena"] = float(input("Unesite cijenu artikla:"))
artikl["korisnik"] = korisnik
prodaja = {}
dan = int(input("Unesite dan isteka prodaje:"))
mjesec = int(input("Unesite mjesec isteka prodaje:"))
godina = int(input("Unesite godinu isteka prodaje:"))
prodaja["datum"] = date(godina, mjesec, dan)
prodaja["korisnik"] = korisnik
prodaja["artikl"] = artikl
print('Informacije o artiklu:')
print('\t\t Naslov:', prodaja["artikl"]["naslov"])
print('\t\t Opis:', prodaja["artikl"]["opis"])
print('\t\t Cijena:', prodaja["artikl"]["cijena"])
print('Datum isteka prodaje:')
print(f'\t\t Dan:', prodaja["datum"].day)
print(f'\t\t Mjesec:', prodaja["datum"].month)
print(f'\t\t Godina:', prodaja["datum"].year)
print('Informacije o korisniku:')
print(f'\t\t Ime:', prodaja["korisnik"]["ime"])
print(f'\t\t Prezime:', prodaja["korisnik"]["prezime"])
print(f'\t\t Telefon:', prodaja["korisnik"]["telefon"])
print(f'\t\t Email:', prodaja["korisnik"]["email"])