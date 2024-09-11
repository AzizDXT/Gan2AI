import os
import subprocess
import requests

def download_model():
    url = 'https://api.ngc.nvidia.com/v2/models/org/nvidia/team/research/stylegan2/1/files?redirect=true&path=stylegan2-ffhqu-1024x1024.pkl'
    model_dir = 'models'
    model_name = 'stylegan2.pkl'
    
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    model_path = os.path.join(model_dir, model_name)

    response = requests.get(url, stream=True)
    with open(model_path, 'wb') as f:
        f.write(response.content)
    print(f'Model downloaded and saved as {model_name}')

def install_requirements():
    print('Installing required packages...')
    subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

if __name__ == '__main__':
    install_requirements()  
    download_model()  