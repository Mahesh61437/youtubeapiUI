# Generated by Django 2.2.1 on 2019-05-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20190529_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchdetail',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
