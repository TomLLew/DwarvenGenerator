from flask import render_template, request, redirect, url_for
from application import service2
import random, requests

female = ["Brewmistress", "Denirim ('priest')", "Earth-Guide", "Farmtender", "Foodmaker",
          "Healer", "Hunter", "Mage", "Teacher", "Weavewender"]

male = ["Denerim ('priest')", "Earth-Guide", "Healer", "Leader", "Mage",
        "Miner", "Sender", "Smith", "Woodsmith", "Hunter"]

clan = ["Longbeards", "Firebeards", "Ironfists", "Stonefoots"]

job = {"clan":"none", "job":"none"}

@service2.route('/job', methods=['GET', 'POST'])
def random_job():
    if request.method == 'POST':
        data = request.args.get("gender")
        if data == "Female":
            job["gender"] = data 
            job["job"] = female[random.randint(0, 9)]
            job["clan"] = clan[random.randint(0 , 3)]
            return job
        elif data == "Male":
            job["gender"] = data 
            job["job"] = male[random.randint(0, 9)]
            job["clan"] = clan[random.randint(0 , 3)]
            return job
     
    return {"job":"failure"}


       