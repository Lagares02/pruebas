class Shipment(object):
    
    def __init__(self, ShipmentID: int = 1 , DateCreated: int = 0, IDDestinityPerson: int = 0, DestinationAddress: str = 'DestinationAddress', EstimatedArrivalDate: int = 0, ClientID: int = 0, DetailShipping: int = 0)-> object:
        self.__ShipmentID = ShipmentID
        self.__DateCreated = DateCreated
        self.__IDDestinityPerson = IDDestinityPerson
        self.__DestinationAddress = DestinationAddress
        self.__EstimatedArrivalDate = EstimatedArrivalDate
        self.__ClientID = ClientID
        self.__DetailShipping = DetailShipping
        
    @property
    def ShipmentID(self) -> int:
        return self.__ShipmentID

    @ShipmentID.setter
    def ShipmentID(self, ShipmentID: int):
        self.__ShipmentID = ShipmentID
        
    @property
    def DateCreated(self) -> int:
        return self.__DateCreated

    @DateCreated.setter
    def DateCreated(self, DateCreated: int):
        self.__DateCreated = DateCreated
    
    @property
    def IDDestinityPerson(self) -> int:
        return self.__IDDestinityPerson

    @IDDestinityPerson.setter
    def IDDestinityPerson(self, IDDestinityPerson: int):
        self.__IDDestinityPerson = IDDestinityPerson
        
    @property
    def DestinationAddress(self) -> str:
        return self.__DestinationAddress

    @DestinationAddress.setter
    def DestinationAddress(self, DestinationAddress: str):
        self.__DestinationAddress = DestinationAddress
        
    @property
    def EstimatedArrivalDate(self) -> int:
        return self.__EstimatedArrivalDate

    @EstimatedArrivalDate.setter
    def EstimatedArrivalDate(self, EstimatedArrivalDate: int):
        self.__EstimatedArrivalDate = EstimatedArrivalDate
        
    @property
    def ClientID(self) -> int:
        return self.__ClientID

    @ClientID.setter
    def ClientID(self, ClientID: int):
        self.__ClientID = ClientID
        
    @property
    def DetailShipping(self) -> int:
        return self.__DetailShipping

    @DetailShipping.setter
    def DetailShipping(self, DetailShipping: int):
        self.__DetailShipping = DetailShipping
        
    def diccionario(self):
        return {"ShippingID": self.ShipmentID, "DateCreated": self.DateCreated, "IDDestinyPerson": self.IDDestinityPerson, "DestinationAddress": self.DestinationAddress, "EstimatedArrivalDate": self.EstimatedArrivalDate, "ClientID": self.ClientID, "DetailShipping": self.DetailShipping}
        
    def __str__(self):
        return str({"ShippingID": self.ShipmentID, "DateCreated": self.DateCreated, "IDDestinyPerson": self.IDDestinityPerson, "DestinationAddress": self.DestinationAddress, "EstimatedArrivalDate": self.EstimatedArrivalDate, "ClientID": self.ClientID, "DetailShipping": self.DetailShipping})
        
if __name__ == '__main__':
    Envio_edwin = Shipment(ShipmentID = 1, DateCreated = 100, IDDestinityPerson = 54321, DestinationAddress = "Cartagena", EstimatedArrivalDate = " ", ClientID = 123, DetailShipping = 12)
    print(Envio_edwin)