from ollama import chat
import time
start_time = time.time()
response = chat(
    model='moondream',
    messages=[
        {
            'role': 'user',
            'content': 'Describe this image',
            'images': [r"F:\Siddhesh\OneDrive - Anvis Digital Pvt Ltd\Downloads\burger_pizza.jpg"]
        }
    ]
)

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(response['message']['content'])