# Generated by Django 4.1 on 2022-12-07 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0010_rename_product_orderitem_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('zip_code', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=30)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signup', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
