# Generated by Django 3.0.4 on 2020-03-26 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(verbose_name='Rank')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('platform', models.CharField(max_length=50, verbose_name='Platform')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('genre', models.CharField(max_length=50, verbose_name='Gênero')),
                ('publisher', models.CharField(max_length=50, verbose_name='Publisher')),
                ('na_sales', models.FloatField(verbose_name='NA Sales')),
                ('eu_sales', models.FloatField(verbose_name='EU Sales')),
                ('jp_sales', models.FloatField(verbose_name='JP Sales')),
                ('other_sales', models.FloatField(verbose_name='Other Sales')),
            ],
        ),
    ]
