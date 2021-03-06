# Generated by Django 3.1.1 on 2020-10-08 16:54

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20201007_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='noimage.jpeg', force_format=None, keep_meta=True, quality=100, size=[400, 500], upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='noimage.jpeg', force_format=None, keep_meta=True, null=True, quality=100, size=[400, 500], upload_to=''),
        ),
    ]
