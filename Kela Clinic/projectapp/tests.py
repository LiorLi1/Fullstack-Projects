from lib2to3.pgen2.token import EQEQUAL
from unicodedata import name
from django.test import TestCase
from django.urls import resolve, reverse
from numpy import record
from requests import request
from projectapp.views import *
from projectapp.models import *
import unittest

from django.test import Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from django.contrib.auth.models import User
from chromedriver_py import binary_path
from django.test import Client,LiveServerTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random




class TestUrls(unittest.TestCase):

    def test_list_url_is_resolved(self):
        list_url = [
            "userlogin","userdash","sentmessage",
            "patientsending","workersdash","login","patientpage","addmedicalrecord",
            "fichinfo","userhome","doctoranswer","doctorinfo","adminsentmess",
            "medinfo","addcart","genmessage","pharmacy","allMedsdoc","pay",
            "payement","checkout","addmedicalrecomandation","doctordash","addpatpage",
            "newcust","rdv","addprivaterecord","adminanswer","admintodoc",
            "adminpharmacy","adminmedinfo","medchange","addmeds","addmed", "logout", "autorization", "admintodocworkday",
            "changepatientdoctor","addpatient","bloodtestpage","deletedoc",
            ]
        for u in list_url:
            url=reverse(u)
            print(resolve(url))

    # def test_list_url_is_resolved(self):
    #     url=reverse('index')
    #     print(resolve(url))
    
    # def test_list_url_is_resolved_pharmacy(self):
    #     url=reverse('pharmacy')
    #     print(resolve(url))

    # def test_list_url_is_resolved_pharmacy(self):
    #     url=reverse('addmed')
    #     print(resolve(url))

    # def test_list_url_is_resolved_pharmacy(self):
    #     url=reverse('addmedicalrecord')
    #     print(resolve(url))

    # def test_list_url_is_resolved_pharmacy_warnings(self):
    #     url=reverse('pharmacy')
    #     print(resolve(url))

    # def test_list_url_is_resolved_pharmacy_warnings(self):
    #     url=reverse('pharmacy')
    #     print(resolve(url))

    # def test_list_url_is_resolved_medinfo(self):
    #     url=reverse('medinfo')
    #     print(resolve(url))

    # def test_list_url_is_resolved_allMedsdoc(self):
    #     url=reverse('allMedsdoc')
    #     print(resolve(url))



class test_exist_med(unittest.TestCase):

    def test_exist(self):
        db_connection = mysql.connector.connect(
        host="database-1.cx6ixgbmnqky.eu-central-1.rds.amazonaws.com",
        user="Admin",
        password="Aa123456",
        database="projectapp")
        cursor = db_connection.cursor()
        cursor.execute("SELECT name FROM meds")
        result = cursor.fetchall()
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
                "ciprofloxacin",
                ]   
        for x in range(len(medsnames)):
            self.assertEqual(medsnames[x],result[x][0])
        cursor.close()





class test_admin(TestCase):
    def test_admin1(self):
        item=Adminmodel()
        item.ID='315199059'
        item.firstname='Lior'
        item.lastname='Liberov'
        item.password='1a2b3c4d5e'
        item.messagesent='hello world'
        item.save()
        record=Adminmodel.objects.get()
        self.assertEqual(record,item)
    
    def test_admin2(self):
        item=Adminmodel()
        item.ID='324561087'
        item.firstname='Jack'
        item.lastname='Maori'
        item.password='8888855555'
        item.messagesent='hello world'
        item.save()
        record=Adminmodel.objects.get()
        self.assertEqual(record,item)

    def test_admin3(self):
        item=Adminmodel()
        item.ID='324561056'
        item.firstname='Matan'
        item.lastname='Tariff'
        item.password='8888844444'
        item.messagesent='hello world'
        item.save()
        record=Adminmodel.objects.get()
        self.assertEqual(record,item)

