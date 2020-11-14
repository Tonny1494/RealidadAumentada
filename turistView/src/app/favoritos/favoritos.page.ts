import { Component, OnInit } from '@angular/core';
import { AuthService } from "src/app/services/auth.service";
import { RestService } from '../services/rest.service'; //importamos nuestro service
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-favoritos',
  templateUrl: './favoritos.page.html',
  styleUrls: ['./favoritos.page.scss'],
})
export class FavoritosPage implements OnInit {

  public user: string;
  constructor(private route: ActivatedRoute,private authservice:AuthService,public rest : RestService, ) { }

  ngOnInit() {
    this.user = this.route.snapshot.paramMap.get("user");
    console.log(this.user);
    this.getFavoritos() ;
  }
  getFavoritos() { //llamamos a la funcion getPost de nuestro servicio.
    this.rest.getFavoritos().subscribe( data => {
      console.log(data);
      for (var elemento of data.results){
        let local = elemento['id_local'];
          this.rest.getLocal(local).subscribe( data => {
            console.log(data);
            let nombreComercial = data['nombre_comercial']
              let idCat = data["categoria"]
              let idLocal = data["id_local"]
              let logo = data["src_logo"]
              let descripcion = data["descripcion"]
              let plantilla = `<ion-item >
                                <ion-avatar >
                                  <img src="${logo}" alt="">
                                </ion-avatar>
                                <ion-label class="info">
                                  <h2><a href="/local/${idLocal}">${nombreComercial}</a></h2>
                                  <p>${descripcion}</p>
                                </ion-label>
                              </ion-item>
                              `
                document.getElementById('Favoritos').innerHTML += plantilla
              
      
                
            }
          )


      }
    })
  }

}
