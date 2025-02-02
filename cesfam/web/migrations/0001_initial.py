# Generated by Django 5.1.4 on 2025-01-30 23:00

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id_doctor', models.AutoField(db_column='idDoctor', primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('contrasena', models.CharField(max_length=128)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='doctores')),
                ('last_login', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('contrasena', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='noticias')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_examen', models.CharField(blank=True, help_text='Nombre opcional del examen (dejar vacío si no aplica).', max_length=150, null=True)),
                ('tipo_examen', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('archivo', models.FileField(blank=True, help_text='Sube un archivo relacionado con el examen (opcional).', null=True, upload_to='examenes/')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('realizado', 'Realizado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examenes', to='web.doctor')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examenes', to='web.paciente')),
            ],
            options={
                'db_table': 'web_examen',
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('realizada', 'Realizada'), ('cancelada', 'Cancelada'), ('pospuesta', 'Pospuesta')], default='pendiente', max_length=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citas', to='web.doctor')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citas', to='web.paciente')),
            ],
            options={
                'db_table': 'web_cita',
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamento', models.CharField(max_length=255, verbose_name='Medicamento')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('dosis', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dosis')),
                ('frecuencia', models.CharField(blank=True, max_length=255, null=True, verbose_name='Frecuencia')),
                ('archivo', models.FileField(blank=True, help_text='Sube una imagen relacionado con la receta (opcional).', null=True, upload_to='recetas/')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recetas', to='web.doctor')),
                ('examen', models.ForeignKey(help_text='Examen relacionado con esta receta (obligatorio).', on_delete=django.db.models.deletion.CASCADE, related_name='recetas', to='web.examen')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recetas', to='web.paciente')),
            ],
        ),
    ]
