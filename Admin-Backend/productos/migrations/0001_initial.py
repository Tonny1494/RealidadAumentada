# Generated by Django 3.1.1 on 2020-09-28 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='id_Categoria', primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=12, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id_comentario', models.IntegerField(db_column='id_Comentario', primary_key=True, serialize=False)),
                ('id_local', models.IntegerField(blank=True, db_column='id_Local', null=True)),
                ('id_usuario', models.IntegerField(blank=True, db_column='id_Usuario', null=True)),
                ('comentario', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
        migrations.CreateModel(
            name='Escaneos',
            fields=[
                ('id_escaneos', models.AutoField(db_column='id_Escaneos', primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('lugar', models.CharField(blank=True, max_length=100, null=True)),
                ('celular', models.IntegerField(blank=True, null=True)),
                ('id_usuario', models.IntegerField(blank=True, db_column='id_Usuario', null=True)),
            ],
            options={
                'verbose_name': 'Escaneos',
                'verbose_name_plural': 'Escaneoss',
            },
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id_favorito', models.AutoField(db_column='id_Favorito', primary_key=True, serialize=False)),
                ('id_local', models.IntegerField(db_column='id_Local')),
                ('id_usuario', models.CharField(blank=True, db_column='id_Usuario', max_length=20, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Favorito',
                'verbose_name_plural': 'Favoritos',
            },
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id_contenido', models.AutoField(db_column='id_Contenido', primary_key=True, serialize=False)),
                ('id_local', models.IntegerField(blank=True, db_column='id_Local', null=True)),
                ('src_path', models.ImageField(blank=True, db_column='src_Path', null=True, upload_to='', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galerias',
            },
        ),
        migrations.CreateModel(
            name='Notificaciones',
            fields=[
                ('id_notificacion', models.IntegerField(db_column='id_Notificacion', primary_key=True, serialize=False)),
                ('alcance', models.CharField(blank=True, max_length=20, null=True)),
                ('notificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('id_usuario', models.IntegerField(blank=True, db_column='id_Usuario', null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Notificaciones',
                'verbose_name_plural': 'Notificacioness',
            },
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id_permiso', models.AutoField(db_column='id_Permiso', primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=20, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Permiso',
                'verbose_name_plural': 'Permisos',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(db_column='id_Rol', primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Rolpermiso',
            fields=[
                ('id_rolpermiso', models.AutoField(db_column='id_RolPermiso', primary_key=True, serialize=False)),
                ('id_rol', models.IntegerField(blank=True, db_column='id_Rol', null=True)),
                ('id_permiso', models.IntegerField(blank=True, db_column='id_Permiso', null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Rolpermiso',
                'verbose_name_plural': 'Rolpermisos',
            },
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id_telefono', models.AutoField(db_column='id_Telefono', primary_key=True, serialize=False)),
                ('id_local', models.IntegerField(blank=True, db_column='id_Local', null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Telefono',
                'verbose_name_plural': 'Telefonos',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('email', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('nombres', models.CharField(blank=True, max_length=100, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=100, null=True)),
                ('contrasena', models.CharField(blank=True, max_length=12, null=True)),
                ('src_imagen', models.ImageField(blank=True, db_column='src_Imagen', max_length=200, null=True, upload_to='', verbose_name='Imagen')),
                ('id_rol', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id_local', models.IntegerField(db_column='id_Local', primary_key=True, serialize=False)),
                ('nombre_comercial', models.CharField(blank=True, db_column='nombre_Comercial', max_length=100, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('src_logo', models.ImageField(blank=True, db_column='src_Logo', null=True, upload_to='', verbose_name='Imagen')),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('estrellas', models.IntegerField(blank=True, null=True)),
                ('vistas', models.IntegerField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=25, null=True)),
                ('categoria', models.CharField(blank=True, max_length=25, null=True)),
                ('latitud', models.CharField(blank=True, max_length=50, null=True)),
                ('longitud', models.CharField(blank=True, max_length=50, null=True)),
                ('adminLocal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locales',
            },
        ),
    ]