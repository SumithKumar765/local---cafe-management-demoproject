from flask import Flask, render_template, request

app = Flask(__name__)

# Menu dictionary
menu = {
    'Pizza': 100,
    'Pasta': 70,
    'Burger': 80,
    'Salad': 50,
    'Coffee': 80,
    'soda':60,
    'family pack ice cream butterscotch with cherry and straw berry topings with chocalate syrup free':400
}

@app.route("/", methods=["GET", "POST"])
def home():
    total = 0
    selected_items = []

    if request.method == "POST":
        selected_items = request.form.getlist("menu_items")
        total = sum(menu[item] for item in selected_items)

    return render_template("index.html", menu=menu, total=total, selected_items=selected_items)

if __name__ == "__main__":
    app.run(debug=True)
