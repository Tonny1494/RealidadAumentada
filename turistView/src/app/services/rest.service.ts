import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError  } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  url = 'https://tonny.pythonanywhere.com/adminD';
  
  constructor(private http: HttpClient) {  }

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }
  
  handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error.message);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong,
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
    }
    // return an observable with a user-facing error message
    return throwError(
      'Something bad happened; please try again later.');
  };

  
   getCategorias(): Observable<any>{
     
    return this.http.get<any>(this.url+'/categoria/?format=json').pipe(retry(2),catchError(this.handleError));
    
    
  }
  getLocales(): Observable<any>{
     
    return this.http.get<any>(this.url+'/local/?format=json').pipe(retry(2),catchError(this.handleError));
    
  }

  getLocal(idLocal:string ): Observable<any>{
     
    return this.http.get<any>(this.url+'/local/'+idLocal+'/?format=json').pipe(retry(2),catchError(this.handleError));
    
    
  }
  getPublicidades(): Observable<any>{
    return this.http.get<any>(this.url+'/publicidad/?format=json').pipe(retry(2),catchError(this.handleError));
  }
  getFavoritos(): Observable<any>{
    return this.http.get<any>(this.url+'/favorito/?format=json').pipe(retry(2),catchError(this.handleError));
  }

  getPerfil(email:string): Observable<any>{
    return this.http.get<any>(this.url+'/usuarioAPP/'+email+'/?format=json').pipe(retry(2),catchError(this.handleError));
  }

  postPerfil(email:string,contrasena:string, nombre:string, apellidos:string, telefono:string){
    let datos = {
      "email": email,
      "nombres": nombre,
      "apellidos": apellidos,
      "contrasena": contrasena,
      "telefono": telefono,
      "src_imagen": null
      }
  
      let options = {
        headers: {
          'Content-Type': 'application/json'
        }
      };
    var urlusuarios = this.url+'/usuarioAPP/';
    return new Promise(resolve => {
      this.http.post(urlusuarios,JSON.stringify(datos),options)
        .subscribe(data => {
          resolve(data);
          });
    });
  };


}
