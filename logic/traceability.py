class Traceability(object):
    
    def __init__(self, TrackingCode: int = 0, Description: str = 'Description', Date: int = 0, Hour: int = 0, ShippingID: int = 0)-> object:
        self.__TrackingCode = TrackingCode
        self.__Description = Description
        self.__Date = Date
        self.__Hour = Hour
        self.__ShippingID = ShippingID
        
    @property
    def TrackingCode(self) -> int:
        return self.__TrackingCode

    @TrackingCode.setter
    def TrackingCode(self, TrackingCode: int):
        self.__TrackingCode = TrackingCode
        
    @property
    def Description(self) -> str:
        return self.__Description

    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description
    
    @property
    def Date(self) -> int:
        return self.__Date

    @Date.setter
    def Date(self, Date: int):
        self.__Date = Date
        
    @property
    def Hour(self) -> int:
        return self.__Hour

    @Hour.setter
    def Hour(self, Hour: int):
        self.__Hour = Hour

    @property
    def ShippingID(self) -> int:
        return self.__ShippingID

    @ShippingID.setter
    def ShippingID(self, ShippingID: int):
        self.__ShippingID = ShippingID
        
    def diccionario(self):
        return {"TrackingCode": self.TrackingCode, "Description": self.Description, "Date": self.Date, "Hour": self.Hour, "ShippingID": self.ShippingID}
        
    def __str__(self):
        return str({"TrackingCode": self.TrackingCode, "Description": self.Description, "Date": self.Date, "Hour": self.Hour, "ShippingID": self.ShippingID})
        
if __name__ == '__main__':
    Traza_edwin = Traceability(TrackingCode = 123, Description = "delicado", Date = 12345, Hour = 24, ShippingID = 1)
    print(Traza_edwin)