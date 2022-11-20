import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Client } from '../modelos/client';

@Injectable({
  providedIn: 'root'
})
export class ClientService {

  url: string = "http://127.0.0.1:8000";

  constructor(
    private http: HttpClient
  ) { }

  obtenerClients(): Observable<Client[]>{
    return this.http.get<Client[]>(`${this.url}/client`);
  }

}
