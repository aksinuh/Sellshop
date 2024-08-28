# Generated by Django 5.0.7 on 2024-08-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_rating_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
