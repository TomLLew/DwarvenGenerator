from flask import render_template, request, jsonify, redirect, url_for
from application import backend
import requests, random, json


stats = {"clan_skill": "none", "Strength": "none", "Defence": "none",
         "Speed": "none", "Luck": "none", "Intelligence": "none"}


@backend.route('/stats', methods=['GET', 'POST'])
def stat_generator():
    form = request.args.get('gender')
    gender = {"gender": "none"}
    gender["gender"] = form
    if request.method == 'POST':
        name = requests.post('http://127.0.0.1:5001/name', params=gender).json()
        job = requests.post('http://127.0.0.1:5002/job', params=gender).json()
        clan = job['clan']
        if clan == "Longbeards":
            for i in stats:
                stats[i]=random.randint(3, 9)
            for key in name, job:
                stats.update(key)
            stats["clan_skill"]="Quick Shot"
            return stats
        elif clan == "Firebeards":
            for i in stats:
                stats[i]=random.randint(3, 9)
            for key in name, job:
                stats.update(key)
            stats["clan_skill"]="Fire Bomb"
            return stats
        elif clan == "Ironfists":
            for i in stats:
                stats[i]=random.randint(3, 9)
            for key in name, job:
                stats.update(key)
            stats["clan_skill"]="Bash"
            return stats
        elif clan == "Stonefoots":
            for i in stats:
                stats[i]=random.randint(3, 9)
            for key in name, job:
                stats.update(key)
            stats["clan_skill"]="Sprint"
            return stats

        return "failure"
