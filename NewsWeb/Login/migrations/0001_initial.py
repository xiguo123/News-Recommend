# Generated by Django 4.0.3 on 2022-03-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bosonnlp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=20, null=True)),
                ('score', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'bosonnlp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.IntegerField(primary_key=True, serialize=False)),
                ('news_title', models.CharField(max_length=100)),
                ('news_content', models.CharField(max_length=1000)),
                ('news_link', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('news_author', models.CharField(blank=True, max_length=10, null=True)),
                ('news_source', models.CharField(blank=True, max_length=30, null=True)),
                ('news_date', models.DateField(blank=True, null=True)),
                ('news_scan', models.IntegerField(blank=True, null=True)),
                ('news_comment', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'news',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Newsparticiple',
            fields=[
                ('news_id', models.IntegerField(primary_key=True, serialize=False)),
                ('news_title', models.CharField(max_length=100)),
                ('news_participle', models.CharField(max_length=1000)),
                ('emotion_score', models.CharField(blank=True, max_length=20, null=True)),
                ('heat', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'newsparticiple',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Similarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_id1', models.IntegerField(blank=True, null=True)),
                ('news_id2', models.IntegerField(blank=True, null=True)),
                ('similarity', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'similarity',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('sex', models.CharField(blank=True, max_length=1, null=True)),
                ('password', models.CharField(max_length=30)),
                ('telephone', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('type', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
