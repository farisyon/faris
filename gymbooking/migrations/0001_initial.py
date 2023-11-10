# Generated by Django 4.1.7 on 2023-10-22 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('slotid', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('shift', models.TextField(max_length=100)),
                ('time', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('username', models.TextField(max_length=100)),
                ('usergender', models.TextField(max_length=100)),
                ('usercategory', models.TextField(max_length=100)),
                ('userphone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(max_length=100)),
                ('notes', models.TextField(blank=True, max_length=255)),
                ('slotid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymbooking.slot')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymbooking.user')),
            ],
        ),
    ]