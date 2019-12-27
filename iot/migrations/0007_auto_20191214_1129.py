# Generated by Django 2.1.15 on 2019-12-14 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0006_auto_20191125_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datapoint',
            old_name='time',
            new_name='collect_time',
        ),
        migrations.RenameField(
            model_name='datapoint',
            old_name='timestamp',
            new_name='report_time',
        ),
        migrations.AlterField(
            model_name='sensor',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True, verbose_name='上次数据时间'),
        ),
    ]
