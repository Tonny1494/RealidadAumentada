import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './guards/auth.guard';
import { NologinGuard } from './guards/nologin.guard';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  },
  {
    path: 'scanner',
    canActivate:[AuthGuard],
    loadChildren: () => import('./scanner/scanner.module').then( m => m.ScannerPageModule)
  },
  {
    path: 'ra-camera',
    canActivate:[AuthGuard],
    loadChildren: () => import('./ra-camera/ra-camera.module').then( m => m.RaCameraPageModule)
  },
  {
    path: 'notificaciones',
    canActivate:[AuthGuard],
    loadChildren: () => import('./notificaciones/notificaciones.module').then( m => m.NotificacionesPageModule)
  },
  {
    path: 'locales',
    canActivate:[AuthGuard],
    loadChildren: () => import('./locales/locales.module').then( m => m.LocalesPageModule)
  },
  {
    path: 'favoritos',
    canActivate:[AuthGuard],
    loadChildren: () => import('./favoritos/favoritos.module').then( m => m.FavoritosPageModule)
  },
  {
    path: 'perfil',
    canActivate:[AuthGuard],
    loadChildren: () => import('./perfil/perfil.module').then( m => m.PerfilPageModule)
  },
  {
    path: 'login',
    canActivate:[NologinGuard],
    loadChildren: () => import('./login/login.module').then( m => m.LoginPageModule)
  },
  {
    path: 'register',
    loadChildren: () => import('./register/register.module').then( m => m.RegisterPageModule)
  },
  {
    path: 'reset-pass',
    loadChildren: () => import('./reset-pass/reset-pass.module').then( m => m.ResetPassPageModule)
  },
  {
    path: 'local/:id',
    canActivate:[AuthGuard],
    loadChildren: () => import('./local/local.module').then( m => m.LocalPageModule)
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
