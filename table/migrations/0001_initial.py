# Generated by Django 4.1.4 on 2022-12-29 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CargoType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WagonAssembly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WagonComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WagonDefect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WagonStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='WagonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ReportTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('wagonNum', models.CharField(max_length=8)),
                ('wagonNumNewComponents', models.IntegerField()),
                ('dateRepair', models.DateField(null=True)),
                ('note', models.CharField(max_length=50)),
                ('CargoType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='table.cargotype', verbose_name='CargoType')),
                ('WagonComponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='table.wagoncomponent', verbose_name='WagonComponent')),
                ('employeeName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='table.employeename', verbose_name='EmployeeName')),
                ('wagonAssembly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='table.wagonassembly', verbose_name='WagonAssembly')),
                ('wagonDefect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='table.wagondefect', verbose_name='WagonDefect')),
                ('wagonStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='table.wagonstatus', verbose_name='WagonStatus')),
                ('wagonType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='table.wagontype', verbose_name='WagonType')),
            ],
        ),
    ]