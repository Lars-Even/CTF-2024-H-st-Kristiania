penger = 250
caps = 0
gjødsel = 0
motorsag = 0
frontklipper = 0
traktor = 0
flag = False

caps_pris = 10
gjødsel_pris = 100
motorsag_pris = 1000
frontklipper_pris = 10000
traktor_pris = 100000
flag_pris = 1000000 

def start():
  
  print(f"Hva skjer, kompis? Hva vil du gjøre?\nDu har {penger} gelter!")

  while True:
    try:
        bruker_svar = int(input("""
    1. Se inventory.
    2. Handle hos felleskjøpet
    3. Avslutte
    > """))
    except ValueError:
       print("Whoooow! Du må kan kun bruke tall!")
       continue

    if(bruker_svar < 1 or bruker_svar > 3):
        print("--------------------------------")
        print("\n")
        print("Du har ikke så mange valg!!! :(")
        continue


    if(bruker_svar == 1):
        print("Her ser du alle tingene dine! Whoooaaw")
        print("--------------------------------------")
        
        if (caps and gjødsel and motorsag and frontklipper and traktor == 0):
            print("oi, du var fattig! :-(")
        if(caps != 0):
            print(f"{caps} x Caps: Er du en ekte råner med så mange caps?")
        if(gjødsel != 0):
            print(f"{gjødsel} x Gjødsel: Hva skal du med så mye gjødsel? Går det bra?")
        if(motorsag != 0):
            print(f"{motorsag} x Motorsag: Kanskje du finner flagget inne i trærne rundt bygget!!")
        if(frontklipper != 0):
            print(f"{frontklipper} x Frontklipere: Sjekk hvem som skal klippe plenen!")
        if(traktor != 0):
            print(f"{traktor} x Traktor: 100% sikker på at du liker John Deere!")
        if(flag == True):
            print("flag{c0f517c72b78e9404c29bbdde053df82}")

    elif(bruker_svar == 2):
        felleskjopet()
    elif(bruker_svar == 3):
        print("Avslutter programmet... Ha det bra, takk for at du handlet hos oss!")
        break




