# Generated by Django 5.1 on 2024-09-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_alter_kits_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='pump',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
