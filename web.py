from flask import Flask,request
import os
import numpy as np
import requests
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('Classification Results on Face Dataset (1000 images).csv', header=None, names=['Image', 'Results'])
filename_value_map = df.set_index('Image')['Results'].to_dict()

@app.route("/home")
def home():
    return "Welcome to the Project 1-Phase 1!"


@app.route("/",methods=["POST"])
def check():
    if 'inputFile' in request.files:
        print(request.files)
        file = request.files['inputFile']
        print(file)
        filename, file_extension = os.path.splitext(file.filename)
        print("Received filename is : ", filename)

        if filename not in filename_value_map:
            'Provided image is not found in excel sheet'
        else:
            return "filename" + ":" + filename_value_map[filename]
    else:
        return "Please upload image file to recognize the person!!"
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)