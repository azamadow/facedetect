# Generated by Django 4.1.4 on 2022-12-13 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Wezipesi')),
            ],
            options={
                'verbose_name': 'Wezipesi',
                'verbose_name_plural': 'Wezipesi',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Detect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Ady')),
                ('surname', models.CharField(max_length=150, verbose_name='Familyasy')),
                ('time_in', models.DateTimeField(auto_now=True, verbose_name='Giren wagty')),
                ('time_out', models.DateTimeField(auto_now=True, verbose_name='Cykan wagty')),
                ('photo', models.ImageField(upload_to='product-img/', verbose_name='Suraty')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.category', verbose_name='Wezipesi')),
            ],
            options={
                'verbose_name': 'Hasaba almak',
                'ordering': ['name'],
            },
        ),
    ]