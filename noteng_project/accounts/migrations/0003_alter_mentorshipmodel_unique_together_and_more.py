# Generated by Django 4.2.7 on 2024-05-03 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_mentorshipmodel'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mentorshipmodel',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='mentorshipmodel',
            name='mentorship_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='mentorshipmodel',
            name='id',
        ),
    ]
