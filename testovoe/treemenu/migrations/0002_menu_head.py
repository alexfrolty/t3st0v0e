# Generated by Django 4.2 on 2023-04-05 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treemenu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='head',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
