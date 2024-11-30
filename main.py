from flask import Flask
import google.generativeai as genai


filename = 'apikey'

def get_file_contents(filename):
    try: 
        with open (filename, 'r') as f:
            return f.read().strip()

    except FileNotFoundError:
        print("'%s' file not found" % filename)


genai.configure(api_key=get_file_contents(filename))
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
