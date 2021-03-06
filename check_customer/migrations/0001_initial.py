# Generated by Django 3.0.5 on 2021-11-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=5)),
                ('gender', models.CharField(max_length=10)),
                ('housing', models.CharField(max_length=150)),
                ('residence_since', models.CharField(max_length=10)),
                ('marital_status', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('foreign', models.CharField(max_length=50)),
                ('employment_status', models.CharField(max_length=50)),
                ('employment_type', models.CharField(max_length=50)),
                ('checking_account', models.CharField(max_length=50)),
                ('savings_account', models.CharField(max_length=50)),
                ('property_type', models.CharField(max_length=100)),
                ('installment_plans', models.CharField(max_length=50)),
                ('existing_credits', models.CharField(max_length=50)),
                ('credit_history', models.CharField(max_length=150)),
                ('credit_amount', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('installment_rate', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=150)),
                ('debtor', models.CharField(max_length=50)),
                ('maintainence', models.CharField(max_length=50)),
            ],
        ),
    ]
