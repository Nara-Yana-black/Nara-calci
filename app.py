from flask import Flask, render_template, request
from fractions import Fraction
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            # Get form data
            num1 = request.form.get("num1", "")
            num2 = request.form.get("num2", "")
            operation = request.form["operation"]
            
            # Handle operations
            if operation == "fraction_to_decimal":
                # Interpret num1 as a fraction (e.g., "1/10")
                result = float(Fraction(num1))
            elif operation == "decimal_to_fraction":
                # Interpret num1 as a decimal and convert to fraction
                result = Fraction(float(num1)).limit_denominator()
            else:
                # Convert inputs to float if they are required
                num1 = float(num1) if num1 else None
                num2 = float(num2) if num2 else None
                
                if operation == "add":
                    result = num1 + num2
                elif operation == "subtract":
                    result = num1 - num2
                elif operation == "multiply":
                    result = num1 * num2
                elif operation == "divide":
                    result = num1 / num2
                elif operation == "power":
                    result = math.pow(num1, num2)
                elif operation == "factorial":
                    result = math.factorial(int(num1))
                elif operation == "percentage":
                    result = (num1 / 100) * num2
        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)