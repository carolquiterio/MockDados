# Generated by Django 3.0.7 on 2020-06-29 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fuel', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ts', models.DateTimeField()),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='device.Device')),
            ],
        ),
        migrations.CreateModel(
            name='AnalyticsFuelWeek',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('count', models.DecimalField(decimal_places=2, max_digits=15)),
                ('min', models.DecimalField(decimal_places=2, max_digits=15)),
                ('max', models.DecimalField(decimal_places=2, max_digits=15)),
                ('avg', models.DecimalField(decimal_places=2, max_digits=15)),
                ('week', models.IntegerField(default=0)),
                ('month', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('ts', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='device.Device')),
            ],
        ),
        migrations.CreateModel(
            name='AnalyticsFuelMonth',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('count', models.DecimalField(decimal_places=2, max_digits=15)),
                ('min', models.DecimalField(decimal_places=2, max_digits=15)),
                ('max', models.DecimalField(decimal_places=2, max_digits=15)),
                ('avg', models.DecimalField(decimal_places=2, max_digits=15)),
                ('month', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('ts', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='device.Device')),
            ],
        ),
        migrations.CreateModel(
            name='AnalyticsFuelDay',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('count', models.DecimalField(decimal_places=2, max_digits=15)),
                ('min', models.DecimalField(decimal_places=2, max_digits=15)),
                ('max', models.DecimalField(decimal_places=2, max_digits=15)),
                ('avg', models.DecimalField(decimal_places=2, max_digits=15)),
                ('day', models.IntegerField(default=0)),
                ('week_day', models.CharField(default='None', max_length=30)),
                ('week', models.IntegerField(default=0)),
                ('month', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('ts', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='device.Device')),
            ],
        ),
    ]
