# Generated by Django 2.0.7 on 2020-05-16 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0003_auto_20200516_2256'),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progress',
            name='user',
        ),
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='category',
        ),
        migrations.RemoveField(
            model_name='sitting',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='sitting',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Progress',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='Sitting',
        ),
    ]
