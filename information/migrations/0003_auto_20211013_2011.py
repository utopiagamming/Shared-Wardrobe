# Generated by Django 3.2.8 on 2021-10-13 12:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('information', '0002_auto_20211013_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopcart',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='if_buy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='cate_id',
            field=models.CharField(max_length=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='create_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.usersinfo'),
        ),
        migrations.AlterUniqueTogether(
            name='shopcart',
            unique_together=set(),
        ),
    ]