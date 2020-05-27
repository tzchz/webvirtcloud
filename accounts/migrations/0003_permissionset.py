# Generated by Django 2.2.12 on 2020-05-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_addAdmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('change_password', 'Can change password'),),
                'managed': False,
                'default_permissions': (),
            },
        ),
    ]
