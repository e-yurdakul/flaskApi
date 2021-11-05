from main import app
from pymysql.cursors import DictCursor
from flaskext.mysql import MySQL

def ender(mysql=""):
    app.config['MYSQL_DATABASE_USER'] = 'priceloo_viewsonic_ana'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'viewsonic_ana123-'
    app.config['MYSQL_DATABASE_DB'] = 'priceloo_viewsonic_ana'
    app.config['MYSQL_DATABASE_HOST'] = '78.135.107.129'
    app.config['MYSQL_CURSORCLASS'] = 'SSCursor'
    mysql = MySQL()
    mysql.init_app(app)
    print(mysql)
    db = mysql.connect()
    cursor = db.cursor(cursor=DictCursor)
    query_string = "SELECT * FROM eticaret LIMIT 2"
    cursor.execute(query_string)
    data = cursor.fetchall()
    return data
    #return "ender fucntiyon "