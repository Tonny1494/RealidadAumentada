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
        url: '/ra-camera',
        icon: 'location'
      },
      {
        title: 'Scanner',
        url: '/scanner',
        icon: 'scan'
      },
      {
        title: 'Locales',
        url: 'locales',
        icon: 'business'
      },
      {
        title: 'Notificaciones',
        url: 'notificaciones',
        icon: 'notifications'
      },
      {
        title: 'Favoritos',
        url: 'favoritos',
        icon: 'heart'
      },
      {
        title: 'Perfil',
        url: 'perfil',
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
