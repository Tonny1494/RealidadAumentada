import { Component, OnInit } from '@angular/core';
import { AuthService } from "src/app/services/auth.service";
import { RestService } from '../services/rest.service'; //importamos nuestro service


@Component({
  selector: 'app-locales',
  templateUrl: './locales.page.html',
  styleUrls: ['./locales.page.scss'],
})
export class LocalesPage implements OnInit {

  constructor(public rest : RestService, private authservice:AuthService) { }

  ngOnInit() {
    this.getCategorias()
  }

  getCategorias() { //llamamos a la funcion getPost de nuestro servicio.
    this.rest.getCategorias().subscribe( data => {
      console.log(data);
      for (var elemento of data.results){
        let tipo = elemento['tipo']
        let categoria = elemento['id_categoria']
        let plantilla = `<ion-list id="${tipo}">
                        <ion-list-header>
                          <h3>${tipo}</h3> 
                        </ion-list-header>
                      </ion-list>`
          document.getElementById('Locales').innerHTML += plantilla

          this.rest.getLocales().subscribe( data => {
            console.log(data);
            for (var elemento of data.results){
              let nombreComercial = elemento['nombre_comercial']
              let idCat = elemento["categoria"]
              let idLocal = elemento["id_local"]
              let logo = elemento["src_logo"]
              let descripcion = elemento["descripcion"]
              if (idCat == categoria){
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
                    document.getElementById(tipo).innerHTML += plantilla
              }
      
                
            }
          })


      }
    })
  }
  
  

}
