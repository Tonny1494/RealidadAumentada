import { Component, OnInit } from '@angular/core';
import { AuthService } from "../services/auth.service";
import { Router } from "@angular/router"
import { ActionSheetController } from '@ionic/angular';



@Component({
  selector: 'app-register',
  templateUrl: './register.page.html',
  styleUrls: ['./register.page.scss'],
})
export class RegisterPage implements OnInit {

  email: string;
  password: string;
  rpass:string;
  name: string;

  
  constructor(private authService: AuthService,  private router : Router, public actionSheetController: ActionSheetController) { }
  

  doRegister()
  {
    this.authService.register(this.email, this.password, this.name).then( () =>{
      this.router.navigate(['/login']);
    }).catch(err => {
      alert('algo ocurrio');
    })
  }
  ngOnInit() {
  }

  async selectImagen(){
    const actionSheet = await this.actionSheetController.create({
      header: 'Foto de perfil',
      cssClass: 'my-custom-class',
      buttons: [{
        text: 'Escoger Foto',
        role: 'destructive',
        icon: 'image',
        handler: () => {
          console.log('Delete clicked');
        }
      }, {
        text: 'Tomar Foto',
        icon: 'camera',
        handler: () => {
          console.log('Share clicked');
        }
      }, {
        text: 'Cancel',
        icon: 'close',
        role: 'cancel',
        handler: () => {
          console.log('Cancel clicked');
        }
      }]
    });
    await actionSheet.present();
  }
  

}
