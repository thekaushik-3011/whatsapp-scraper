# WhatsApp Scraper

This project utilizes the Selenium library to scrape specific WhatsApp chat data, which you provide. The program automates the process of opening the Chrome browser, navigating to WhatsApp Web, but you have to log in by scanning the QR code for the first time.

Once logged in, it accesses your desired chat and scrolls through the chat history (the number of times can be adjusted) to gather the following data:

1. **Message**: The content of each message.
2. **Time**: The time at which each message was sent.
3. **Date**: The date on which each message was sent.
4. **Sender**: The sender of each message.

The scraped data is then stored in CSV format. You can perform various operations on the dataset generated, depending on your requirements.

## How to Use

1. Ensure you have Google Chrome installed on your machine.
2. Clone this repository to your local machine.
3. Install the necessary dependencies {Python: 3.12.2, Selenium: 4.1.0, tqdm: 4.66.2}.
4. Run the `whatsapp_scraper.py` script.
5. Scan the QR code displayed in the Chrome browser to log in to WhatsApp Web.
6. Specify the chat you want to scrape.
7. Wait for the program to finish scraping the chat data.
8. Find the generated CSV file containing the scraped data in the project directory.

## Customization

You can customize the behavior of the scraper by adjusting parameters such as the number of times to scroll through the chat history or modifying the data extraction process according to your needs.

## Dependencies

- Selenium
- ChromeDriver (Ensure compatibility with your Chrome browser version)
