from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # We use an H1 tag so it's easy to see in the browser
    return "<h1>Version 1.0: Deployment Successful!</h1><p>Managed by Argo CD GitOps.</p>"

if __name__ == "__main__":
    # Must listen on 0.0.0.0 to be accessible inside a container
    app.run(host='0.0.0.0', port=80)
