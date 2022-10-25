class Client(object):
    
    def __init__(self, ClientID: int = 1 , Name: str = 'Name', Surname: str = 'Surname', Direction: str = 'Direction', Phone: int = 0)-> object:
        self.__ClientID = ClientID
        self.__Name = Name
        self.__Surname = Surname
        self.__Direction = Direction
        self.__Phone = Phone
        
    @property
    def ClientID(self) -> int:
        return self.__ClientID

    @ClientID.setter
    def ClientID(self, ClientID: int):
        self.__ClientID = ClientID
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name
        
    @property
    def Surname(self) -> str:
        return self.__Surname

    @Surname.setter
    def Surname(self, Surname: str):
        self.__Surname = Surname
        
    @property
    def Direction(self) -> str:
        return self.__Direction

    @Direction.setter
    def Direction(self, Direction: str):
        self.__Direction = Direction
        
    @property
    def Phone(self) -> str:
        return self.__Phone

    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone
        
    def diccionario(self):
        return {"ClientID": self.ClientID, "Name": self.Name, "Surname": self.Surname, "Direction": self.Direction, "Phone": self.Phone}
        
    def __str__(self):
        return str({"ClientID": self.ClientID, "Name": self.Name, "Surname": self.Surname, "Direction": self.Direction, "Phone": self.Phone})
        
if __name__ == '__main__':
    edwin = Client(ClientID = 12345, Name = "Edwin", Surname = "Puertas", Direction = "Cartagena", Phone = "3020000")
    print(edwin)