# Generated by Django 3.0.3 on 2020-04-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todomodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=100)),
                ('targetdate', models.DateField()),
                ('taskdescp', models.TextField()),
            ],
        ),
    ]
