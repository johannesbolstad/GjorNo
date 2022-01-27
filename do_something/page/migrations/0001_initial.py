# Generated by Django 3.1.6 on 2021-03-13 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(verbose_name='date for activity')),
                ('place', models.CharField(choices=[('U', 'Ute'), ('I', 'Inne')], default='U', max_length=1)),
                ('paid', models.CharField(choices=[('B', 'Betalt'), ('G', 'Gratis')], default='B', max_length=1)),
            ],
            options={
                'verbose_name_plural': 'activities',
            },
        ),
    ]