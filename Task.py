import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Verify validation message appear when first name start with small letter 

class TestCase1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")


    def test_firstname_small_letter(self):
        driver = self.driver
        driver.get("https://phptravels.net/register")
        firstName = driver.find_element_by_name("firstname")
        firstName.send_keys("test")
        lastname = driver.find_element_by_name("lastname")
        lastname.send_keys("Test")
        phone = driver.find_element_by_name("phone")
        phone.send_keys("123456789")
        email = driver.find_element_by_name("email")
        email.send_keys("axswa@aa.com")
        password = driver.find_element_by_name("password")
        password.send_keys("123456")
        confirmPassword = driver.find_element_by_name("confirmpassword")
        confirmPassword.send_keys("123456")
        signUp = driver.find_element_by_css_selector(".signupbtn")
        signUp.submit()
        WebDriverWait(driver, 10)
        try:
            WebDriverWait(driver, 5).until(EC.title_is('My Account'))
            print("TestCase fail First name should starting with capital letter")
        except NoSuchElementException:
            return False

# Verify validation message appear when start with small letter 

class TestCase2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")


    def test_lasttname_small_letter(self):
        driver = self.driver
        driver.get("https://phptravels.net/register")
        firstName = driver.find_element_by_name("firstname")
        firstName.send_keys("Test")
        lastname = driver.find_element_by_name("lastname")
        lastname.send_keys("test")
        phone = driver.find_element_by_name("phone")
        phone.send_keys("123456789")
        email = driver.find_element_by_name("email")
        email.send_keys("aarsa1@aa.com")
        password = driver.find_element_by_name("password")
        password.send_keys("123456")
        confirmPassword = driver.find_element_by_name("confirmpassword")
        confirmPassword.send_keys("123456")
        signUp = driver.find_element_by_css_selector(".signupbtn")
        signUp.submit()
        try:
            WebDriverWait(driver, 5).until(EC.title_is('My Account'))
            print("TestCase fail lastname should starting with capital letter")
        except NoSuchElementException:
            return False


# Verify first name isn’t equal last name 
        
class TestCase3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")


    def test_firstName_equal_lastName(self):
        driver = self.driver
        driver.get("https://phptravels.net/register")
        firstName = driver.find_element_by_name("firstname")
        firstName.send_keys("Test")
        lastname = driver.find_element_by_name("lastname")
        lastname.send_keys("test")
        phone = driver.find_element_by_name("phone")
        phone.send_keys("123456789")
        email = driver.find_element_by_name("email")
        email.send_keys("aar1@aa.com")
        password = driver.find_element_by_name("password")
        password.send_keys("123456")
        confirmPassword = driver.find_element_by_name("confirmpassword")
        confirmPassword.send_keys("123456")
        signUp = driver.find_element_by_css_selector(".signupbtn")
        signUp.submit()
        try:
            if firstName.getAttribute("value") == lastname.getAttribute("value"):
                print("TestCase failed firstname shoudn't equal lastname")
        except NoSuchElementException:
            return False



# Verify user enter a valid mobile number 

class TestCase4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")


    def test_phone_short(self):
        driver = self.driver
        driver.get("https://phptravels.net/register")
        firstName = driver.find_element_by_name("firstname")
        firstName.send_keys("Test")
        lastname = driver.find_element_by_name("lastname")
        lastname.send_keys("test")
        phone = driver.find_element_by_name("phone")
        phone.send_keys("123456789")
        email = driver.find_element_by_name("email")
        email.send_keys("aa3@aa.com")
        password = driver.find_element_by_name("password")
        password.send_keys("123456")
        confirmPassword = driver.find_element_by_name("confirmpassword")
        confirmPassword.send_keys("123456")
        signUp = driver.find_element_by_css_selector(".signupbtn")
        signUp.submit()
        try:
            if phone.getAttribute("value") < 3 :
                print("phone is short")
        except NoSuchElementException:
            return False


# Verify user enter a valid email 

class TestCase5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")


    def test_email(self):
        driver = self.driver
        driver.get("https://phptravels.net/register")
        firstName = driver.find_element_by_name("firstname")
        firstName.send_keys("Test")
        lastname = driver.find_element_by_name("lastname")
        lastname.send_keys("test")
        phone = driver.find_element_by_name("phone")
        phone.send_keys("123456789")
        email = driver.find_element_by_name("email")
        email.send_keys("a1@aa.com")
        password = driver.find_element_by_name("password")
        password.send_keys("123456")
        confirmPassword = driver.find_element_by_name("confirmpassword")
        confirmPassword.send_keys("123456")
        signUp = driver.find_element_by_css_selector(".signupbtn")
        signUp.submit()
        try:
            email.getAttribute(contains(translate(text(),@)))
        except NoSuchElementException:
            return False
        

# Verify password is matched 

class TestCase6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")


    def test_password_equal_confirm_password(self):
        driver = self.driver
        driver.get("https://phptravels.net/register")
        firstName = driver.find_element_by_name("firstname")
        firstName.send_keys("Test")
        lastname = driver.find_element_by_name("lastname")
        lastname.send_keys("test")
        phone = driver.find_element_by_name("phone")
        phone.send_keys("123456789")
        email = driver.find_element_by_name("email")
        email.send_keys("aar1@aa.com")
        password = driver.find_element_by_name("password")
        password.send_keys("123456")
        confirmPassword = driver.find_element_by_name("confirmpassword")
        confirmPassword.send_keys("123456")
        signUp = driver.find_element_by_css_selector(".signupbtn")
        signUp.submit()
        try:
            if password.getAttribute("value") != confirmPassword.getAttribute("value"):
                print("TestCase failed ")
        except NoSuchElementException:
            return False
        
# Verify user is successfully login after entering a valid data  

class TestCase7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")


    def test_login_succed(self):
        driver = self.driver
        driver.get("https://phptravels.net/register")
        firstName = driver.find_element_by_name("firstname")
        firstName.send_keys("Test")
        lastname = driver.find_element_by_name("lastname")
        lastname.send_keys("test")
        phone = driver.find_element_by_name("phone")
        phone.send_keys("123456789")
        email = driver.find_element_by_name("email")
        email.send_keys("aar1@aa.com")
        password = driver.find_element_by_name("password")
        password.send_keys("123456")
        confirmPassword = driver.find_element_by_name("confirmpassword")
        confirmPassword.send_keys("123456")
        signUp = driver.find_element_by_css_selector(".signupbtn")
        signUp.submit()
        try:
            WebDriverWait(driver, 5).until(EC.title_is('My Account'))
            print("TestCase succeed")
        except NoSuchElementException:
            return False
        



    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()


