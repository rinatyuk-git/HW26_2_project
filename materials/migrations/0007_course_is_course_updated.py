# Generated by Django 5.1.1 on 2024-10-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0006_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_course_updated',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Курс обновлен'),
        ),
    ]