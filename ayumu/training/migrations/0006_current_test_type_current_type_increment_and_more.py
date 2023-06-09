# Generated by Django 4.0.4 on 2022-05-21 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_alter_eng_options_alter_rus_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='current',
            name='test_type',
            field=models.CharField(choices=[('ER', 'ER'), ('RE', 'RE')], default='ER', max_length=2),
        ),
        migrations.AddField(
            model_name='current',
            name='type_increment',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='eng',
            name='eng',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='rus',
            name='rus',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
