# Generated by Django 3.2.4 on 2021-06-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0011_alter_storage_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='file',
            field=models.ImageField(default=True, upload_to='data/'),
        ),
    ]
