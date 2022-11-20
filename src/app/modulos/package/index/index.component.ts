import { Component } from '@angular/core';
import { Package } from 'src/app/modelos/package';
import { PackageService } from 'src/app/servicios/package.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent {
  packages: Package[] = [];
  constructor(private packageServicio: PackageService) { }
  ngOnInit(): void {
    this.packageServicio.obtenerPackages()
    .subscribe(packages => this.packages = packages);
  }
}
