from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class PatientModel(models.Model):
    ID=models.CharField(db_column='ID',max_length=9,primary_key=True)
    firstname=models.TextField(db_column='firstname')
    lastname=models.TextField(db_column='lastname')
    password=models.CharField(db_column='password',max_length=10)
    messagesent=models.TextField(db_column='messagesent')
    doctoranswer=models.TextField(db_column='doctoranswer')
    DID=models.CharField(db_column='DID',max_length=9)
    medicalrecord=models.TextField(db_column='medicalrecord')
    privaterecord=models.TextField(db_column='privaterecord')
    adminmess=models.TextField(db_column='adminmess')
    adminanswer=models.TextField(db_column='adminanswer')
    #model PatientInfos
    age=models.IntegerField(db_column='age')
    poids=models.IntegerField(db_column='poids')
    taille=models.IntegerField(db_column='taille')
    allergies=models.TextField(db_column='allergies')
    BMI=models.IntegerField(db_column='BMI')
    phone=models.CharField(db_column='phone',max_length=10)
    medrecom=models.TextField(db_column='medrecom')
    appointement=models.TextField(db_column='appointement')
    autorizations=models.TextField(db_column='autorizations')
    latestreport=models.TextField(db_column='latestreport',default='null')
    class Meta:
        managed = True
        db_table = 'user'

class DoctorModel(models.Model):
    ID=models.CharField(db_column='ID',max_length=9,primary_key=True)
    firstname=models.TextField(db_column='firstname')
    lastname=models.TextField(db_column='lastname')
    password=models.CharField(db_column='password',max_length=10)
    workdays=models.TextField(db_column='workday')
    adminmess=models.TextField(db_column='adminmess')
    adminanswer=models.TextField(db_column='adminanswer')
    speciality=models.TextField(db_column='speciality')
    doctormessages=models.TextField(db_column='doctormessages',default='null')
    doctorsanswer=models.TextField(db_column='doctorsanswer',default='null')
    class Meta:
        managed = True
        db_table = 'doctor'


class Adminmodel(models.Model):
    ID=models.CharField(db_column='ID',max_length=9,primary_key=True)
    firstname=models.TextField(db_column='firstname')
    lastname=models.TextField(db_column='lastname')
    password=models.CharField(db_column='password',max_length=10)
    messagesent=models.TextField(db_column='messagesent')
    class Meta:
        managed = True
        db_table = 'admin'

class MessageModel(models.Model):
    ID=models.CharField(db_column='ID',max_length=9,primary_key=True)
    message=models.TextField(db_column='message')
    class Meta:
        managed = True
        db_table = 'generalmessage'


class MedsModel(models.Model):
    # med data base
    ID=models.IntegerField(db_column='ID',primary_key=True)
    name=models.TextField(db_column='name')
    description=models.TextField(db_column='description')
    price=models.FloatField(db_column='price')
    reason=models.TextField(db_column='reason')
    type=models.TextField(db_column='type')
    estock=models.IntegerField(db_column='estock')
    pstock=models.IntegerField(db_column='pstock')
    class Meta:
        managed = True
        db_table = 'meds'

class cartModel(models.Model):
     # cart data bases
    CID=models.CharField(db_column='CID',max_length=9,primary_key=True)
    MIDS=models.CharField(db_column='MIDS',max_length=50)
    totalprice=models.IntegerField(db_column='totalprice')
    name=models.TextField(db_column='name')
    class Meta:
        managed = True
        db_table = 'customercart'

class newcustomerModel(models.Model):
    firstname=models.TextField(db_column='firstname')
    lastname=models.TextField(db_column='lastname')
    email=models.TextField(db_column='email')
    phone=models.CharField(db_column='phone',max_length=10,primary_key=True)
    class Meta:
        managed = True
        db_table = 'newcustomer'

class bloodTestModel(models.Model):
    CID=models.CharField(db_column='CID',max_length=9,primary_key=True)
    alk_phos=models.TextField(db_column='alk_phos')
    hdl=models.TextField(db_column='hdl')
    iron=models.TextField(db_column='iron')
    creat=models.TextField(db_column='creat')
    hb=models.TextField(db_column='hb')
    urea=models.TextField(db_column='urea')
    class Meta:
        managed = True
        db_table = 'bloodTest'