# Generated by Django 5.0.2 on 2024-02-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of the art', max_length=100)),
                ('image', models.ImageField(upload_to='art')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('tags', models.CharField(help_text='Tags (Separated by space. Example: #nature #waterfall)', max_length=200)),
            ],
        ),
    ]