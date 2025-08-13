from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Sample data structure
budget_data = {
    "salary": 3000,
    "expenses": {
        "Food": 0,
        "Media": 0,
        "Transport": 0,
        "Loisirs": 0,
        "Bank": 0,
        "Clothes": 0
    }
}

@app.route('/')
def index():
    total_expenses = sum(budget_data["expenses"].values())
    budget_remaining = budget_data["salary"] - total_expenses
    return render_template("index.html", data=budget_data, remaining=budget_remaining)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    category = request.form.get("category")
    amount = float(request.form.get("amount", 0))
    if category in budget_data["expenses"]:
        budget_data["expenses"][category] += amount
    total_expenses = sum(budget_data["expenses"].values())
    budget_remaining = budget_data["salary"] - total_expenses
    return jsonify({"remaining": budget_remaining, "expenses": budget_data["expenses"]})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
