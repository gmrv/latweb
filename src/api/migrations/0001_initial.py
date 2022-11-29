# Generated by Django 4.1.3 on 2022-11-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LivenessReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ts', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Наименование', max_length=250)),
                ('is_deleted', models.BooleanField(default=False)),
                ('code', models.PositiveBigIntegerField(default=0, help_text='Код')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
    ]