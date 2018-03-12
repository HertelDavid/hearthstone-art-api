# Generated by Django 2.0.3 on 2018-03-11 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=255)),
                ('card_name', models.CharField(max_length=255)),
                ('card_text', models.CharField(max_length=255)),
                ('s3_image_link', models.CharField(max_length=255)),
            ],
        ),
    ]
