from flask import Flask, request, jsonify
import torchvision.models as models
import torch
from torchvision import  transforms
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

classes = ['Cardboard', 'Food Organics', 'Glass', 'Metal', 'Miscellaneous Trash', 'Paper', 'Plastic', 'Textile Trash', 'Vegetation']


resnet18_whole = models.resnet18(weights=None)
head = torch.nn.Linear(resnet18_whole.fc.in_features, len(classes))
resnet18_whole.fc = head
resnet18_whole.load_state_dict(torch.load('./models/resnet18_whole.pth', map_location=torch.device('cpu')))
resnet18_whole.eval()


transform = transforms.Compose([
    transforms.Resize((224, 224)),  
    transforms.ToTensor(),          
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  
])

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/predict', methods=['POST'])
def predict():
    # Here you would typically process the input data and make a prediction
    # For demonstration, we'll just return a dummy 

    if 'file' not in request.files:
        return jsonify({'error': 'No file part in request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        image = Image.open(file.stream).convert('RGB')
        image.save('./uploaded/'+file.filename)
        image = transform(image).unsqueeze(0)  # Add batch dimension
        with torch.no_grad():
            output = resnet18_whole(image)
            _, predicted = torch.max(output, 1)
            # Convert the predicted class index to a label
            # For example, if you have a mapping of indices to labels
            label = classes[predicted.item()]
        
        print(file.filename," > ", label)
        
        return jsonify({'prediction': label})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
   
    app.run(debug=True)