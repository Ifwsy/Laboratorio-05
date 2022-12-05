from personaje import Personaje

class Enano(Personaje):
    def __init__(self,n="",r="",a="",v="",d="",b="",c="",auvi=""):
        super().__init__(n,r,a,v,d,b)
        self.__clan=c
        self.__aumentoVida=auvi

    def __str__(self):
        return super().__str__()+" Clan: {} / Aumento de vida: {}".format(self.__clan,self.__aumentoVida)
    
    def GetClan(self):
        return self.__clan
    def GetAumentoVida(self):
        return self.__aumentoVida
    def SetClan(self,c):
        self.__clan=c
    def SetAumentoVida(self,auvi):
        self.__aumentoVida=auvi
    
    def AumentaVida(self,aumentoVida):
        aumentoHP = 0
        if aumentoVida >= 50 or aumentoVida <= 100 and self.__vida == 40:
            aumentoHP = aumentoVida
        return self.__vida + aumentoHP


"""
def aumentaVida(hum):
    aumentoHP = input("Ingrese su aumento de vida (Este debe estar entre 50 y 100)")
    vida = vida + aumentoHP
    hum.SetVida(vida)
"""
"""
aumentoHP = input("Ingrese su aumento de vida (Este debe estar entre 50 y 100)")
if vida == 10 and self.__vida >=50:
aumentoHP = aumentoHP
"""