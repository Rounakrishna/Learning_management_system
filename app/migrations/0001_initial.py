# Generated by Django 5.0.6 on 2024-07-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
