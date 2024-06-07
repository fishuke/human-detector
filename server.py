from flask import Flask, request, jsonify, render_template
import base64
from api import check

app = Flask(__name__)

def is_base64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s.encode('utf-8')
    except Exception:
        return False

@app.route('/api/human_detector', methods=['POST'])
def human_detector():
    img_data = request.json.get('img', '')
    if img_data:
        if is_base64(img_data):
            res = check(img_data)
            return res
        else: 
            return jsonify({"error": "Please provide a valid Base64 URL", "ishuman": None})
    else:
        return jsonify({
            "error": "Please provide an img",
            "ishuman": None
        })

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)