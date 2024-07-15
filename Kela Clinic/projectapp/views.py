from random import random
from tkinter import Frame
from xml.etree.ElementTree import tostring
#rom cv2 import COLOR_BGR2GRAY, destroyAllWindows
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
#from traitlets import All
from projectapp.models import *
import mysql.connector
from django.http import JsonResponse
import random
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
#import numpy as np
#import cv2
#import pickle
from django.core.files.storage import FileSystemStorage
import requests
import json
import os
import time
#from PIL import Image  
#import PIL  
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="projectapp"
)
cursor = db_connection.cursor()
print(db_connection)
# START PAGE WITH ANIMATION

medsnames =  ["Methylphenidate Hydrochloride",
                "Glimepiride",
                "Methocarbamol",
                "Acetaminophen",
                "Oasis TEARS PLUS",
                "Selenium",
                "Calcium Acetate",
                "entresto",
                "Etodolac",
                "Ciclosporin",
                "Lithium Bromatum",
                "Flovent Diskus",
                "Methyldopa",
                "Tazorac",
                "Linezolid",
                "Losartan",
                "ciprofloxacin"
                ]   
Warn=[]
for med in medsnames:
            path = "https://api.fda.gov/drug/label.json?search=" + med
            response = requests.get(path)
            js = response.json()["results"]
            contect_medical = js[0]
            WARNINGS  = ""
            if 'boxed_warning' in contect_medical:
                WARNINGS = contect_medical["boxed_warning"]
            elif 'warnings' in contect_medical:
                WARNINGS = contect_medical["warnings"]
            else:
                WARNINGS = contect_medical["warnings_and_cautions"]
            if len(WARNINGS)>1:
                Warn.append(WARNINGS[0])
            else:
                Warn+=WARNINGS
zip_iterator = zip(medsnames, Warn)
a_dictionary = dict(zip_iterator)


def index(request):
    return render(request, 'customers/homepage.html')

def newcust(request):
    if request.method == 'POST':
        firstname1 = request.POST.get('firstname')
        lastname1 = request.POST.get('lastname')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('phone')
        print(firstname1,lastname1,email1,phone1)
        saveobject=newcustomerModel()
        saveobject.firstname=firstname1
        saveobject.lastname=lastname1
        saveobject.email=email1
        saveobject.phone=phone1
        saveobject.save()
        return render(request, 'customers/homepage.html')

def userlogin(request):
    return render(request, 'customers/loginpage.html')

#login functions###############################
def login(request):
    return render(request, 'doctors/loginpage.html')

def userdash(request):
    mess=MessageModel.objects.filter(ID=1)
    try:        
        if request.method == 'POST':
                ID = request.POST.get('ID')
                password = request.POST.get('password')
                print(ID,password)
                PatientModel1 = PatientModel.objects.filter(ID=ID, password=password)
                PatientModeltest = PatientModel.objects.filter(ID=ID, password=password).first()
                DID=PatientModeltest.DID
                DoctorModel3 = DoctorModel.objects.filter(ID=DID).first()
                print(DoctorModel3)
                workday2=DoctorModel3.workdays
                print(workday2)
                x = workday2.split(",")
                dictOfWords = { i : 10 for i in x }
                meds = PatientModeltest.medrecom.split(",")
                dictOfWords1 = { i : 10 for i in meds }
                hours=['10:00','10:30','11:00','11:30','12:00','12:30','13:00']
                dichours = { i : 10 for i in hours }
                DoctorModel1 = DoctorModel.objects.filter(ID=DID)
                AdminModel1 = Adminmodel.objects.filter(ID=222333444)
                print(dictOfWords) 
                if PatientModel1:
                    return render(request, 'customers/dash.html', {"DoctorModel": DoctorModel1,"AdminModel": AdminModel1,"PatientModel": PatientModel1, "message":mess,'dictOfWords':dictOfWords,'medslist':dictOfWords1,"dichours":dichours})  
                else:
                    return render(request, 'customers/loginpage.html')
    except:
        return render(request, 'customers/loginpage.html')

