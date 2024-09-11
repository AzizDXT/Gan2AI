import sys
sys.path.insert(0, './stylegan2')  # تأكد من وجود المجلد stylegan2 في المسار
import dnnlib
import legacy
import numpy as np
from PIL import Image
import torch, os
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

def generate_image(model_path):
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    
    # فتح نموذج StyleGAN2 بدلاً من StyleGAN3
    with open(model_path, 'rb') as f:
        G = legacy.load_network_pkl(f)['G_ema'].to(device)

    # توليد صورة عشوائية باستخدام z
    z = torch.from_numpy(np.random.randn(1, G.z_dim)).to(device)
    img = G(z, None, truncation_psi=0.7, noise_mode='const')[0]
    img = (img.permute(1, 2, 0) * 127.5 + 128).clamp(0, 255).to(torch.uint8).cpu().numpy()
    
    image = Image.fromarray(img)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'generated_image.png')
    image.save(image_path)
    return 'generated_image.png'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    image_file = generate_image('./models/stylegan2.pkl')  # استخدام النموذج الخاص بـ StyleGAN2
    return render_template('index.html', image_file=image_file)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
