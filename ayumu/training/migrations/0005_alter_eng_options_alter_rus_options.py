# Generated by Django 4.0.4 on 2022-05-19 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_eng_rus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eng',
            options={'ordering': ('eng',)},
        ),
        migrations.AlterModelOptions(
            name='rus',
            options={'ordering': ('rus',)},
        ),
    ]
