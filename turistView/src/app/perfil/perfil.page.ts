import { Component, OnInit } from '@angular/core';
import { RestService } from "src/app/services/rest.service";
import { AuthService } from "src/app/services/auth.service";
import { AngularFireAuth } from "@angular/fire/auth"



@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.page.html',
  styleUrls: ['./perfil.page.scss'],
})
export class PerfilPage implements OnInit {

  nombre: string;
  apellido: string;
  telefono: string;
  email: string;
  image: string;
  read:boolean;
  
  constructor(private rest:RestService, private auth: AuthService,    private AFauth: AngularFireAuth    ) { }

  ngOnInit() {
    this.read = true;
    this.getPerfil();
  }

  editInfo(){
    this.read= false;
  }

  
  getPerfil(){
    return this.AFauth.currentUser.then(auth =>{
      return this.rest.getPerfil(auth.email).subscribe( infoUsuario => {
        console.log(infoUsuario);
        this.nombre = infoUsuario["nombres"]
        this.email = infoUsuario["email"]
        this.apellido = infoUsuario["apellidos"]
        this.telefono = infoUsuario["telefono"]
        this.image = infoUsuario["src_imagen"]
    });
    });
  }
  

}
