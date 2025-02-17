# Funzioni

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



#######

# Classi e oggetti
# programmazione a oggetti

# la classe è un'astrazione di una cosa reale (es. persone). le classi hanno delle proprietà (es. nome e cognome)

class persona:      # è come se fosse uno stampino
    nome = "Luca"
    cognome = "Rossi"

persona1 = persona()   # tutti gli oggetti (persona1, persona2...) derivano dalla stessa classe
persona2 = persona()

# un'istanza è l'oggetto specifico. istanza = oggetto che deriva da uno stampino

print(persona1.nome)  # così com'è è uguale a persona2


# Costruttore (è una funzione che viene chiamata automaticamente)

class Persona:
    def __init__(self, nome, cognome):   # self è il riferimento a se stesso (ci permette di capire che istanza è)
        self.nome = nome
        self.cognome = cognome

Persona1 = Persona("Luca", "Rossi")
Persona2 = Persona("Marco", "Verdi")


print(Persona1.nome)
print(Persona2.nome)




class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("ciao sono " + self.nome)

Persona1 = Persona("Luca", "Rossi")
Persona2 = Persona("Marco", "Verdi")

Persona1.saluta()
Persona2.saluta()


# il parametro self aiuta a capire di che istanza particolare si sta parlando

Persona2.nome = "Maria"
Persona2.saluta()



#######

# Programmazione a oggetti
# Ereditarietà

# è il concetto secondo cui una classe figlia che deriva da una classe madre eredità ciò che ha la classe madre più cose aggiuntive

class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("ciao sono " + self.nome)


class Insegnante(Persona):   # questa classe estende Persona (aggiunge cose extra)
    pass

person1 = Persona("Luca", "Rossi")
insegnante1 = Insegnante("Anna", "Neri")

person1.saluta()
insegnante1.saluta()


# costruttore della classe figlia
# overriding: qualsiasi funzione con lo stesso nome verrà sovrascritta

class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia   # è una cosa extra
        

person1 = Persona("Luca", "Rossi")
insegnante1 = Insegnante("Anna", "Neri", "Matematica")

insegnante1.saluta()

print(insegnante1.materia)


# saluta in modo diverso
class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia

    def saluta(self):
        print("buongiorno sono " + self.nome + " " + self.cognome)  # abbiamo fatto overriding

    def dai_voto(self):
        print("bravo, un bel 8")


insegnante1 = Insegnante("Anna", "Neri", "Matematica")
insegnante1.saluta()
insegnante1.dai_voto()

