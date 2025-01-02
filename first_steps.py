"""just say something to avoid problems"""

messaggio = input("inserisci qualcosa:")

print(messaggio)

#######

# Variabili

X = 5

# nomi illegali: che iniziano con numero, che hanno spazi, che hanno trattini -

# camel case: pesoPersona
# pascal case: PesoPersona
# snake case: peso_person <- consigliato


x, y, z = 32, 100, 987  # tutte le variabili diverse
print(x)
print(y)
print(z)


A = B = C = 32  # tutte le variabili uguali


citta = ["roma", "milano", "napoli"]
r, m, n = citta
print(r)
print(m)
print(n)


Y = 8.5
Z = X + Y
print(Z)

#######

# Tipi di dati

print(type(X))

X = "ciao"
print(type(X))

# int: numeri interi
# float: numeri con la virgola
# str: stringa
# bool: True o False
# list: non sono array, sono es. x = ["roma", "milano", "napoli"]
# tuple: x = ("roma", "milano", "napoli")
# range: generatore di valori, x = range(60)
# dict: usano un rapporto chiave-valore
# set



#######

# Casting

# convertire un tipo di dato in un altro

X = "ciao sono "
Y = str(5)

X = 5
Y = int("5")

print(X + Y)



#######
# exercises

numero = 5
nome = "Mario"
pi = 3.14
vero_o_falso = True

numero_come_stringa = str(numero)  # converti in stringa
pi_come_intero = int(pi)  # converti in intero

x = 10
y = 20
z = "30"
print(x + y + int(z))


stringa1 = "Hello"
stringa2 = "world"
stringa_concatenata = stringa1 + " " + stringa2  # anche lo spazio è considerato un carattere
print(stringa_concatenata)


var_bool = True
print(type(var_bool) == bool)  # è vero o falso che la variabile è booleana?


lista = [1, 2, 3]
print(type(lista) == list)  # vogliamo sapere se è una lista



#######

# Stringhe

x = "ciao"  # stringhe a singola linea
y = 'ciao'  # singola o doppia virgoletta non conta

# stringa multilinea
z = """ciao
sono
chiara
wow"""

# le stringhe vengono trattate come array # una stringa è un insieme di tanti caratteri (possiamo accedere a ogni singolo carattere)
print(y[0])  # prende solo la prima lettera della parola ciao (per gli indici si parte sempre da 0)

print(len(y))  # quanti caratteri ci sono nella parola ciao (parte da 1)

for carattere in "computer":
    print(carattere)


print(x[:3])  # solo i primi 3 caratteri (da 0 al carattere 3 non compreso)
print(x[2:])  # da 2 compreso alla fine
print(z[2:7])  # conta anche lo spazio
print(x[-2])  # si prendono i caratteri partendo dalla fine

print(x.upper())  # tutto maiuscolo
print(x.lower())  # tutto minuscolo
print(x.strip())  # toglie lo spazio davanti e in fondo
print(x.replace("o", "w"))  # rimpiazza le o con delle w


# format  # come combinare numeri e stringhe
prova = "Ciao sono nato il {}"
print(prova.format(2))

prova2 = "Ciao sono nato il {2}, peso {0}, e alto {1}"  # uso gli indici
print(prova2.format(65, 1.70, 2))


# escape dei caratteri (voglio mettere qualcosa tra virgolette nel testo)
prova3 = "Ciao sono Chiara e sono \"figa\""
prova4 = 'Sono alla ricerca dell\'amore'

print(prova4)
print(prova4.split())
lista = prova4.split()
print(len(lista))  # quante parole ci sono nella lista



######

# Boolean

x = True
y = False


if 5 < 10:
    print("Sono minore di 10")
else:
    print("Sono maggiore di 10")



print(bool(1))  # Dice che è true, mentre per 0 è false

# I valori che danno sempre false sono:
    # bool(False)
    # bool(None)
    # bool(0)
    # bool("")
    # bool(())
    # bool([])
    # bool({})


##


pane = 0

if pane:                                      # se il pane esiste (non 0) 
    print("non andare al supermercato")
else:
    print("uscire a prendere il pane")


lista = ["pane", "latte"]

if lista: 
    print("andare al supermercato")
else:
    print("non andare al supermercato")




#######

# Operazioni aritmetiche 


# +
# - 
# / 
# *
# % (modulo, dà il resto della divisione) 
# ** (potenza) 
# // (floor division, risultato divisione arrotondato per difetto)

x = 5
y = 9


print(x / y)


# La precedenza ce l'hanno * e /, poi + e -


### Operatori di assegnamento (ce ne sono altre più complesse)

# Invece di scrivere questo
x = x + 2
#Scrivo questo
x += 2    # Vale per tutti gli operatori

print(x)




# min, max, abs (absolute), pow (potenza)

z = min(5, 10, 25)
z = abs(-5)
z = pow(4,3)

print(z)



#######

# if

x = 11

if 5 < 10:
    print("5 è minore di 10")  # se è falso e non metto else non mi manda a schermo niente 
# le cose fanno riferimento all'if solo se sono indentate (sennò si è fuori dall'if)

if x == 10:  # x uguale a 10, diverso è !=, maggiore uguale >=, minore uguale <=
    print("condizione verificata")
else:
    print("condizione non verificata")



if x < 10: 
    print("minore di 10")
elif x == 10:
    print("uguale a 10")  # ulteriore condizione (posso mettere quanti elif voglio, mentre if e else sono solo 1)
else:
    print("maggiore di 10")




if 10 <= x <= 20: 
    print("compreso tra 10 e 20")




# end, or, not

if x > 10 and x < 20:
    print("compreso tra 10 e 20")  # presuppone che entrambe le condizioni siano verificate


x = 11
y= 5

if x > 10 and y > 10:
    print("condizione verificata")
else:
    print("non verificata")


if x > 10 or y > 10:
    print("condizione verificata")  # almeno una è verificata
else:
    print("non verificata")



if not(x < 10): 
    print("condizione verificata")  # è una negazione
else:
    print("non verificata")


##

# scorciatoia

if x > 10: print ("è maggiore di 10")  # si può fare solo se c'è una sola istruzione dopo i due punti

print("è maggiore di 10") if x > 10 else print("è minore di 10")


##

# if innestati o annidati

# es. accetto solo i numeri pari (il resto della divisione deve dare 0)

if x % 2 == 0:  # numero pari
    print("numero pari")
    if(x < 10):
        print("numero pari e minore di 10")
else: 
    print("numero dispari, non mi interessa se è maggiore o minore di 10")


