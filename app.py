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
@app.route('/book', methods=['GET', 'POST'])\
def book():\
    availability = load_json('availability.json')\
    message = None\
\
    if request.method == 'POST':\
        name = request.form.get('name', '').strip()\
        role = request.form.get('role', '').strip()\
        slot = request.form.get('slot')\
\
        # Validation: name required\
        if not name:\
            message = "Name is required."\
            return render_template('book.html', availability=availability, message=message)\
\
        # Validation: role required\
        if not role:\
            message = "Role is required."\
            return render_template('book.html', availability=availability, message=message)\
\
        # Validation: slot must exist\
        if slot not in availability:\
            message = "Selected slot is no longer available."\
            return render_template('book.html', availability=availability, message=message)\
\
        # Validation: slot cannot be in the past\
        from datetime import datetime\
        slot_dt = datetime.strptime(slot, "%Y-%m-%d %H:%M")\
        if slot_dt < datetime.now():\
            message = "You cannot book a past date."\
            return render_template('book.html', availability=availability, message=message)\
\
        # Save appointment\
        appointments = load_json('appointments.json')\
        appointments[name] = \{\
            "role": role,\
            "slot": slot,\
            "rescheduled": False,\
            "reason": ""\
        \}\
        save_json('appointments.json', appointments)\
\
        # Remove slot from availability\
        availability.remove(slot)\
        save_json('availability.json', availability)\
\
        message = "Appointment booked successfully!"\
        return render_template('book.html', availability=availability, message=message)\
\
    return render_template("book.html", availability=availability)\
\
@app.route('/reschedule', methods=['GET', 'POST'])\
def reschedule():\
    availability = load_json('availability.json')\
    appointments = load_json('appointments.json')\
    message = None\
\
    if request.method == 'POST':\
        name = request.form.get('name', '').strip()\
        new_slot = request.form.get('slot')\
        reason = request.form.get('reason', '').strip()\
\
        # Validation: name required\
        if not name:\
            message = "Name is required."\
            return render_template('reschedule.html', availability=availability, message=message)\
\
        # Validation: candidate must exist\
        if name not in appointments:\
            message = "No appointment found for this name."\
            return render_template('reschedule.html', availability=availability, message=message)\
\
        # Validation: reason required\
        if not reason:\
            message = "Reschedule reason is required."\
            return render_template('reschedule.html', availability=availability, message=message)\
\
        # Validation: cannot reschedule twice\
        if appointments[name]["rescheduled"]:\
            message = "You have already rescheduled once."\
            return render_template('reschedule.html', availability=availability, message=message)\
\
        # Validation: new slot must exist\
        if new_slot not in availability:\
            message = "Selected slot is not available."\
            return render_template('reschedule.html', availability=availability, message=message)\
\
        # Validation: new slot cannot be in the past\
        from datetime import datetime\
        slot_dt = datetime.strptime(new_slot, "%Y-%m-%d %H:%M")\
        if slot_dt < datetime.now():\
            message = "You cannot choose a past date."\
            return render_template('reschedule.html', availability=availability, message=message)\
\
        # Update appointment\
        old_slot = appointments[name]["slot"]\
        appointments[name]["slot"] = new_slot\
        appointments[name]["rescheduled"] = True\
        appointments[name]["reason"] = reason\
        save_json('appointments.json', appointments)\
\
        # Return old slot to availability\
        availability.append(old_slot)\
        availability.remove(new_slot)\
        save_json('availability.json', availability)\
\
        message = "Appointment rescheduled successfully!"\
        return render_template('reschedule.html', availability=availability, message=message)\
\
    return render_template('reschedule.html', availability=availability)\
\
@app.route("/appointments")\
def appointments_view():\
    appointments = load_json("appointments.json")\
    return render_template("appointments.html", appointments=appointments)\
\
if __name__ == "__main__":\
    app.run(debug=True)\
}