from flask import Flask, render_template, request

app = Flask(__name__)

## containers for base64 strings
original_image = ""
style_image = ""



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submitImage1", methods=['POST'])
def recieve_original_image():
    global original_image
    data = request.get_json()
    base64_image = data.get('image')
    
    if base64_image.startswith("data:image"):
        base64_image = base64_image.split(",")[1] 
        
    original_image = base64_image
    
    return f"recieved original image"

@app.route("/submitImage2", methods=['POST'])
def recieve_style_image():
    global style_image
    data = request.get_json()
    base64_image = data.get('image')
    
    if base64_image.startswith("data:image"):
        base64_image = base64_image.split(",")[1]
    
    style_image = base64_image    
    
    return "recieved style image"



if __name__ == '__main__':
    app.run(debug = True)