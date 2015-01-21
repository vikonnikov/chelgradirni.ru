# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phrase', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '\u043a\u043b\u044e\u0447\u0435\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e',
                'verbose_name_plural': '\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('position', models.IntegerField(verbose_name='\u041f\u043e\u0437\u0438\u0446\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0440\u0430\u0437\u0434\u0435\u043b \u043c\u0435\u043d\u044e',
                'verbose_name_plural': '\u0420\u0430\u0437\u0434\u0435\u043b\u044b \u043c\u0435\u043d\u044e',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('url', models.CharField(max_length=100, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
                ('content', models.TextField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435')),
                ('description', models.TextField(max_length=100, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('keywords', models.ManyToManyField(to='core.Keyword')),
            ],
            options={
                'verbose_name': '\u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='page',
            field=models.OneToOneField(to='core.Page'),
            preserve_default=True,
        ),
    ]
