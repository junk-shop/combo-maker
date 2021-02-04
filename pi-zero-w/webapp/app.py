from flask import Flask, render_template, request
import pickle
import json
import os

app = Flask(__name__)

f = open("/home/pi/pi-zero-w/2021.txt")
lines = f.readlines()

daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', lines=map(json.dumps, lines))

@app.route('/', methods=['POST'])
def form():
    newLines = []
    for j in range(12):
        days = daysPerMonth[j]
        monthStr = ""
        for i in range(days):
            if request.form.get('m' + str(j) + 'd' + str(i)):
                monthStr += "1"
            else:
                monthStr += "0"
        newLines.append(monthStr)
    print(newLines)
    with open('/home/pi/p-zero-w/2021.txt', 'w') as f:
        for line in newLines:
            f.write("%s\n" % line)
    os.system('python3 /home/pi/pi-zero-w/epaper/PPT.py')
    return render_template('index.html', lines=map(json.dumps, newLines))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
