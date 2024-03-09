# Generated by Django 5.0.2 on 2024-03-09 08:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('BOOK_FREE', '책: 자유책'), ('BOOK_LOUNGING', '책: 라운징'), ('BOOK_DESIGNATED', '책: 지정책'), ('ENGLISH', '영어')], default='BOOK_FREE', max_length=20)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
                ('host_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '모임 프로그램',
                'verbose_name_plural': '모임 프로그램',
            },
        ),
    ]
