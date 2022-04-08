from flask import Flask, request, session,jsonify
import random

app = Flask("ITsafe API Server", static_url_path='')
app.secret_key = "ajsd8h218hd8hcs8hj9219ejd9ch8mc91u239m921cvu39du2191jd"


@app.route('/api/start_game', methods=["GET"])
def start_game():
    session["number"] = random.randint(0,100)
    session["tries"] = 0

    return jsonify({"success": True})


@app.route('/api/guess_the_number', methods=["POST"])
def guess_the_number():
    guess = int(request.json["guess"])
    session["tries"] +=1

    if guess < session["number"]:
        status = "smaller"
    elif guess > session["number"]:
        status = "bigger"
    else:
        status = "you win"

    return jsonify({"status": status, "tries":session["tries"]})

debug = True
app.run(host='0.0.0.0', port=1337, debug=debug)
