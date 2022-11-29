# Generated by Django 4.1.3 on 2022-11-28 00:58

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
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=50, verbose_name='メニュー名')),
                ('size', models.CharField(max_length=3, verbose_name='サイズ')),
                ('price', models.IntegerField(verbose_name='値段')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真2')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真3')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真4')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真5')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False, verbose_name='storeid')),
                ('store_name', models.CharField(max_length=30, verbose_name='店舗名')),
                ('adress', models.CharField(max_length=80, verbose_name='住所')),
                ('seat', models.IntegerField(verbose_name='席数')),
                ('seat_reservationable', models.ImageField(upload_to='', verbose_name='予約可能な席数')),
                ('bussiness_hours', models.TimeField(verbose_name='営業時間')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真2')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真3')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真4')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真5')),
                ('photo6', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真6')),
                ('photo7', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真7')),
                ('photo8', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真8')),
                ('photo9', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真9')),
                ('photo10', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真10')),
                ('bp_id', models.ForeignKey(max_length=16, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='事業者ID')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='予約日時')),
                ('nop', models.IntegerField(verbose_name='予約人数')),
                ('reservation_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='予約者名')),
                ('reservation_mail', models.CharField(blank=True, max_length=40, null=True, verbose_name='予約者メールアドレス')),
                ('reservation_phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='予約者電話番号')),
                ('menu1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_1', to='comp.menu', verbose_name='メニュー1')),
                ('menu2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_2', to='comp.menu', verbose_name='メニュー2')),
                ('menu3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_3', to='comp.menu', verbose_name='メニュー3')),
                ('menu4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_4', to='comp.menu', verbose_name='メニュー4')),
                ('menu5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_5', to='comp.menu', verbose_name='メニュー5')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comp.store', verbose_name='店舗ID')),
                ('user_id', models.ForeignKey(blank=True, max_length=16, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザーID')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comp.store', verbose_name='店舗ID'),
        ),
        migrations.CreateModel(
            name='Kuchikomi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='評価点数')),
                ('impression', models.TextField(max_length=2000, verbose_name='評価内容')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comp.store', verbose_name='店舗ID')),
                ('user_id', models.ForeignKey(max_length=16, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザーID')),
            ],
        ),
    ]
