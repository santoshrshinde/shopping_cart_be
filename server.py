from sanic import Sanic, response
from sanic.response import text
from sanic import json

#import mysql.connector
import mysql.connector

# database connection
db = mysql.connector.connect(host='127.0.0.1', user='root', passwd='Reset@123', db='demo', port=3306)   

app = Sanic("ShoppingCart")
app.config.LOGGING = True

# get users api
@app.get("/get_users")
# @cursor()
async def getUsers(request):
    cursor = db.cursor(dictionary=True)
    cursor.execute("select * from user")
    users = cursor.fetchall()
    return json({"success": True, "users": users})
