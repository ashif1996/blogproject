# Generated by Django 3.2.15 on 2022-12-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0008_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read the blog post...', max_length=200),
        ),
    ]