class doctor_test(TestCase):
    def test_doctor1(self):
        item=DoctorModel()
        item.ID='324461056'
        item.firstname='Alex'
        item.lastname='Yohananoff'
        item.password='1234567890'
        item.workdays='Monday'
        item.adminmess='hello world'
        item.adminanswer='hello you too'
        item.speciality='cancer'
        item.doctormessages='hello'
        item.doctorsanswer='bye'
        item.save()
        record=DoctorModel.objects.get()
        self.assertEqual(record,item)
    
    def test_doctor2(self):
        item=DoctorModel()
        item.ID='324561056'
        item.firstname='John'
        item.lastname='Elbaz'
        item.password='1234567790'
        item.workdays='Monday'
        item.adminmess='hello world'
        item.adminanswer='hello you too'
        item.speciality='cancer'
        item.doctormessages='hello'
        item.doctorsanswer='bye'
        item.save()
        record=DoctorModel.objects.get()
        self.assertEqual(record,item)

    def test_doctor3(self):
        item=DoctorModel()
        item.ID='324661056'
        item.firstname='Mark'
        item.lastname='Efraim'
        item.password='1234467890'
        item.workdays='Monday'
        item.adminmess='hello world'
        item.adminanswer='hello you too'
        item.speciality='cancer'
        item.doctormessages='hello'
        item.doctorsanswer='bye'
        item.save()
        record=DoctorModel.objects.get()
        self.assertEqual(record,item)

class patient_test(TestCase):
    def test_patient1(self):
        item=PatientModel()
        item.ID='324561156'
        item.firstname='Matan'
        item.lastname='Gershon'
        item.password='1234567890'
        item.messagesent='hello world'
        item.doctoranswer='hello you too'
        item.DID='324561157'
        item.medicalrecord='very sick'
        item.privaterecord='bee allergie'
        item.adminmess='hello world'
        item.adminanswer='hello you too'
        item.age=23
        item.poids=25
        item.taille=30
        item.allergies='bee'
        item.BMI=65
        item.phone='0521234567'
        item.medrecom='get away of bees'
        item.appointement='tuesday'
        item.autorizations='no'
        item.latestreport='is stupid'
        item.save()
        record=PatientModel.objects.get()
        self.assertEqual(record,item)

    def test_patient2(self):
        item=PatientModel()
        item.ID='324561256'
        item.firstname='Matan'
        item.lastname='Sasi'
        item.password='1234567890'
        item.messagesent='hello world'
        item.doctoranswer='hello you too'
        item.DID='324561257'
        item.medicalrecord='very ill'
        item.privaterecord='bee allergie'
        item.adminmess='hello world'
        item.adminanswer='hello you too'
        item.age=23
        item.poids=25
        item.taille=30
        item.allergies='bee'
        item.BMI=65
        item.phone='0521234567'
        item.medrecom='get away of bees'
        item.appointement='tuesday'
        item.autorizations='no'
        item.latestreport='is stupid'
        item.save()
        record=PatientModel.objects.get()
        self.assertEqual(record,item)

    def test_patient3(self):
        item=PatientModel()
        item.ID='324561356'
        item.firstname='Matan'
        item.lastname='Suisa'
        item.password='1234567890'
        item.messagesent='hello world'
        item.doctoranswer='hello you too'
        item.DID='324561357'
        item.medicalrecord='has cancer'
        item.privaterecord='bee allergie'
        item.adminmess='hello world'
        item.adminanswer='hello you too'
        item.age=23
        item.poids=25
        item.taille=30
        item.allergies='bee'
        item.BMI=65
        item.phone='0521234567'
        item.medrecom='get away of bees'
        item.appointement='tuesday'
        item.autorizations='no'
        item.latestreport='is stupid'
        item.save()
        record=PatientModel.objects.get()
        self.assertEqual(record,item)

class message_test(TestCase):
    def test_message1(self):
        item=MessageModel()
        item.ID='322451738'
        item.message='hello world'
        item.save()
        record=MessageModel.objects.get()
        self.assertEqual(record,item)

    def test_message2(self):
        item=MessageModel()
        item.ID='322451748'
        item.message='hello israel'
        item.save()
        record=MessageModel.objects.get()
        self.assertEqual(record,item)

    def test_message3(self):
        item=MessageModel()
        item.ID='322451758'
        item.message='hello taiwan'
        item.save()
        record=MessageModel.objects.get()
        self.assertEqual(record,item)

