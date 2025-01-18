   from flask import Flask, request, jsonify
   import google.generativeai as genai
   import os

   app = Flask(__name__)

   # Configure the Gemini API
   api_key = os.getenv("GEMINI_API_KEY")
   genai.configure(api_key=api_key)

   @app.route('/analyze', methods=['POST'])
   def analyze():
       youtube_link = request.form['youtube_link']
       model = genai.GenerativeModel("gemini-1.5-flash")
       response = model.generate_content(f"Analyze products in video: {youtube_link}")
       return jsonify(response.text)

   if __name__ == '__main__':
       app.run(debug=True)
