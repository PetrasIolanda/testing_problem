from selenium.webdriver import Chrome, ChromeOptions
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


EXPECTED_COLOR = "rgba(222, 20, 33, 1)"

def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(0.3)

options = ChromeOptions().add_argument("--user-data-dir=<101.0.4951.54>")

browser = Chrome(chrome_options=options)
browser.get('https://politrip.com/')

time.sleep(1)

# to accept cookie notification so that it doesn't interfere
cookie_cta = browser.find_element(By.ID, 'cookiescript_accept')
cookie_cta.click()

# Navigate to Signup Page
button = browser.find_element(By.ID, 'qa_header-signup')
button.click()

time.sleep(1)

def check_color(color, orginal_color):
   return color == orginal_color

# Fill user's first name
username = browser.find_element(By.ID, 'first-name')
if "error" in username.get_attribute('outerHTML'):
   obtained_color = username.value_of_css_property('border-bottom-color')
   if not check_color(obtained_color, "rgba(222, 20, 33, 1)"):
      print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")
# username.send_keys('Iolanda')
slow_typing(username, 'Iolanda')

time.sleep(1)

# Fill user's last name
username = browser.find_element(By.ID, 'last-name')
if "error" in username.get_attribute('outerHTML'):
   obtained_color = username.value_of_css_property('border-bottom-color')
   if not check_color(obtained_color, "rgba(222, 20, 33, 1)"):
      print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")
# username.send_keys('Petras')
slow_typing(username, 'Petras')

time.sleep(1)
# Fill user's email ID
email = browser.find_element(By.ID, 'email')
if "error" in email.get_attribute('outerHTML'):
   obtained_color = email.value_of_css_property('border-bottom-color')
   if not check_color(obtained_color, "rgba(222, 20, 33, 1)"):
      print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")
slow_typing(email, 'petras_iolanda@yahoo.com')

time.sleep(1)
# Fill user's password
password = browser.find_element(By.ID, 'sign-up-password-input')
if "error" in password.get_attribute('outerHTML'):
   obtained_color = password.value_of_css_property('border-bottom-color')
   if not check_color(obtained_color, "rgba(222, 20, 33, 1)"):
      print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")
slow_typing(password, "IolandaP24")

# Fill confirm password
password1 = browser.find_element(By.ID, 'sign-up-confirm-password-input')
if "error" in password.get_attribute('outerHTML'):
   obtained_color = password.value_of_css_property('border-bottom-color')
   if not check_color(obtained_color, "rgba(222, 20, 33, 1)"):
      print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")
slow_typing(password1, "IolandaP24")
time.sleep(1)

error_messages = ["This field can not be empty", "Please enter a valid email adress", "Password must contain at least 8 characters, 1 uppercase letter, 1 lowercase letter and 1 digit"]
message_body_html_elements = browser.find_elements(By.CLASS_NAME, 'msg-body')
for msg in message_body_html_elements:
   error_msg = msg.get_attribute('innerHTML').split("span")[1][1:-2]
   if error_msg not in error_messages:
      print(f"{msg.get_attribute('outerHTML')} is missing error message")

#How did you hear about us
select = Select(browser.find_element(By.ID,'sign-up-heard-input'))
select.select_by_value('webSearch')

# click on signup page
button = browser.find_element(By.CLASS_NAME, 'button-label')
button.click()


print(browser.title)
