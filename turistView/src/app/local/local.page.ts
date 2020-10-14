import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { RestService } from '../services/rest.service'; //importamos nuestro service


@Component({
  selector: 'app-local',
  templateUrl: './local.page.html',
  styleUrls: ['./local.page.scss'],
})
export class LocalPage implements OnInit {

  public idLocal: string;

  public nombreComercial : string;
  public logo : string;
  public descripcion : string;
  public direccion : string;
  public vistas : string;
  public like : string;
 
  constructor(private route: ActivatedRoute,public rest : RestService) { }

  ngOnInit() {
    this.idLocal = this.route.snapshot.paramMap.get("id");
    this.getInfoLocal();
  }
  getInfoLocal() { //llamamos a la funcion getPost de nuestro servicio.
    this.rest.getLocal(this.idLocal).subscribe( infLocal => {
      console.log(infLocal)
        this.nombreComercial = infLocal['nombreComercial']
        this.logo = infLocal["srcLogo"]
        this.descripcion = infLocal["descripcion"]
        this.direccion = infLocal["direccion"]
        this.vistas = infLocal["vistas"]
        this.like = infLocal["like"]
        

      
    })
  }

}