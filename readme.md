📘 Recruiter Appointment Scheduler
A Flask-based web application that allows candidates to book, reschedule, and manage recruiter appointments.
Built as part of the Digital Transformation for Business module.

🌟 Overview
This project implements a simple but fully functional appointment scheduling system with:

Booking

Rescheduling (once only)

Dark mode

Role‑based slot durations

ICS calendar export

JSON storage

Availability editor

Error handling

Basic email logic (blocked by Gmail, documented)

The app is intentionally lightweight and easy to run locally.

✨ Features
✔ Core Functionality
Appointment Booking  
Candidates select a slot and book an appointment.

Double‑Booking Prevention  
A slot cannot be booked twice.

Rescheduling (One Time Only)  
Candidates may reschedule once.
A second attempt triggers a clear error message.

Role‑Based Slot Duration  
Slot length adjusts automatically based on role (e.g., Developer = 45 min).

Dark Mode  
Toggle between light and dark UI themes.

✔ Data Handling
JSON Storage  
All appointments stored in appointments.json.

JSON Updates  
Booking, rescheduling, and cancellation update the JSON file immediately.

✔ Export Features
ICS Export  
Each appointment can be downloaded as a .ics calendar file
(Google Calendar, Outlook, Apple Calendar compatible).

CSV Export  
CSV export was intentionally skipped and documented.

✔ Email Notifications (Partially Implemented)
Email logic implemented using Flask‑Mail.

Gmail blocks SMTP access without app passwords → sending disabled.

Documented in the report.

⚠ Features Not Included
Recruiter dashboard

Full conflict detection (booking logic already prevents conflicts)

CSV export (skipped intentionally)

📸 Screenshots
Screenshots are included in the /screenshots folder:

Availability Editor

Booking Page

Reschedule Page

JSON After Booking

JSON After Rescheduling

Second Reschedule Error

GitHub Repository

Trello Board

Dark Mode

Figure captions are included in the report.

🤖 AI‑Use Statement
Artificial Intelligence tools were used to support development of this project.
Specifically, Microsoft Copilot was used to:

Generate and refine code snippets (Flask routes, HTML templates, JSON handling)

Debug errors and improve logic (slot parsing, rescheduling rules)

Suggest UI improvements (dark mode, button placement)

Provide documentation text (README sections, comments)

Assist with testing scenarios and edge‑case reasoning

All AI‑generated content was reviewed, tested, and modified by the developer.
The final implementation reflects the developer’s own decisions, structure, and integration work.

AI tools were not used to automatically generate the entire project, nor to bypass learning outcomes.
They served as an assistant for problem‑solving, debugging, and documentation.

How to Run the App
1. Install dependencies
Code
pip install flask flask-mail
2. Run the server
Code
python app.py
3. Open the browser
Code
http://127.0.0.1:5000/
🧪 Testing Notes
Rescheduling works only once

Double booking is prevented

ICS export works for each appointment

Email sending is disabled due to Gmail restrictions

JSON updates immediately after each action

📜 License
This project is for academic use within the Digital Transformation for Business module.
