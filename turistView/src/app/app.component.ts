import { Component, OnInit } from '@angular/core';

import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import { AuthService } from "src/app/services/auth.service";
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent implements OnInit {
  public selectedIndex = 0;
  public user: string;
  public appPages = [];

  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private authservice:AuthService,
    private route: ActivatedRoute
  ) {
    this.initializeApp();
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
    });
  }

  ngOnInit() {
    this.user = this.route.snapshot.paramMap.get("user");
    this.appPages = [
      {
        title: 'RA-360',
        url: '/ra-camera/'+this.user,
        icon: 'location'
      },
      {
        title: 'Scanner',
        url: '/scanner/'+this.user,
        icon: 'scan'
      },
      {
        title: 'Locales',
        url: 'locales/'+this.user,
        icon: 'business'
      },
      {
        title: 'Notificaciones',
        url: 'notificaciones/'+this.user,
        icon: 'notifications'
      },
      {
        title: 'Favoritos',
        url: 'favoritos/'+this.user,
        icon: 'heart'
      },
      {
        title: 'Perfil',
        url: 'perfil/'+this.user,
        icon: 'person'
      }
    ];
    const path = window.location.pathname.split('folder/')[1];
    if (path !== undefined) {
      this.selectedIndex = this.appPages.findIndex(page => page.title.toLowerCase() === path.toLowerCase());
    }
  }

  logout(){
    this.authservice.logout();
  }

  ionViewWillLeave(){
    let elem: any = <HTMLElement>document.getElementById('menu');
    
      elem.style = "display: none";
      console.log(elem);
  }
}
