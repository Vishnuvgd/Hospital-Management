# Generated by Django 4.2.2 on 2023-06-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0009_alter_bookingmodel_doc_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='doc_name',
            field=models.CharField(max_length=20),
        ),
    ]
