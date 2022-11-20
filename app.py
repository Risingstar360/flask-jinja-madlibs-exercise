from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = "martinnorris200"
debug = DebugToolbarExtension(app)

@app.route("/")
def home_form():
    prompts = story.prompts
    return render_template("home_form.html", prompts=prompts)

@app.route("/your-story")
def story_time():
    text = story.generate(request.args)
    return render_template("story.html", text=text)