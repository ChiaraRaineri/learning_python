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
