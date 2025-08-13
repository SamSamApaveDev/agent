from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Sample data
user_data = {
    "salary": 3000,
    "expenses": {
        "Food": 450,
        "Media": 120,
        "Bank": 300,
        "Clothes": 180
    }
}

@app.route('/')
def index():
    total_expenses = sum(user_data["expenses"].values())
    budget_available = user_data["salary"] - total_expenses
    return render_template("index.html",
                           salary=user_data["salary"],
                           expenses=user_data["expenses"],
                           total_expenses=total_expenses,
                           budget=budget_available)

@app.route('/update', methods=['POST'])
def update():
    for category in user_data["expenses"]:
        value = request.form.get(category)
        if value:
            try:
                user_data["expenses"][category] = float(value)
            except ValueError:
                pass
    return redirect(url_for('index'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
