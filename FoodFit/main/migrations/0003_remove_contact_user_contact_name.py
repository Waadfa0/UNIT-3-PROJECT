# Generated by Django 5.0.3 on 2024-04-01 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_recipe_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default=2, max_length=64),
            preserve_default=False,
        ),
    ]
