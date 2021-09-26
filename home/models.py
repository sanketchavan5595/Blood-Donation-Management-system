from django.db import models

# Create your models here.
class Bloodbank(models.Model):
    bankid = models.AutoField(db_column='bankID', primary_key=True)  # Field name made lowercase.
    location = models.CharField(max_length=20, blank=True, null=True)
    bankname = models.CharField(db_column='bankName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bloodbank'
    
    def __str__(self):
        return self.bankname
    

class Hospital(models.Model):
    hospitalid = models.AutoField(db_column='hospitalID', primary_key=True)  # Field name made lowercase.
    location = models.CharField(max_length=20, blank=True, null=True)
    hospitalname = models.CharField(db_column='hospitalName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hospital'
    
    def __str__(self):
        return self.hospitalname

class Donor(models.Model):
    donorid = models.AutoField(db_column='donorID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bankid = models.ForeignKey(Bloodbank, models.DO_NOTHING, db_column='bankID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'donor'
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Blood(models.Model):
    bloodid = models.AutoField(db_column='bloodID', primary_key=True)  # Field name made lowercase.
    bloodtype = models.CharField(db_column='bloodType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bankid = models.ForeignKey('Bloodbank', models.DO_NOTHING, db_column='bankID', blank=True, null=True)  # Field name made lowercase.
    donorid = models.ForeignKey('Donor', models.DO_NOTHING, db_column='donorID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'blood'
    
    def __str__(self):
        return str(self.bloodid) + ' ' + self.bloodtype


class Orders(models.Model):
    bankid = models.OneToOneField(Bloodbank, models.DO_NOTHING, db_column='bankID', primary_key=True)  # Field name made lowercase.
    hospitalid = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='hospitalID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'
        unique_together = (('bankid', 'hospitalid'),)
    
    def __str__(self):
        return self.bankid + self.hospitalid


class Patient(models.Model):
    patientid = models.AutoField(db_column='patientID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    pbloodtype = models.CharField(db_column='pBloodType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hospitalid = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='hospitalID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient'
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname