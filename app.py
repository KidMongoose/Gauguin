from flask import Flask, redirect, url_for, render_template, session
from models import *
import calendar
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/student/dashboard')
def student_dashboard():
    return render_template('dashboard.html')

@app.route('/student/settings')
def student_settings():
    return render_template('settings.html')

@app.route('/student/view/assignments')
def student_view_assignments():
    return render_template('assignments.html')

@app.route('/student/events/calendar')
def student_calendar():
    student_calendar = calendar.HTMLCalendar(firstweekday=0)
    student_current_date = datetime.datetime.now()
    return render_template('calendar.html', calendar=student_calendar.formatmonth(student_current_date.year, student_current_date.month))

@app.route('/student/events/reminders')
def student_event_reminders():
    return render_template('reminders.html')

@app.route('/student/messages')
def student_messages():
    return render_template('messages.html')

@app.route('/professor/dashboard')
def professor_dashboard():
    return render_template('dashboard.html')

@app.route('/professor/view/assignments')
def professor_view_assignments():
    return render_template('assignments.html')

@app.route('/professor/settings')
def professor_settings():
     return render_template('settings.html')

@app.route('/professor/events/calendar')
def professor_calendar():
    professor_calendar = calendar.HTMLCalendar(firstweekday=0)
    professor_current_date = datetime.datetime.today()
    return render_template('calendar.html', calendar= professor_calendar.formatmonth(professor_current_date.year, professor_current_date.month))
    
@app.route('/professor/events/reminders')
def professor_event_reminders():
    return render_template('reminders.html')

@app.route('/professor/messages')
def professor_messages():
    return render_template('messages.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404 - Page not found')

if __name__ == '__main__':
    app.run()