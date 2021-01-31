from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from productos import views
from productos.views import *
from django.urls import re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
#from productos.views import CategoriaViewSet,ComentarioViewSet,EscaneosViewSet,FavoritoViewSet,GaleriaViewSet,LocalViewSet,NotificacionesViewSet,PermisoViewSet,RolViewSet,RolpermisoViewSet,TelefonoViewSet,UsuarioViewSet,tablaLocal
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'comentario', ComentarioViewSet)
router.register(r'escaneo', EscaneosViewSet)
router.register(r'favorito', FavoritoViewSet)
router.register(r'galeria', GaleriaViewSet)
router.register(r'local', LocalViewSet)
router.register(r'permiso', PermisoViewSet)
router.register(r'notificaciones', NotificacionesViewSet)
router.register(r'rol', RolViewSet)
router.register(r'rolpermiso', RolpermisoViewSet)
router.register(r'telefono', TelefonoViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'usuarioAPP', UsuarioAPPViewSet)
router.register(r'publicidad', PublicidadViewSet)




# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('adminD/', include(router.urls)),
    path('', views.login, name="login"),
    path('index/', views.index, name="index"),
    path('tablaUsuario/', views.tablaUsuario, name="tablaUsuario"),
    path('tablaLocal/', views.tablaLocal, name="tablaLocal"),
    path('tablaLocal/(?P<id_local>)$', localDelete, name="localDelete"),
    path('tablaCategoria/', views.tableCategoria, name="tablaCategoria"),
    path('tablaCategoria/(?P<id_categoria>)$', categoriaDelete, name="categoriaDelete"),
    path('tablaFavorito/', views.tableFavorito, name="tablaFavorito"),
    path('tablaFavorito/(?P<id_favorito>)$', favoritoDelete, name="favoritoDelete"),
    path('tablaTelefono/', views.tableTelefono, name="tablaTelefono"),
    path('tablaGaleria/', views.tableGaleria, name="tablaGaleria"),
    path('tablaGaleria2/', views.tableGaleria2, name="tablaGaleria2"),
     path('notificaciones/', views.notificaciones, name="notificaciones"),
    path('registrarCategoria/', registrarCategoria, name="registrarCategoria"),
    path('registrarLocal/', registrarLocal, name="registrarLocal"),
    path('registrarUsuario/', registrarUsuario, name="registrarUsuario"),
    path('registrarPublicidad/', registrarPublicidad, name="registrarPublicidad"),
    path('registrarNotificaciones/', registrarNotificaciones, name="registrarNotificaciones"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('logout/', views.logout_view, name='logout'),
    path('localDelete/', views.localDelete, name='localDelete'),
    path('usuarioDelete/', views.usuarioDelete, name='usuarioDelete'),
    path('editarLocal/', views.editarLocal, name='editarLocal'),
    path('editarUsuario/', views.editarUsuario, name='editarUsuario'),
    path('updatefavorito/<int:favorito_id>', views.update_favorito),
    path('guardar-token/',guardar_token,name='guardar-token'),
    #RECUPERACION DE CORREO
    
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "productos/password/password_reset_form.html"), name ='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "productos/password/password_reset_done.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "productos/password/password_reset_confirm.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "productos/password/password_reset_complete.html"), name ='password_reset_complete')
]

urlpatterns += [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)