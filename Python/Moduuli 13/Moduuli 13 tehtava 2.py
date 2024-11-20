
from flask import Flask, jsonify, abort
import mysql.connector

app=Flask(__name__)

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='elias',
         password='Kesko123',
        collation="utf8mb4_general_ci",
         autocommit=True
         )

def get_airport_icao(ident):
    cursor=yhteys.cursor()
    cursor.execute("SELECT ident, name, municipality FROM airport where ident=%s", (ident,))
    result=cursor.fetchone()
    cursor.close()
    if result:
        return {"ICAO": result[0], "NAME": result[1], "MUNICIPALITY": result[2]}
    return None

@app.route('/kenttä/<string:ident>', methods=['GET'])
def airport_info(ident):
    airport=get_airport_icao(ident)
    if airport:
        return jsonify(airport)
    else:
        abort(404, description="Lentokenttää ei löydy")

if __name__ == '__main__':
    app.run(port=3000, debug=True)