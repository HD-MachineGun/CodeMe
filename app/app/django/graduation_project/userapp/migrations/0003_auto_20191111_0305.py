# Generated by Django 2.2.4 on 2019-11-10 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_problemcounting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemcounting',
            name='problem_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='userapp.Problem'),
        ),
    ]
