import flask
import requests
app = flask.Flask(__name__, template_folder="dynamic")

@app.route("/")
def home():
    return flask.render_template("anticheats.html")

@app.route("/baby")
def baby():
    return """
    <h1>Don't click it</h1>
    <form action="/baby/sendhentai" method="post">
        <button type="submit">Click if u hate niggers</button>
    </form>
    """

@app.route("/baby/sendhentai", methods=["POST"])
def send():
    if flask.request.method == "POST":
        response = requests.get("https://api.waifu.pics/nsfw/waifu")
        image_url = response.json().get("url")
        discord_webhook_url = "https://discord.com/api/webhooks/1309969379345301575/_of_IBZSuGNo9vVXJm6A1FlTr8g7v_YKvt2VZJQrv9XHOPDl9idmuNyUAKFtQm6Yb8G6"
        requests.post(discord_webhook_url, json={"content": "A nigger pressed the button"})
        return flask.redirect("/baby")

app.run(host="0.0.0.0", port=5000)
