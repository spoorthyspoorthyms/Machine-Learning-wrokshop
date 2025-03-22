from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {
        "id": 1,
        "name": "Item1",
        "price":10.99
    },
    {
        "id": 2,
        "name": "Item2",
        "price":15.49
    },
]

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

if __name__=='__main__':
    app.run(debug=True)