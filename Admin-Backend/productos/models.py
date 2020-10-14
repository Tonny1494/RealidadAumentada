from django.db import models

class Permiso(models.Model):
    id_permiso = models.AutoField(db_column='id_Permiso', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = "Permisos"
class Rol(models.Model):
    id_rol = models.AutoField(db_column='id_Rol', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = "Roles"
class Rolpermiso(models.Model):
    id_rolpermiso = models.AutoField(db_column='id_RolPermiso', primary_key=True)  # Field name made lowercase.
    id_rol = models.ForeignKey(Rol,on_delete=models.CASCADE,blank=True, null=True) # Field name made lowercase.
    id_permiso = models.ForeignKey(Permiso,on_delete=models.CASCADE,blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Rolpermiso'
        verbose_name_plural = "Rolpermisos"

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='id_Categoria', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=12, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"
    def __str__(self):
        return self.tipo

class Usuario(models.Model):
    email = models.CharField(primary_key=True, max_length=40)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    contrasena = models.CharField(max_length=12, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    src_imagen = models.ImageField(verbose_name="Imagen",db_column='src_Imagen', max_length=200, blank=True, null=True)  # Field name made lowercase.
    id_rol = models.ForeignKey(Rol,on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = "Usuarios"
    def __str__(self):
        return self.email

class Local(models.Model):
    id_local =models.AutoField(db_column='id_Local', primary_key=True)
     #models.IntegerField(db_column='id_Local', primary_key=True)  # Field name made lowercase.
    nombre_comercial = models.CharField(db_column='nombre_Comercial', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    src_logo = models.ImageField(verbose_name="Imagen",db_column='src_Logo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    likes = models.IntegerField(blank=True, null=True)
    estrellas = models.IntegerField(blank=True, null=True)
    vistas = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=25, blank=True, null=True)
    categoria = models.ForeignKey(Categoria ,on_delete=models.CASCADE, blank=True, null=True)
    latitud = models.CharField(max_length=50, blank=True, null=True)
    longitud = models.CharField(max_length=50, blank=True, null=True)
    adminLocal=models.ForeignKey('auth.User',on_delete=models.CASCADE,blank=True, null=True)
    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = "Locales"
    def __str__(self):
        return self.nombre_comercial
class Favorito(models.Model):
    id_favorito = models.AutoField(db_column='id_Favorito', primary_key=True)  # Field name made lowercase.
    id_local = models.ForeignKey(Local,on_delete=models.CASCADE,blank=True, null=True)
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = "Favoritos"
    def __str__(self):
        return self.id_favorito

class Notificaciones(models.Model):
    id_notificacion = models.IntegerField(db_column='id_Notificacion', primary_key=True)  # Field name made lowercase.
    alcance = models.CharField(max_length=20, blank=True, null=True)
    notificacion = models.CharField(max_length=50, blank=True, null=True)
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Notificaciones'
        verbose_name_plural = "Notificacioness"

class Escaneos(models.Model):
    id_escaneos = models.AutoField(db_column='id_Escaneos', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(blank=True, null=True)
    lugar = models.CharField(max_length=100, blank=True, null=True)
    celular = models.CharField(max_length=10,blank=True, null=True)
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=True, null=True) # Field name made lowercase.

    class Meta:
        verbose_name = 'Escaneos'
        verbose_name_plural = "Escaneoss"

class Comentario(models.Model):
    id_comentario = models.IntegerField(db_column='id_Comentario', primary_key=True)  # Field name made lowercase.
    id_local = models.ForeignKey(Local,on_delete=models.CASCADE,blank=True, null=True)
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=True, null=True)  # Field name made lowercase.
    comentario = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = "Comentarios"

class Galeria(models.Model):
    id_contenido = models.AutoField(db_column='id_Contenido', primary_key=True)  # Field name made lowercase.
    id_local = models.ForeignKey(Local,on_delete=models.CASCADE,blank=True, null=True) # Field name made lowercase.
    src_path = models.ImageField(verbose_name="Imagen" , db_column='src_Path', max_length=100, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = "Galerias"

class Telefono(models.Model):
    id_telefono = models.AutoField(db_column='id_Telefono', primary_key=True)  # Field name made lowercase.
    id_local = models.ForeignKey(Local,on_delete=models.CASCADE,blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(max_length=10,blank=True, null=True)

    class Meta:
        verbose_name = 'Telefono'
        verbose_name_plural = "Telefonos"