from personaje import Personaje

class Elfo(Personaje):
    def __init__(self,n="",r="",a="",v="",d="",b="",rei=""):
        super().__init__(n,r,a,v,d,b)
        self.__reino=rei

    def __str__(self):
        return super().__str__()+" Reino: {}".format(self.__reino)
    
    def GetReino(self):
        return self.__reino
    def SetReino(self,rei):
        self.__reino=rei


    def QuitaVida(self):
        quitaHP = 10/100
        return self.__vida + quitaHP
