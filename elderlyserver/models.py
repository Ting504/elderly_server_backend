from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    mail = models.CharField(max_length=45, blank=True, null=True)
    gender = models.BooleanField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    degree = models.IntegerField(blank=True, null=True)
    interested = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user'

class Work(models.Model):
    id = models.AutoField(primary_key=True)
    des = models.CharField(max_length=45, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    hourly_pay = models.FloatField(blank=True, null=True)
    is_long = models.BooleanField(blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    publisher_id_w = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='publisher_id_w')

    class Meta:
        db_table = 'work'

class Volntary(models.Model):
    id = models.AutoField(primary_key=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    des = models.CharField(max_length=45, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    time_money = models.FloatField(blank=True, null=True)
    publisher_id_v = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='publisher_id_v')

    class Meta:
        db_table = 'volntary'

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    des = models.CharField(max_length=45, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    time_money = models.FloatField(blank=True, null=True)
    publisher_id_w = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='publisher_id_w')

    class Meta:
        db_table = 'activity'

class ApplicationWork(models.Model):
    id = models.AutoField(primary_key=True)
    des = models.CharField(max_length=45, blank=True, null=True)
    is_agree = models.BooleanField(blank=True, null=True)
    applicant_id_w = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='applicant_id_w')
    work_id = models.ForeignKey(Work, on_delete=models.DO_NOTHING, db_column='work_id')

    class Meta:
        db_table = 'application_work'

class ApplicationVoluntary(models.Model):
    id = models.AutoField(primary_key=True)
    des = models.CharField(max_length=45, blank=True, null=True)
    application_id_v = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='application_id_v')
    volntary_id = models.ForeignKey(Volntary, on_delete=models.DO_NOTHING, db_column='volntary_id')
    is_agreed = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'application_voluntary'

class ApplicationActivity(models.Model):
    id = models.AutoField(primary_key=True)
    des = models.CharField(max_length=45, blank=True, null=True)
    activity_id = models.ForeignKey(Activity, on_delete=models.DO_NOTHING, db_column='activity_id')
    applicant_id_a = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='applicant_id_a')
    is_agreed = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'application_activity'