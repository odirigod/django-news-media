# Generated by Django 2.1.1 on 2018-09-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180909_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(default='Donald Trump', max_length=60),
            preserve_default=False,
        ),
    ]
