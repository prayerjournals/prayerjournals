# Generated by Django 2.2.14 on 2020-08-17 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_note_image1_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='note',
            name='image1',
            field=models.ImageField(upload_to="note_images/<class 'django.contrib.auth.models.User'>/<django.db.models.fields.CharField>/", verbose_name='Image'),
        ),
    ]