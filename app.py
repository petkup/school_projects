from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    decimal = request.args.get("decimal", "")
    if decimal:
        binary = binary_from(decimal)
        hexadecimal = hex_from(decimal)
    else:
        binary = ""
        hexadecimal = ""
    return (
            """<h1 style='color:green'>Základy klaudových technológií: skúška</h1><form action="" method="get">
                Decimal number: <input type="text" name="decimal">
                <input type="submit" value="Convert to binary/hexadecimal">
            </form>"""
        + "Binary: "
        + binary
        + "<h1 style='color:green'>---------</h1>"
        + "Hexadecimal: "
        + hexadecimal
    )

def binary_from(decimal):
    try:
        binary_number = int(decimal)
        return bin(binary_number)
    except ValueError:
        return "invalid input"

def hex_from(decimal):
    try:
        binary_number = int(decimal)
        return hex(binary_number)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run()
