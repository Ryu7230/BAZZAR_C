# Generated by Django 4.1.3 on 2022-11-17 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='ユーザーID')),
                ('password', models.CharField(max_length=20, verbose_name='パスワード')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('mail', models.CharField(max_length=40, verbose_name='メールアドレス')),
                ('phone', models.CharField(max_length=11, verbose_name='電話番号')),
            ],
        ),
    ]