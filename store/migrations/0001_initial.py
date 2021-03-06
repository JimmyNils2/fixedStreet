# Generated by Django 3.2.6 on 2021-09-16 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProdCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'prodcategory',
                'verbose_name_plural': 'prodcategories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='store')),
                ('price', models.FloatField()),
                ('available', models.BooleanField(default=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.prodcategory')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
