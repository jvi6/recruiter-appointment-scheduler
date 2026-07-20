{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, render_template, request, redirect\
import json\
\
app = Flask(__name__)\
\
def load_json(filename):\
    with open(filename, "r") as f:\
        return json.load(f)\
\
def save_json(filename, data):\
    with open(filename, "w") as f:\
        json.dump(data, f, indent=4)\
\
@app.route("/availability", methods=["GET", "POST"])\
def availability():\
    availability = load_json("availability.json")\
\
    if request.method == "POST":\
        slot = request.form["slot"]\
        availability.append(slot)\
        save_json("availability.json", availability)\
        return redirect("/availability")\
\
    return render_template("availability.html", availability=availability)\
\
@app.route("/book", methods=["GET", "POST"])\
def book():\
    availability = load_json("availability.json")\
    appointments = load_json("appointments.json")\
\
    if request.method == "POST":\
        name = request.form["name"]\
        role = request.form["role"]\
        slot = request.form["slot"]\
\
        if slot not in availability:\
            return "Slot unavailable."\
\
        appointment = \{\
            "name": name,\
            "role": role,\
            "original_time": slot,\
            "rescheduled_time": None,\
            "reschedule_reason": None,\
            "reschedule_count": 0\
        \}\
\
        appointments.append(appointment)\
        save_json("appointments.json", appointments)\
\
        availability.remove(slot)\
        save_json("availability.json", availability)\
\
        return redirect("/appointments")\
\
    return render_template("book.html", availability=availability)\
\
@app.route("/reschedule", methods=["GET", "POST"])\
def reschedule():\
    appointments = load_json("appointments.json")\
    availability = load_json("availability.json")\
\
    if request.method == "POST":\
        name = request.form["name"]\
        new_slot = request.form["slot"]\
        reason = request.form["reason"]\
\
        for appt in appointments:\
            if appt["name"] == name:\
                if appt["reschedule_count"] == 1:\
                    return "You have already rescheduled once."\
\
                if new_slot not in availability:\
                    return "Slot unavailable."\
\
                availability.append(appt["original_time"])\
                availability.remove(new_slot)\
\
                appt["rescheduled_time"] = new_slot\
                appt["reschedule_reason"] = reason\
                appt["reschedule_count"] = 1\
\
                save_json("appointments.json", appointments)\
                save_json("availability.json", availability)\
\
                return redirect("/appointments")\
\
    return render_template("reschedule.html", availability=availability)\
\
@app.route("/appointments")\
def appointments_view():\
    appointments = load_json("appointments.json")\
    return render_template("appointments.html", appointments=appointments)\
\
if __name__ == "__main__":\
    app.run(debug=True)\
}