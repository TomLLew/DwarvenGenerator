from flask import render_template, request, redirect, url_for
from application import backend
import requests
import random

stats = {"clan_skill": "none", "Strength": "none", "Defence": "none",
         "Speed": "none", "Luck": "none", "Intelligence": "none"}


@backend.route('/', methods=['GET', 'POST'])
def stat_generator():
    form = request.form.get('sex')
    sex = {"sex": "none"}
    sex["sex"] = form
    if request.method == 'POST':
        name = requests.post('http://127.0.0.1:5001/', params=sex)
        job = requests.post('http://127.0.0.1:5002/', params=sex)
        print(name.text)
        print(job.text)
        clan = job.text
        print(clan[clan]
        if clan == "Longbeards":
            for i in stats:
                stats[i]=random.randint(3, 9)
            stats["clan_skill"]="Sleight of Hand"
            data=dict(name.items() + job.items() + stats.items())
            return data
        elif clan == "Firebeards":
            for i in stats:
                stats[i]=random.randint(3, 9)
            stats["clan_skill"]="Marksmanship"
            data=dict(name.items() + job.items() + stats.items())
            return data
        elif clan == "Ironfists":
            for i in stats:
                stats[i]=random.randint(3, 9)
            stats["clan_skill"]="Melee Combat"
            data=dict(name.items() + job.items() + stats.items())
            return data
        elif clan == "Stonefoots":
            for i in stats:
                stats[i]=random.randint(3, 9)
            stats["clan_skill"]="Stamina"
            data=dict(name.items() + job.items() + stats.items())
            return data

        return "failure"
