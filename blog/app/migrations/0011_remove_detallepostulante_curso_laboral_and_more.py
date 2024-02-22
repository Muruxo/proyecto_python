# Generated by Django 5.0.2 on 2024-02-22 01:03

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_educacion_nivel_edu_alter_educacion_titulo_edu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallepostulante',
            name='curso_laboral',
        ),
        migrations.RemoveField(
            model_name='detallepostulante',
            name='experiencia_laboral',
        ),
        migrations.AlterField(
            model_name='empleo',
            name='fecha_empleo',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='postulados',
            name='fecha_postulado',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='postulados',
            name='id_empleo_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='postulados', to='app.empleo'),
        ),
    ]
