import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Shipment } from '../modelos/shipment';

@Injectable({
  providedIn: 'root'
})
export class ShipmentService {

  url: string = "http://127.0.0.1:8000";

  constructor(
    private http: HttpClient
  ) { }

  obtenerShipments(): Observable<Shipment[]>{
    return this.http.get<Shipment[]>(`${this.url}/shipment`);
  }

}
