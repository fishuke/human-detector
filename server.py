from flask import Flask, request, render_template_string, jsonify  # Added jsonify import
import base64
def is_base64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False

app = Flask(__name__)

@app.route('/api/human_detector')
def home():
    img_url = request.args.get('img', '')
    if img_url:
        if is_base64(img_url):  # Fixed function call to is_base64
            return img_url
        else: 
            return jsonify({"error": "please provide a base64 url","ishuman": None})  # Fixed Json to jsonify
    else:
        return jsonify({
            "error": "Please provide an img",
            "ishuman": None
        })

if __name__ == '__main__':
    app.run(debug=True)
