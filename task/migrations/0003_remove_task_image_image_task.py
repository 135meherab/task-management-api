# Generated by Django 4.2.7 on 2024-02-13 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task.task'),
        ),
    ]
