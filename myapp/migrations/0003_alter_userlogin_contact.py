# Generated by Django 4.2.1 on 2023-05-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_userlogin_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='Contact',
            field=models.CharField(max_length=12),
        ),
    ]