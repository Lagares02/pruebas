class Invoice(object):
    
    def __init__(self, InvoiceID: int = 1 , ShipmentID: int = 0, PackID: int = 0, FactDate: int = 0, Quantity: int = 0, Subtotal: int = 0, ShippingCost: int = 0, Total: int = 0)-> object:
        self.__InvoiceID = InvoiceID
        self.__ShipmentID = ShipmentID
        self.__PackID = PackID
        self.__FactDate = FactDate
        self.__Quantity = Quantity
        self.__Subtotal = Subtotal
        self.__ShippingCost = ShippingCost
        self.__Total = Total
        
    @property
    def InvoiceID(self) -> int:
        return self.__InvoiceID
    
    @InvoiceID.setter
    def InvoiceID(self, InvoiceID: int):
        self.__InvoiceID = InvoiceID    
    
    @property
    def ShipmentID(self) -> int:
        return self.__ShipmentID

    @ShipmentID.setter
    def ShipmentID(self, ShipmentID: int):
        self.__ShipmentID = ShipmentID
        
    @property
    def PackID(self) -> int:
        return self.__PackID

    @PackID.setter
    def PackID(self, PackID: int):
        self.__PackID = PackID
    
    @property
    def FactDate(self) -> int:
        return self.__FactDate

    @FactDate.setter
    def FactDate(self, FactDate: int):
        self.__FactDate = FactDate
        
    @property
    def Quantity(self) -> int:
        return self.__Quantity

    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity
        
    @property
    def Subtotal(self) -> int:
        return self.__Subtotal

    @Subtotal.setter
    def Subtotal(self, Subtotal: int):
        self.__Subtotal = Subtotal
        
    @property
    def ShippingCost(self) -> int:
        return self.__ShippingCost

    @ShippingCost.setter
    def ShippingCost(self, ShippingCost: int):
        self.__ShippingCost = ShippingCost
        
    @property
    def Total(self) -> int:
        return self.__Total

    @Total.setter
    def Total(self, Total: int):
        self.__Total = Total
        
    def diccionario(self):
        return {"InvoiceID": self.InvoiceID, "ShipmentID": self.ShipmentID, "PackID": self.PackID, "FactDate": self.FactDate, "Quantity": self.Quantity, "Subtotal": self.Subtotal, "ShippingCost": self.ShippingCost, "Total": self.Total}
        
    def __str__(self):
        return str({"InvoiceID": self.InvoiceID, "ShipmentID": self.ShipmentID, "PackID": self.PackID, "FactDate": self.FactDate, "Quantity": self.Quantity, "Subtotal": self.Subtotal, "ShippingCost": self.ShippingCost, "Total": self.Total})
        
if __name__ == '__main__':
    Factura_edwin = Invoice(InvoiceID = 1, ShipmentID = 2, PackID = 3, FactDate = " ", Quantity = 100, Subtotal = 1500, ShippingCost = 500, Total = 2000)
        
    print(Factura_edwin)