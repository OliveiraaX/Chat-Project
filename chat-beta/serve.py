from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
    <!doctype html>
    <html>
        <head>
            <title>Forum Test</title>
        </head>
        <body>
            <h1>Welcome to Forum Test</h1>
            <iframe src="IP" width="100%" height="800px"></iframe>
        </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(host='IP', port=5000, debug=True)
