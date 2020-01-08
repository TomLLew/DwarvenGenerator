from flask import render_template, request, redirect, url_for, jsonify
from application import service1
import random, requests, json

f_f_name = ["Yarsubelle", "Kobrebella", "Voddaebella", "Katdrouna", "Ulmaengrid",
            "Thraluhilde", "Ornetrude", "Huvribella", "Fosgribella", "Nekonelyn"]  

m_f_name = ["Gormon", "Halamar", "Luvon", "Vorvorick", "Skarseat",
          "Thaznat", "Ylra", "Guka", "Elberar", "Joilbe"]

l_name = ["The Magnificent", "The Protective", "The Hungry", "Boulderstone", "Copperguard",
          "Understone", "Mudsunder", "Grumblehelm", "Snowbane", "Flintgrip"]

name = {"firstname":"none", "lastname":"none"}

@service1.route('/', methods=['GET', 'POST'])
def random_name():
    if request.method == 'POST':
        data = request.args.get("sex")
        if data == 'Female':
            name["firstname"] = f_f_name[random.randint(0, 9)]
            name["lastname"] = l_name[random.randint(0, 9)]
            return name
        elif data == 'Male':
            name["firstname"] = m_f_name[random.randint(0, 9)]
            name["lastname"] = l_name[random.randint(0, 9)]
            return name
        return {"firstname":"failure"}
    