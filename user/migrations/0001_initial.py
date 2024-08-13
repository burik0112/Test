# Generated by Django 4.2.15 on 2024-08-13 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Working', models.BooleanField()),
                ('TimeSheetCodeEN', models.CharField(max_length=56)),
                ('TimeSheetCodeRU', models.CharField(max_length=56)),
                ('TimeSheetCodeTR', models.CharField(max_length=56)),
                ('TimeSheetCode', models.CharField(max_length=10)),
                ('DescriptionRU', models.TextField()),
            ],
        ),
    ]
