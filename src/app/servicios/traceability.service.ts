import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Traceability } from '../modelos/traceability';

@Injectable({
  providedIn: 'root'
})
export class TraceabilityService {

  url: string = "http://127.0.0.1:8000";

  constructor(
    private http: HttpClient
  ) { }

  obtenerTraceabilitys(): Observable<Traceability[]>{
    return this.http.get<Traceability[]>(`${this.url}/traceability`);
  }

}
