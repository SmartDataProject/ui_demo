import pandas as pd
import numpy as np
from flask import Flask, jsonify, request
app = Flask(__name__)



@app.route('/post', methods=['POST'])
def get_posts():
    user_input = request.json
    print(user_input)
    df = pd.DataFrame(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        columns=['a', 'b', 'c'])
    result = 'Moderate Mobile Gamer'
    game_type = "(You are a " + result +")"
    return "<h6>" + game_type + "</h1>" + df.to_html()
