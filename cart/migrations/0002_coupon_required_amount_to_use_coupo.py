# Generated by Django 3.1.14 on 2022-12-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='required_amount_to_use_coupo',
            field=models.PositiveBigIntegerField(default=100),
            preserve_default=False,
        ),
    ]