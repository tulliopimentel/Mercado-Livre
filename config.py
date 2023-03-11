import os
import app

key = os.urandom(16)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', key)