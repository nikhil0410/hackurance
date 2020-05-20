# Generated by Django 2.0.7 on 2020-05-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_getfreequote'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollmentmodel',
            name='expected_product',
            field=models.CharField(choices=[('Life Insurance', 'Life Insurance'), ('Group Insurance', 'Group Insurance'), ('Travel Insurance', 'Travel Insurance'), ('Health Insurance', 'Health Insurance'), ('Dental insurance', 'Dental insurance'), ('Vision insurance', 'Vision insurance'), ('Accident insurance', 'Accident insurance'), ('Critical illiness insurance', 'Critical illiness insurance'), ('Motor Policy', 'Motor Policy')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='enrollmentmodel',
            name='prob_of_buying',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='enrollmentmodel',
            name='product',
            field=models.CharField(choices=[('Life Insurance', 'Life Insurance'), ('Group Insurance', 'Group Insurance'), ('Travel Insurance', 'Travel Insurance'), ('Health Insurance', 'Health Insurance'), ('Dental insurance', 'Dental insurance'), ('Vision insurance', 'Vision insurance'), ('Accident insurance', 'Accident insurance'), ('Critical illiness insurance', 'Critical illiness insurance'), ('Motor Policy', 'Motor Policy')], max_length=100, null=True),
        ),
    ]