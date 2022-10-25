class Shipment_details(object):
    
    def __init__(self, DetailShipping: int = 0, ShippingType: str = 'ShippingType', ShippingCost: int = 0)-> object:
        self.__DetailShipping = DetailShipping
        self.__ShippingType = ShippingType
        self.__ShippingCost = ShippingCost
        
    @property
    def DetailShipping(self) -> int:
        return self.__DetailShipping

    @DetailShipping.setter
    def DetailShipping(self, DetailShipping: int):
        self.__DetailShipping = DetailShipping
        
    @property
    def ShippingType(self) -> str:
        return self.__ShippingType

    @ShippingType.setter
    def ShippingType(self, ShippingType: str):
        self.__ShippingType = ShippingType
    
    @property
    def ShippingCost(self) -> int:
        return self.__ShippingCost

    @ShippingCost.setter
    def ShippingCost(self, ShippingCost: int):
        self.__ShippingCost = ShippingCost

    def diccionario(self):
        return {"DetailShipping": self.DetailShipping, "ShippingType": self.ShippingType, "ShippingCost": self.ShippingCost}
    
    def __str__(self):
        return str({"DetailShipping": self.DetailShipping, "ShippingType": self.ShippingType, "ShippingCost": self.ShippingCost})
        
if __name__ == '__main__':
    detalles_edwin = Shipment_details(DetailShipping = 123, ShippingType = "terrestre", ShippingCost = 1000)
    print(detalles_edwin)