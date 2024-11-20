from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    """Tarkistaa, onko annettu luku alkuluku."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:number>', methods=['GET'])
def check_prime(number):
    """Palauttaa JSON-vastauksen, joka kertoo, onko luku alkuluku."""
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
