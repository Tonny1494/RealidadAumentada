import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
//
//
import { CameraPreview } from '@ionic-native/camera-preview/ngx';
import { Geolocation } from '@ionic-native/geolocation/ngx';
import { DeviceMotion} from '@ionic-native/device-motion/ngx';
import { DeviceOrientation } from '@ionic-native/device-orientation/ngx';
import { AndroidPermissions } from '@ionic-native/android-permissions/ngx';

//
import { GooglePlus } from '@ionic-native/google-plus/ngx'
import { Facebook } from '@ionic-native/facebook/ngx';

import { AngularFirestoreModule } from "@angular/fire/firestore"; //Modulo Firestore (BD)
import { firebaseConfig } from '../environments/environment';
import { AngularFireModule } from '@angular/fire';
import { AngularFireAuthModule } from '@angular/fire/auth';

import {HttpClientModule } from '@angular/common/http';



@NgModule({
  declarations: [AppComponent],
  entryComponents: [],
  imports: [
    BrowserModule,
    IonicModule.forRoot(),
    AppRoutingModule,
    AngularFirestoreModule,
    AngularFireModule.initializeApp(firebaseConfig), //Modulo 1 a importa
    AngularFireAuthModule, // Modulo 2 a importar
    HttpClientModule
  ],
  providers: [
    StatusBar,
    SplashScreen,
    AndroidPermissions,
    DeviceOrientation,
    DeviceMotion,
    Geolocation,
    CameraPreview,
    Facebook,
    GooglePlus,
    { provide: RouteReuseStrategy, useClass: IonicRouteStrategy }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
