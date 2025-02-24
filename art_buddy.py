import requests # allows us to make http calls like get/post request
from PIL import Image # now importing python image library to display/handle images
from io import BytesIO # Helps convert raw image data from the API into an actual image.

api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjFjNDQxNWNhNjNkNjljNWI1Mzk4NGQyN2E3YTU5ZGMwIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDItMjRUMDU6NDI6MjcuMjk1NDE5In0.OOMfOJWIAlQf1ppaNtRrl3nN53vowm989IBAP1Cwzc0" # Without this token, the API won't allow access.

user_input = input("Enter the description for the image: ")

url = "https://api.monsterapi.ai/v1/generate/txt2img" # The API endpoint (url) is where we send requests to generate images.
headers = {"Authorization": f"Bearer {api_token}"} # The headers contain the Authorization token (needed for authentication).

response = requests.post(url, json={"prompt":user_input,"safe_filter":True},headers=headers)

if response.status_code == 200:
    print("Loading.....This may take a few seconds.")
    process_id = response.json().get("process_id")

    while True:
        # The program enters a loop to check the status of image generation.
        # It sends a GET request to the API with the process_id to check if the image is ready.

        status_data = requests.get(f"https://api.monsterapi.ai/v1/status/{process_id}",headers=headers).json()
        status = status_data.get("status")

        if status == "COMPLETED":
            image_url = status_data['result']['output'][0]
            img = Image.open(BytesIO(requests.get(image_url).content)).show()
            break
        elif status == "FAILED":
            print("Image generation failed...")
            break
else:
    print(f"Error: {response.status_code}")


"""

Normally, when we download an image from the internet, it is stored as binary data (raw bytes). However, the PIL (Python Image Library) expects an image file or an image stream to open and display it properly.

BytesIO acts like a bridge between the raw image data and PIL by converting the downloaded bytes into a format that PIL can read.

"""