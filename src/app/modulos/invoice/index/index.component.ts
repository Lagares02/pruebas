import { Component } from '@angular/core';
import { Invoice } from 'src/app/modelos/invoice';
import { InvoiceService } from 'src/app/servicios/invoice.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent {
  invoices: Invoice[] = [];
  constructor(private invoiceServicio: InvoiceService) { }
  ngOnInit(): void {
    this.invoiceServicio.obtenerInvoices()
    .subscribe(invoices => this.invoices = invoices);
  }
}
