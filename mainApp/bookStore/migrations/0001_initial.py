# Generated by Django 4.0.2 on 2022-02-10 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_name', models.CharField(max_length=30)),
                ('english_name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookStore.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Nutritions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kcal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sodiumn_mg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saturated_fat_g', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sugars_g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size_ml', models.CharField(max_length=20)),
                ('size_fluid_ounce', models.CharField(max_length=20)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookStore.drinks')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=500)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookStore.drinks')),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookStore.menu'),
        ),
        migrations.CreateModel(
            name='Allergy_drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookStore.allergy')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookStore.drinks')),
            ],
        ),
    ]