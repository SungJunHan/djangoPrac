# Generated by Django 4.0.2 on 2022-02-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videosname',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
