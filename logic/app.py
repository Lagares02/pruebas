import uvicorn
from fastapi import FastAPI
from invoice_controller import InvoiceController
from package import Package
from package_controller import PackageController
from client import Client
from client_controller import ClientController
from shipment import Shipment
from shipment_controller import ShipmentController
from invoice import Invoice
from shipment_details_controller import Shipment_detailsController
from traceability import Traceability
from traceability_controller import TraceabilityController
from shipment_details import Shipment_details

app = FastAPI()
pk_object = PackageController()
ct_object = ClientController()
sm_object = ShipmentController()
iv_object = InvoiceController()
tc_object = TraceabilityController()
sd_object = Shipment_detailsController()


@app.get("/")
def read_root():
    return {"200": "Welcome To Student Restful API"}


@app.get("/api/package")
async def root():
    return pk_object.show()

@app.post("/api/package")
async def add(PackID: int, Dimensions: int, Weigth: int, Type: str, Condition: str, Observations: str):
    return pk_object.add(Package(PackID=PackID, Dimensions=Dimensions, Weigth=Weigth, Type=Type, Condition=Condition, Observations=Observations))

@app.get("/api/client")
async def root():
    return ct_object.show()

@app.post("/api/client")
async def add(ClientID: int, Name: str, Surname: str, Direction: str, Phone: str):
    return ct_object.add(Client(ClientID=ClientID, Name=Name, Surname=Surname, Direction=Direction, Phone=Phone))

@app.get("/api/shipment")
async def root():
    return sm_object.show()

@app.post("/api/shipment")
async def add(ShipmentID: int, DateCreated: int, IDDestinityPerson: int, DestinationAddress: str, EstimatedArrivalDate: int, ClientID: int, DetailShipping: int):
    return sm_object.add(Shipment(ShipmentID=ShipmentID, DateCreated=DateCreated, IDDestinityPerson=IDDestinityPerson, DestinationAddress=DestinationAddress, EstimatedArrivalDate=EstimatedArrivalDate, ClientID=ClientID, DetailShipping=DetailShipping))

@app.get("/api/invoice")
async def root():
    return iv_object.show()

@app.post("/api/invoice")
async def add(InvoiceID: int, ShipmentID: int, PackID: int, FactDate: int, Quantity: int, Subtotal: int, ShippingCost: int, Total: int):
    return iv_object.add(Invoice(InvoiceID=InvoiceID, ShipmentID=ShipmentID, PackID=PackID, FactDate=FactDate, Quantity=Quantity, Subtotal=Subtotal, ShippingCost=ShippingCost, Total=Total))

@app.get("/api/traceability")
async def root():
    return tc_object.show()

@app.post("/api/traceability")
async def add(TrackingCode: int, Description: str, Date: int, Hour: int, ShippingID: int):
    return tc_object.add(Traceability(TrackingCode=TrackingCode, Description=Description, Date=Date, Hour=Hour, ShippingID=ShippingID))

@app.get("/api/shipping_details")
async def root():
    return sd_object.show()

@app.post("/api/shipping_details")
async def add(DetailsShipping: int, ShippingType: str, ShippingCost: int):
    return sd_object.add(Shipment_details(DetailShipping=DetailsShipping, ShippingType=ShippingType, ShippingCost=ShippingCost))

if __name__ == "__main__":
    uvicorn.run(app, port=33507)