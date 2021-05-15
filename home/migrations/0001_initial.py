# Generated by Django 3.1.3 on 2020-12-02 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('ingredients', models.TextField()),
                ('description', models.TextField()),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('image', models.ImageField(default='default.jpg', upload_to='food_pics')),
                ('type', models.CharField(choices=[('SN', 'śniadania'), ('LU', 'lunche'), ('ZU', 'zupy'), ('SA', 'sałatki'), ('SU', 'surówki'), ('CI', 'ciasta'), ('OB', 'obiady'), ('DO', 'dodatki'), ('PO', 'podwieczorki'), ('KO', 'kolacje')], max_length=2)),
            ],
        ),
    ]
