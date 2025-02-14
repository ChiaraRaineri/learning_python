"""just say something to avoid problems"""

# ctrl + l to clear the console

#######

# List
# parentesi quadre []
# collezioni di dati ordinate, indicizzate, modificabili e permettono duplicati
# sono tipo gli array

x = ["milano", "roma", "napoli", "venezia"]   # tipi tutti uguali
y = ["ciao", 90, False]   # tipi mischiati

print(type(x))
print(len(x))

z = list(("milano", "roma", "napoli"))  # costruttore list (non mettere le parentesi quadre)
print(len(z))


print(x[0])  # l'indice è da 0 a 3 (è la lunghezza - 1)
print(x[2]) 
print(x[-1])  # parte dall'ultimo della lista
print(x[1:])  # tutti dopo l'1 compreso
print(x[1:3])  # 3 non incluso

x[0] = "brescia"  # riassegno il valore all'indice 0
x[1:3] = ["brescia", "udine"]  # sostituisco da 1 a 3 non compreso


# inserire elementi con append(), insert(), extend()

x = ["milano", "roma", "napoli", "venezia"]
y = ["brescia", "udine"]
x.append("brescia")  # inserisce il nuovo valore in fondo
x.insert(1, "brescia")  # inserisce il valore nuovo nell'indice 1 senza sostituire il valore esistente
x.extend(y)  # x prende anche i valori di y


# rimuovere elementi con remove(), pop(), del(), clear()

x.remove("milano")
x.pop(1)  # se non c'è dentro niente rimove l'ultimo
del x[0]
x.clear()  # pulisce la lista (ma x esiste ancora)


# ciclare gli element: for in, per indice, while e short hand

for citta in x:
    print(citta)

for i in range(len(x)):  # range di 4 numeri (0,1,2,3). per ogni indice del range manda a schermo i valori della lista
    print(x[i])

i = 0
while i < len(x):
    print(x[i])
    i +=1


# modificare l'ordine con asc, desc, reverse

x = ["udine", "roma", "napoli", "venezia", "ancona"]

x.sort()  # le mette in ordine alfabetico
print(x)
x.sort(reverse=True)  # ordine inverso

y = x  # non copia x, ma fa riferimento a x (se cambio y[0] cambio anche x[0])
y[0] = "new york"
print(x)

y = x.copy()  # crea una copia di x (indipendente)
y = list(X)  # crea una copia di x


# unire insieme più liste

x = ["udine", "bari", "napoli", "ancona"]
y = ["milano", "venezia"]

print(x + y)

for citta in y:
    x.append(citta)

print(x)

x.extend(y)



#######

# Tuple
# collezioni di dati ordinati, indicizzate, non modificabili e permettono duplicati
# parentesi tonde()


x = ("milano", "roma", "napoli")
y = ("milano", True, 56)

print(type(x))

z = ("milano",)  # tupla con un solo valore

print(len(x))

x = tuple(("milano", "roma", "napoli"))  # altro modo di creare una tuple

# usando gli indici possiamo fare le stesse cose delle list

if "milano" in x:
    print("ok")


# non è possibile modificare gli elementi nella tuple
# c'è un escamotage trasformando la tuple in una lista e ritrasformadola in una tuple
y = list(x)
y[0] = "venezia"
x = tuple(y)
print(x)


# spacchettare una tuple (unpack)

citta = ("milano", "roma", "napoli")

(x, y, z) = citta

print(x)
print(y)
print(z)  # se ci fossero altri valori dopo napoli, z diventa una lista con tutti i valori restanti


for citta in citta:
    print(citta)


# si possono unire le tuple con + (si crea una nuova tuple)

# count: quante volte un valore si trova nella tupla

lista_citta = ("milano", "roma", "napoli", "udine", "milano")

x = lista_citta.count("milano")
print(x)

x = lista_citta.index("udine")    # se è presente due volte prende la prima
print(x)



#######

# Set
# collezioni di dati non ordinate, non indicizzate, non modificabili e non permettono duplicati
# parentesi graffe (alt gr + maiusc + [)

# sia normale che mischiato

x = {"milano", "roma", "napoli"}

print(type(x))
print(len(x))

y = set(("milano", "roma", "napoli"))


# non posso indicizzare perché i valori non sono ordinati
print(x)  # ogni volta che faccio una run dà i valori in ordine casuale


# per accedere a un set bisogna usare un loop

for citta in x:
    print(citta)  # anche qui a ogni run vengono visualizzati in modo casuale


print("milano" in x)  # guardo se un elemento esiste nel set


# aggiungere e rimuovere elementi

x.add("venezia")  # aggiungere
print(x)

# unire un set a un altro
y = {"venezia", "udine"}
x.update(y)
print(x)


x.remove("milano")
x.discard("roma")  # se metto un elemento che non esiste, remove dà errore e discard non restituisce niente

x.pop()  # rimuove un elemento a caso

x.clear()  # set vuoto

del x   # x non esiste più


# unioni

x = {"milano", "roma", "napoli"}
y = {"venezia", "udine", "roma"}

# union() crea un nuovo set
z = x.union(y)
print(z)

x.update(y)  # non crea un nuovo set, ma aggiorna quello esistente
print(x)  # sia update che union escludono gli elementi duplicati

# per lavorare con gli elementi duplicati
x.intersection_update(y)  # resituisce solo i duplicati (lavora sul set esistente)

z = x.intersection(y)  # restituisce un nuovo set

# per tenere tutto tranne i duplicati
z = x.symmetric_difference(y)

x.symmetric_difference_update(y)

print(z)
print(x)



#######

# Dictionary
# collezioni di dati ordinate, modificabili, non permettono duplicati
# parentesi graffe (coppie chiave e valore)

persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}

print(persona)

# se ci fossero due "eta" per esempio ne metterebbe solo una (no duplicati)

print(type(persona))


# accedere agli elementi
print(persona["cognome"])

print(persona.get("nome"))

print(persona.keys())
print(persona.values())
print(persona.items())  # lista di tuple

print("nome" in persona)  # se una chiave esiste


# modificare gli elementi
persona["nome"] = "marco"
print(persona)

persona.update({"nome": "anna"})


# aggiungere elementi
persona["colore"] = "blu"

persona.update({"colore": "nero"})


# rimuovere elementi
persona.pop("nome")

persona.popitem()  # rimuove l'ultimo elemento

persona.clear() # dict vuoto

# del persona["nome"]


# ciclare gli elementi
for x in persona:
    print(x)  # manda a schermo la chiave

for x in persona:
    print(persona[x])  # manda a schermo il valore

for x in persona.values():
    print(x)

for x in persona.keys():
    print(x)

for x, y in persona.items():
    print(x, y)


# copiare dict

x = persona.copy()
print(x)


x = dict(persona)


# dict annidati

persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25,
    "indirizzo": {
        "citta": "milano",
        "cap": "00000",
        "civico": 45
    }
}

print(persona)

print(persona["indirizzo"]["civico"])
