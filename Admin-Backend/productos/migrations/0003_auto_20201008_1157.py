# Generated by Django 3.1.1 on 2020-10-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20201007_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='id_local',
            field=models.AutoField(db_column='id_Local', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]