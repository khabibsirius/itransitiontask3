from flask import Flask, request
import math

app = Flask(__name__)


def lcm(x, y):
    if x == 0 or y == 0:
        return 0
    return abs(x * y) // math.gcd(x, y)


@app.route('/<path:email>', methods=['GET'])
def get_lcm(email):
    try:
        x = request.args.get('x')
        y = request.args.get('y')

        if x is None or y is None:
            return "NaN"

        x = int(x)
        y = int(y)

        if x < 0 or y < 0:
            return "NaN"

        result = lcm(x, y)
        return str(result)

    except (ValueError, TypeError):
        return "NaN"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
