# Generated by Django 2.2.1 on 2019-05-23 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceated', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=300)),
                ('rfc', models.CharField(max_length=30)),
                ('contacto', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=30)),
                ('creado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceated', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('numFactura', models.CharField(max_length=20)),
                ('concepto', models.CharField(max_length=250)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=8)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('moneda', models.CharField(choices=[('PESO MXN', 'PESO MXN'), ('DOLAR', 'DOLAR')], max_length=9)),
                ('estatus', models.CharField(choices=[('Aprobado', 'Aprobado'), ('Por pagar', 'Por Pagar'), ('Pagado', 'Pagado'), ('Pagado-Complemento', 'Pagado-Complemento')], max_length=20)),
                ('fechaRecepcion', models.DateField()),
                ('xml', models.ImageField(blank=True, null=True, upload_to='xml/')),
                ('pdf', models.ImageField(blank=True, null=True, upload_to='pdf/')),
                ('otros', models.ImageField(blank=True, null=True, upload_to='otros/')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Empresa')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]