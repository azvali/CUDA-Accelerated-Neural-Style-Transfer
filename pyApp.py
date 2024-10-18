from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/cuda_convert", methods = ['POST'])
def cuda_convert():
    data = request.get_json()
    original_image = data.get('original_image')
    style_image = data.get('style_image')
    use_cuda = data.get('use_cuda')
    
    if original_image.startswith("data:image"):
        original_image = original_image.split(",")[1]
    if style_image.startswith("data:image"):
        style_image = style_image.split(",")[1]
    
    
    return "recieved cuda convert"


@app.route("/cpu_convert", methods=['POST'])
def cpu_convert():
    
    data = request.get_json()
    original_image = data.get('original_image')
    style_image = data.get('style_image')
    use_cuda = data.get('use_cuda')
    
    if original_image.startswith("data:image"):
        original_image = original_image.split(",")[1]
    if style_image.startswith("data:image"):
        style_image = style_image.split(",")[1]
    
     
    return "recieved cpu convert"



























# @app.route("/submitImage1", methods=['POST'])
# def recieve_original_image():
#     global original_image
#     data = request.get_json()
#     base64_image = data.get('image')
    
#     if base64_image.startswith("data:image"):
#         base64_image = base64_image.split(",")[1] 
        
#     original_image = base64_image
    
#     return f"recieved original image"

# @app.route("/submitImage2", methods=['POST'])
# def recieve_style_image():
#     global style_image
#     data = request.get_json()
#     base64_image = data.get('image')
    
#     if base64_image.startswith("data:image"):
#         base64_image = base64_image.split(",")[1]
    
#     style_image = base64_image    
    
#     return "recieved style image"



if __name__ == '__main__':
    app.run(debug = True)