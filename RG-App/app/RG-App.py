# from flask import Flask, request, jsonify   # Flask is a framework for building web applications in py 
# from flask_cors import CORS       # flask cors is a python library that enables access to your app from the outside (Gemini api)
# import google.generativeai as genai # import the ai generation api
# import os 

# app = Flask(__name__)   # initalize the flask app , this lets the "py app.py" execution inform where the flask app stuff is 
# CORS(app)   #  allows for other domains to interact or not 

# genai.configure(api_key="AIzaSyCV2EA8qzsqjZ976iBLA5_G9k4f8lbtPWk") # generated api key to use Gemini

# @app.route('/generate_recipe', methods=['POST'])    # take request POST from frontend /generate_recipe

# def generate_recipe(): # handles POST requests to process data 
#     data = request.json # get json data from request body
#     ingredients = data.get("ingredients")    # extract ingredients from json data (front end)

#     if not ingredients: # if no ingredients 
#         return jsonify({"error": "No ingredients provided"}), 400 # generate error to the frontend 
    
#     prompt = f"Create a recipe using these ingredients: {', '.join(ingredients)}." # What we are feeding the Gemini, seperate by comma

#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(prompt)

#         if not response or not hasattr(response, "text"):
#             return jsonify({"error": "Model failed to generate a recipe"}), 500

#         return jsonify({"recipe": response.text})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500  # Handle unexpected errors

# if __name__ == '__main__':
#     app.run(debug=True) #starts server 
