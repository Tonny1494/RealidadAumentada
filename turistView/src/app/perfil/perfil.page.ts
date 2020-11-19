import { Component, OnInit } from '@angular/core';
import { AuthService } from "src/app/services/auth.service";
import { AngularFireAuth } from "@angular/fire/auth"


@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.page.html',
  styleUrls: ['./perfil.page.scss'],
})
export class PerfilPage implements OnInit {

  constructor(private authservice:AuthService ) { }

  ngOnInit() {
    console.log(this.authservice.getPerfil());
  }
  logout(){
    this.authservice.logout();
  }

  

}
