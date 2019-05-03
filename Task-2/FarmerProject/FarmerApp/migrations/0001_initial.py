# Generated by Django 2.2.1 on 2019-05-01 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
                ('crop', models.CharField(max_length=100)),
                ('sowing_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FarmerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_after_sowing', models.IntegerField(blank=True)),
                ('fertilizer', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(max_length=100)),
                ('unit', models.CharField(choices=[('L', 'Litre'), ('kg', 'kilograms'), ('g', 'grams'), ('mL', 'mililitre'), ('ton', 'tones')], max_length=10)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FarmerApp.FarmData')),
            ],
        ),
        migrations.AddField(
            model_name='farmdata',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FarmerApp.FarmerData'),
        ),
    ]
