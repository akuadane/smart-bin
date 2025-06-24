# Waste Classification Project

This project consists of a machine learning-based waste classification system with a Flask API backend and an Angular web application frontend. The system can classify waste images into 9 different categories: Cardboard, Food Organics, Glass, Metal, Miscellaneous Trash, Paper, Plastic, Textile Trash, and Vegetation.

## Project Structure

```
project/
├── api.py                 # Flask API server
├── requirements.txt       # Python dependencies
├── models/               # Trained ML models
│   └── resnet18_whole.pth
├── uploaded/             # Directory for uploaded images
├── waste-predictor/      # Angular web application
│   ├── package.json
│   └── src/
│       └── app/
└── README.md
```

## Features

- **Image Upload**: Upload waste images through the web interface
- **Real-time Classification**: Get instant predictions using a ResNet18 model
- **Interactive UI**: Drag-and-drop interface for organizing waste categories
- **Visual Feedback**: Highlighted containers based on classification results

## Prerequisites

- Python 3.8 or higher
- Node.js 18 or higher
- npm or yarn package manager

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd smart-bin
```

### 2. Set up the Python Environment (Backend)

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Set up the Angular Application (Frontend)

```bash
# Navigate to the Angular project directory
cd waste-predictor

# Install Node.js dependencies
npm install
```

## Running the Application

### Step 1: Start the Flask API Server

Open a terminal and run the Flask API:

```bash
# Make sure you're in the project root directory
# Activate virtual environment if not already activated
python3 api.py
```

The API server will start on `http://127.0.0.1:5000` with the following endpoints:
- `GET /hello` - Health check endpoint
- `POST /predict` - Image classification endpoint

### Step 2: Start the Angular Web Application

Open another terminal and start the Angular development server:

```bash
# Navigate to the waste-predictor directory
cd waste-predictor

# Start the development server
npm start
```

The web application will be available at `http://localhost:4200`

## How to Use

1. **Open the Web Application**: Navigate to `http://localhost:4200` in your browser
2. **Upload an Image**: Click the "Choose File" button in the upload section
3. **View Results**: The system will automatically classify the image and highlight the appropriate waste category container
4. **Organize Categories**: Use the drag-and-drop interface to organize waste categories into different containers

## API Endpoints

### POST /predict
Upload an image for waste classification.

**Request:**
- Content-Type: `multipart/form-data`
- Body: Form data with a `file` field containing the image

**Response:**
```json
{
  "prediction": "Cardboard"
}
```

### GET /hello
Health check endpoint.

**Response:**
```json
{
  "message": "Hello, World!"
}
```

## Model Information

The project uses a ResNet18 model (`resnet18_whole.pth`) trained on waste classification data. The model can classify images into 9 different waste categories:

- Cardboard
- Food Organics
- Glass
- Metal
- Miscellaneous Trash
- Paper
- Plastic
- Textile Trash
- Vegetation

## Troubleshooting

### Common Issues

1. **Port Already in Use**: If port 5000 is already in use, modify the port in `api.py`
2. **CORS Issues**: The API includes CORS support, but ensure both servers are running
3. **Model Loading**: Ensure the `models/resnet18_whole.pth` file exists in the project directory
4. **Image Upload**: Make sure the `uploaded/` directory exists and has write permissions

### Dependencies

If you encounter dependency issues:

```bash
# Update Python packages
pip install --upgrade -r requirements.txt

# Update Node.js packages
cd waste-predictor
npm update
```

## Development

### Backend Development
- The Flask API is in `api.py`
- Model files are stored in the `models/` directory
- Uploaded images are saved in the `uploaded/` directory

### Frontend Development
- Angular application is in the `waste-predictor/` directory
- Main component logic is in `waste-predictor/src/app/app.component.ts`
- Styling is in `waste-predictor/src/app/app.component.css`

## License

MIT License

Copyright (c) 2024 Waste Classification Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
