# -*- coding: utf-8 -*-
import hashlib
import json
from time import time
from flask import Flask, render_template, jsonify, request
from datetime import datetime

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.current_transactions = []
        self.difficulty = difficulty  # Hash must start with this many zeros
        self.create_block(proof=1, previous_hash='0')  # Genesis block

    def create_block(self, proof, previous_hash):
        nonce = 0
        timestamp = datetime.fromtimestamp(time()).strftime('%d/%m/%Y %H:%M:%S')
        
        # Proof of Work: Mine block until hash meets difficulty
        while True:
            block = {
                'index': len(self.chain) + 1,
                'timestamp': timestamp,
                'transactions': self.current_transactions,
                'proof': proof,
                'previous_hash': previous_hash if previous_hash else self.hash(self.chain[-1]),
                'nonce': nonce
            }
            
            block_hash = self.hash(block)
            # Check if hash meets difficulty requirement (starts with required zeros)
            if block_hash.startswith('0' * self.difficulty):
                block['hash'] = block_hash
                break
            
            nonce += 1
        
        self.current_transactions = []  # Reset giao dịch
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        self.current_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': datetime.fromtimestamp(time()).strftime('%d/%m/%Y %H:%M:%S')
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_copy = block.copy()
        block_copy.pop('hash', None)
        block_string = json.dumps(block_copy, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
    
    def get_stats(self):
        total_blocks = len(self.chain)
        total_transactions = sum(len(block['transactions']) for block in self.chain)
        pending_transactions = len(self.current_transactions)
        return {
            'total_blocks': total_blocks,
            'total_transactions': total_transactions,
            'pending_transactions': pending_transactions,
            'chain_valid': True
        }
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Kiểm tra hash của block hiện tại
            if current_block['hash'] != self.hash(current_block):
                return False
            
            # Kiểm tra previous_hash trỏ đến block trước
            if current_block['previous_hash'] != previous_block['hash']:
                return False
        
        return True
    
    def reset(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(proof=1, previous_hash='0')

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_chain')
def get_chain():
    response = {'chain': blockchain.chain, 'length': len(blockchain.chain)}
    return jsonify(response)

@app.route('/get_stats')
def get_stats():
    return jsonify(blockchain.get_stats())

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

@app.route('/validate_chain')
def validate_chain():
    is_valid = blockchain.is_chain_valid()
    return jsonify({'valid': is_valid, 'message': 'Blockchain hợp lệ' if is_valid else 'Blockchain không hợp lệ'})

@app.route('/reset_chain')
def reset_chain():
    blockchain.reset()
    return jsonify({'message': 'Blockchain đã được reset', 'chain': blockchain.chain})

if __name__ == '__main__':
    app.run(debug=True)