# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agencycomp(models.Model):
    company_id = models.CharField(primary_key=True, max_length=10)
    company_name = models.TextField(blank=True, null=True)
    company_address = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'agencyComp'


class Agencyinfo(models.Model):
    agency_id = models.CharField(primary_key=True, max_length=10)
    user_no = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='user_no')
    company = models.ForeignKey(Agencycomp, models.DO_NOTHING, blank=True, null=True)
    agency_name = models.TextField(blank=True, null=True)
    agency_gender = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    agency_phone = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    house = models.ManyToManyField(to='Houseinfo', through='Publishhouse',
                                   through_fields=('agency', 'house'))
    class Meta:
        db_table = 'agencyInfo'


class Bookhouse(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey('Buyer', models.DO_NOTHING)
    house = models.ForeignKey('Houseinfo', models.DO_NOTHING)
    book_time = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'bookHouse'
        unique_together = (('buyer', 'house'),)


class Buyer(models.Model):
    buyer_id = models.CharField(primary_key=True, max_length=10)
    user_no = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='user_no')
    buyer_name = models.TextField(blank=True, null=True)
    buyer_gender = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    buyer_phone = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    stars = models.ManyToManyField(to='Houseinfo', through='Starhouse', related_name='stars',
                                   through_fields=('buyer', 'house'))
    books = models.ManyToManyField(to='Houseinfo', through='Bookhouse', related_name='books',
                                   through_fields=('buyer', 'house'))
    class Meta:
        db_table = 'buyer'


class Decoration(models.Model):
    decoration_id = models.CharField(primary_key=True, max_length=10)
    decoration_type = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'decoration'


class Houseinfo(models.Model):
    house_id = models.CharField(primary_key=True, max_length=10)
    housetype = models.ForeignKey('Housetype', models.DO_NOTHING)
    ownership = models.ForeignKey('Ownership', models.DO_NOTHING, blank=True, null=True)
    decoration = models.ForeignKey(Decoration, models.DO_NOTHING, blank=True, null=True)
    house_name = models.TextField()
    house_price = models.IntegerField(blank=True, null=True)
    house_size = models.IntegerField(blank=True, null=True)
    agency = models.ManyToManyField(to='Agencyinfo', through='Publishhouse',
                                       through_fields=('house', 'agency'))
    star_buyer = models.ManyToManyField(to='Buyer', through='Starhouse', related_name='star_buyer',
                                        through_fields=('house', 'buyer'))
    book_buyer = models.ManyToManyField(to='Buyer', through='Bookhouse', related_name='book_buyer',
                                        through_fields=('house', 'buyer'))
    class Meta:
        db_table = 'houseInfo'


class Housetype(models.Model):
    housetype_id = models.CharField(primary_key=True, max_length=10)
    housetype_name = models.TextField(blank=True, null=True)
    housetype_detail = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'houseType'


class Ownership(models.Model):
    ownership_id = models.CharField(primary_key=True, max_length=10)
    ownership_type = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'ownership'


class Publishhouse(models.Model):
    id = models.AutoField(primary_key=True)
    agency = models.ForeignKey('Agencyinfo', models.DO_NOTHING)
    house = models.ForeignKey('Houseinfo', models.DO_NOTHING)
    publish_time = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'publishHouse'
        unique_together = (('agency', 'house'),)


class Starhouse(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey('Buyer', models.DO_NOTHING)
    house = models.ForeignKey('Houseinfo', models.DO_NOTHING)
    star_time = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'starHouse'
        unique_together = (('buyer', 'house'),)


class Userinfo(models.Model):
    user_no = models.CharField(primary_key=True, max_length=10)
    usertype = models.ForeignKey('Usertype', models.DO_NOTHING, blank=True, null=True)
    user_psw = models.CharField(max_length=20)

    class Meta:
        db_table = 'userInfo'


class Usertype(models.Model):
    usertype_id = models.CharField(primary_key=True, max_length=10)
    usertype_name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'userType'
