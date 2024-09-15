import sys
import concurrent.futures  
import shutil  
sys.path.insert(0, './stylegan2')  # تأكد من وجود المجلد stylegan2 في المسار

import zipfile  
import os
import dnnlib
import legacy
import numpy as np
from PIL import Image
import torch
import time
import random
from tqdm import tqdm 

output_dir = 'generated_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_image(model_path, img_number):
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    
    with open(model_path, 'rb') as f:
        G = legacy.load_network_pkl(f)['G_ema'].to(device)

    z = torch.from_numpy(np.random.randn(1, G.z_dim)).to(device)
    img = G(z, None, truncation_psi=0.7, noise_mode='const')[0]
    img = (img.permute(1, 2, 0) * 127.5 + 128).clamp(0, 255).to(torch.uint8).cpu().numpy()

    unique_id = f'{int(time.time())}_{random.randint(1000, 9999)}'
    image_name = f'image_{img_number}_{unique_id}.png'
    image_path = os.path.join(output_dir, image_name)

    image = Image.fromarray(img)
    image.save(image_path)

    print(f"\033[92m[INFO] Generated Image {img_number}: {image_name}\033[0m")
    print("[+] Generating Successfully")  

    return img_number

def zip_images(batch_num):
    zip_filename = f"images_batch_{batch_num}.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk(output_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, os.path.relpath(file_path, output_dir))
    
    shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    print(f"[INFO] تم ضغط {batch_num * 1000} صورة في الملف {zip_filename}")

def main():
    model_path = './models/stylegan2.pkl' 

    num_images = int(input("Enter the number of images to generate: "))

    num_workers = 5

    image_numbers = list(range(1, num_images + 1))

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        with tqdm(total=num_images, desc="Generating Images", unit="image") as pbar:
            batch_num = 0
            futures = {executor.submit(generate_image, model_path, img_num): img_num for img_num in image_numbers}

            for future in concurrent.futures.as_completed(futures):
                img_number = futures[future]
                try:
                    future.result()  
                except Exception as exc:
                    print(f"Image {img_number} generated an exception: {exc}")
                else:
                    pbar.update(1) 

                if img_number % 1000 == 0:
                    batch_num += 1
                    zip_images(batch_num)

if __name__ == "__main__":
    main()