def userdashbutton(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        PatientModeltest = PatientModel.objects.filter(ID=ID).first()
        DID=PatientModeltest.DID
        DoctorModel3 = DoctorModel.objects.filter(ID=DID).first()
        print(DoctorModel3)
        workday2=DoctorModel3.workdays
        print(workday2)
        x = workday2.split(",")
        workday = { i : 10 for i in x }
        meds = PatientModeltest.medrecom.split(",")
        dictOfWords1 = { i : 10 for i in meds }
        hours=['10:00','10:30','11:00','11:30','12:00','12:30','13:00']
        dichours = { i : 10 for i in hours }
        print(workday) 
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        AdminModel1 = Adminmodel.objects.filter(ID=222333444)
        if PatientModel1:
            return render(request, 'customers/dash.html', {"DoctorModel": DoctorModel1,"AdminModel": AdminModel1,"PatientModel": PatientModel1, "message":mess,'dictOfWords':workday,'medslist':dictOfWords1,"dichours":dichours})  

def rdv(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('CID')
        day=request.POST.get('Cday')
        hour=request.POST.get('hour')
        print(ID,day)
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        PatientModeltest = PatientModel.objects.filter(ID=ID).first()
        DID=PatientModeltest.DID
        DoctorModel3 = DoctorModel.objects.filter(ID=DID).first()
        print(DoctorModel3)
        workday2=DoctorModel3.workdays
        print(workday2)
        x = workday2.split(",")
        dictOfWords = { i : 10 for i in x }
        meds = PatientModeltest.medrecom.split(",")
        dictOfWords1 = { i : 10 for i in meds }
        hours=['10:00','10:30','11:00','11:30','12:00','12:30','13:00']
        dichours = { i : 10 for i in hours }
        app=day+" "+hour
        PatientModel3 = PatientModel.objects.filter(appointement=app,DID=DID)
        print(PatientModel3)
        if PatientModel3:     
            messages.error(request," is already Taken choose an other appointement")           
        else:
            cursor.execute("UPDATE `user` SET `appointement` = '%s' WHERE `user`.`ID` = '%s';"%(app,ID))
            db_connection.commit()
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        AdminModel1 = Adminmodel.objects.filter(ID=222333444)
        print(dictOfWords)
        if PatientModel1:
            return render(request, 'customers/dash.html', {"DoctorModel": DoctorModel1,"AdminModel": AdminModel1,"PatientModel": PatientModel1, "message":mess,'dictOfWords':dictOfWords,'medslist':dictOfWords1,'dichours':dichours}) 

def doctorinfo(request):
    mess=MessageModel.objects.filter(ID=1)
    allmed=MedsModel.objects.all()
    if request.method == 'POST':
        ID = request.POST.get('ID')
        DoctorModel1 = DoctorModel.objects.filter(ID=ID)
        DoctorModelall = DoctorModel.objects.all()
        if DoctorModel1:
                return render(request, 'doctors/privateinfo.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':allmed,"DoctorModelall":DoctorModelall})


def workersdash(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        DoctorModel1 = DoctorModel.objects.filter(ID=ID, password=password)
        PatientModel1 = PatientModel.objects.filter(DID=ID)
        Adminmodel1 = Adminmodel.objects.filter(ID=ID, password=password)
        print(PatientModel1)
        if DoctorModel1:
            return render(request, 'doctors/dash.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1, "message":mess})  
        elif Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            PatientModelall= PatientModel.objects.all()
            newcustomerModelall = newcustomerModel.objects.all()
            return render(request, 'admin/dash.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModelall , "PatientModel":PatientModelall , "message":mess,'newcustomerModel':newcustomerModelall })
        else:
            return render(request, 'doctors/loginpage.html')
    else:
        return render(request, 'doctors/loginpage.html')      

def admindashbtn(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
         ID = request.POST.get('ID')
         Adminmodel1 = Adminmodel.objects.filter(ID=ID)
         if Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            PatientModelall= PatientModel.objects.all()
            newcustomerModelall = newcustomerModel.objects.all()
            return render(request, 'admin/dash.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModelall , "PatientModel":PatientModelall , "message":mess,'newcustomerModel':newcustomerModelall })

def dochomebut(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        DoctorModel1 = DoctorModel.objects.filter(ID=ID)
        PatientModel1 = PatientModel.objects.filter(DID=ID)
        print(PatientModel1)
        if DoctorModel1:
            return render(request, 'doctors/dash.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1, "message":mess})  

def adminpharmacy(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        allmed=MedsModel.objects.all()      
        return render(request, 'admin/pharmacygest.html', {"AdminModel": Adminmodel1, "message":mess, 'meds':allmed})

def addmeds(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        allmed=MedsModel.objects.all()      
        return render(request, 'admin/addmeds.html', {"AdminModel": Adminmodel1, "message":mess, 'meds':allmed})

def addmed(request):
    #add new medical
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST' and request.FILES['myfile']:
        ID = request.POST.get('AID')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        pstock = request.POST.get('pstock')
        estock = request.POST.get('estock')
        reason= request.POST.get('reason')
        saveobj=MedsModel()
        saveobj.name=name
        saveobj.description=description
        saveobj.price=price
        saveobj.pstock=pstock
        saveobj.estock=estock
        saveobj.reason=reason
        saveobj.save()
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        med=MedsModel.objects.filter(name=name).first()
        medid=med.ID
        fs.save('projectapp\\static\\pharmacieimg\\'+str(medid)+'.jpg', myfile)
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        allmed=MedsModel.objects.all()      
        return render(request, 'admin/addmeds.html', {"AdminModel": Adminmodel1, "message":mess, 'meds':allmed})


def adminmedinfo(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('DID')
        MID = request.POST.get('MID')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        MedsModel1 = MedsModel.objects.filter(ID=MID)
        samemeds=MedsModel.objects.filter(ID=MID).first()
        samemedsreason=samemeds.reason
        MedsModelR = MedsModel.objects.filter(reason=samemedsreason)
        if Adminmodel1 and MedsModel1 :
            return render(request, 'admin/medinfo.html', {"Adminmodel": Adminmodel1, "message":mess, 'meds':MedsModel1,'meds2':MedsModelR,"a_dictionary":a_dictionary})

def medchange(request):
    #change quantities remove med
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('AID')
        MID = request.POST.get('MID')
        estock = request.POST.get('estock')
        pstock = request.POST.get('pstock')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        MedsModel1 = MedsModel.objects.filter(ID=MID)
        cursor.execute("UPDATE `meds` SET `estock` = '%s' WHERE `meds`.`ID` = '%s';"%(estock,MID))
        db_connection.commit()
        cursor.execute("UPDATE `meds` SET `pstock` = '%s' WHERE `meds`.`ID` = '%s';"%(pstock,MID))
        db_connection.commit()
        samemeds=MedsModel.objects.filter(ID=MID).first()
        samemedsreason=samemeds.reason
        MedsModelR = MedsModel.objects.filter(reason=samemedsreason)
        if Adminmodel1 and MedsModel1 :
            return render(request, 'admin/medinfo.html', {"Adminmodel": Adminmodel1, "message":mess, 'meds':MedsModel1,'meds2':MedsModelR,"a_dictionary":a_dictionary})    

def addpatpage(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        NID = request.POST.get('NID')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        newcustomerModel1 = newcustomerModel.objects.filter(phone=NID)
        docmodels1 = DoctorModel.objects.all()
        print(Adminmodel1)
        if Adminmodel1:
            return render(request, 'admin/addpat.html', {"Adminmodel":Adminmodel1,"message":mess,'newcustomerModel':newcustomerModel1,'docmodels':docmodels1})  

def addpatient(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST' and request.FILES['myfile']and request.FILES['myfile2']and request.FILES['myfile3']and request.FILES['myfile4']:
        try:
            ID = request.POST.get('AID') 
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            password = request.POST.get('password')
            CID = request.POST.get('CID')
            Age = request.POST.get('Age')
            Weight = request.POST.get('Weight')
            Size = request.POST.get('Size')
            phone = request.POST.get('phone')
            Allergies = request.POST.get('Allergies')
            DID = request.POST.get('DID')
            bloodtest(CID)
            print(ID,firstname,lastname,password,CID,Age,Weight,Size,Allergies,DID)
            directory = str(firstname)
            parent_dir = 'projectapp/images/'
            path = os.path.join(parent_dir, directory)
            print(path)
            os.mkdir(path)
            saveob=PatientModel()
            saveob.ID=CID
            saveob.firstname=firstname
            saveob.lastname=lastname
            saveob.password=password
            saveob.DID=DID
            saveob.age=Age
            saveob.poids=Weight
            saveob.taille=Size
            saveob.BMI=(int(Weight))/((int(Size)/100)*(int(Size)/100))
            saveob.phone=phone
            saveob.allergies=Allergies
            saveob.autorizations='no'
            saveob.save()
            img1 = request.FILES['myfile']
            img2 = request.FILES['myfile2']
            img3 = request.FILES['myfile3']
            img4 = request.FILES['myfile4']
            fs = FileSystemStorage()
            fs.save(path+'/'+CID+'.jpg', img1)
            fs.save(path+'/img2.jpg', img2)
            fs.save(path+'/img3.jpg', img3)
            fs.save(path+'/img4.jpg', img4)
            cursor.execute("DELETE FROM `newcustomer` WHERE `newcustomer`.`phone` = '%s';"%(phone))
            parent_dir2 = 'projectapp/static/dashstatic/img/'
            fs = FileSystemStorage()
            fs.save(parent_dir2+'/'+CID+'.png', img1)
            db_connection.commit()
            Adminmodel1 = Adminmodel.objects.filter(ID=ID)
            newcustomerModel1 = PatientModel.objects.filter(ID=CID)
            print(newcustomerModel1)
            if Adminmodel1:
                newcustomerModelall = newcustomerModel.objects.all()
                DoctorModelall= DoctorModel.objects.all()
                PatientModelall= PatientModel.objects.all()
                return render(request, 'admin/dash.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModelall , "PatientModel":PatientModelall , "message":mess,"newcustomerModel":newcustomerModelall }) 
        except:
            messages.error(request," ID ALREADY TAKEN ")
            Adminmodel1 = Adminmodel.objects.filter(ID=ID)
            if Adminmodel1:
                newcustomerModelall = newcustomerModel.objects.all()
                DoctorModelall= DoctorModel.objects.all()
                PatientModelall= PatientModel.objects.all()
                return render(request, 'admin/dash.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModelall , "PatientModel":PatientModelall , "message":mess,"newcustomerModel":newcustomerModelall })

def adddocpage(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        print(Adminmodel1)
        print("in add page")
        if Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            return render(request, 'admin/adddoc.html', {"Adminmodel":Adminmodel1,"message":mess,"DoctorModel":DoctorModelall}) 

def adddoctor(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST' and request.FILES['myfile'] :
        AID = request.POST.get('AID')
        ID = request.POST.get('ID')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        speciality = request.POST.get('spec')
        password='Aa123456'
        saveobj=DoctorModel()
        saveobj.ID=ID
        saveobj.firstname=firstname
        saveobj.lastname=lastname
        saveobj.speciality=speciality
        saveobj.password=password
        saveobj.workdays=None
        saveobj.adminmess=None
        saveobj.adminanswer=None
        saveobj.save()
        img1 = request.FILES['myfile']
        parent_dir2 = 'projectapp/static/dashstatic/img/'
        fs = FileSystemStorage()
        fs.save(parent_dir2+'/'+ID+'.png', img1)
        Adminmodel1 = Adminmodel.objects.filter(ID=AID)
        if Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            return render(request, 'admin/adddoc.html', {"Adminmodel":Adminmodel1,"message":mess,"DoctorModel":DoctorModelall}) 

def deletedoc(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        DID = request.POST.get('DID')
        ID = request.POST.get('ID')    
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        cursor.execute("DELETE FROM `doctor` WHERE `doctor`.`ID` = '%s';"%(DID))
        db_connection.commit()
        if Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            PatientModelall= PatientModel.objects.all()
            newcustomerModelall = newcustomerModel.objects.all()
            return render(request, 'admin/dash.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModelall , "PatientModel":PatientModelall , "message":mess,'newcustomerModel':newcustomerModelall })


def deletepatient(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PID')
        ID = request.POST.get('ID')    
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        cursor.execute("DELETE FROM `user` WHERE `user`.`ID` = '%s';"%(PID))
        db_connection.commit()
        if Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            PatientModelall= PatientModel.objects.all()
            newcustomerModelall = newcustomerModel.objects.all()
            return render(request, 'admin/dash.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModelall , "PatientModel":PatientModelall , "message":mess,'newcustomerModel':newcustomerModelall })



def deletemed(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        MID = request.POST.get('MID')
        ID = request.POST.get('AID') 
        print(ID)  
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        cursor.execute("DELETE FROM `meds` WHERE `meds`.`ID` = '%s';"%(MID))
        db_connection.commit()
        if Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            PatientModelall= PatientModel.objects.all()
            newcustomerModelall = newcustomerModel.objects.all()
            return render(request, 'admin/dash.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModelall , "PatientModel":PatientModelall , "message":mess,'newcustomerModel':newcustomerModelall })



def allMedsdoc(request):   
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        type = request.POST.get('type')
        DoctorModel1 = DoctorModel.objects.filter(ID=ID)
        Painkillers = MedsModel.objects.filter(type='painkiller')
        Narco = MedsModel.objects.filter(type='narcoleptics')
        pastes = MedsModel.objects.filter(type='pastes')
        cold = MedsModel.objects.filter(type='anti-cold mecicine')
        allmed=MedsModel.objects.all()      
        if DoctorModel1:
            if type=='painkiller':
                return render(request, 'doctors/Medall.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':Painkillers})  
            if type=='narcoleptics':
                return render(request, 'doctors/Medall.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':Narco})
            if type=='pastes':
                return render(request, 'doctors/Medall.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':pastes})                
            if type=='anti-cold mecicine':
                return render(request, 'doctors/Medall.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':cold})
            if type=='all':
                return render(request, 'doctors/Medall.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':allmed})

  
#######################################################################################################################################
def medinfo(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('DID')
        MID = request.POST.get('MID')
        DoctorModel1 = DoctorModel.objects.filter(ID=ID)
        MedsModel1 = MedsModel.objects.filter(ID=MID)
        samemeds=MedsModel.objects.filter(ID=MID).first()
        samemedsreason=samemeds.reason
        MedsModelR = MedsModel.objects.filter(reason=samemedsreason)
        if DoctorModel1 and MedsModel1 :
            return render(request, 'doctors/medinfo.html', {"DoctorModel": DoctorModel1, "message":mess, 'meds':MedsModel1,'meds2':MedsModelR,"a_dictionary":a_dictionary})
def pharmacybutton(request):    
    allmed=MedsModel.objects.all()
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        PatientModeltest = PatientModel.objects.filter(ID=ID).first()
        if PatientModel1:
            meds = PatientModeltest.medrecom.split(",")
            dictOfWords1 = { i : 10 for i in meds } 
            return render(request, 'customers/pharmacy.html', {"PatientModel": PatientModel1, "message":mess, "med":allmed,"a_dictionary":a_dictionary,'medslist':dictOfWords1})        


def bloodtestpage(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        Bloodtest= bloodTestModel.objects.filter(CID=ID)
        if PatientModel1:
            return render(request, 'customers/bloodtestpage.html', {"PatientModel": PatientModel1, "message":mess,"Bloodtest":Bloodtest})

def fichinfo(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        Fichinfo = request.POST.get('FID')
        ID = request.POST.get('ID')   
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        PatientModel1 = PatientModel.objects.filter(ID=Fichinfo)
        DoctorModel1 = DoctorModel.objects.filter(ID=Fichinfo)
        if DoctorModel1:
          return render(request, 'admin/ficheinfodoc.html', {"AdminModel": Adminmodel1,"DoctorModel": DoctorModel1, "message":mess})  
        elif  PatientModel1:
            PatientModel2 = PatientModel.objects.filter(ID=Fichinfo).first()
            DID=PatientModel2.DID
            DoctorModel1 = DoctorModel.objects.filter(ID=DID)
            return render(request, 'admin/ficheinfopatient.html', {"AdminModel": Adminmodel1, "PatientModel":PatientModel1,"DoctorModel":DoctorModel1, "message":mess })

# Add Medical Record
def addmedicalrecord(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PID')
        DID = request.POST.get('DID')
        date = request.POST.get('date')
        Diagnonsis = request.POST.get('Diagnonsis')
        report = request.POST.get('message')
        lastreport = date+ " : " +report
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID).first()
        mes=PatientModel1.medicalrecord
        medrecord=Diagnonsis+", "+mes+" "
        PatientModel2 = PatientModel.objects.filter(ID=PID)
        cursor.execute("UPDATE `user` SET `medicalrecord` = '%s' WHERE `user`.`ID` = '%s';"%(medrecord,PID))
        cursor.execute("UPDATE `user` SET `latestreport` = '%s' WHERE `user`.`ID` = '%s';"%(lastreport,PID))
        alldoc=DoctorModel.objects.all()
        allmeds=MedsModel.objects.all()
        db_connection.commit()
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel2, "message":mess,"alldoc":alldoc,'allmeds':allmeds})  

def cleardrugprescription(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PID')
        DID = request.POST.get('DID')
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID).first()
        PatientModel2 = PatientModel.objects.filter(ID=PID)
        cursor.execute("UPDATE `user` SET `medrecom` = '%s' WHERE `user`.`ID` = '%s';"%('',PID))
        alldoc=DoctorModel.objects.all()
        allmeds=MedsModel.objects.all()
        db_connection.commit()
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel2, "message":mess,"alldoc":alldoc,'allmeds':allmeds})

def logout(request):
    return render(request, 'doctors/loginpage.html')


def addmedicalrecomandation(request):
    #doctor send drug recomandation
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PID')
        DID = request.POST.get('DID')
        messages = request.POST.get('message')
        print(PID,DID,messages)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID).first()
        mes=PatientModel1.medrecom
        addmeds=mes+','+messages
        PatientModel2 = PatientModel.objects.filter(ID=PID)
        cursor.execute("UPDATE `user` SET `medrecom` = '%s' WHERE `user`.`ID` = '%s';"%(addmeds,PID))
        alldoc=DoctorModel.objects.all()
        allmeds=MedsModel.objects.all()
        db_connection.commit()
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel2, "message":mess,"alldoc":alldoc,'allmeds':allmeds})  

def changepatientdoctor(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PID')
        DID = request.POST.get('DID')
        docpassid = request.POST.get('docpassid')
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel2 = PatientModel.objects.filter(ID=PID)
        app=''
        cursor.execute("UPDATE `user` SET `DID` = '%s' WHERE `user`.`ID` = '%s';"%(docpassid,PID))
        cursor.execute("UPDATE `user` SET `appointement` = '%s' WHERE `user`.`ID` = '%s';"%(app,PID))
        alldoc=DoctorModel.objects.all()
        db_connection.commit()
        allmeds=MedsModel.objects.all()
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel2, "message":mess,"alldoc":alldoc,'allmeds':allmeds})  

def adminanswer(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        AID = request.POST.get('AID')
        PID = request.POST.get('PID')
        message = request.POST.get('message')
        cursor.execute("UPDATE `user` SET `adminanswer` = '%s' WHERE `user`.`ID` = '%s';"%(message,PID))
        db_connection.commit()
        Adminmodel1 = Adminmodel.objects.filter(ID=AID)
        PatientModel1 = PatientModel.objects.filter(ID=PID)
        PatientModel2 = PatientModel.objects.filter(ID=PID).first()
        DID=PatientModel2.DID
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        return render(request, 'admin/ficheinfopatient.html', {"AdminModel": Adminmodel1, "PatientModel":PatientModel1,"DoctorModel":DoctorModel1, "message":mess })

def autorization(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        AID = request.POST.get('AID')
        PID = request.POST.get('PID')
        message = request.POST.get('autor')
        cursor.execute("UPDATE `user` SET `autorizations` = '%s' WHERE `user`.`ID` = '%s';"%(message,PID))
        db_connection.commit()
        Adminmodel1 = Adminmodel.objects.filter(ID=AID)
        PatientModel1 = PatientModel.objects.filter(ID=PID)
        PatientModel2 = PatientModel.objects.filter(ID=PID).first()
        DID=PatientModel2.DID
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        return render(request, 'admin/ficheinfopatient.html', {"AdminModel": Adminmodel1, "PatientModel":PatientModel1,"DoctorModel":DoctorModel1, "message":mess })

def admintodoc(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        AID = request.POST.get('ID')
        DID = request.POST.get('DID')
        message = request.POST.get('message')
        cursor.execute("UPDATE `doctor` SET `adminanswer` = '%s' WHERE `doctor`.`ID` = '%s';"%(message,DID))
        db_connection.commit()
        Adminmodel1 = Adminmodel.objects.filter(ID=AID)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        return render(request, 'admin/ficheinfodoc.html', {"AdminModel": Adminmodel1, "DoctorModel":DoctorModel1, "message":mess })

def addprivaterecord(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PID')
        DID = request.POST.get('DID')
        messages = request.POST.get('message')
        print(PID,DID,messages)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID).first()
        PatientModel2 = PatientModel.objects.filter(ID=PID)
        mess=PatientModel1.privaterecord
        add= messages+" "+mess
        cursor.execute("UPDATE `user` SET `privaterecord` = '%s' WHERE `user`.`ID` = '%s';"%(add,PID))
        alldoc=DoctorModel.objects.all()
        db_connection.commit()
        allmeds=MedsModel.objects.all()
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel2, "message":mess,"alldoc":alldoc,'allmeds':allmeds})  

def sentmessage(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        if PatientModel1:
            return render(request, 'customers/messagesent.html', {"PatientModel": PatientModel1, "message":mess})  

def patientpage(request):
    #personal patient page for doctor
    #patients model page
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PID')
        DID = request.POST.get('DIC')
        print(PID,DID)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID)
        alldoc=DoctorModel.objects.all()
        #display data of patients
        allmeds=MedsModel.objects.all()
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1, "message":mess,"alldoc":alldoc,'allmeds':allmeds})  

def patientsending(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        reason = request.POST.get('reason')
        message = request.POST.get('message')
        print(ID)
        TO = request.POST.get('TO')
        if TO=='My doctor':
            messagetodoc= 'Reason: ' + reason + ' | Message: '+ message
            cursor.execute("UPDATE `user` SET `messagesent` = '%s' WHERE `user`.`ID` = '%s';"%(messagetodoc,ID))
            db_connection.commit()
        elif TO=='The Manager':
            messagetoadmin='Reason: '+reason+' | Message: '+message
            cursor.execute("UPDATE `user` SET `adminmess` = '%s' WHERE `user`.`ID` = '%s';"%(messagetoadmin,ID))
            db_connection.commit()
        print(reason,message)
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        if PatientModel1:
            return render(request, 'customers/messagesent.html', {"PatientModel": PatientModel1, "message":mess}) 


def doctoranswer(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        PID = request.POST.get('PAT')
        DID = request.POST.get('DID')
        reason = request.POST.get('reason')
        message = request.POST.get('message')
        messagefromdoc= 'Reason: '+reason+ ' | ' + ' Message: '+message
        cursor.execute("UPDATE `user` SET `doctoranswer` = '%s' WHERE `user`.`ID` = '%s';"%(messagefromdoc,PID))
        db_connection.commit()
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        PatientModel1 = PatientModel.objects.filter(ID=PID)
        alldoc=DoctorModel.objects.all()
        allmeds=MedsModel.objects.all()
        if DoctorModel1:
            return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1, "message":mess,"alldoc":alldoc,'allmeds':allmeds})  

def genmessage(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        message = request.POST.get('message')
        Adminmodel1 = Adminmodel.objects.filter(ID=ID) 
        mesID='1'
        cursor.execute("UPDATE `generalmessage` SET `message` = '%s' WHERE `generalmessage`.`ID` = '%s';"%(message,mesID))
        db_connection.commit()
        if Adminmodel1:
            DoctorModelall= DoctorModel.objects.all()
            PatientModelall= PatientModel.objects.all()
            newcustomerModelall = newcustomerModel.objects.all()
            return render(request, 'admin/dash.html', {"newcustomerModel":newcustomerModelall,"AdminModel": Adminmodel1,"DoctorModel": DoctorModelall , "PatientModel":PatientModelall , "message":mess }) 

def adminsentmess(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        doctor=DoctorModel.objects.filter(ID=ID).first()
        doctorname=doctor.lastname
        reason = request.POST.get('reason')
        message = request.POST.get('message')
        doctorid = request.POST.get('doctorid')
        print(doctorid)
        TO = request.POST.get('TO')
        if TO=='doctor':
           messagetodoc="DR "+doctorname+' Reason: '+reason+ ' | Message: '+message
           cursor.execute("UPDATE `doctor` SET `doctormessages` = '%s' WHERE `doctor`.`ID` = '%s';"%(messagetodoc,doctorid))
           cursor.execute("UPDATE `doctor` SET `doctorsanswer` = '%s' WHERE `doctor`.`ID` = '%s';"%(messagetodoc,ID))
           db_connection.commit()
        if TO=='The Manager':
            messagetoman='Reason:'+reason+' | Message:'+message
            cursor.execute("UPDATE `doctor` SET `adminmess` = '%s' WHERE `doctor`.`ID` = '%s';"%(messagetoman,ID))
            db_connection.commit()
        print(reason,message)
        DoctorModel1 = DoctorModel.objects.filter(ID=ID)
        PatientModel1 = PatientModel.objects.filter(DID=ID)
        print(PatientModel1)
        if DoctorModel1:
            return render(request, 'doctors/dash.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1, "message":mess})  

def updatecart(request):
   mess=MessageModel.objects.filter(ID=1)
   if request.method == 'POST':
        ID = request.POST.get('CID')
        cursor.execute("DELETE FROM `customercart` WHERE `customercart`.`CID` = '%s';"%(ID))
        db_connection.commit()
        PatientModel1 = PatientModel.objects.filter(ID=ID)
        PatientModeltest = PatientModel.objects.filter(ID=ID).first()
        DID=PatientModeltest.DID
        DoctorModel3 = DoctorModel.objects.filter(ID=DID).first()
        print(DoctorModel3)
        workday2=DoctorModel3.workdays
        print(workday2)
        x = workday2.split(",")
        workday = { i : 10 for i in x }
        meds = PatientModeltest.medrecom.split(",")
        dictOfWords1 = { i : 10 for i in meds }
        hours=['10:00','10:30','11:00','11:30','12:00','12:30','13:00']
        dichours = { i : 10 for i in hours }
        print(workday) 
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        AdminModel1 = Adminmodel.objects.filter(ID=222333444)
        if PatientModel1:
            return render(request, 'customers/dash.html', {"DoctorModel": DoctorModel1,"AdminModel": AdminModel1,"PatientModel": PatientModel1, "message":mess,'dictOfWords':workday,'medslist':dictOfWords1,"dichours":dichours})  

def checkout(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        CID = request.POST.get('CID')
        cursor.execute("DELETE FROM `customercart` WHERE `customercart`.`CID` = '%s';"%(CID))
        db_connection.commit()
        PatientModel1 = PatientModel.objects.filter(ID=CID)
        if PatientModel1:
            return render(request, 'customers/checkout.html',{"PatientModel":PatientModel1})
#############################################################################################################################################################################


def addcart(request):
    allmed=MedsModel.objects.all()
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        CID = request.POST.get('CID') 
        MID = request.POST.get('MID')
        NAME = request.POST.get('NAME')
        CommandeenCour = cartModel.objects.filter(CID=CID)
        PatientModel1 = PatientModel.objects.filter(ID=CID)
        PatientModeltest = PatientModel.objects.filter(ID=CID).first()
        pname=PatientModeltest.firstname
        CommandeenCour1 = cartModel.objects.filter(CID=CID).first()
        Medic = MedsModel.objects.filter(ID=MID).first()
        if Medic.type=='narcoleptics':
            if PatientModeltest.autorizations=='no':
                    face_cascade = cv2.CascadeClassifier('C:\\Users\\kevyn\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml')
                    recognizer = cv2.face.LBPHFaceRecognizer_create() 
                    recognizer.read('C:/Users/kevyn/Documents/GitHub/PM2022_TEAM_16/projectapp/trainner.yml')
                    labels = {}
                    with open("C:/Users/kevyn/Documents/GitHub/PM2022_TEAM_16/projectapp/labels.pickle", "rb") as f :
                        og_labels = pickle.load(f)
                        labels = {v:k for k,v in og_labels.items()}
                    cap = cv2.VideoCapture(0)

                    while True:
                        ret,frame= cap.read()
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
                        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5,minNeighbors=5)     
                        for(x,y,w,h) in faces:
                            #print(x,y,w,h)
                            roi_gray= gray[y:y+h ,x:x+w]
                            roi_color = frame[y:y+h ,x:x+w]
                            id_,conf = recognizer.predict(roi_gray)
                            if conf >= 60 :
                                #print(id_)
                                #print(labels[id_])
                                font = cv2.FONT_HERSHEY_SIMPLEX
                                name = labels[id_]
                                color = (255,255,255)
                                stroke= 2
                                print(name)
                            cv2.putText(frame,name,(x+1,y+1),font,2,color, stroke, cv2.LINE_AA)
                            # use recognize
                            color = (250,0,0)
                            stroke=5
                            end_cord_x = x+w
                            end_cord_y = y + h 
                            cv2.rectangle(frame, (x,y),(end_cord_x,end_cord_y), color,stroke) #dessign le rectagle          
                            if pname==name or cv2.waitKey(20) & 0xFF == ord('q'):
                                prixmed=Medic.price
                                if CommandeenCour:          
                                    listmedoc=CommandeenCour1.MIDS+','+MID
                                    prixajouter=CommandeenCour1.totalprice+prixmed
                                    names=CommandeenCour1.name+','+NAME
                                    cursor.execute("UPDATE `customercart` SET `totalprice` = '%s' WHERE `customercart`.`CID` = '%s';"%(prixajouter,CID))
                                    db_connection.commit()
                                    cursor.execute("UPDATE `customercart` SET `MIDS` = '%s' WHERE `customercart`.`CID` = '%s';"%(listmedoc,CID))
                                    db_connection.commit()
                                    cursor.execute("UPDATE `customercart` SET `name` = '%s' WHERE `customercart`.`CID` = '%s';"%(names,CID))
                                    db_connection.commit()
                                    x = names.split(",")
                                    dictOfWords = { i : 10 for i in x }
                                    meds = PatientModeltest.medrecom.split(",")
                                    dictOfWords1 = { i : 10 for i in meds }
                                    print(dictOfWords1)                    
                                    cap.release()
                                    cv2.destroyAllWindows()
                                    messages.success(request,"Facial Recongnizer accepted !Product Add")   
                                    return render(request, 'customers/pharmacy.html', {"PatientModel": PatientModel1, "message":mess, "med":allmed,"a_dictionary":a_dictionary,"CommandeenCour":dictOfWords,"medslist":dictOfWords1})
                                else:
                                    saveobject=cartModel()
                                    print(NAME)
                                    saveobject.CID=CID
                                    saveobject.MIDS=MID
                                    saveobject.totalprice=prixmed
                                    saveobject.name=NAME
                                    saveobject.save()
                                    CommandeenCour2 = cartModel.objects.filter(CID=CID)
                                                        
                                    cap.release()
                                    cv2.destroyAllWindows()
                                    return render(request, 'customers/pharmacy.html', {"PatientModel": PatientModel1, "message":mess, "med":allmed,"a_dictionary":a_dictionary,"CommandeenCour":CommandeenCour2})
        prixmed=Medic.price
        if CommandeenCour:          
          listmedoc=CommandeenCour1.MIDS+','+MID
          prixajouter=CommandeenCour1.totalprice+prixmed
          names=CommandeenCour1.name+','+NAME
          cursor.execute("UPDATE `customercart` SET `totalprice` = '%s' WHERE `customercart`.`CID` = '%s';"%(prixajouter,CID))
          db_connection.commit()
          cursor.execute("UPDATE `customercart` SET `MIDS` = '%s' WHERE `customercart`.`CID` = '%s';"%(listmedoc,CID))
          db_connection.commit()
          cursor.execute("UPDATE `customercart` SET `name` = '%s' WHERE `customercart`.`CID` = '%s';"%(names,CID))
          db_connection.commit()
          x = names.split(",")
          dictOfWords = { i : 10 for i in x }
          meds = PatientModeltest.medrecom.split(",")
          dictOfWords1 = { i : 10 for i in meds }
          print(dictOfWords1)
          return render(request, 'customers/pharmacy.html', {"PatientModel": PatientModel1, "message":mess, "med":allmed,"a_dictionary":a_dictionary,"CommandeenCour":dictOfWords,"medslist":dictOfWords1})
        else:
            saveobject=cartModel()
            print(NAME)
            saveobject.CID=CID
            saveobject.MIDS=MID
            saveobject.totalprice=prixmed
            saveobject.name=NAME
            saveobject.save()
            CommandeenCour2 = cartModel.objects.filter(CID=CID)
            return render(request, 'customers/pharmacy.html', {"PatientModel": PatientModel1, "message":mess, "med":allmed,"a_dictionary":a_dictionary,"CommandeenCour":CommandeenCour2})

def admintodocworkday(request):
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        DID = request.POST.get('DID')
        print(DID)
        ID = request.POST.get('ID')
        print(ID)
        workdays = request.POST.get('days')
        print(workdays)
        cursor.execute("UPDATE `doctor` SET `workday` = '%s' WHERE `doctor`.`ID` = '%s';"%(workdays,DID))
        db_connection.commit()
        Adminmodel1 = Adminmodel.objects.filter(ID=ID)
        print(Adminmodel1)
        DoctorModel1 = DoctorModel.objects.filter(ID=DID)
        return render(request, 'admin/ficheinfodoc.html', {"AdminModel": Adminmodel1, "DoctorModel":DoctorModel1, "message":mess })

def pay(request):
    mess=MessageModel.objects.filter(ID=1)
    allmed=MedsModel.objects.all()
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        CID = request.POST.get('CID') 
        CommandeenCour = cartModel.objects.filter(CID=CID)
        CommandeenCour1 = cartModel.objects.filter(CID=CID).first()
        x = CommandeenCour1.name.split(",")
        res = {i:x.count(i) for i in x}
        dictOfWords = { i : 10 for i in x }
        total=CommandeenCour1.totalprice
        dic = {total:1}
        PatientModel1 = PatientModel.objects.filter(ID=CID)
        print(res)
        return render(request, 'customers/resumercomande.html', {"PatientModel": PatientModel1, "message":mess, "med":allmed,"CommandeenCour":CommandeenCour,'res':res,'dic':dic})

def newbloodtest(request):
    if request.method == 'POST':
            mess=MessageModel.objects.filter(ID=1)
            creat = random.uniform(0, 1)
            hdl = random.randint(0, 40)
            hb = random.randint(0, 50)
            iron = random.randint(0, 100)
            urea = random.randint(0,50)
            alk_phos = random.randint(0,100)
            ID = request.POST.get('CID')
            DID = request.POST.get('DID')
            PatientModel1 = PatientModel.objects.filter(ID=ID)
            cursor.execute("UPDATE `bloodTest` SET `alk_phos` = '%s' WHERE `bloodTest`.`CID` = '%s';"%(alk_phos,ID))
            db_connection.commit()
            cursor.execute("UPDATE `bloodTest` SET `hdl` = '%s' WHERE `bloodTest`.`CID` = '%s';"%(hdl,ID))
            db_connection.commit()
            cursor.execute("UPDATE `bloodTest` SET `iron` = '%s' WHERE `bloodTest`.`CID` = '%s';"%(iron,ID))
            db_connection.commit()
            cursor.execute("UPDATE `bloodTest` SET `creat` = '%s' WHERE `bloodTest`.`CID` = '%s';"%(creat,ID))
            db_connection.commit()
            cursor.execute("UPDATE `bloodTest` SET `hb` = '%s' WHERE `bloodTest`.`CID` = '%s';"%(hb,ID))
            db_connection.commit()
            cursor.execute("UPDATE `bloodTest` SET `urea` = '%s' WHERE `bloodTest`.`CID` = '%s';"%(urea,ID))
            db_connection.commit()
            DoctorModel1 = DoctorModel.objects.filter(ID=DID)
            alldoc=DoctorModel.objects.all()
            #display data of patients
            allmeds=MedsModel.objects.all()
            print(ID)
            if DoctorModel1:
                return render(request, 'doctors/patientinfo.html', {"DoctorModel": DoctorModel1,"PatientModel": PatientModel1, "message":mess,"alldoc":alldoc,'allmeds':allmeds})  
            

def bloodtest(id):
    tests = []
    creat = random.uniform(0, 1)
    hdl = random.randint(0, 40)
    hb = random.randint(0, 50)
    iron = random.randint(0, 100)
    urea = random.randint(0,50)
    alk_phos = random.randint(0,100)
    saveobj=bloodTestModel()
    saveobj.CID=id
    saveobj.creat=creat
    saveobj.hdl=hdl
    saveobj.hb=hb
    saveobj.iron=iron
    saveobj.urea=urea 
    saveobj.alk_phos=alk_phos
    saveobj.save()


def payement(request):
    allmed=MedsModel.objects.all()
    mess=MessageModel.objects.filter(ID=1)
    if request.method == 'POST':
        CID = request.POST.get('CID') 
        print(CID)
        CommandeenCour1 = cartModel.objects.filter(CID=CID)
        return render(request, 'customers/pay.html',{"CommandeenCour":CommandeenCour1})
 ###########################################################################################################################################################################           



