import time
from io import BytesIO

from undetected_chromedriver import Chrome, options
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


from utils import get_captcha


URL = "https://www.vfsvisaservicesrussia.com/Global-Appointment/Account/RegisteredLogin?q=shSA0YnE4pLF9Xzwon/x/BGxVUxGuaZP3eMAtGHiEL0kQAXm+Lc2PfVNUJtzf7vWRu19bwvTWMZ48njgDU5r4g=="

chrome_options = options.ChromeOptions()
chrome_options.add_argument("--disable-javascript")
driver = Chrome(options=chrome_options)


while True:
    driver.get(URL)
    email = driver.find_element(By.ID, "EmailId")
    password = driver.find_element(By.ID, "Password")

    email.send_keys("travelvisabot@gmail.com")
    password.send_keys("Tvb2022!")

    captcha = driver.find_element(By.ID, "CaptchaImage")
    bytes_image = captcha.screenshot_as_png

    image = Image.open(BytesIO(bytes_image))
    captcha_text = get_captcha(image)

    captcha_input = driver.find_element(By.ID, "CaptchaInputText")
    captcha_input.send_keys(captcha_text)

    form_button = driver.find_element(By.ID, "btnSubmit")
    form_button.click()

    time.sleep(10)
    
    try:
        error = driver.find_element(By.CLASS_NAME, "validation-summary-errors")
        if error:
            time.sleep(120)
    except:
        pass

    try:
        ul_left_navbar = driver.find_element(By.CLASS_NAME, "leftNav-ul")
    except NoSuchElementException:
        continue
    break

form_button = driver.find_element(By.CLASS_NAME, "leftNav-ul")
zapis = form_button.find_element(By.CLASS_NAME, "inactive-link")
zapis.click()