# Generated by Django 3.2.7 on 2021-09-30 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas_app', '0002_auto_20210920_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='cantidad',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='unidad',
            field=models.CharField(choices=[('mililitros', 'Mililitros'), ('litros', 'Litros'), ('kilos', 'Kilos'), ('gramos', 'Gramos'), ('cucharadas', 'Cucharadas'), ('unidades', 'Unidades')], default='unidades', max_length=20),
        ),
        migrations.AlterField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
