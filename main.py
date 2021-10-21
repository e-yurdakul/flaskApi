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
#app.config['MYSQL_CURSORCLASS'] = 'SSCursor'
mysql = MySQL()
mysql.init_app(app)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Ender YURDAKUL</h1><p>Tebrikler ilk Web API'ınızı başarıyla geliştirdiniz!</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/test', methods=['GET'])
def api_all():
    import api.v1.user as a
    b=a.user_return(mysql=mysql)
    return jsonify(b),200


app.run()