class meds_test(TestCase):
    def test_meds1(self):
        item=MedsModel()
        item.ID=123456789
        item.name='concerta'
        item.description='focus drug'
        item.price='120'
        item.reason='no focus'
        item.type='narcoliptic'
        item.estock=25
        item.pstock=20
        item.save()
        record=MedsModel.objects.get()
        self.assertEqual(record,item)
    
    def test_meds2(self):
        item=MedsModel()
        item.ID=123456880
        item.name='ritalin'
        item.description='focus drug'
        item.price='200'
        item.reason='no focus'
        item.type='narcoliptic'
        item.estock=35
        item.pstock=30
        item.save()
        record=MedsModel.objects.get()
        self.assertEqual(record,item)

    def test_meds3(self):
        item=MedsModel()
        item.ID=123456881
        item.name='acamol'
        item.description='anti cold'
        item.price='60'
        item.reason='has cold'
        item.type='anti cold'
        item.estock=200
        item.pstock=205
        item.save()
        record=MedsModel.objects.get()
        self.assertEqual(record,item)

class cart_test(TestCase):
    def test_cart1(self):
        item=cartModel()
        item.CID='324561156'
        item.MIDS='123456789'
        item.totalprice=205
        item.name='Matan'
        item.save()
        record=cartModel.objects.get()
        self.assertEqual(record,item)
    
    def test_cart2(self):
        item=cartModel()
        item.CID='324561256'
        item.MIDS='123456880'
        item.totalprice=210
        item.name='Matan'
        item.save()
        record=cartModel.objects.get()
        self.assertEqual(record,item)
    
    def test_cart3(self):
        item=cartModel()
        item.CID='324561356'
        item.MIDS='123456881'
        item.totalprice=213
        item.name='Matan'
        item.save()
        record=cartModel.objects.get()
        self.assertEqual(record,item)

class newcust_test(TestCase):
    def test_newcust1(self):
        item=newcustomerModel()
        item.firstname='Matan'
        item.lastname='Suisa'
        item.email='matan.sui1@gmail.com'
        item.phone='0521234567'
        item.save()
        record=newcustomerModel.objects.get()
        self.assertEqual(record,item)

    def test_newcust2(self):
        item=newcustomerModel()
        item.firstname='Matan'
        item.lastname='Shlomo'
        item.email='matan.shl1@gmail.com'
        item.phone='0521234467'
        item.save()
        record=newcustomerModel.objects.get()
        self.assertEqual(record,item)

    def test_newcust3(self):
        item=newcustomerModel()
        item.firstname='Matan'
        item.lastname='Gershon'
        item.email='matan.gersh1@gmail.com'
        item.phone='0521334567'
        item.save()
        record=newcustomerModel.objects.get()
        self.assertEqual(record,item)

class bloodtest_test(TestCase):
    def test_bloodtest1(self):
        item=bloodTestModel()
        item.CID='111222333'
        item.alk_phos=59
        item.hdl=38
        item.iron=43
        item.creat=0.8
        item.hb=38
        item.urea=37
        item.save()
        record=bloodTestModel.objects.get()
        self.assertEqual(record,item)

    def test_bloodtest2(self):
        item=bloodTestModel()
        item.CID='555666777'
        item.alk_phos=58
        item.hdl=37
        item.iron=42
        item.creat=0.7
        item.hb=37
        item.urea=36
        item.save()
        record=bloodTestModel.objects.get()
        self.assertEqual(record,item)

    def test_bloodtest3(self):
        item=bloodTestModel()
        item.CID='666777888'
        item.alk_phos=57
        item.hdl=36
        item.iron=41
        item.creat=0.6
        item.hb=35
        item.urea=35
        item.save()
        record=bloodTestModel.objects.get()
        self.assertEqual(record,item)
        


