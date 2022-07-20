# Generated by Django 4.0.6 on 2022-07-20 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DispEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeEntry', models.CharField(max_length=50)),
                ('trademark', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('trademark', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('dispentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='computo.dispentry')),
                ('name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            bases=('computo.dispentry',),
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('dispentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='computo.dispentry')),
                ('name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            bases=('computo.dispentry',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computo.computer')),
            ],
        ),
        migrations.AddField(
            model_name='computer',
            name='monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computo.monitor'),
        ),
        migrations.AddField(
            model_name='computer',
            name='keyboard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computo.keyboard'),
        ),
        migrations.AddField(
            model_name='computer',
            name='mouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computo.mouse'),
        ),
    ]
