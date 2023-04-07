import os

from flask import Flask, request, jsonify
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

app = Flask(__name__)
agent = create_csv_agent(OpenAI(temperature=0), 'tracker.csv', verbose=True)

@app.route('/api', methods=['POST'])
def process_query():
    user_input = request.json['query']
    response = agent.run(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
