# Generated by Django 4.1.7 on 2023-03-21 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0004_tag_order_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='scmapp.tag'),
        ),
    ]
