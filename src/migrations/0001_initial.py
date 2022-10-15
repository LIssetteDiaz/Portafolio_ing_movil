# Generated by Django 3.1.7 on 2022-10-01 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accionpagina',
            fields=[
                ('accionid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fechain', models.DateField()),
                ('modulo', models.CharField(max_length=100)),
                ('fechaout', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'accionpagina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('menu', models.CharField(max_length=200)),
                ('accion', models.CharField(max_length=250)),
                ('usuario', models.BigIntegerField()),
            ],
            options={
                'db_table': 'auditoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('codename', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('pasillo', models.CharField(max_length=6)),
                ('estante', models.CharField(max_length=6)),
                ('casillero', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'bodega',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('nroboleta', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fechaboleta', models.DateField()),
                ('totalboleta', models.BigIntegerField()),
            ],
            options={
                'db_table': 'boleta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('cargoid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'cargo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('clienteid', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('comunaid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('despachoid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fechasolicitud', models.DateField()),
                ('fechadespacho', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'despacho',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detalleorden',
            fields=[
                ('detalleid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.BigIntegerField()),
            ],
            options={
                'db_table': 'detalleorden',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('direccionid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('nombresector', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'direccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direccioncliente',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'direccioncliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(blank=True, max_length=200, null=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('empleadoid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fechaingreso', models.DateField()),
                ('fechadesvinculacion', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('empresaid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('razonsocial', models.CharField(max_length=50)),
                ('rutcuerpo', models.BigIntegerField()),
                ('dv', models.CharField(max_length=1)),
                ('fono', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('rutina', models.CharField(max_length=150)),
                ('mensaje', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'error',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('estadoid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estadoorden',
            fields=[
                ('estadoordenid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'estadoorden',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numerofactura', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fechafactura', models.DateField()),
                ('neto', models.BigIntegerField()),
                ('iva', models.BigIntegerField()),
                ('totalfactura', models.BigIntegerField()),
            ],
            options={
                'db_table': 'factura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Familiaproducto',
            fields=[
                ('familiaproid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'familiaproducto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Guiadespacho',
            fields=[
                ('nroguia', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fechaguia', models.DateField()),
            ],
            options={
                'db_table': 'guiadespacho',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notacredito',
            fields=[
                ('nronota', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fechanota', models.DateField()),
                ('total', models.BigIntegerField()),
            ],
            options={
                'db_table': 'notacredito',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ordencompra',
            fields=[
                ('ordenid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fechapedido', models.DateField()),
            ],
            options={
                'db_table': 'ordencompra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('personaid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('runcuerpo', models.BigIntegerField()),
                ('dv', models.CharField(max_length=1)),
                ('apellidopaterno', models.CharField(max_length=25)),
                ('apellidomaterno', models.CharField(max_length=25)),
                ('nombres', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('productoid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.BigIntegerField()),
                ('stock', models.BigIntegerField()),
                ('stockcritico', models.BigIntegerField()),
                ('fechavencimiento', models.DateField(blank=True, null=True)),
                ('codigo', models.CharField(max_length=17)),
                ('imagen', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productoproveedor',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'productoproveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('proveedorid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('razonsocial', models.CharField(max_length=50)),
                ('rutcuerpo', models.BigIntegerField()),
                ('dv', models.CharField(max_length=1)),
                ('fono', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('recepcionid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecharecepcion', models.DateField()),
                ('cantidad', models.BigIntegerField()),
            ],
            options={
                'db_table': 'recepcion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('regionid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rolusuario',
            fields=[
                ('rolid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'rolusuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipobarrio',
            fields=[
                ('tipobarrioid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'tipobarrio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipodocumento',
            fields=[
                ('tipodocumentoid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'tipodocumento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipoproducto',
            fields=[
                ('tipoproductoid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tipoproducto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tiporubro',
            fields=[
                ('rubroid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tiporubro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipovivienda',
            fields=[
                ('tipoviviendaid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'tipovivienda',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuarioid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=25)),
                ('nombreusuario', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('nroventa', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.BigIntegerField()),
                ('fechaventa', models.DateField()),
                ('totalventa', models.BigIntegerField()),
            ],
            options={
                'db_table': 'venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ventadiaria',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('totalventa', models.BigIntegerField()),
            ],
            options={
                'db_table': 'ventadiaria',
                'managed': False,
            },
        ),
    ]
