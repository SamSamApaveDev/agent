from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

# Données utilisateur
user_data = {
    "salary": 0,
    "charges": []
}

@app.route('/')
def index():
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    total_charges = sum(user_data["charges"])
    budget_available = user_data["salary"] - total_charges

    events_today = ["(Connexion à Google Calendar requise)"]
    events_yesterday = ["(Connexion à Google Calendar requise)"]

    return render_template('index.html',
                           salary=user_data["salary"],
                           charges=user_data["charges"],
                           budget=budget_available,
                           today=today,
                           yesterday=yesterday,
                           events_today=events_today,
                           events_yesterday=events_yesterday)

@app.route('/configure', methods=['GET', 'POST'])
def configure():
    if request.method == 'POST':
        salary = float(request.form.get('salary', 0))
        charges_raw = request.form.get('charges', '')
        charges = [float(c.strip()) for c in charges_raw.split(',') if c.strip().replace('.', '', 1).isdigit()]
        user_data["salary"] = salary
        user_data["charges"] = charges
        return redirect(url_for('index'))
    return render_template('configure.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
