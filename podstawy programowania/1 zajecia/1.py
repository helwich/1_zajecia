print("sa")
print(2)

# potęgowanie
pow = 2 ** 10
print(pow)

# ciekawostka - mnozenei tekstu
text = "CDV"
print(text * 2)

#pobieranie danych z klawiatury
name = input()
print("Twoje imie: " + name)

surname = input()
print("Twoje imie: " + name + " a nazwisko " + surname)

lenght = len(surname)
print(lenght)



#----------

print("Podaj nazwisko")
surname = input()
print("Zmienna nazwisko jest typu ")
print(type(surname))
lenght = len(surname)
print("zmienna dlugosc jest type ")
print(type(lenght))

lenght = str(lenght)
print("po konwersji zmienna dlugosc jest type ")
print(type(lenght))



#--------------
zadanko do zrobienia:
#--------------

print("Podaj imie: ")
imie = input()

print("Podaj nazwisko: ")
nazwisko = input()

print("Podaj wiek: ")
wiek = input()

print("Twoje imie to: " + imie )
print("Twoje nazwisko to: " + nazwisko )
print("Masz : " + wiek + " lat" )
print("-----")
dlugoscNazwiska = len(nazwisko)
print("Długość twojego nazwiska to: " + str(dlugoscNazwiska) + " znaków")



#--------------------

'''
komentarz 


'''




#--------
tutaj nie przelacza na nastepna linie

print("\nPodaj swoj wiek: ", end="")
wiek = input()
print(wiek)



#----------------
ostatni znak

surname = "Kowalski"
firstLetter = surname[0]

lastLetter = surname[len(surname) - 1]
print(lastLetter)


#---------------
#konwersja

x = "5"
print(type(x))
x = int(x)
print(type(x))

# z calkowitej na zmiennoprzecinkowe

y = 4
print(type(y)) # int
y = y / 2
print(type(y)) # float
print(y)

surname = "Kowalski"
print(surname[0]) # 1 litera - K
print(surname[0:3]) # od 0 do 3 znaku - Kow
print(surname[-2]) # przed ostatnia litera - K
print(surname[-2:]) # Ki - od przedostatniego znaku do konca
print(surname[:-2]) #  Kowals - od pierwszego do przedostatniego
print(surname[:-2:2]) # 

#-----------------



