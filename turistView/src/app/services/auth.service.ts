import { Injectable } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/auth'
import { AngularFirestore } from "@angular/fire/firestore";
import { GooglePlus } from '@ionic-native/google-plus/ngx'
import { auth } from 'firebase'
import { Router } from "@angular/router";
import { Facebook, FacebookLoginResponse } from '@ionic-native/facebook/ngx';
import { map } from "rxjs/operators"


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor( private google : GooglePlus, 
    private AFauth: AngularFireAuth, 
    private router : Router,
    private fb: Facebook,
    private db : AngularFirestore){}

    login(email:string, password:string){

    return new Promise((resolve, rejected) =>{
    this.AFauth.signInWithEmailAndPassword(email, password).then(user => {
    resolve(user);

    }).catch(err => rejected(err));
    });


    }

    register(email : string, password : string, name : string){

    return new Promise ((resolve, reject) => {
    this.AFauth.createUserWithEmailAndPassword(email, password).then( res =>{
    console.log(res.user.uid);
    const uid = res.user.uid;
      this.db.collection('users').doc(uid).set({
        name : name,
        uid : uid
      })

    resolve(res)
    }).catch( err => reject(err))
    })
    }

    resetPassword(email: string){
    return this.AFauth.sendPasswordResetEmail(email);
    }

    logout(){
    this.AFauth.signOut().then(() => {
    this.google.disconnect();
    this.router.navigate(['/login']);
    })
    }
    loginWithGoogle(){
    return this.google.login({}).then( result=> {
    const user_data_google = result;
    return this.AFauth.signInWithCredential(auth.GoogleAuthProvider.credential(null,user_data_google.accessToken))
    } )
    }

    loginWithFacebook(){
    return this.fb.login(['email','public_profile']).then( (response: FacebookLoginResponse)=>{
    const credentia_fb = auth.FacebookAuthProvider.credential(response.authResponse.accessToken);
    return this.AFauth.signInWithCredential(credentia_fb);
    })

    }

    getPerfil(){
      return this.AFauth.currentUser.then(auth =>{
        console.log(auth.email);
      });
    }

  }

