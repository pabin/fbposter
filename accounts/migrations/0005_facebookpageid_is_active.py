# Generated by Django 2.1.7 on 2019-06-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_facebookpageid_is_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookpageid',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]