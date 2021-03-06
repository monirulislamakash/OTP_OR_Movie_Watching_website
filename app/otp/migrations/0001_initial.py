# Generated by Django 3.2 on 2021-05-22 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(default='', max_length=40)),
                ('video', models.CharField(default='', max_length=10000)),
                ('thmnul', models.ImageField(default='', upload_to='static/thumnel/')),
                ('download', models.CharField(default='', max_length=10000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otp.category')),
            ],
        ),
    ]
