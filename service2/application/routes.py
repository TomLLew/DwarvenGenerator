from flask import render_template, request, redirect, url_for
from application import service2
import random, requests

female = ["Brewmistress", "Denirim ('priest')", "Earth-Guide", "Farmtender", "Foodmaker",
          "Healer", "Hunter", "Mage", "Teacher", "Weavewender"]

male = ["Denerim ('priest')", "Earth-Guide", "Healer", "Leader", "Mage",
        "Miner", "Sender", "Smith", "Woodsmith", "Hunter"]

clan = ["Longbeards", "Firebeards", "Ironfists", "Stonefoots"]

job = {"clan":"none", "job":"none", "sex":"none"}

@service2.route('/', methods=['GET', 'POST'])
def random_name():
    if request.method == 'POST':
        data = request.form.get('sex')
        if data == "Female":
            job["sex"] = data 
            job["job"] = female[random.randint(0, 9)]
            job["clan"] = clan[random.randint(0 , 3)]
            return job
        elif data == "Male":
            job["sex"] = data 
            job["job"] = male[random.randint(0, 9)]
            job["clan"] = clan[random.randint(0 , 3)]
            return job


       