print("#######MINI BANKOMAT########")

stanje_računa = 500
while True:
    print("Birajte 1 za PROVJERU STANJA RAČUNA! ")
    print("Birajte 2 za UPLATU NOVCA NA RAČUN! ")
    print("Birajte 3 za PODIZANJE NOVCA S RAČUNA! ")
    print("Birajte 4 za IZLAZ!")
    izbor = input("Unesite broj: ")
    if izbor == "1":
        print(f"Stanje vašeg računa je {stanje_računa} €")
    elif izbor == "2":
        izbor2 = (int(input("Koliko novca želite uplatiti? €")))
        novo_stanje = izbor2 + stanje_računa
        print(f"Novo stanje računa je {novo_stanje}")

    elif izbor == "3":
        izbor3= (int(input("Koliko želite podignuti novca? €")))
        novo_stanje1 = novo_stanje - izbor3
        if izbor3 > novo_stanje:
            print("Nemate dovoljno novca!!")
        else:
            print(f"Trenutno stanje računa je {novo_stanje1}€")
    elif izbor == "4":
        print("Hvala što ste koristili bankomat,ugodan dan!!")
        break
    else:
        print("Neispravan odabir!!")

