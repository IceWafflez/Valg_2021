from datetime import datetime
import sqlite3
from flask import Flask, request
app = Flask(__name__)







class Data:
    def __init__(self, request) -> None:
        self.request = request
        def extract(key):
            return self.request.form[key]
        
        self.token = extract("token")
        self.vote = extract("vote")
        self.ts = datetime.utcnow()


@app.route('/vote', methods=['POST'])
def result():
    data = Data(request)
    conn = sqlite3.connect('DB/valg.db')
    c = conn.cursor()
    print(c.execute(f"SELECT COUNT(*) FROM voter WHERE token='{data.token}' AND token_used=0"))

    return "Submitted !"

#c.execute(f"SELLECT COUNT(*) FROM voter WHERE token={data.token} AND token is_used=0")


#-----------------------------------------------------------------------------------------

app.run(host="127.0.0.1", port=8080, debug=False)