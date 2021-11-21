# Generated by Django 3.2.8 on 2021-11-19 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_remove_topic_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.CharField(choices=[('', '----------'), ('news', 'News'), ('sports', 'Sports'), ('game', 'Games'), ('fashion', 'Fashion'), ('technology', 'Technology')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.topic'),
        ),
    ]