def felleskjopet():
    global penger
    global caps
    global gjødsel
    global motorsag
    global frontklipper
    global traktor
    global flag

    while True:
        print("Hva vil du kjøpe?")
        print(f"--- DU HAR {penger} KRONER ---")
        try:
            bruker_svar = int(input("""
    1. Caps
    2. Gjødsel
    3. Motorsag
    4. Frontklipper
    5. Traktor
    6. Flag
    7. Tilbake til menyen
    > """))
        except ValueError:
            print("Whoooow! Du må kan kun bruke tall!")

        if(bruker_svar == 1):
            if(penger < caps_pris):
                print("Du har ikke nok penger til å kjøpe en traktor.")
                print(f"!-- DU HAR {penger} KRONER --!")
                break

            print(f"")

            while True:
                try:
                    caps_input = input(f"Caps koster {caps_pris} kroner. Hvor mange capser ønsker du å kjøpe?\n    > ")

                    if not caps_input:
                        raise ValueError("Du må skrive inn et tall.")
                    cinput = int(caps_input)

                    if(penger <= (caps_pris*cinput)):
                        print(f"Du har ikke nok penger til å kjøpe {cinput} caps til {cinput*caps_pris} kroner!!\n")
                        break
                    
                    elif cinput < 0:
                        penger = penger + abs(cinput * caps_pris)
                        print(f"Gratulerer! Du har kjøpt {cinput} caps til {abs(caps_pris * cinput)} kroner!")
                        caps = caps + cinput
                        break
                    else:                            
                        penger = penger - (cinput * caps_pris)
                        print(f"Gratulerer! Du har kjøpt {cinput} caps for {cinput * caps_pris}")
                        caps = caps + cinput
                        break
                except ValueError:
                    print("Du kan ikke kjøpe med bokstaver, dumrian!")

        elif(bruker_svar == 2):
            if(penger < gjødsel_pris):
                print("Du har ikke nok penger til å kjøpe en traktor.")
                print(f"!-- DU HAR {penger} KRONER --!")
                break
            print(f"")
            
            
            while True:
                try:
                    gjødsel_input = input(f"Gjødsel koster {gjødsel_pris} per kilo. Hvor mye ønsker du og kjøpe?\n    > ")

                    if not gjødsel_input:
                        raise ValueError("Du må skrive inn et tall.")
                    ginput = int(gjødsel_input)
                    
                    if(penger <= (ginput*gjødsel_pris)):
                        print(f"Du har ikke nok penger til å kjøpe {ginput} kilo gjødsel til {gjødsel_pris*ginput}")
                        break
                    elif(ginput < 0):
                        penger = penger + abs(ginput*gjødsel_pris)
                        print(f"Gratulerer! Du har kjøpt {ginput} kilo gjødsel for {ginput*gjødsel_pris}!")
                        gjødsel = gjødsel + ginput
                        break                        
                    else:
                        penger = penger - (ginput * gjødsel_pris)
                        print(f"Gratulerer! Du har kjøpt {ginput} kilo gjødsel for {ginput*gjødsel_pris}!")
                        gjødsel = gjødsel + ginput
                        break
                except ValueError:
                    print(f"Kun tall! Prøv på nytt?")

        elif(bruker_svar == 3):
            if(penger < motorsag_pris):
                print("Du har ikke nok penger til å kjøpe en traktor.")
                print(f"!-- DU HAR {penger} KRONER --!")
                break

            
            while True:
                try:
                    motorsag_input = input(f"STIHL Motorsag koster {motorsag_pris} kroner. Hvor mange motorsager ønsker du å kjøpe?\n   > ")

                    if not motorsag_input:
                        raise ValueError("Du må skrive inn et tall.")
                    minput = int(motorsag_input)



                    if(penger <= (minput*motorsag_pris)):
                        print(f"Du har ikke nok penger til å kjøpe så mange motorsager :-//")
                        break
                    
                    elif(minput < 0):
                        penger = penger + abs(minput*motorsag_pris) 
                        print(f"Gratulerer! Du har kjøpt {minput} stykker for {minput*motorsag_pris}!")
                        motorsag = motorsag + minput
                        break
                    else:
                        penger = penger - (minput * motorsag_pris)
                        print(f"Gratulerer! Du har kjøpt {minput} stykker for {minput*motorsag_pris}!")
                        motorsag = motorsag + minput
                        break
                except ValueError:
                    print(f"Ikke riktig! Prøv igjen?")

        elif(bruker_svar == 4):
            if(penger < frontklipper_pris):
                print("Du har ikke nok penger til å kjøpe en traktor.")
                print(f"!-- DU HAR {penger} KRONER --!")
                break
            print(f"")


            while True:
                try:
                    frontklipper_input = input(f"Frontklippere koster {frontklipper_pris} per klipper. Hvor mange vil du kjøpe?\n    > ")

                    if not frontklipper_input:
                        raise ValueError("Du må skrive inn et tall.")
                    finput = int(frontklipper_input)



                    if(penger <= (finput*frontklipper_pris)):
                        print(f"Du har ikke nok penger til å kjøpe så mange motorsager :-//")
                        break
                    
                    elif(finput < 0):
                        penger = penger + abs(finput*frontklipper_pris) 
                        print(f"Gratulerer! Du har kjøpt {finput} for {finput*frontklipper_pris}!")
                        frontklipper = frontklipper + finput
                        break
                    else:
                        penger = penger - (finput * frontklipper_pris)
                        print(f"Gratulerer! Du har kjøpt {finput} for {finput*frontklipper_pris}!")
                        frontklipper = frontklipper + finput
                        break
                except ValueError:
                    print(f"Ikke riktig! Prøv igjen?")

        elif(bruker_svar == 5):
            if(penger < traktor_pris):
                print("Du har ikke nok penger til å kjøpe en traktor.")
                print(f"!-- DU HAR {penger} KRONER --!")
                break

            while True:
                try:
                    traktor_input = input(f"Trenger du og pløye jord? Traktorene koster {traktor_pris}\n    > ")

                    if not traktor_input:
                        raise ValueError("Kun tall.")
                    tinput = int(traktor_input)
                    
                    
                    if(penger < tinput*traktor_pris):
                        print("Du har ikke nok penger til å kjøpe så mange! :-///\n")
                        break
                    
                    elif(tinput < 0):
                        penger = penger + abs(tinput*traktor_pris)
                        print(f"Gratulerer! Du har kjøpt {tinput} traktor for {traktor_pris*tinput} kroner!\n")
                        traktor = tinput + traktor
                        break
                    else:                        
                        penger = penger - (tinput*traktor_pris)
                        print(f"Gratulerer! Du har kjøpt {tinput} traktor for {tinput*traktor_pris}!\n")
                        traktor = tinput + traktor
                        break

                except ValueError:
                    print("Kun tall.")

        elif(bruker_svar == 6):
            if(penger < flag_pris):
                print("Du har ikke nok penger til å kjøpe flagget!")
                print(f"!-- DU HAR {penger} KRONER --!")
                break
            
            while True:
                try:
                    flag_input = int(input(f"Flagget koster {flag_pris}. Hvor mange har du lyst på?\n   > "))
                    
                    if not flag_input:
                        raise ValueError("Du må skrive inn et tall.")
                    
                    if(penger < flag_input*flag_pris):
                        print("Du har ikke nok penger til å kjøpe så mange! :-(\n")
                        break
                    elif(flag_input < 0):
                        penger = penger + abs(flag_input*flag_pris)
                        print(f"Gratulerer! Du har kjøpt {flag_input} flagget for {flag_pris*flag_input} kroner!\n") 
                        flag = True
                        break
                    else:
                        penger = penger - (flag_input*flag_pris)
                        print(f"Gratulerer! Du har kjøpt {flag_input} flagget for {flag_input*flag_pris}!\n")
                        flag = True
                        break

                except ValueError:
                    print("Kun tall.")
        
        elif(bruker_svar == 7):
            break
start()