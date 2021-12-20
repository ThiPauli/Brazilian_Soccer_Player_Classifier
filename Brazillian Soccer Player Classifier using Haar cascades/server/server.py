#Creating a Python Flask server, a micro web server
from flask import Flask, request, jsonify
import util

app = Flask(__name__)

#creating the API called classify image
@app.route('/classify_image', methods = ['GET', 'POST'])

#This function will be doing the image classification using our saved model previously
def classify_image():
    #getting the image from the user
    image_data = request.form['image_data']

    #using that image in the fuction classify_image, which will do Base64 encoded string.
    #After, convert it to JSON
    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

#the main method run the python class server on this particular port
if __name__ == '__main__':
    print("Starting Python Flask Server for Player Soccer Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)