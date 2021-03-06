# Generated by Django 4.0.2 on 2022-02-10 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videosName',
            fields=[
                ('id', models.IntegerField(max_length=200, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=200)),
                ('uploadDate', models.DateTimeField(verbose_name='date published')),
                ('replyCnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=100)),
                ('writer', models.CharField(max_length=100)),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube.videosname')),
            ],
        ),
    ]
