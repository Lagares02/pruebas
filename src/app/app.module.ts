import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { InicioComponent } from './plantilla/inicio/inicio.component';
import { ErrorComponent } from './plantilla/error/error.component';
import { HttpClientModule } from '@angular/common/http';
import { BarraNavegacionComponent } from './plantilla/barra-navegacion/barra-navegacion.component';
import { PiePaginaComponent } from './plantilla/pie-pagina/pie-pagina.component';

@NgModule({
  declarations: [
    AppComponent,
    InicioComponent,
    ErrorComponent,
    BarraNavegacionComponent,
    PiePaginaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