"""
class SeleniumTestCase(StaticLiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        #service = Service(f"{settings.BASE_DIR}/chromedriver")
        service = Service(binary_path)
        cls.driver = webdriver.Chrome(executable_path='projectapp/chromedriver.exe', options=options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

class AuthenticationFormTest(SeleniumTestCase):
    def test_authentication_form(self):
        # Create a user to login with
        user = User.objects.create_user(
            username="test@user.com", password="12345"
        )

        # Go to the login page
        self.driver.get("http://localhost:8000/projectapp/userlogin")
       
        # Find HTML elements
        username_input = self.driver.find_element_by_name("ID")
        password_input = self.driver.find_element_by_name("password")
        # login_button = self.driver.find_elements_by_name("but_sub")
        
        username_input.send_keys("332531235")
        password_input.send_keys("Aa123456")
        button_i = self.driver.find_element_by_xpath("//button[@id='but_sub']")
        self.driver.execute_script('arguments[0].click()', button_i)
      

        # Wait for request
        time.sleep(0.5)

        # Check that the user is logged in
        self.assertEqual(self.driver.current_url, "http://localhost:8000/projectapp/userdash")







class AuthenticationFormTest2(SeleniumTestCase):
    def test_authentication_form(self):
        # Create a user to login with
        user = User.objects.create_user(
            username="222333444", password="Aa123456"
        )
       
        
        self.driver.get("http://localhost:8000/projectapp/login")
        username_input = self.driver.find_element_by_id("Id")
        password_input = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_id("but_sub")

        # Type in an email that doesn't exist
        username_input.send_keys("222333444")

        # Type in a password
        password_input.send_keys("Aa123456")
        login_button.click()
      

        more_button = self.driver.find_element_by_xpath("//button[@id='but_more']")
        self.driver.execute_script('arguments[0].click()', more_button)
       
        txtaera_message = self.driver.find_element_by_id("floatingTextarea")
        test_list = ["welocme","test","intergtion test","POPintergtion","doctor testing"]
        txt_message = "intergtion test {0}".format(str(random.randint(1, 999999999)))

        txtaera_message.send_keys(txt_message)
        time.sleep(1)

        new_message = self.driver.find_element_by_xpath("//button[@id='btAns']")
        self.driver.execute_script('arguments[0].click()', new_message)
        elem_newMess = self.driver.find_element_by_id("newMessage").text
        self.assertEqual(elem_newMess,txt_message)

##############################################################################################
class AuthenticationFormTest3(SeleniumTestCase):
    def test_authentication_form(self):
        # Create a user to login with
        user = User.objects.create_user(
            username="test@user.com", password="12345"
        )

        # Go to the login page
        self.driver.get("http://localhost:8000/projectapp/userlogin")
       
        # Find HTML elements
        username_input = self.driver.find_element_by_name("ID")
        password_input = self.driver.find_element_by_name("password")
        username_input.send_keys("332531235")
        password_input.send_keys("Aa123456")

        script_format = 'arguments[0].click()'
        but_i = self.driver.find_element_by_xpath("//button[@id='but_sub']")
        self.driver.execute_script(script_format, but_i)
        but_to_phar=self.driver.find_element_by_xpath("//button[@id='button']")
        self.driver.execute_script(script_format, but_to_phar)
        time.sleep(1)

        list_select_med = ["Selenium","Etodolac","Selenium","Tazorac","Selenium"]
        for med in list_select_med:
              but_to_phar=self.driver.find_element_by_xpath("//button[@id='{0}']".format(med))
              self.driver.execute_script(script_format, but_to_phar)

        WebDriverWait(self.driver,12).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='drop']"))).click()
        self.driver.execute_script(script_format,  self.driver.find_element_by_xpath("//button[@id='sal']"))

        txt_count_med1 = self.driver.find_element_by_xpath("//td[@id='{0}']".format(list_select_med[0])).text
        txt_count_med2 = self.driver.find_element_by_xpath("//td[@id='{0}']".format(list_select_med[1])).text
        txt_count_med3 = self.driver.find_element_by_xpath("//td[@id='{0}']".format(list_select_med[3])).text
        total_count = int(txt_count_med1) + int(txt_count_med2) + int(txt_count_med3)
        self.assertEqual(len(list_select_med), total_count)
        
        



class AuthenticationFormTest4(SeleniumTestCase):
    def test_authentication_form(self):

        user = User.objects.create_user(
            username="222333444", password="Aa123456"
        )
       
        
        self.driver.get("http://localhost:8000/projectapp/login")
        username_input = self.driver.find_element_by_id("Id")
        password_input = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_id("but_sub")
        username_input.send_keys("222333444")
        password_input.send_keys("Aa123456")
        login_button.click()
        time.sleep(1)
        self.assertEqual(self.driver.current_url, "http://localhost:8000/projectapp/workersdash")
        ##---------------------need to add code down
        # WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='drop']"))).click()
        # self.driver.execute_script('arguments[0].click()',  self.driver.find_element_by_xpath("//button[@id='sal']"))    
        # self.assertEqual(self.driver.current_url, "http://localhost:8000/projectapp/login")
        #time.sleep(0.5)
"""
##############################################################################################




