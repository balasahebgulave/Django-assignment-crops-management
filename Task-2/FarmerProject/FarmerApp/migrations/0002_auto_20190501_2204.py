# Generated by Django 2.2.1 on 2019-05-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledata',
            name='price',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scheduledata',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]