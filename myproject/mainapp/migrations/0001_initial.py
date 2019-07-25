# Generated by Django 2.2.3 on 2019-07-25 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pbrand', models.CharField(max_length=20, null=True)),
                ('pitem', models.CharField(max_length=20, null=True)),
                ('productimg_name', models.CharField(max_length=40, null=True)),
                ('gifticon', models.FileField(null=True, upload_to='')),
                ('originalprice', models.IntegerField(null=True)),
                ('lowerlimit', models.IntegerField(null=True)),
                ('pub_date', models.DateTimeField(null=True, verbose_name='date published')),
            ],
        ),
    ]
