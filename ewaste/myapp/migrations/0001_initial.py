# Generated by Django 4.1 on 2022-08-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form_edonator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=122)),
                ('Contact_no', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('e_img', models.FileField(upload_to='')),
            ],
        ),
    ]
