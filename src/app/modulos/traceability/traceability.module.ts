import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { TraceabilityRoutingModule } from './traceability-routing.module';
import { IndexComponent } from './index/index.component';


@NgModule({
  declarations: [
    IndexComponent
  ],
  imports: [
    CommonModule,
    TraceabilityRoutingModule
  ]
})
export class TraceabilityModule { }
