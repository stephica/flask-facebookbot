from flask import Flask,jsonify,request
import os

app = Flask(__name__)
conf = dict()
conf["TOKEN"] = os.environ["TOKEN"]
conf["VCODE"] = os.environ["VCODE"]


@app.route("/")
def index():
    return jsonify({"info":"success"})

@app.route("/token/<utoken>",methods=["GET","POST"])
def user_hook(utoken):
    pass



@app.route("/webhook/",methods=["GET","POST"])
def webhook():
    print("heyo",file=sys.stderr)
    if request.method =="POST":
        print(request.data,file=sys.stderr)
        return jsonify({"info":"success"})
    else:
        verification_code = request.args.get("hub.verify_token")
        if verification_code == conf["VCODE"]:
            return request.args.get("hub.challenge")
        return "sorry"


if __name__ =="__main__":
    app.run(debug=True)
