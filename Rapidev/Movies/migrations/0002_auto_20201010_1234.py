# Generated by Django 3.1 on 2020-10-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesdata',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='moviesdata',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='moviesdata',
            name='genre',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='moviesdata',
            name='imgPath',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='moviesdata',
            name='language',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='moviesdata',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='mpaarating',
            name='type',
            field=models.CharField(default='', max_length=20),
        ),
    ]