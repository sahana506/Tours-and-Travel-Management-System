# Generated by Django 4.1.5 on 2023-01-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='details',
            name='age',
            field=models.IntegerField(),
        ),
    ]
