class Personaje():
    def __init__(self,n="",r="",a="",v="",d="",b=""):
        self.__nombre=n
        self.__raza=r
        self.__arma=a
        self.__vida=v
        self.__daño=d
        self.__bonificacion=b
    
    def __str__(self):
        return "Nombre: {} / Raza: {} / Arma: {} / Vida: {} / Daño: {} / Bonificación: {} /".format(self.__nombre,self.__raza,self.__arma,self.__vida,self.__daño,self.__bonificacion)

    def GetNombre(self):
        return self.__nombre
    def GetRaza(self):
        return self.__raza
    def GetArma(self):
        return self.__arma
    def GetVida(self):
        return self.__vida
    def GetDaño(self):
        return self.__daño
    def GetBonificacion(self):
        return self.__bonificacion

    def SetNombre(self,n):
        self.__nombre=n
    def SetRaza(self,r):
        self.__raza=r
    def SetArma(self,a):
        self.__arma=a
    def SetVida(self,v):
        self.__vida=v
    def SetDaño(self,d):
        self.__daño=d
    def SetBonificacion(self,b):
        self.__bonificacion=b

    
    def Historia(self,raza):
        if raza == "Elfo":
            print("Eres un caballero, con un sentido de la justicia inquenbrantable inquebrantable")
        elif raza == "Enano":
            print("Eres ")
        elif raza == "Hombre":
            print("Vivio en una aldea una vez")
            
    def Victoria(self):
        pass
    def Derrota(self,raza):
        if raza=="Elfo":
                print("")
    def MensajeInicial(self):
        pass