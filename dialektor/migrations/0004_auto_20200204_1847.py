# Generated by Django 3.0.1 on 2020-02-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dialektor', '0003_metadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata',
            name='fileID',
            field=models.CharField(default='defaultID', max_length=100),
        ),
        migrations.AddField(
            model_name='metadata',
            name='title',
            field=models.CharField(default='defaultTitle', max_length=300),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='category',
            field=models.CharField(default='defaultCategory', max_length=100),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='collection',
            field=models.CharField(default='defaultCollection', max_length=200),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='tags',
            field=models.CharField(default='defaultTags', max_length=200),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='user_id',
            field=models.CharField(default='defaultID', max_length=100),
        ),
    ]
