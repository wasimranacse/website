# Generated by Django 2.2.4 on 2019-08-27 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_song_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showbusinessprofile',
            name='type_of_business',
        ),
        migrations.RemoveField(
            model_name='showuserprofile',
            name='full_name',
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
        migrations.DeleteModel(
            name='BusinessProfile',
        ),
        migrations.DeleteModel(
            name='ShowBusinessProfile',
        ),
        migrations.DeleteModel(
            name='ShowUserProfile',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
