# Generated by Django 2.0.4 on 2018-04-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
