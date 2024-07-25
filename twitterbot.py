import os, re, time, requests
from bardapi import Bard
from bs4 import BeautifulSoup
# import for webdriver 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# imports for enduring loading of elements
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class InstagramBot:

    def __init__(self, email, password, username):

        self.email = email
        self.password = password
        self.username = username
        # initializing chrome options
        chrome_options = Options()
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        # Remove headless mode
        #chrome_options.add_argument('--headless') 
        #chrome_options.add_experimental_option("detach", True)
        # adding the path to the chrome driver and
        # integrating chrome_options with the bot
        self.bot = webdriver.Chrome(
            options = chrome_options
        )

    def gmail_login(self):
        bot = self.bot

        bot.get('https://accounts.google.com/InteractiveLogin/identifier?elo=1&ifkv=AXo7B7VxCqTIv7hm_EaXQzOlN1eay0eadANf_SgDGVaLoWHGG-BRZxX2609devJZuSSkux6wdJccXA&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

        login_elements = {"email": ['//*[@id ="identifierId"]', self.email],
                         "next": '//*[@id="identifierNext"]',
                    "password": ['//*[@id ="password"]/div[1]/div / div[1]/input', self.password],
                    "pwnext": '//*[@id="passwordNext"]'
                    }
        
        timeout = 10
        try:
            # find the username box and enter the username
            element_present = EC.presence_of_element_located((By.XPATH, login_elements['email'][0]))
            WebDriverWait(bot, timeout).until(element_present)
            loginBox = bot.find_element(By.XPATH, login_elements['email'][0])
            loginBox.send_keys(login_elements['email'][1])
            print("Getting next button")
            nextButton = bot.find_element(By.XPATH, login_elements['next'])
            print("Clicking next button")
            nextButton.click()

            # find the password box and enter our password
            element_present = EC.presence_of_element_located((By.XPATH, login_elements['password'][0]))
            WebDriverWait(bot, timeout).until(element_present)
            print("Getting password input")
            passWordBox = bot.find_element(By.XPATH, login_elements['password'][0])
            print("Sending password input")
            passWordBox.send_keys(login_elements['password'][1])

            # click the next / login button
            print("Getting next button")
            nextButton =  bot.find_element(By.XPATH, login_elements['pwnext'])
            print("Clicking next button")
            nextButton.click()
            
            element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]'))
            WebDriverWait(bot, timeout).until(element_present)
            privacy_message = bot.find_element(By.XPATH, '//*[@id="yDmH0d"]')
            
            time.sleep(5)
            print('Login Successful...!!')

        except TimeoutException:
                print ("Timed out waiting for page to load")

        except Exception as e:
            print(f'Login Failed Error: {e}')


    def random_delay(self, min_delay=2, max_delay=5):
        time.sleep(random.uniform(min_delay, max_delay))

    def simulate_typing(self, element, text):
        for char in text:
            element.send_keys(char)
            self.random_delay(0.1, 0.3)

    def random_mouse_movements(self):
        actions = ActionChains(self.bot)
        self.bot.maximize_window()  # Maximize the window to ensure movements stay within bounds
        window_size = self.bot.get_window_size()
        width = window_size['width']
        height = window_size['height']
        
        for _ in range(random.randint(5, 10)):
            x_offset = random.randint(0, width - 1)
            y_offset = random.randint(0, height - 1)
            actions.move_by_offset(x_offset, y_offset)
            actions.perform()
            actions.reset_actions()  # Reset actions to avoid cumulative offsets
            self.random_delay(0.5, 1.5)

    def instagram_login(self):
        """
            Method for signing in the user
            with the provided email and password.
        """
        bot = self.bot

        timeout = 100

        # fetches the login page
        bot.get('https://www.instagram.com/accounts/login/')
        self.random_delay(3, 5)

        # Simulate random mouse movements
        self.random_mouse_movements()

        login_elements = {
            "username": ['//*[@name="username"]', self.username],
            "password": ['//*[@name="password"]', self.password]
        }

        for key, value in login_elements.items():  # for username, password
            try:
                element_present = EC.presence_of_element_located((By.XPATH, value[0]))
                WebDriverWait(bot, timeout).until(element_present)
                login_element = bot.find_element(By.XPATH, value[0])
                self.simulate_typing(login_element, value[1])
                self.random_delay(1, 2)
            except TimeoutException:
                print("Timed out waiting for page to load")
            except Exception as e:
                print(e)
                print("Cannot find element")
                continue

        try:
            element_present = EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"]'))
            WebDriverWait(bot, timeout).until(element_present)
            login_button = bot.find_element(By.XPATH, '//*[@type="submit"]')
            self.random_delay(1, 3)
            login_button.click()
            print("Clicked login button")
        except TimeoutException:
            print("Timed out waiting for login button to be clickable")
        except Exception as e:
            print(e)
            print("Cannot find login button")

        self.random_delay(5, 7)


    def join_livestream(self, user_url):
        bot = self.bot
        bot.get(user_url)

        timeout = 10

        try:
            # Wait for the profile picture element to be clickable
            element_present = EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[1]/div/div/div[1]/div[1]/svg/circle[1]'))
            WebDriverWait(bot, timeout).until(element_present)
            profile_picture = bot.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[1]/div/div/div[1]/div[1]/svg/circle[1]')
            profile_picture.click()
            print("Clicked on the profile picture to join the live stream")
        except TimeoutException:
            print("Timed out waiting for profile picture to be clickable")
        except Exception as e:
            print(f'Error clicking profile picture: {e}')
