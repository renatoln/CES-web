# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 10:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import fontawesome.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('matricula', models.CharField(max_length=16, unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=250)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='GrupoObjeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, unique=True)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Grupo de Objetos',
                'verbose_name_plural': 'Grupos de Objetos',
            },
        ),
        migrations.CreateModel(
            name='GrupoUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=50, unique=True)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('acessos', models.ManyToManyField(to='ces.GrupoObjeto')),
            ],
            options={
                'verbose_name': 'Grupo de usuários',
                'verbose_name_plural': 'Grupos de usuários',
            },
        ),
        migrations.CreateModel(
            name='MemberGrupoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ces.GrupoUsuario')),
            ],
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reservaInicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('reservaFim', models.DateTimeField(default=django.utils.timezone.now)),
                ('retirada', models.DateTimeField(null=True)),
                ('devolucao', models.DateTimeField(null=True)),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Solicitado Retirada'), (2, 'Emprestado'), (3, 'Solicitado Devolução'), (4, 'Devolvido'), (8, 'Solicitado Reserva')], default=0)),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
                'permissions': (('can_see_details', 'Can see details Movimentacao'), ('can_mark_retired', 'Set Objeto as retired'), ('can_mark_returned', 'Set Objeto as returned')),
            },
        ),
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('status', models.IntegerField(choices=[(1, 'Disponível'), (2, 'Indisponível'), (3, 'Pendente')], default=1)),
            ],
            options={
                'verbose_name': 'Objeto',
                'verbose_name_plural': 'Objetos',
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='TipoObjeto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('icone', fontawesome.fields.IconField(blank=True, max_length=60)),
            ],
            options={
                'verbose_name': 'Tipo de objeto',
                'verbose_name_plural': 'Tipos de objeto',
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
            bases=('ces.usuario',),
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ces.Setor')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
            },
            bases=('ces.usuario',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ces.Departamento')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
            },
            bases=('ces.usuario',),
        ),
        migrations.AddField(
            model_name='objeto',
            name='tipoObjeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ces.TipoObjeto', verbose_name='Tipo de Objeto'),
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='objeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ces.Objeto'),
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='membergrupousuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grupousuario',
            name='usuarios',
            field=models.ManyToManyField(through='ces.MemberGrupoUsuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grupoobjeto',
            name='objetos',
            field=models.ManyToManyField(to='ces.Objeto'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
