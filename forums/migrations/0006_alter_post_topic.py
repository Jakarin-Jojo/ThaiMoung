# Generated by Django 3.2.8 on 2021-11-20 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0005_alter_topic_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(choices=[('Batman', 'Batman'), ('Thailand', 'Thailand'), ('Apple', 'Apple'), ('Football', 'Football'), ('Fashion Show', 'Fashion Show'), ('Japan', 'Japan')], default='', on_delete=django.db.models.deletion.CASCADE, to='forums.topic'),
        ),
    ]