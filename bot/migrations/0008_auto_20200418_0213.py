# Generated by Django 3.0.5 on 2020-04-18 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_profile_cant_fdm'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cant_abs',
            field=models.IntegerField(default=0, verbose_name='Cantidad de ABS'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cant_cnc',
            field=models.IntegerField(default=0, verbose_name='Cantidad de maquinas CNC'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cant_litro_resina',
            field=models.IntegerField(default=0, verbose_name='Cantidad de Litros de Resina'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cant_petg',
            field=models.IntegerField(default=0, verbose_name='Cantidad de PETG'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cant_pla',
            field=models.IntegerField(default=0, verbose_name='Cantidad de PLA'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cant_printerSLA_DLP',
            field=models.IntegerField(default=0, verbose_name='Cantidad de impresoras SLA o DLP'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cant_tpu',
            field=models.IntegerField(default=0, verbose_name='Cantidad de TPU'),
        ),
        migrations.AddField(
            model_name='profile',
            name='diametro_filamento',
            field=models.CharField(max_length=100, null=True, verbose_name='Diametros de filamento'),
        ),
        migrations.AddField(
            model_name='profile',
            name='espesor_acrilico',
            field=models.CharField(max_length=100, null=True, verbose_name='Espesor del acrilico'),
        ),
        migrations.AddField(
            model_name='profile',
            name='espesor_plied_madera',
            field=models.CharField(max_length=100, null=True, verbose_name='Espesor Plied Madera'),
        ),
        migrations.AddField(
            model_name='profile',
            name='espesor_pvc',
            field=models.CharField(max_length=100, null=True, verbose_name='Espesor del PVC'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_cnc',
            field=models.BooleanField(default=False, verbose_name='Tiene maquina CNC'),
        ),
        migrations.AddField(
            model_name='profile',
            name='m2_acrilico',
            field=models.IntegerField(default=0, verbose_name='Cantidad de m2 acrilico'),
        ),
        migrations.AddField(
            model_name='profile',
            name='m2_plied_madera',
            field=models.IntegerField(default=0, verbose_name='M2 de Plied o Madera'),
        ),
        migrations.AddField(
            model_name='profile',
            name='m2_pvc',
            field=models.IntegerField(default=0, verbose_name='M2 de PVC'),
        ),
        migrations.AddField(
            model_name='profile',
            name='materiales_cnc',
            field=models.CharField(max_length=100, null=True, verbose_name='Tipo de material de CNC'),
        ),
        migrations.AddField(
            model_name='profile',
            name='tipo_resina',
            field=models.CharField(max_length=50, null=True, verbose_name='Tipo de Resina'),
        ),
    ]
