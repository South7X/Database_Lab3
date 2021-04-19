# Generated by Django 2.2.5 on 2021-04-18 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencycomp',
            fields=[
                ('company_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('company_name', models.TextField(blank=True, null=True)),
                ('company_address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'agencyComp',
            },
        ),
        migrations.CreateModel(
            name='Agencyinfo',
            fields=[
                ('agency_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('agency_name', models.TextField(blank=True, null=True)),
                ('agency_gender', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('agency_phone', models.DecimalField(blank=True, decimal_places=0, max_digits=11, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Agencycomp')),
            ],
            options={
                'db_table': 'agencyInfo',
            },
        ),
        migrations.CreateModel(
            name='Bookhouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book_time', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bookHouse',
            },
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('buyer_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('buyer_name', models.TextField(blank=True, null=True)),
                ('buyer_gender', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('buyer_phone', models.DecimalField(blank=True, decimal_places=0, max_digits=11, null=True)),
            ],
            options={
                'db_table': 'buyer',
            },
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('decoration_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('decoration_type', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'decoration',
            },
        ),
        migrations.CreateModel(
            name='Houseinfo',
            fields=[
                ('house_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('house_name', models.TextField()),
                ('house_price', models.IntegerField(blank=True, null=True)),
                ('house_size', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'houseInfo',
            },
        ),
        migrations.CreateModel(
            name='Housetype',
            fields=[
                ('housetype_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('housetype_name', models.TextField(blank=True, null=True)),
                ('housetype_detail', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'houseType',
            },
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('ownership_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ownership_type', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ownership',
            },
        ),
        migrations.CreateModel(
            name='Usertype',
            fields=[
                ('usertype_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('usertype_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'userType',
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('user_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('user_psw', models.CharField(max_length=20)),
                ('usertype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Usertype')),
            ],
            options={
                'db_table': 'userInfo',
            },
        ),
        migrations.CreateModel(
            name='Starhouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('star_time', models.DateField(blank=True, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Buyer')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Houseinfo')),
            ],
            options={
                'db_table': 'starHouse',
                'unique_together': {('buyer', 'house')},
            },
        ),
        migrations.CreateModel(
            name='Publishhouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('publish_time', models.DateField(blank=True, null=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Agencyinfo')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Houseinfo')),
            ],
            options={
                'db_table': 'publishHouse',
                'unique_together': {('agency', 'house')},
            },
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='agency',
            field=models.ManyToManyField(through='myapp.Publishhouse', to='myapp.Agencyinfo'),
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='book_buyer',
            field=models.ManyToManyField(related_name='book_buyer', through='myapp.Bookhouse', to='myapp.Buyer'),
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='decoration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Decoration'),
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='housetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Housetype'),
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='ownership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Ownership'),
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='star_buyer',
            field=models.ManyToManyField(related_name='star_buyer', through='myapp.Starhouse', to='myapp.Buyer'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='books',
            field=models.ManyToManyField(related_name='books', through='myapp.Bookhouse', to='myapp.Houseinfo'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='stars',
            field=models.ManyToManyField(related_name='stars', through='myapp.Starhouse', to='myapp.Houseinfo'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='user_no',
            field=models.ForeignKey(db_column='user_no', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Userinfo'),
        ),
        migrations.AddField(
            model_name='bookhouse',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Buyer'),
        ),
        migrations.AddField(
            model_name='bookhouse',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Houseinfo'),
        ),
        migrations.AddField(
            model_name='agencyinfo',
            name='house',
            field=models.ManyToManyField(through='myapp.Publishhouse', to='myapp.Houseinfo'),
        ),
        migrations.AddField(
            model_name='agencyinfo',
            name='user_no',
            field=models.ForeignKey(db_column='user_no', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Userinfo'),
        ),
        migrations.AlterUniqueTogether(
            name='bookhouse',
            unique_together={('buyer', 'house')},
        ),
    ]