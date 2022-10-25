class Package(object):
    
    def __init__(self, PackID: int = 1 , Dimensions: int = 0, Weigth: int = 0, Type: str = 'Type', Condition: str = 'Condition', Observations: str = 'Observations')-> object:
        self.__PackID = PackID
        self.__Dimensions = Dimensions
        self.__Weigth = Weigth
        self.__Type = Type
        self.__Condition = Condition
        self.__Observations = Observations
        
    @property
    def PackID(self) -> int:
        return self.__PackID

    @PackID.setter
    def PackID(self, PAckID: int):
        self.__PackID = PAckID
        
    @property
    def Dimensions(self) -> int:
        return self.__Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions: int):
        self.__Dimensions = Dimensions
    
    @property
    def Weigth(self) -> int:
        return self.__Weigth

    @Weigth.setter
    def Weigth(self, Weigth: int):
        self.__Weigth = Weigth
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type
        
    @property
    def Condition(self) -> str:
        return self.__Condition

    @Condition.setter
    def Condition(self, Condition: str):
        self.__Condition = Condition
        
    @property
    def Observations(self) -> str:
        return self.__Observations

    @Observations.setter
    def Observations(self, Observations: str):
        self.__Observations = Observations
        
    def diccionario(self):
        return {"PackID": self.PackID, "Dimensions": self.Dimensions, "Weigth": self.Weigth, "Type": self.Type, "Condition": self.Condition, "Observations": self.Observations}
    
    def __str__(self):
        return str({"PackID": self.PackID, "Dimensions": self.Dimensions, "Weigth": self.Weigth, "Type": self.Type, "Condition": self.Condition, "Observations": self.Observations})
        
if __name__ == '__main__':
    Paquete_edwin = Package(PackID = 12345, Dimensions = 100, Weigth = 1000, Type = "big", Condition = "good", Observations = "nothing")
    print(Paquete_edwin)
    