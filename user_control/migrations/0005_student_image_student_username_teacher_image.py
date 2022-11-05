# Generated by Django 4.1.2 on 2022-11-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0004_fileupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='Rasheed', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.TextField(null=True),
        ),
    ]
