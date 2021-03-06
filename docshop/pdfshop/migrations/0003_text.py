# Generated by Django 2.1.5 on 2019-02-09 07:07

from django.db import migrations, models
import pdfshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfshop', '0002_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('path', pdfshop.models.ContentTypeRestrictedFileField(upload_to='txt')),
            ],
        ),
    ]
