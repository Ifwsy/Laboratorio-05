from enano import Enano
from elfo import Elfo
from humano import Humano
import random

#P1
listaEN=[]
listaEL=[]
listaHU=[]
#P2
listaP2=["Elfo","Enano","Humano"]


def IngresaDatos():
    print("***Kombat Textual***")
    nombre = input("Ingrese el nombre de su personaje: ").capitalize() #Nombre
    print("Elfo, Enano o Humano") #Raza
    global raza
    raza = input("Elija una de las razas disponibles: ").capitalize()
    while raza != "Elfo" and raza != "Enano" and raza != "Humano":
        print("Elija una de las opiones disponibles!!!")
        print("Elfo, Enano o Humano")
        raza = input("Elija una de las razas disponibles: ").capitalize()
    print("'Espada' / 'Hacha' / 'Arco'") #Arma
    arma = input("Elija un tipo de arma: ").capitalize()
    while arma != "Espada" and arma != "Hacha" and arma != "Arco":
        print("Elija una de las opiones disponibles!!!")
        print("'Espada' / 'Hacha' / 'Arco'")
        arma = input("Elija un tipo de arma: ").capitalize()
    if raza == "Elfo":
        print("La vida debe ser entre 40 y 100")
        vida = int(input("Ingrese la vida que desee: "))
        while vida < 40 or vida > 100:
            print("La vida debe ser entre 40 y 100!!!")
            vida = int(input("Ingrese la vida que desee: "))
        if arma == "Espada":
            daño = 41
        elif arma == "Hacha":
            daño = 35
        elif arma == "Arco":
            daño = 23
        bonificacion = ("Se le quita el 10% de su vida")
        reino = input("Ingresa tu reino: ").capitalize()
        quitaHP = 10/100
        elf = Elfo()
        elf.SetNombre(nombre)
        elf.SetRaza(raza)
        elf.SetArma(arma)
        #elf.SetVida(vida)
        elf.SetVida(float(vida-quitaHP))
        elf.SetDaño(daño)
        elf.SetBonificacion(bonificacion)
        elf.SetReino(reino)
        listaEL.append(elf)
    if raza == "Enano":
        vida = 23
        if arma == "Espada":
            daño = 41
        elif arma == "Hacha":
            daño = 35
        elif arma == "Arco":
            daño = 23
        bonificacion = ("Aumento de la vida ")
        clan = input("Ingresa el nombre de tu clan: ").capitalize()
        try:
            print("El aumento de vida debe estar entre 50 y 100")
            aumentoVida = int(input("Ingresa el aumento de vida que desees: "))
            while aumentoVida <=49 or aumentoVida >= 101:
                print("El aumento de vida debe estar entre 50 y 100!!!")
                aumentoVida = int(input("Ingresa el aumento de vida que desees: "))
        except UnboundLocalError:
            print("No ingreso los valores correctamente")
        except ValueError:
            print("No ingreso los valores correctos")
        ena = Enano()
        ena.SetNombre(nombre)
        ena.SetRaza(raza)
        ena.SetArma(arma)
        #ena.SetVida(vida)
        ena.SetVida(vida+aumentoVida)
        ena.SetDaño(daño)
        ena.SetBonificacion(bonificacion)
        #ena.SetVida(ena.SetAumentoVida(ena.SetVida()))
        ena.SetAumentoVida(aumentoVida)
        ena.SetClan(clan)
        listaEN.append(ena)
    if raza == "Humano":
        vida = 80
        if arma == "Espada":
            daño = 41
        elif arma == "Hacha":
            daño = 35
        elif arma == "Arco":
            daño = 23
        bonificacion = ("Aumento del daño ")
        familia = input("Ingresa el nombre de tu familia: ").capitalize()
        hum = Humano()
        hum.SetNombre(nombre)
        hum.SetRaza(raza)
        hum.SetArma(arma)
        hum.SetVida(vida)
        hum.SetDaño(daño)
        hum.SetBonificacion(bonificacion)
        hum.SetFamilia(familia)
        listaHU.append(hum)

def Combate(lista,raza):
    P2=random.choice(listaP2)
    print("Bienvenido guerrero, mi nombre es Erke y esta es mi arena, LA GRAN ARENA DE PEFKA!!!")
    print("Comienza la ronda 1!!")
    print("Y tu enemigo sera un",P2)
    ronda = 1
    while ronda <=10:
        if raza == "Elfo":
            print("Eres de la raza ",raza)
            vida = listaEL[3]
            print("Tu vida es de",vida)
            #print(P2)
            accion = input("Atacar o retirarse").capitalize()
            if accion == "Atacar":
                pass
            elif accion == "Retirarse":
                pass
        elif raza == "Enano":
            print("Eres de la raza ",raza)
            vida = listaEN[3]
            print("Tu vida es de",vida)
            #print(P2)
            accion = input("Atacar o retirarse").capitalize()
            if accion == "Atacar":
                pass
            elif accion == "Retirarse":
                pass  
        elif raza == "Humano":
            print("Eres de la raza ",raza)
            vida = listaHU[3]
            print("Tu vida es de",vida)
            #print(P2)
            daño = listaHU[4]
            print("NOTA: Con el pasar de las rondas se le ira restando 1 a su daño")
            try:
                dañoin = int(input("Ingrese el aumento de daño deseado: "))
                dañof = daño + dañoin
                print("Su daño ha aumentado a ",dañof)
            except ValueError:
                print("No ingreso los valores correctos")
            accion = input("Atacar o retirarse").capitalize()
            if accion == "Atacar":
                pass
            elif accion == "Retirarse":
                pass
    print("El ganador es ")

def VerDatos(lista):
    for i in range(len(lista)):
        print(str(lista[i]))

def main():
    IngresaDatos()
    VerDatos(listaEL)
    VerDatos(listaEN)
    VerDatos(listaHU)
    if raza == "Elfo":
        Combate(listaEL,Elfo)
    elif raza == "Enano":
        Combate(listaEN,Enano)
    elif raza == "Humano":
        Combate(listaHU,Humano)
    VerDatos(listaEL)
    VerDatos(listaEN)
    VerDatos(listaHU)
main()



