from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.shop = (By.CSS_SELECTOR, "a[href*='shop']")
        self.name = (By.CSS_SELECTOR, "[name='name']")
        self.email = (By.NAME, "email")
        self.check = (By.ID, "exampleCheck1")
        self.gender= (By.ID, "exampleFormControlSelect1")
        self.submit = (By.XPATH, "//input[@value='Submit']")
        self.successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(self.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(self.name)

    def getEmail(self):
        return self.driver.find_element(self.email)

    def getCheckBox(self):
        return self.driver.find_element(self.check)

    def getGender(self):
        return self.driver.find_element(self.gender)

    def submitForm(self):
        return self.driver.find_element(self.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(self.successMessage)




