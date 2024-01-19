# Generated by Django 4.1.5 on 2023-01-07 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phno', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=2)),
                ('dest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.dest')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.sources')),
            ],
        ),
    ]
