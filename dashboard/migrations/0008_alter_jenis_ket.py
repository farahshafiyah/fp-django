# Generated by Django 4.1.5 on 2023-02-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_remove_brand_kategori_brand_jenis_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenis',
            name='ket',
            field=models.CharField(max_length=50),
        ),
    ]
