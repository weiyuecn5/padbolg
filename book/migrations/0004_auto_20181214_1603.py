# Generated by Django 2.0.2 on 2018-12-14 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pad',
            fields=[
                ('zhbh', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('stsl', models.CharField(blank=True, max_length=100)),
                ('cwbh', models.TextField()),
                ('gxsj', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='book',
        ),
        migrations.DeleteModel(
            name='Shujuku',
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
