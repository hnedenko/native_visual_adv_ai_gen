import requests
from dotenv import load_dotenv
import os
import time
import json
import httpx


class NativeAdAIGen:
    def __init__(self):
        load_dotenv(dotenv_path='../.venv/.env')

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": os.getenv("COMFYUI_API_KEY")
        }

        file = "./simple_text_to_image_API.json"
        with open(file, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

        self.API_URL = 'https://api.runpod.ai/v2/e028q7wb3gb6ak'

    def generate_ad(self, context='', publisher='', width=128, height=128, steps = 10):

        # edit prompt
        prompt = 'An advertising image consists of a PRODUCT and a BACKGROUND. '
        prompt = prompt + 'The PRODUCT is the main object in the frame and must be clearly visible. '
        prompt = prompt + 'The BACKGROUND is all other details (background, lighting, atmosphere). '
        prompt = prompt + 'Both are equally important. '
        prompt = prompt + "\n\n"
        prompt = prompt + 'PRODUCT details:' + publisher
        prompt = prompt + "\n\n"
        prompt = prompt + 'BACKGROUND details:' + context
        self.data['6']["inputs"]["text"] = prompt

        # edit resolution
        self.data['27']["inputs"]["width"] = width
        self.data['27']["inputs"]["height"] = height

        # edit generation steps count
        self.data['31']["inputs"]["steps"] = steps

        # send requests to gen
        run_response = requests.post(f'{self.API_URL}/run', headers=self.headers, json=self.data)
        run_response.raise_for_status()
        task_id = run_response.json().get('id')
        print(f"Задание отправлено. ID: {task_id}")

        # update gen status
        while True:
            time.sleep(2)  # Задержка 2 секунды

            status_response = requests.get(f'{self.API_URL}/status/{task_id}', headers=self.headers)
            status_response.raise_for_status()
            status_data = status_response.json()
            current_status = status_data.get('status')

            print(f"Текущий статус: {current_status}")

            if current_status == 'COMPLETED':
                # check gen status
                return status_data.get('output')

            if current_status == 'FAILED':
                raise Exception(f"Генерация завершилась ошибкой: {status_data}")

    async def download_image(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.content
