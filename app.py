from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>ML Ops Assignment 1</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 50px; }
        h1 { color: #333; }
        .container { border: 2px solid #333; padding: 20px; display: inline-block; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to ML Ops Assignment 1</h1>
        <p><strong>Collaborators:</strong></p>
        <p>Shaheer Haq (21i-1657)</p>
        <p>Abdullah Iftikhar (21i-1687)</p>
        <p>This is the first assignment of ML Ops.</p>
    </div>
</body>
</html>
"""


@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)


if __name__ == '__main__':
    app.run(debug=True)
