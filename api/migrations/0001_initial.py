# Generated by Django 5.0.6 on 2024-06-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keynum', models.IntegerField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('office', models.CharField(max_length=200)),
                ('tac', models.CharField(max_length=200)),
                ('hm', models.CharField(max_length=200)),
            ],
        ),
    ]
