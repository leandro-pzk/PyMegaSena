# Generated by Django 3.2.9 on 2022-05-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_palpitearquivo_palp_file_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palpitearquivo',
            name='palp_file_nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
