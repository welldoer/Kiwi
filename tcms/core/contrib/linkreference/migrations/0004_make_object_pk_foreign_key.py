# Generated by Django 2.0 on 2017-12-29 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testruns', '0001_initial'),
        ('linkreference', '0003_disconect_from_content_types'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linkreference',
            old_name='object_pk',
            new_name='test_case_run',
        ),
        migrations.AlterField(
            model_name='linkreference',
            name='test_case_run',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='testruns.TestCaseRun'),
        ),
    ]
