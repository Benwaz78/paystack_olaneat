# Generated by Django 2.1 on 2021-04-26 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0002_auto_20210423_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydata',
            name='reference_code',
            field=models.PositiveIntegerField(default=1234567),
            preserve_default=False,
        ),
    ]
