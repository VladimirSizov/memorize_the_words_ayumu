# Generated by Django 4.0.4 on 2022-05-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0020_remove_current_ff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='current',
            name='last_word_eng',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='current',
            name='last_word_rus',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
