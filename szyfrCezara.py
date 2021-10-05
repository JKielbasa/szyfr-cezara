#importuje pakiet tkinter jako tk
import tkinter as tk

#importuje z pakietu functools funkcje partial
from functools import partial

# tworze okno programu 
okno = tk.Tk()

# przypisuje oknie wielkosc w pikselach
okno.geometry("350x350")

#nazwywam okno
okno.title("Szyfr Cezara")



# definiuje funkcje dla argumentow slowo i x 
def szyfr_cezara(zaszyfrowane_slowo, slowo, x):
    
    # pobieram wartosc z entry i przypisuje do zmiennej 
    slowo = (slowo.get())
    # pobieram wartosc z entry i przypisuje do zmniennej 
    x = (x.get()) 
      
    
    # definiuje zmienna ktora jest pustym stringiem
    nowe_slowo=""
    
    # tworze petle for ktorej zadaniem jest rozpoznanie malych i duzych liter we wprowadzonym do programu slowie
    for letter in slowo:
        
        # definiuje zmienne ktore odpowiada pokazuja czy litera jest mala czy duza 
        mala_litera=False
        duza_litera=False
       
        # zmieniam wartosc litery na wartosc z tablicy ASCII
        # jezeli wartosc z tablicy ASCII wprowadzonej litery jest miedzy 97 a 122 jest
        #ona odczytywana przez program jako mala litera 
        if ord(letter) >= 97 and ord(letter) <= 122:
            # jeseli lietra zostaa odczytana jako mala zmienna mala_lietra zmienia swoja wartosc na True
            mala_litera=True
        
        # zmieniam wartosc litery na wartosc z tablicy ASCII   
        # jeÅ¼eli wartosc z tablicy ASCII wprowadzonej litery jest miedzy 65 a 90 jest
        #ona odczytywana przez program jako mala litera     
        elif ord(letter) >= 65 and ord(letter) <= 90:
            # jezeli litera zostala odczytana jako duza zmienna duza_litera zmnienia swoja wartosc na True 
            duza_litera=True
       
        # jezeli literze nie zostala przyporzadkowana watrosc z tablicy ASCII ktora nie odpowiada zadnemu
        #z powyzszych zakresow to drukuje w konsole ta litere (znak) i pisze ze jest on nieprawidlowy 
        else:
            print(letter + ': nieprawidlowy znak')
        # zwracam wartosc funkcji jako None
            return None
        
        
        
        #deklaruje nowwa zmienna ktorej przypisuje wartosc litery z tablicy ASCII i odejmuje
        #do niej zmienna x ktora odpowiada za ilosc przesuniec daniej litery w szfrze po alfabecie
        nowa_litera = ord(letter) - x
        
        #jezeli litera jest litera mala to sprawdzam czy nowa litera miesci sie w zakresie malych liter w ASCII 
        if mala_litera:
            # jesli nowa litera wychodzi poza zakres to program przechodzi na poczatek
            #alfabetu i dodaje liczbe o jaka przekrozony zostal zakres 
            if nowa_litera < 97:
               nowa_litera = nowa_litera + 26
               
            
        # jezeli lietra jest litera duza to sprawdzam czy nowa litera nuescue sue w zajresie duzych liter ASCII    
        if duza_litera:
           # jesli nowa litera wychodzi poza zakres to program przechodzi na poczatek
           #alfabetu i dodaje liczbe o jaka przekroczony zostal zakres 
           if nowa_litera < 65:
                nowa_litera = nowa_litera + 26
            
        
        # przypisuje zmiennej nowa_litera wartosc stringu nowej litery 
        nowa_litera = chr(nowa_litera)
        
        
        # dodaje do wczesniej zadeklarowanego pustego stringu nowa litere
        nowe_slowo = nowe_slowo + nowa_litera 
        
        # nadaje atrybut zmiennej zaszyfrowane_slowo czyli tekst i wynik pracy funkci szyfr_cezara
        zaszyfrowane_slowo.config(text= "Zaszyfrowane słowo: %s" % nowe_slowo  )
        
        


# definiuje etykiety ktore sa wyswietlane w oknie
etykieta = tk.Label(okno, text="Zaszyfruj!")
etykieta2 = tk.Label(okno, text=" Słowo do zaszyfrowania: ") 
etykieta3 = tk.Label(okno, text=" O ile znakow chcesz przesunac litery? ")
zaszyfrowane_slowo = tk.Label(okno)

# ustalam gdzie maja byc wyswietlane etykiety
etykieta.grid(row=1, column=2)   
etykieta2.grid(row=2, column=1, sticky="E", pady=2) 
etykieta3.grid(row=3, column=1, sticky="E", pady=2)
zaszyfrowane_slowo.grid(row=5, column=1)


# zmienna reprezentujca wartosc entry
slowo = tk.StringVar()
x = tk.IntVar()


# definiuje pola do wpisywania dancy w okienku i przypisuje im wartosci wpisanych wyrazen w okienku 
pole_slowo =  tk.Entry(okno, textvariable = slowo)
pole_x = tk.Entry(okno, textvariable = x)

# ustalam gdzie maja byc wyswietlane pola do wpisywania
pole_slowo.grid(row=2, column=2, pady=2)
pole_x.grid(row=3, column=2, pady=2)

# uzywam funkcji partial aby dodac warosci do funkci szyfr_cezara
szyfr_cezara = partial(szyfr_cezara, zaszyfrowane_slowo, slowo, x)

# definiuje przycisk ktory po nacisniecu na niego wywoal funkcje szyfr_cezara
przycisk = tk.Button(okno, text ="Szyfruj", command = szyfr_cezara)
przycisk.grid(row = 4, column = 2, pady=2)   


# zapetlam wyswietlanie okienka
okno.mainloop()
