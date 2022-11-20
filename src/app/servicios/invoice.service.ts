import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Invoice } from '../modelos/invoice';

@Injectable({
  providedIn: 'root'
})
export class InvoiceService {

  url: string = "http://127.0.0.1:8000";

  constructor(
    private http: HttpClient
  ) { }

  obtenerInvoices(): Observable<Invoice[]>{
    return this.http.get<Invoice[]>(`${this.url}/invoice`);
  }

}
