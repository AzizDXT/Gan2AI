Here's the updated `README.md` file for your `Gan2AI` project, which uses StyleGAN2 instead of StyleGAN3:

```markdown
# **Gan2AI: Image Generation Using StyleGAN2**

![Gan2AI Logo](https://raw.githubusercontent.com/AzizDXT/Gan2AI/main/LogoG2.png)

### **Description**

Gan2AI is a Python-based project that utilizes the **StyleGAN2** model to generate high-quality, semi-realistic images. The project comes with a Flask-based web interface that allows users to generate and view images with just one click. It leverages NVIDIA's state-of-the-art **StyleGAN2** for generating highly realistic images.

### **Features**

- **StyleGAN2 Integration**: Uses NVIDIA's StyleGAN2 to generate semi-realistic images.
- **Flask Web Interface**: Simple web interface for generating and displaying images.
- **Random Image Generation**: Creates random images based on a pre-trained model.

---

## **Project Structure**

```
Gan2AI/
│
├── models/                   # Pre-trained models (downloaded via Setup.py)
│   └── stylegan2-ffhq-config-f.pkl  # Pre-trained model for face generation
│
├── static/                   # Static directory (for images, CSS)
│   └── generated_image.png   # Auto-generated images
│   └── style.css             # Main CSS page
│   └── logo.png              # Main logo
|
├── templates/                # HTML templates for Flask
│   └── index.html            # Main HTML page
│
├── venv/                     # Virtual environment directory (created by the user)
│
├── RunGAN2.py                # Main script for generating images
├── Setup.py                  # Script to download model and install dependencies
├── requirements.txt          # List of dependencies for the project
└── README.md                 # Project documentation
```

---

## **Installation Instructions**

Follow these steps to set up and run the **Gan2AI** project on your local machine.

### **1. Clone the repository**

```bash
git clone https://github.com/AzizDXT/Gan2AI.git
cd Gan2AI
```

### **2. Set up a virtual environment**

It's recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### **3. Run the Setup script**

Run the `Setup.py` script to install the necessary dependencies and download the StyleGAN2 model:

```bash
python Setup.py
```

### **4. Run the application**

Once the model is downloaded and the dependencies are installed, run the following command to generate images:

```bash
python RunGAN2.py
```

### **5. Generate Images**

After running `RunGAN2.py`, a new image will be generated and saved as `generated_image.png` in the `static/` folder. The image will also be displayed automatically.

---

## **Requirements**

- Python 3.8+
- `torch`, `torchvision` for running the model
- `Flask` for serving the web interface
- NVIDIA GPU (optional but recommended for faster generation)

---

### **Setup.py**

The script installs the required packages and downloads the pre-trained StyleGAN2 model:

---

## **License**

This project is licensed under the MIT License.

---

### **Contributions**

Contributions are welcome! Feel free to open an issue or submit a pull request to suggest improvements or fix bugs.

---

