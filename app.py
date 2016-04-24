from flask import Flask,jsonify,request
import sys

app = Flask(__name__)
TOKEN = os.environ["TOKEN"]


@app.route("/")
def index():
    return jsonify({"info":"success"})

@app.route("/webhook/",methods=["GET","POST"])
def webhook():
    if request.method == "POST":
        print(request.data,file=sys.stderr)
        return jsonify({"info":"success"})


    else:
        verification_code = request.args.get("hub.verify_token")
        if verification_code == os.environ["VCODE"]:
            return request.args.get("hub.challenge")
        return "sorry"


if __name__ =="__main__":
    app.run(debug=True)
