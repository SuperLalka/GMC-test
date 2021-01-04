# Generated by Django 3.1.4 on 2021-01-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_group',
            field=models.CharField(choices=[('admin', 'administrator'), ('client', 'client')], default='client', help_text='Select user group', max_length=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a description for the book', max_length=1000,
                                   null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='Enter the ISBN of the book', max_length=17),
        ),
    ]
