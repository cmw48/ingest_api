# Generated by Django 2.0.4 on 2018-05-05 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0003_paper_record_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='text',
            new_name='papertext',
        ),
    ]