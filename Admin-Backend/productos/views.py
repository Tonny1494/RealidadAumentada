from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.response import Response
from django.contrib.auth import login as do_login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from .serializers import UserSerializer, GroupSerializer,TCategoriaSerializer,TComentarioSerializer,TEscaneosSerializer,TFavoritoSerializer,TGaleriaSerializer,TLocalSerializer,TNotificacionesSerializer,TPermisoSerializer,TRolSerializer,TRolpermisoSerializer,TTelefonoSerializer,TUsuarioSerializer
from .models import Categoria,Comentario,Escaneos,Favorito,Galeria,Local,Notificaciones,Permiso,Rol,Rolpermiso,Telefono,Usuario
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = TCategoriaSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = TComentarioSerializer

class EscaneosViewSet(viewsets.ModelViewSet):
        queryset = Escaneos.objects.all()
        serializer_class = TEscaneosSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
        queryset = Favorito.objects.all()
        serializer_class = TFavoritoSerializer

class GaleriaViewSet(viewsets.ModelViewSet):
        queryset = Galeria.objects.all()
        serializer_class =TGaleriaSerializer
class LocalViewSet(viewsets.ModelViewSet):
        queryset = Local.objects.all()
        serializer_class = TLocalSerializer
class NotificacionesViewSet(viewsets.ModelViewSet):
        queryset = Notificaciones.objects.all()
        serializer_class = TNotificacionesSerializer
class PermisoViewSet(viewsets.ModelViewSet):
        queryset = Permiso.objects.all()
        serializer_class = TPermisoSerializer
class RolViewSet(viewsets.ModelViewSet):
        queryset = Rol.objects.all()
        serializer_class = TRolSerializer
class RolpermisoViewSet(viewsets.ModelViewSet):
        queryset = Rolpermiso.objects.all()
        serializer_class = TRolpermisoSerializer
class TelefonoViewSet(viewsets.ModelViewSet):
        queryset = Telefono.objects.all()
        serializer_class = TTelefonoSerializer
class UsuarioViewSet(viewsets.ModelViewSet):
        queryset = Usuario.objects.all()
        serializer_class = TUsuarioSerializer
def index(request):
	 return render(request,'productos/index.html')

def tablaUsuario(request):
	return render(request,'productos/tablaUsuario.html')
def tablaLocal(request):
        local=Local.objects.all()
        contexto={'locales':local}
        return render(request,'productos/tablaLocal.html', contexto)
def tableCategoria(request):
        categoria=Categoria.objects.all()
        contexto={'categorias':categoria}
        return render(request,'productos/tablaCategoria.html',contexto)
def tableFavorito(request):
        favorito=Favorito.objects.all()
        contexto={'favoritos':favorito}
        return render(request,'productos/tablaFavorito.html',contexto)
def tableTelefono(request):
        telefono=Telefono.objects.all()
        contexto={'telefonos':telefono}
        return render(request,'productos/tablaTelefono.html',contexto)
def tableGaleria(request):
        galeria=Galeria.objects.all()
        contexto={'galerias':galeria}
        return render(request,'productos/tablaGaleria.html',contexto)
def localDelete(request,id_local):
        local=Local.objects.get(id_local=id_local)
        local.delete()
        return render(request,'productos/tablaLocal.html', {"locales":Local.objects.all()})
def categoriaDelete(request,id_categoria):
        categoria=Categoria.objects.get(id_categoria=id_categoria)
        categoria.delete()
        return render(request,'productos/tablaCategoria.html', {"categorias":Categoria.objects.all()})
def favoritoDelete(request,id_favorito):
        favorito=Favorito.objects.get(id_favorito=id_favorito)
        favorito.delete()
        return render(request,'productos/tablaFavorito.html', {"favoritos":Favorito.objects.all()})
def telefonoDelete(request,id_telefono):
        telefono=Telefono.objects.get(id_telefono=id_telefono)
        telefono.delete()
        return render(request,'productos/tablaTelefono.html', {"telefonos":Telefono.objects.all()})
def galeriaDelete(request,id_contenido):
        galeria=Galeria.objects.get(id_contenido=id_contenido)
        galeria.delete()
        return render(request,'productos/tablaGaleria.html', {"galerias":Galeria.objects.all()})
# ...
@csrf_exempt
def login(request):
    # Creamos el formulario de autenticación vacío
    print("hola mundo")
    #user = authenticate(username="chjoguer", password='zywcCQAmPf')
   # print(user)
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)
            print("verificando")

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                print("si existe")
                # Y le redireccionamos a la portada
               # return redirect('registroNoticias/')
                return render(request, "productos/index.html")

        else:
                print(form.is_valid())
                print("Password o usuario incorrecto")
                return render(request, "productos/login.html", {'form': form,'mensaje':"Usuario o cotrnaseña iconrrecta."})


    # Si llegamos al final renderizamos el formulario
    return render(request, "productos/login.html", {'form': form ,'mensaje':""})

def logout_view(request):
    logout(request)
    return redirect('/')

def registrarCategoria(request):
        if request.method=='POST':
                if(request.POST.get("tipo")!=None and request.POST.get("descripcion")!=None):
                        categoria = Categoria(tipo=request.POST.get("tipo"),descripcion=request.POST.get("descripcion"))
                        categoria.save()
                        #return HttpResponse(status=200)
                        return render(request, 'productos/crear/crearCategoria.html') 
                return HttpResponse(status=404)
        if request.method=='GET':
                return render(request, 'productos/crear/crearCategoria.html') 
def registrarLocal(request):
        if request.method=='POST':
                if(request.POST.get("vista")!=None and request.POST.get("direccion")!=None and request.POST.get("nombrec")!=None and request.POST.get("like")!=None and request.POST.get("descripcion")!=None):
                        local = Local(vistas=request.POST.get("vista"),descripcion=request.POST.get("descripcion"),likes=request.POST.get("like"),direccion=request.POST.get("direccion"),nombre_comercial=request.POST.get("nombrec"))
                        local.save()
                        #return HttpResponse(status=200)
                        return render(request, 'productos/crear/crearLocal.html') 
                return HttpResponse(status=404)
        if request.method=='GET':
                return render(request, 'productos/crear/crearLocal.html') 
