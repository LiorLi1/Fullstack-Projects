from random import random
from tkinter import Frame
from cv2 import COLOR_BGR2GRAY, destroyAllWindows
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from projectapp.models import *
import mysql.connector
from django.http import JsonResponse
import random
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import numpy as np
import cv2
import pickle

import requests
import json
def test(a_dictionary):
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