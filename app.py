import os
import glob
from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path="/")

@app.route("/")
def hello_world():
    print("static folder path:", app.static_folder)
    static_files = "<br>".join(get_urls())
    return "<h1>Static files</h1> <p><b>Location:</b> {}</p> {}".format(app.static_folder, static_files)

def get_urls():
    urls = []
    static_files = glob.glob(app.static_folder + '**/**', recursive=True)
    for static_file in static_files:
        short_name = static_file.replace(app.static_folder, "")
        if os.path.isfile(static_file):
            #print("<a href='{0}'>{0}</a>".format(shortFile))
            urls.append("<a href='{0}'>{0}</a>".format(short_name))
    return urls

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'favicon'), 'favicon.ico')

if __name__ == "__main__":
    app.run(debug=True)