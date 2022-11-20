import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ErrorComponent } from './plantilla/error/error.component';
import { InicioComponent } from './plantilla/inicio/inicio.component';

const routes: Routes = [
  { path: 'inicio', component: InicioComponent },
  { path: '', pathMatch: 'full', redirectTo: '/inicio' },
  { 
    path: 'seguridad', 
    loadChildren: () => import('./modulos/seguridad/seguridad.module')
    .then(x => x.SeguridadModule) 
  },
  {
    path: 'package',
    loadChildren: () => import('./modulos/package/package.module')
    .then(x => x.PackageModule)
  },
  {
    path: 'client',
    loadChildren: () => import('./modulos/client/client.module')
    .then(x => x.ClientModule)
  },
  {
    path: 'invoice',
    loadChildren: () => import('./modulos/invoice/invoice.module')
    .then(x => x.InvoiceModule)
  },
  {
    path: 'shipment',
    loadChildren: () => import('./modulos/shipment/shipment.module')
    .then(x => x.ShipmentModule)
  },
  {
    path: 'traceability',
    loadChildren: () => import('./modulos/traceability/traceability.module')
    .then(x => x.TraceabilityModule)
  },
  { path: '**', component: ErrorComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
