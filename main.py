from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time

# generate all dates within a range
def generate_dates(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date.strftime("%d.%m.%Y")
        current_date += timedelta(days=1)

# run browser
driver = webdriver.Chrome()

# Open website Telc
driver.get("https://results.telc.net/")

# Input birthday
dob_input = driver.find_element(By.ID, "input-17")
dob_input.send_keys("dd.mm.yyyy") # your birthday here

# range of Attendee ID (use yours numbers [in my case was 7 numbers])
start_number = 0000000
end_number = 0000000

# range of Issue date (use your date)
# use start date for date of your exam and end date for current date
start_date = datetime.strptime("dd.mm.yyyy", "%d.%m.%Y")
end_date = datetime.strptime("dd.mm.yyyy", "%d.%m.%Y")

# loop for every Attendee ID
for participant_num in range(start_number, end_number + 1):
    # formating to put 0 before the start number (if require)
    formatted_participant_num = f"{participant_num:07d}"

    # find field for Attendee ID
    participant_input = driver.find_element(By.ID, "input-13")

    # clean the field (Ctrl + A і Backspace)
    participant_input.send_keys(Keys.CONTROL, 'a')
    participant_input.send_keys(Keys.BACKSPACE)

    # send new ID
    participant_input.send_keys(formatted_participant_num)

    # loop for every date
    for check_date in generate_dates(start_date, end_date):
        # find a date field
        date_input = driver.find_element(By.ID, "input-21")

        # clean the field (Ctrl + A і Backspace)
        date_input.send_keys(Keys.CONTROL, 'a')
        date_input.send_keys(Keys.BACKSPACE)

        # send new date
        date_input.send_keys(check_date)

        # find button with class (no id there)
        submit_button = driver.find_element(By.CLASS_NAME, "c-button")
        submit_button.click()

        # waiting time for new try
        time.sleep(1)

# close browser
driver.quit()
