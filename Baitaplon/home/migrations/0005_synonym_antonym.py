# Generated by Django 4.2.4 on 2023-10-17 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_dictionaryentry_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('synonym', models.CharField(max_length=100)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='synonyms', to='home.dictionaryentry')),
            ],
        ),
        migrations.CreateModel(
            name='Antonym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antonym', models.CharField(max_length=100)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='antonyms', to='home.dictionaryentry')),
            ],
        ),
    ]
