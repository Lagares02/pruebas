import { Component } from '@angular/core';
import { Shipment } from 'src/app/modelos/shipment';
import { ShipmentService } from 'src/app/servicios/shipment.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent {
  shipments: Shipment[] = [];
  constructor(private shipmentServicio: ShipmentService) { }
  ngOnInit(): void {
    this.shipmentServicio.obtenerShipments()
    .subscribe(shipments => this.shipments = shipments);
  }
}
