# Generated by Django 5.2.1 on 2025-05-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_regno_student_admno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='admNo',
            new_name='regNo',
        ),
        migrations.AlterField(
            model_name='student',
            name='feeBal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
