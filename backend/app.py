# ============================================================================
# FILE App.py
#   Description:
#     File containing the service routes and functions for the Flask backend.
# ============================================================================

# Importing dependencies
from flask import Flask

# Initiating Flask server instance
app = Flask(__name__)

# Test service
@app.route("/test")
def test():
    return "This is a test output."

# Initiating server if App is main file
if __name__ == '__main__':
    app.run()