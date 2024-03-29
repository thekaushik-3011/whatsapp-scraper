import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from tqdm import tqdm

# Path to the chromedriver executable
chromedriver_path = 'chromedriver.exe'

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("user-data-dir=C:/Users/salla/AppData/Local/Google/Chrome/User Data/Kaushik")

# Initialize Chrome WebDriver with options
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Navigate to the WhatsApp Web URL
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 100)
# print("Scan the QR code to log in to WhatsApp Web.")
sleep(2)

# Fix the XPath expression by wrapping the target variable with quotes
target = '"Nishant Bhatija"'
contact_path = f'//span[contains(@title, {target})]'
contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
contact.click()

def scroll_chat_step_by_step():
    message_elements_in = driver.find_elements(By.CLASS_NAME, "message-in")
    message_elements_out = driver.find_elements(By.CLASS_NAME, "message-out")
    
    # Get the last message element
    last_message_element = message_elements_in[-1] if message_elements_in else message_elements_out[-1]
    
    # Scroll to the last message element
    driver.execute_script("arguments[0].scrollIntoView();", last_message_element)

# Extract the chat messages with date and time
chat_data = []
total_messages = 0

# Get the total number of messages
while True:
    message_elements_in = driver.find_elements(By.CLASS_NAME, "message-in")
    message_elements_out = driver.find_elements(By.CLASS_NAME, "message-out")
    new_total_messages = len(message_elements_in) + len(message_elements_out)
    if new_total_messages == total_messages:
        break
    total_messages = new_total_messages
    scroll_chat_step_by_step()
    sleep(1)

# Scroll and extract messages with loading bar
for _ in tqdm(range(10), desc="Extracting messages", unit="scroll"):
    message_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "message")]')

    for message_element in message_elements:
        message_text = message_element.find_element(By.CLASS_NAME, "selectable-text").text
        message_time_element = message_element.find_element(By.CLASS_NAME, "copyable-text")
        message_time = message_time_element.get_attribute("data-pre-plain-text").split(']')[0].strip('[')
        message_time, message_date = message_time.split(',')

        # Determine the sender
        message_classes = message_element.get_attribute("class")
        if "message-out" in message_classes:
            sender = "Me"
        else:
            sender = target

        chat_data.append([message_text, message_time.strip(), message_date.strip(), sender])
    
    scroll_chat_step_by_step()
    sleep(2)

# Write the chat data to a CSV file
csv_filename = 'chat_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Message', 'Time', 'Date', 'Sender'])
    writer.writerows(chat_data)
print(f"Chat data has been exported to {csv_filename}")

# Close the browser window
driver.quit()