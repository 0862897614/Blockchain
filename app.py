import hashlib
import json
from time import time
from flask import Flask, render_template, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(proof=1, previous_hash='0')  # Genesis block

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        block['hash'] = self.hash(block)
        
        self.current_transactions = []  # Reset giao dịch
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        self.current_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_chain')
def get_chain():
    response = {'chain': blockchain.chain, 'length': len(blockchain.chain)}
    return jsonify(response)

@app.route('/mine_block')
def mine_block():
    if not blockchain.current_transactions:
        return jsonify({'message': 'No transactions to mine'}), 400
    block = blockchain.create_block(proof=1, previous_hash=None)
    return jsonify(block)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data = request.json
    if not all(k in data for k in ['sender', 'receiver', 'amount']):
        return jsonify({'message': 'Missing values'}), 400
    index = blockchain.add_transaction(data['sender'], data['receiver'], data['amount'])
    return jsonify({'message': f'Transaction added to Block {index}'})

if __name__ == '__main__':
    app.run(debug=True)