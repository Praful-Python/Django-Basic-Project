# Generated by Django 3.0.7 on 2020-06-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytestbasic', '0002_auto_20200618_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='customer_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
