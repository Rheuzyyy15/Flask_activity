from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample data - inventory items
items = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500},
    {"id": 3, "name": "Headphones", "price": 150}
]


# 1. Welcome Endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})


# 2. Get all items (JSON format)
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"items": items})


# 3. Get item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404


# 4. Add a new item (POST request)
@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_id = max(item["id"] for item in items) + 1
    new_item = {"id": new_id, "name": data["name"], "price": data["price"]}
    items.append(new_item)

    return jsonify(new_item), 201


# 5. Render items in an HTML page using Jinja2
@app.route('/items_html', methods=['GET'])
def items_html():
    return render_template('items.html', items=items)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
