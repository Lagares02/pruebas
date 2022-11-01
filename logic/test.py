import unittest
from logic.client import Client
from logic.package import Package
from logic.invoice import Invoice
from logic.shipment import Shipment
from logic.shipment_details import Shipment_details
from logic.traceability import Traceability


class TestClient(unittest.TestCase):
    person = Client(ClientID = 1 , Name = 'Name', Surname = 'Surname', Direction = 'Direction', Phone = 0)

    def test_instance(self):
        self.assertIsInstance(self.person, Client, "Its instance!")

    def test_ClientID(self):
        self.assertEqual(self.person.ClientID, 1)

    def test_Name(self):
        self.assertEqual(self.person.Name, 'Name')

    def test_Surname(self):
        self.assertEqual(self.person.Surname, 'Surname')
        
    def test_Direction(self):
        self.assertEqual(self.person.Direction, 'Direction')
        
    def test_Phone(self):
        self.assertEqual(self.person.Phone, 0)

    def test__str__(self):
        self.assertEqual(self.person.__str__(), {'ClientID': 1, 'Name': 'Name', 'Surname': 'Surname', 'Direction': 'Direction', 'Phone': 0})

class TestPackage(unittest.TestCase):
    object = Package(PackID = 1 , Dimensions = 0, Weigth = 0, Type = 'Type', Condition = 'Condition', Observations = 'Observations')
    
    def test_instance(self):
        self.assertIsInstance(self.object, Package, "its instance!")
    
    def test_PackageID(self):
        self.assertEqual(self.object.PackID, 1)

    def test_Dimensions(self):
        self.assertEqual(self.object.Dimensions, 0)

    def test_Weigth(self):
        self.assertEqual(self.object.Weigth, 0)
        
    def test_Type(self):
        self.assertEqual(self.object.Type, 'Type')
        
    def test_Condition(self):
        self.assertEqual(self.object.Condition, 'Condition')
        
    def test_Observations(self):
        self.assertEqual(self.object.Observations, 'Observations')

    def test__str__(self):
        self.assertEqual(self.object.__str__(), {'PackageID': 1, 'Dimension': 0, 'Weigth': 0, 'Type': 'Type', 'Condition': 'Condition', 'Observations': 'Observations'})

class TestInvoice(unittest.TestCase):
    report = Invoice(InvoiceID = 1 , ShipmentID = 0, PackID = 0, FactDate = 0, Quantity = 0, Subtotal = 0, ShippingCost = 0, Total = 0)
    
    def test_instance(self):
        self.assertIsInstance(self.report, Invoice, "its instance!")
    
    def test_InvoiceID(self):
        self.assertEqual(self.report.InvoiceID, 1)

    def test_ShipmentID(self):
        self.assertEqual(self.report.ShipmentID, 0)

    def test_PackID(self):
        self.assertEqual(self.report.PackID, 0)
        
    def test_FactDate(self):
        self.assertEqual(self.report.FactDate, 0)
        
    def test_Quantity(self):
        self.assertEqual(self.report.Quantity, 0)
        
    def test_Subtotal(self):
        self.assertEqual(self.report.Subtotal, 0)
        
    def test_ShippingCost(self):
        self.assertEqual(self.report.ShippingCost, 0)
        
    def test_Total(self):
        self.assertEqual(self.report.Total, 0)

    def test__str__(self):
        self.assertEqual(self.report.__str__(), {'InvoiceID': 1 , 'ShipmentID': 0, 'PackID': 0, 'FactDate': 0, 'Quantity': 0, 'Subtotal': 0, 'ShippingCost': 0, 'Total': 0})

class TestShipment(unittest.TestCase):
    order = Shipment(ShipmentID = 1 , DateCreated = 0, IDDestinityPerson = 0, DestinationAddress = 'DestinationAddress', EstimatedArrivalDate = 0, ClientID = 0, DetailShipping = 0)
    
    def test_instance(self):
        self.assertIsInstance(self.order, Shipment, "its instance!")
    
    def test_ShipmentID(self):
        self.assertEqual(self.order.ShipmentID, 1)

    def test_DateCreated(self):
        self.assertEqual(self.order.DateCreated, 0)

    def test_IDDestinityPerson(self):
        self.assertEqual(self.order.IDDestinityPerson, 0)
        
    def test_DestinationAddress(self):
        self.assertEqual(self.order.DestinationAddress, 'DestinationAddress')
        
    def test_EstimatedArrivalDate(self):
        self.assertEqual(self.order.EstimatedArrivalDate, 0)
        
    def test_ClientID(self):
        self.assertEqual(self.order.ClientID, 0)
        
    def test_DetailShipping(self):
        self.assertEqual(self.order.DetailShipping, 0)

    def test__str__(self):
        self.assertEqual(self.order.__str__(), {'ShipmentID': 1 , 'DateCreated': 0, 'IDDestinityPerson': 0, 'DestinationAddress': 'DestinationAddress', 'EstimatedArrivalDate': 0, 'ClientID': 0, 'DetailShipping': 0})

class TestShipment_details(unittest.TestCase):
    orderDet = Shipment_details(DetailShipping = 0, ShippingType = 'ShippingType', ShippingCost = 0)

    def test_instance(self):
        self.assertIsInstance(self.orderDet, Shipment_details, "Its instance!")

    def test_DetailShipping(self):
        self.assertEqual(self.orderDet.DetailShipping, 0)

    def test_ShippingType(self):
        self.assertEqual(self.orderDet.ShippingType, 'ShippingType')
        
    def test_ShippingCost(self):
        self.assertEqual(self.orderDet.ShippingCost, 0)

    def test__str__(self):
        self.assertEqual(self.orderDet.__str__(), {'DetailShipping': 0, 'ShippingType': 'ShippingType', 'ShippingCost': 0})

class TestTraceability(unittest.TestCase):
    route = Traceability(TrackingCode = 0, Description = 'Description', Date = 0, Hour = 0, ShippingID = 0)
    
    def test_instance(self):
        self.assertIsInstance(self.route, Traceability, "its instance!")

    def test_TrackingCode(self):
        self.assertEqual(self.route.TrackingCode, 0)
        
    def test_Description(self):
        self.assertEqual(self.route.Description, 'Description')
        
    def test_Date(self):
        self.assertEqual(self.route.Date, 0)
        
    def test_Hour(self):
        self.assertEqual(self.route.Hour, 0)
        
    def test_ShippingID(self):
        self.assertEqual(self.route.ShippingID, 0)

    def test__str__(self):
        self.assertEqual(self.route.__str__(), {'TrackingCode': 0, 'Description': 'Description', 'Date': 0, 'Hour': 0, 'ShippingID': 0})

if __name__ == '__main__':
    unittest.main()