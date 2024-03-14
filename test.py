from handler.chatgpt_selenium_automation import ChatGPTAutomation
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
# Define the path where the chrome driver is installed on your computer
chrome_driver_path = r"C:\Users\amams\OneDrive\Desktop\chromedriver.exe"

# the sintax r'"..."' is required because the space in "Program Files" 
# in my chrome_path
chrome_path = r'"E:\Downloads\chrome-win64\chrome-win64\chrome.exe"'

# Create an instance
chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)

# Define a prompt and send it to chatGPT
prompt = "What are the benefits of exercise?"
chatgpt.send_prompt_to_chatgpt(prompt)

# Retrieve the last response from chatGPT
response = chatgpt.return_last_response()
print(response)

# Save the conversation to a text file
file_name = "conversation.txt"
chatgpt.save_conversation(file_name)

# Close the browser and terminate the WebDriver session
chatgpt.quit()