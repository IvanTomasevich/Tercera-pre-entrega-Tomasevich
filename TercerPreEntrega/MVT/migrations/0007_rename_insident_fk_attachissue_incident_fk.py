# Generated by Django 4.2.1 on 2023-05-21 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MVT', '0006_alter_attachissue_insident_fk_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachissue',
            old_name='insident_fk',
            new_name='incident_fk',
        ),
    ]
