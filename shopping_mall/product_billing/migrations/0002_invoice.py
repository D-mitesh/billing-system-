# Generated by Django 4.2.11 on 2024-04-07 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
        ('product_billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('products', models.ManyToManyField(related_name='invoices', to='product_billing.productbilling')),
                ('sold_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices_sold', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]