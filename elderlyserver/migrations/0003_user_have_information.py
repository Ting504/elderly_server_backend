# Generated by Django 5.2 on 2025-06-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elderlyserver', '0002_applicationactivity_is_over_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='have_information',
            field=models.BooleanField(blank=True, null=True, verbose_name='是否已经提供个人信息'),
        ),
    ]
