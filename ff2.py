# Import the necessary modules
import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact():
    # Clear the screen
    clear()
    
    # Enhanced header
    put_html('''
        <div style="background-color: black; color: white; padding: 15px; text-align: center; border-radius: 10px;">
            <h1>🎉 Fun Fact Generator 🎉</h1>
        </div>
    ''')
    
    # URL for fetching the fun fact
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    # Fetch data from the API
    response = requests.get(url)
    data = json.loads(response.text)
    useless_fact = data['text']
    
    # Display the fact in a styled box
    put_html(f'''
        <div style="margin: 20px auto; padding: 20px; max-width: 600px; text-align: center; border: 2px solid #ddd; 
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); border-radius: 10px; background-color: #f9f9f9;">
            <p style="color: #007BFF; font-size: 20px; font-weight: bold; font-family: Arial, sans-serif;">{useless_fact}</p>
        </div>
    ''')
    
    # Add a button to fetch another fact
    put_buttons(
        [{"label": "Click me for another fact!", "value": "new_fact", "color": "success"}],
        onclick=lambda _: get_fun_fact()
    )

# Driver Function
if __name__ == '__main__':
    # Display initial heading
    put_html('''
        <div style="background-color: black; color: white; padding: 15px; text-align: center; border-radius: 10px;">
            <h1>🎉 Fun Fact Generator 🎉</h1>
        </div>
    ''')
    
    # Initial button to fetch the first fact
    put_buttons(
        [{"label": "Click me for a fun fact!", "value": "new_fact", "color": "success"}],
        onclick=lambda _: get_fun_fact()
    )
    hold()
