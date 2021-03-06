# Generated by Django 2.2.4 on 2019-08-23 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField(max_length=25)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ShowUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.UserProfile')),
            ],
        ),
    ]
