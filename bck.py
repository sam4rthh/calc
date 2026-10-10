from flask import Flask, render_template, request
 
app = Flask(__name__)
 
 
@app.route("/")
def home():
    return render_template("index.html")
 
 
@app.route("/calculate", methods=["POST"])
def calculate():
    num1_input = request.form.get("num1", "")
    num2_input = request.form.get("num2", "")
    operator = request.form.get("operator", "+")

    try:
        num1 = float(num1_input)
        num2 = float(num2_input)
    except (ValueError, TypeError):
        return render_template(
            "index.html",
            error="Enter a valid number in both fields.",
            num1=num1_input,
            num2=num2_input,
            operator=operator,
        )

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "%":
        if num2 == 0:
            return render_template(
                "index.html",
                error="Cannot calculate a remainder with zero.",
                num1=num1_input,
                num2=num2_input,
                operator=operator,
            )
        result = num1 % num2
    elif operator == "/":
        if num2 == 0:
            return render_template(
                "index.html",
                error="Cannot divide by zero.",
                num1=num1_input,
                num2=num2_input,
                operator=operator,
            )
        result = num1 / num2
    else:
        return render_template(
            "index.html",
            error="Choose a supported operation.",
            num1=num1_input,
            num2=num2_input,
            operator="+",
        )

    return render_template(
        "index.html",
        result=f"{result:g}",
        num1=num1_input,
        num2=num2_input,
        operator=operator,
    )
 
if __name__ == "__main__":
    app.run(debug=True)