import { Component, OnInit } from '@angular/core';
import { AuthService } from "../services/auth.service";
import { Router } from "@angular/router"
import { ToastController } from '@ionic/angular';
import { RestService } from "../services/rest.service"; //importamos nuestro service


@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {

  public email: string;
  public password: string;
  
  constructor(public rest: RestService,private authService: AuthService,  private router : Router, private toastC: ToastController) { }

  doLogin()
  {
    this.authService.login(this.email, this.password).then( () =>{
      this.router.navigate(['/ra-camera']);
    }).catch(err => {
      this.toastMessage("Los datos son incorrectos o no existe el usuario");
    })
  }

  async toastMessage(message: string){
    const toast = await this.toastC.create({
      message: message,
      duration: 2000
    });

    toast.present();
  }

  loginGoogle() {
    
    this.authService.loginWithGoogle().then( a =>{
      this.toastMessage("Ingreso Exitoso");
      this.rest.postPerfil(a.user.email,null,a.user.displayName,a.user.displayName,null).then(() =>{
        console.log("Se registro en pythonanywhere");
      }).catch(err => {
        alert(err);
      });
      this.router.navigate(['/ra-camera']);
    }).catch(err =>{
      alert('algo salio mal contacta a soporte');
      alert(err);
      console.log(err);
    })
 }

  loginFacebook() {

    this.authService.loginWithFacebook().then( a =>{
      this.toastMessage("Ingreso Exitoso");
      this.rest.postPerfil(a.user.email,null,a.user.displayName,a.user.displayName,null).then(() =>{
        console.log("Se registro en pythonanywhere");
      }).catch(err => {
        alert(err);
      });
      this.router.navigate(['/ra-camera']);
    }).catch(err =>{
      alert('algo salio mal contacta a soporte')
      alert(err);
      console.log(err);
    })
 }

  ngOnInit() {
  }

}
