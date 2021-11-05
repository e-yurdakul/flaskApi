import flask
from flask import request, jsonify
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['MYSQL_DATABASE_USER'] = 'priceloo_viewsonic_ana'
app.config['MYSQL_DATABASE_PASSWORD'] = 'viewsonic_ana123-'
app.config['MYSQL_DATABASE_DB'] = 'priceloo_viewsonic_ana'
app.config['MYSQL_DATABASE_HOST'] = '78.135.107.129'
# app.config['MYSQL_CURSORCLASS'] = 'SSCursor'
mysql = MySQL()
mysql.init_app(app)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Ender YURDAKUL</h1><p>Tebrikler ilk Web API'ınızı başarıyla geliştirdiniz!</p>'''\

@app.route('/aa', methods=['GET'])
def homez():
    import aaa as a

    print(a.ender(mysql=mysql))
    return '''<h1>asdf!</p>'''
@app.route('/bb', methods=['GET'])
def homezz():
    db = mysql.connect()
    cursor = db.cursor(cursor=DictCursor)
    query_string = "SELECT * FROM eticaret LIMIT 2"
    cursor.execute(query_string)
    data = cursor.fetchall()
    return f"{data}"
    #return '''<h1>asdf!</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/test', methods=['GET'])
def api_all():
    import api.v1.user as a
    b=a.user_return(mysql=mysql)
    return jsonify(b),200
try:
    pass
except:
    print("asd"),
if __name__ == '__main__':
    app.run()