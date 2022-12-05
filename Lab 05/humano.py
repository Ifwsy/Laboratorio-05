from personaje import Personaje

class Humano(Personaje):
    def __init__(self, n="", r="", a="", v="", d="", b="",f=""):
        super().__init__(n, r, a, v, d, b)
        self.__familia=f

    def __str__(self):
        return super().__str__()+" Familia: {}".format(self.__familia)

    def GetFamilia(self):
        return self.__familia
    def SetFamilia(self,f):
        self.__familia=f
    
    def SuperBono(self):
        pass
    