# Generated by Django 2.2.3 on 2019-07-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0010_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('item', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=40)),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
