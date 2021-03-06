# Generated by Django 3.2.7 on 2021-09-21 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recetas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='imagen',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='unidad',
            field=models.CharField(choices=[('cucharadas', 'Cucharadas'), ('unidades', 'Unidades'), ('mililitros', 'Mililitros'), ('litros', 'Litros'), ('kilos', 'Kilos'), ('gramos', 'Gramos')], default='unidades', max_length=20),
        ),
        migrations.AlterField(
            model_name='receta',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
