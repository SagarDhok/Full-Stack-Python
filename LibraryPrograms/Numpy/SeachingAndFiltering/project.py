# Recipe Website - Full Stack Project

# One-Click Setup

# Install dependencies
# Run: sh setup.sh

# setup.sh (Create this file and run it to set up everything automatically)

'''
#!/bin/bash

# Backend Setup
echo "Setting up backend..."
mkdir -p backend && cd backend
python3 -m venv venv
source venv/bin/activate
pip install flask flask-cors flask-bcrypt flask-jwt-extended pymongo
cat > app.py <<EOL
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'secret'
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['recipes']
users_collection = db['users']
recipes_collection = db['recipes']

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    users_collection.insert_one({'username': data['username'], 'password': hashed_password})
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users_collection.find_one({'username': data['username']})
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        token = create_access_token(identity=data['username'])
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.json
    recipes_collection.insert_one(data)
    return jsonify({'message': 'Recipe added successfully'})

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = list(recipes_collection.find({}, {'_id': 0}))
    return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
EOL
cd ..

# Frontend Setup
echo "Setting up frontend..."
npx create-react-app frontend
cd frontend
npm install axios
cat > src/App.js <<EOL
import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
    const [recipes, setRecipes] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:5000/recipes")
            .then(response => setRecipes(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h1>Recipe List</h1>
            <ul>
                {recipes.map((recipe, index) => (
                    <li key={index}>
                        <h3>{recipe.title}</h3>
                        <p>{recipe.instructions}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
EOL

# Instructions
echo "Setup complete! Run 'sh setup.sh' to start everything."
'''

# Now, just run the setup script:
# sh setup.sh

# This will automatically install everything and set up both backend and frontend for you.
