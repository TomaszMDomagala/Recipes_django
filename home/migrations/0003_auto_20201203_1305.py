# Generated by Django 3.1.3 on 2020-12-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201202_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='type',
            field=models.CharField(choices=[('śniadania', 'Sniadania'), ('lunche', 'Lunche'), ('zupy', 'Zupy'), ('sałatki', 'Salatki'), ('surówki', 'Surowki'), ('ciasta', 'Ciasta'), ('obiady', 'Obiady'), ('dodatki', 'Dodatki'), ('podwieczorki', 'Podwieczorki'), ('kolacje', 'Kolacje')], max_length=12),
        ),
    ]