class integration_Admin_Test(LiveServerTestCase):

    def setUp(self):
        self.client = Client()


    def test_login(self):
        # Get login page
        response = self.client.get("http://127.0.0.1:8000/projectapp/login")
      
        # Check response code
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        #self.assertTrue('LOGIN' response.content)

        # Log the user in
        self.client.login(ID='222333444', password="Aa123456")

    #     # Check response code
        response = self.client.get('http://127.0.0.1:8000/projectapp/workersdash')
        self.assertEquals(response.status_code, 200)
        self.client.logout()
        # Check response code
        response = self.client.get('http://127.0.0.1:8000/projectapp/workersdash')
        self.assertTrue(response.status_code, 404)

    #     # Check 'Log out' in response
    #     self.assertTrue('Log out' in response.content)

class integration_patient_Test(LiveServerTestCase):

    def setUp(self):
        self.client = Client()


    def test_login(self):
        #Get login page
        response = self.client.get("http://127.0.0.1:8000/projectapp/userlogin")
      
        #Check response code
        self.assertEquals(response.status_code, 200)

        
        #Log the user in
        self.client.login(ID='332531235', password="Aa123456")

        #Check response code
        response = self.client.post('http://127.0.0.1:8000/projectapp/userdash',data={'ID':'332531235','password':'Aa123456'})
        self.assertEquals(response.status_code, 200)
        self.client.logout()
        #Check response code
        response = self.client.post('http://127.0.0.1:8000/projectapp/userdash',data={'ID':'332531234','password':'Aa123455'})
        self.assertTrue(response,self.client.post("http://127.0.0.1:8000/projectapp/userlogin"))

   
class integration_doctor_Test(LiveServerTestCase):

    def setUp(self):
        self.client = Client()


    def test_login(self):
        #Get login page
        response = self.client.get("http://127.0.0.1:8000/projectapp/login")
      
        #Check response code
        self.assertEquals(response.status_code, 200)

        
        #Log the user in
        self.client.login(ID='111222333', password="Aa123456")

        #Check response code
        response = self.client.post('http://127.0.0.1:8000/projectapp/workersdash',data={'ID':'111222333','password':'Aa123456'})
        self.assertEquals(response.status_code, 200)
        self.client.logout()
        #Check response code
        response = self.client.post('http://127.0.0.1:8000/projectapp/workersdash',data={'ID':'111222334','password':'Aa123455'})
        self.assertTrue(response,self.client.post("http://127.0.0.1:8000/projectapp/login"))
    
# class doctorinfo_test(LiveServerTestCase):
#     def setUp(self):
#         self.client=Client()

#     def test_doctorinfo(self):
#         Get login page
#         response = self.client.get("http://127.0.0.1:8000/projectapp/login")
      
#         Check response code
#         self.assertEquals(response.status_code, 200)

        
#         Log the user in
#         self.client.login(ID='222333444', password="Aa123456")

#         Check response code
#         response = self.client.post('http://127.0.0.1:8000/projectapp/workersdash',data={'ID':'222333444','password':'Aa123456'})
#         self.assertEquals(response.status_code, 200)
        
#         response=self.client.post('http://127.0.0.1:8000/projectapp/doctorinfo',data={'ID':'222333444'})
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'customers/bloodtestpage.html')        
    



    


