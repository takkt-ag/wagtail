# Generated by Django 4.0.3 on 2022-04-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0067_alter_customformpagesubmission_form_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customimage",
            name="file_hash",
            field=models.CharField(
                blank=True, db_index=True, editable=False, max_length=40
            ),
        ),
        migrations.AlterField(
            model_name="customimagefilepath",
            name="file_hash",
            field=models.CharField(
                blank=True, db_index=True, editable=False, max_length=40
            ),
        ),
        migrations.AlterField(
            model_name="customimagewithauthor",
            name="file_hash",
            field=models.CharField(
                blank=True, db_index=True, editable=False, max_length=40
            ),
        ),
    ]
