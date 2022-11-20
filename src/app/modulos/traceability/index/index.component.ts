import { Component } from '@angular/core';
import { Traceability } from 'src/app/modelos/traceability';
import { TraceabilityService } from 'src/app/servicios/traceability.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent {
  traceabilitys: Traceability[] = [];
  constructor(private traceabilityServicio: TraceabilityService) { }
  ngOnInit(): void {
    this.traceabilityServicio.obtenerTraceabilitys()
    .subscribe(traceabilitys => this.traceabilitys = traceabilitys);
  }
}
