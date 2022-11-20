import { Component } from '@angular/core';
import { Client } from 'src/app/modelos/client';
import { ClientService } from 'src/app/servicios/client.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent {
  clients: Client[] = [];
  constructor(private clientServicio: ClientService) { }
  ngOnInit(): void {
    this.clientServicio.obtenerClients()
    .subscribe(clients => this.clients = clients);
  }
}
