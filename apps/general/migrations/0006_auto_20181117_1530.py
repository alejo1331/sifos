# Generated by Django 2.1.3 on 2018-11-17 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_auto_20181117_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=50),
        ),
    ]
