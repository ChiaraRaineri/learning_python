# FUNZIONI

def fai_la_pasta():  # definizione
    print("metti l'acqua")
    print("fai bollire")
    print("metti la pasta")

fai_la_pasta()


# parametri in funzione (il parametro è la variabile generica che utilizziamo nella definizione della variabile)

def fai_la_pasta(tipo_pasta):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)

fai_la_pasta("fusilli")  # argomento: valore effettivo che va al posto del parametro


def fai_la_pasta(tipo_pasta, metti_sugo):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    if metti_sugo:
        print("prepara sugo")  # è un boolean

fai_la_pasta("spaghetti", True)


# arbitrary arguments (non sappiamo quanti parametri metteremo)

def fai_la_pasta(*opzioni):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + opzioni[0])
    if opzioni[1]:
        print("prepara sugo")

fai_la_pasta("fusilli", True)


# keyword arguments

def fai_la_pasta(tipo_pasta, sugo):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    if sugo:
        print("prepara sugo")

fai_la_pasta(sugo = True, tipo_pasta = "fusilli")


# parametri di default

def fai_la_pasta(tipo_pasta = "spaghetti"):  # di default faccio gli spaghetti
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)

fai_la_pasta()


# return dei valori

def fai_somma(num1, num2):
    somma = num1 + num2
    return somma

x = fai_somma(2, 2)
print(x)
