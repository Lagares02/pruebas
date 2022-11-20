import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Package } from '../modelos/package';

@Injectable({
  providedIn: 'root'
})
export class PackageService {

  url: string = "http://127.0.0.1:8000";

  constructor(
    private http: HttpClient
  ) { }

  obtenerPackages(): Observable<Package[]>{
    return this.http.get<Package[]>(`${this.url}/package`);
  }

}
