from flask import Flask 
from public import public
from admin import admin
from institute import institute
from speaker import speaker
from user import user
app=Flask(__name__)
app.secret_key="session"

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(institute)
app.register_blueprint(speaker)
app.register_blueprint(user)
app.run(debug=True,port="5008")



