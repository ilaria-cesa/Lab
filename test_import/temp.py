

if __name__ == "__main__": #fa una condizione per cui se realizzata lancia la funzione definita sopra
    print("ciao")
else:
    print("ciao ciao")

#MAIN viene mi serve per capire se sto lancuando il file direttamente o lo lanci da un altro file

def sum_thing(a, b):
    return a+b

if __name__ == "__main__": #fa una condizione per cui se realizzata lancia la funzione definita sopra
    print(sum_thing(2,7)) #qui me lo printa perche è il file dove ho scritto la funz mentre dall altra parte non mi printa 9 perche salta questo pezzo
