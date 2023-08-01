from flask import Flask, request, jsonify

app = Flask(__name__)

records = []

# Create a new record
@app.route('/records', methods=['POST'])
def create_record():
    data = request.get_json()
    data['id'] = len(records) +1 # give a unique to each record
    records.append(data)
    return jsonify(data)

# Get record by ID
@app.route('/records/<int:record_id>', methods=['GET'])
def get_records(record_id):
    for record in records:
        if record['id'] == record_id:
            return jsonify(record)
    return 'record not found'

# Get record by a query
@app.route('/records', methods=['GET'])
def get_all_records():
    query = request.args.get('query')
    if query:
        filtered_records = [record for record in records if query in record.values()]
        return jsonify(filtered_records)
    return jsonify(records)

# Delete a record by name
@app.route('/records', methods=['DELETE'])
def delete_records():
    name = request.args.get('name')
    if name:
        for record in records:
            if record['name'] == name:
                records.remove(record)
                return 'record deleted', 200
        return 'record not found', 404
    return 'missing name paramater', 400

# update a record
@app.route('/records/<int:id>', methods=['PUT'])
def update_records(id):
    record = next((record for record in records if record['id'] == id), None)
    if record is None:
        return jsonify({'error': 'record not found'}), 404

    data = request.get_json() 
    record.update(data)
    return jsonify(record)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
