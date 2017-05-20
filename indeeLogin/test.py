# -*- coding: utf-8 -*-
"""
Created on Mon May 15 21:55:19 2017

@author: rohit
"""

#from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils import formats
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest
import random




class LoginTestCase(LiveServerTestCase):

    def setUp(self):

        self.selenium = webdriver.Chrome('C:\Python34\chromedriver.exe')
        super(LoginTestCase, self).setUp()
        self.urlSignUp = 'https://indee.tv/signup'
        self.urlSignIn = 'https://indee.tv/login'




    def tearDown(self):
        self.selenium.quit()
        super(LoginTestCase, self).tearDown()

    """
    #TC_001 :: Assert HTML Page title.
    def test_001(self):

        selenium = self.selenium
        #Opening the link we want to test
        selenium.get(self.urlSignUp)

        return selenium.title
        self.assertIn('Indee',selenium.title)

    """
    #TC_002 ::Assert Email element presence on the Registration Page.
    def test_002(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #Check the Login Page Signup Elements
        emailElement = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input').get_attribute("placeholder")

        #Assert Email ID text field
        self.assertIn('Email', emailElement)

    
    #TC_003 :: Validates Email for invalid format. i.e., "[^@]+@[^@]+\.[^@]+" is not followed.
    def test_003(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input').send_keys('abc')
            email_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/p')
            print(email_error_status1.text)
            #print(email_error_status1)
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")

            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(5)
                email_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/p')
                print(email_error_status2.text)
                self.assertIn('Please enter a valid email address',email_error_status2.text)

            except Exception as e:
                print(e)
                
    
    #TC_004 :: Validates Email for valid format. i.e., "[^@]+@[^@]+\.[^@]+" is followed.
    def test_004(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input').send_keys("abc"+str(random.randint(0,999))+"@def.com")
            email_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/p')
            email_error_status1.text
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")

            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(5)
                email_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/p')
                print(email_error_status2.text)

            except NoSuchElementException:
                print("The Input Email ID is correct")

    
    #TC_005 :: Validates already existing mail  id with the currently entered one.
    def test_005(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input').send_keys('abc@xyz.com')
            email_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/p')
            email_error_status1.text
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")

            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(10)
                email_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/p')
                print(email_error_status2.text)
                self.assertIn('This user already exists',email_error_status2.text)

            except NoSuchElementException:
                print("The Input Email ID is correct")

    
    #TC_006 :: Validate a blank Email form box.
    def test_006(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input').send_keys('xyz@abc.com')
            email_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/p')
            print(email_error_status1.text)
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")

            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                time.sleep(2)
                actions.move_to_element(selenium.find_element_by_xpath(
                            '//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input')).click()
                time.sleep(2)
                actions.send_keys(Keys.BACKSPACE * 11)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(2)
                email_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/p')
                print(email_error_status2.text)
                self.assertIn('The email field cannot be left empty.',email_error_status2.text)

            except NoSuchElementException:
                print("The Input Email ID is correct")

    
    #TC_007 :: Assert Password element presence on the Registration Page.
    def test_007(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #Check the Login Page Signup Elements
        passwordElement = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[3]/input').get_attribute("placeholder")

        #Assert Password Element in Sign Up Page
        self.assertIn('Password',passwordElement)


    #TC_008 :: Validate a invalid password of length less than 6 characters.
    def test_008(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[3]/input').send_keys('pass')
            time.sleep(2)
            password_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[4]/p')
            print(password_error_status1.text)
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")
            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.BACKSPACE)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(5)
                password_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[4]/p')
                print(password_error_status2.text)
                self.assertIn('Passwords should have minimum 6 characters.',password_error_status2.text)

            except Exception as e:
                print(e)

    #TC_009 :: Validate a valid password of length greater than or equal to 6 characters.
    def test_009(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[3]/input').send_keys('password')
            time.sleep(2)
            password_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[4]/p')
            print(password_error_status1.text)
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")
            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.SPACE)
                actions.send_keys(Keys.BACKSPACE)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(5)
                password_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[4]/p')
                print(password_error_status2.text)
                #self.assertIn('Passwords should have minimum 6 characters.',password_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)

            except Exception as e:
                print("The entered password is correct")


    #TC_010 :: Validate a blank Password form box.
    def test_010(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[3]/input').send_keys('password')
            time.sleep(2)

            password_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[4]/p')
            time.sleep(3)

        except NoSuchElementException:
            print("No such element exists")
            try:
                time.sleep(1)
                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                actions.move_to_element(selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[3]/input')).click()

                actions.send_keys(Keys.BACKSPACE*8)
                actions.perform()

                time.sleep(5)
                password_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[4]/p')
                print(password_error_status2.text)
                self.assertIn('The password field cannot be left empty.',password_error_status2.text)

            except Exception as e:
                print(e)


    #TC_011 :: Assert Confirm Password element presence on the Registration Page.
    def test_011(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #Check the Login Page Signup Elements
        emailElement = selenium.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/input").get_attribute("placeholder")
        #email = emailElement

        self.assertIn('Confirm Password',emailElement)


    #TC_012 :: Validate mismatching Password and Confirm Password fields.
    def test_012(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/input').send_keys('passwordd')
            time.sleep(2)
            selenium.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/input").click()
            password_error_status1 = selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[6]')
            print(password_error_status1.find_element_by_xpath("//p[@class='text-error regular-text']").text)
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")
            try:
                actions = ActionChains(selenium)

                actions.send_keys(Keys.BACKSPACE)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(5)
                password_error_status2 = selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[4]')
                print(password_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)
                self.assertIn('Passwords do not match',password_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)

            except Exception as e:
                print(e)

    #TC_013 :: Validate mismatching Password and Confirm Password fields.
    def test_013(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input text in the Passsword Text box
            selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[3]/input').send_keys('password')
            #Input different text in the Confirm Passsword Text box
            selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/input').send_keys('passwor')
            time.sleep(2)
            selenium.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/input").click()
            password_error_status1 = selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[6]')
            print(password_error_status1.find_element_by_xpath("//p[@class='text-error regular-text']").text)
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")
            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.BACKSPACE)
                time.sleep(2)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(5)
                password_error_status2 = selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[4]')
                print(password_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)
                self.assertIn('Passwords do not match',password_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)

            except Exception as e:
                print(e)


    #TC_014 :: Validate matching Password and Confirm Password fields.
    def test_014(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input text in the Passsword Text box
            selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[3]/input').click()
            time.sleep(1)
            selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[3]/input').send_keys('password')
            time.sleep(1)

            #Input different text in the Confirm Passsword Text box
            selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/input').click()
            time.sleep(1)
            selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/input').send_keys('password')
            time.sleep(1)
            selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/input').click()
            time.sleep(3)

            actions2 = ActionChains(selenium)
            actions2.send_keys(Keys.DELETE)
            actions2.send_keys(Keys.TAB)
            actions2.perform()
            time.sleep(3)

            #Validate Both Passwords match
            self.assertTrue(selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/i'))


        except Exception as e:
            print(e)


    #TC_015 :: Assert First Name element presence on the Registration Page.
    def test_015(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #Check the Login Page Signup Elements
        emailElement = selenium.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[7]/input").get_attribute("placeholder")
        #email = emailElement

        self.assertIn('First Name',emailElement)



    #TC_016 :: Validate a blank First Name form box.
    def test_016(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input text First Name in the Text box
            selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[7]/input').send_keys('Barry')
            selenium.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[7]/input").click()
            firstName_error_status1 = selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[8]')
            firstName_error_status1.find_element_by_xpath("//p[@class='text-error regular-text']").text
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")

            try:
                #selenium.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[7]/input").clear()
                actions = ActionChains(selenium)
                actions.send_keys(Keys.BACKSPACE*5)
                actions.perform()
                time.sleep(8)
                firstName_error_status2 = selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[8]')
                print(firstName_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)
                self.assertIn('First name cannot be left empty.',firstName_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)

            except NoSuchElementException:
                print("The Input First name is correct")

    #TC_017 :: Validate special characters/alphanumeric characters in the First Name field.
    def test_017(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[7]/input').send_keys('Basd')
            selenium.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[7]/input").click()
            firstName_error_status1 = selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[8]')
            firstName_error_status1.find_element_by_xpath("//p[@class='text-error regular-text']").text
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")

            try:

                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(8)
                firstName_error_status2 = selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[8]')
                print(firstName_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)
                #self.assertIn('First name cannot be left empty.',firstName_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)

            except NoSuchElementException:
                print("The Input First name is valid")


    #TC_018 :: Assert Last Name element presence on the Registration Page.
    def test_018(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #Check the Login Page Signup Elements
        lastName = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[9]/input').get_attribute("placeholder")

        self.assertIn('Last Name', lastName)



    #TC_019 :: Validate a blank Last Name form box.
    def test_019(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[9]/input').send_keys('Allen')
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[9]/input').click()
            lastName_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[10]')
            lastName_error_status1.find_element_by_xpath("//p[@class='text-error regular-text']").text
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")

            try:
                #selenium.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[7]/input").clear()
                actions = ActionChains(selenium)
                actions.send_keys(Keys.BACKSPACE*5)
                actions.perform()
                time.sleep(8)
                lastName_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[10]')
                print(lastName_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)
                self.assertIn('Last name cannot be left empty.',lastName_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)

            except NoSuchElementException:
                print("The Input First name is correct")

    #TC_020 :: Validate special characters/alphanumeric characters in the Last Name field.
    def test_020(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[9]/input').send_keys('Basd')
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[9]/input').click()
            lastName_error_status1 = selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[8]')
            lastName_error_status1.find_element_by_xpath("//p[@class='text-error regular-text']").text
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")

            try:
                #selenium.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[7]/input").clear()
                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(8)
                lastName_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[10]')
                print(lastName_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)
                #self.assertIn('First name cannot be left empty.',firstName_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)

            except NoSuchElementException:
                print("The Input First name is valid")


    #TC_021 :: Assert Company Name element presence on the Registration Page.
    def test_021(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #Check the Login Page Signup Elements
        companyNameElement = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[11]/input').get_attribute("placeholder")
        self.assertIn('Company Name (Optional)',companyNameElement)


    #TC_022 :: Assert Terms and Conditions Checkbox element presence on the Registration Page.
    def test_022(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #Assert Terms& Conditions Checkbox in Sign Up Page
        self.assertTrue(selenium.find_element_by_id('input-tos'))

    #TC_023 :: Validate Terms and Conditions Checkbox function
    def test_023(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #check Terms& Conditions Checkbox before selection
        self.assertFalse(selenium.find_element_by_id('input-tos').is_selected())
        time.sleep(2)

        #Click the Checkbox
        selenium.find_element_by_id('input-tos').click()
        time.sleep(2)

        #check Terms& Conditions Checkbox after selection
        self.assertTrue(selenium.find_element_by_id('input-tos').is_selected())


    #TC_024 :: Assert Sign Up button element presence on the Registration Page.
    def test_024(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)
        time.sleep(2)

        #Submit the form
        self.assertTrue(selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[13]/button'))


    #TC_025 :: Validate Sign Up Button without entering any form fields and checkbox.
    def test_025(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #Submit the form
        formSubmit = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[13]/button').click()
        time.sleep(2)

        #Check for Errors

        #Check Email ID field for error
        email_error_status = selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[2]')
        print(email_error_status.find_element_by_xpath("//p[@class='text-error regular-text']").text)
        self.assertIn('The email field cannot be left empty.',email_error_status.find_element_by_xpath("//p[@class='text-error regular-text']").text)
        self.assertTrue(email_error_status.find_element_by_xpath("//p[@class='text-error regular-text']"))
        time.sleep(1)

        #Check Password field for error
        password_error_status = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[4]/p')
        print(password_error_status.text)
        self.assertIn('The password field cannot be left empty.',password_error_status.text)
        time.sleep(1)

        #Check Confirm Password field for error
        confirmPassword_error_status = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/input')
        self.assertFalse(confirmPassword_error_status.text)
        time.sleep(1)

        #Check First Name Field for Error
        firstName_error_status = selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[8]')
        print(firstName_error_status.find_element_by_xpath("//p[@class='text-error regular-text']").text)
        self.assertTrue(firstName_error_status.find_element_by_xpath("//p[@class='text-error regular-text']").text)
        time.sleep(1)

        #Check Last Name Field for error
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[9]/input').click()
        lastName_error_status = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[10]')
        print(lastName_error_status.find_element_by_xpath("//p[@class='text-error regular-text']").text)
        self.assertTrue(lastName_error_status.find_element_by_xpath("//p[@class='text-error regular-text']"))
        time.sleep(1)


    #TC_026 :: Validate Sign Up Button with all fields entered and checkbox selected.
    def test_026(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #Enter Email ID
        selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input').send_keys("abc"+str(random.randint(0,999))+"@def.com")
        time.sleep(1)

        #Enter Password
        selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[3]/input').send_keys('password')
        time.sleep(1)

        #Enter Confirm Password
        selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/input').send_keys('password')
        time.sleep(1)

        #Check First Name Field for Error
        selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[7]/input').send_keys('Barry')
        time.sleep(1)

        #Check Last Name Field for error
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[9]/input').send_keys('Allen')
        time.sleep(1)

        #Select Terms and Conditions Checkbox
        selenium.find_element_by_id('input-tos').click()
        time.sleep(1)

        #Submit the form
        formSubmit = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[13]/button').click()
        time.sleep(8)

        #Check current URl
        print(selenium.current_url)
        self.assertIn('https://indee.tv/app/projects',selenium.current_url)


    #TC_027 :: Validate Sign Up Button with all fields entered and checkbox unselected.
    def test_027(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #Enter Email ID
        selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input').send_keys("abc"+str(random.randint(0,999))+"@def.com")
        time.sleep(1)

        #Enter Password
        selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[3]/input').send_keys('password')
        time.sleep(1)

        #Enter Confirm Password
        selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/input').send_keys('password')
        time.sleep(1)

        #Check First Name Field for Error
        selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[2]/form/div[7]/input').send_keys('Barry')
        time.sleep(1)

        #Check Last Name Field for error
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[9]/input').send_keys('Allen')
        time.sleep(1)

        #Submit the form
        formSubmit = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[13]/button').click()
        time.sleep(8)

        #Check current URl
        print(selenium.current_url)
        self.assertIn(self.urlSignUp,selenium.current_url)

        #Check Sign Up button is disabled
        self.assertTrue(selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[13]/button').get_attribute("disabled"))


    #TC_028 :: Validate Sign In Link in Sign Up Page.
    def test_028(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #Check Sign In Link in Sign Up Page
        self.assertTrue(selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'))


    #TC_029 :: Validate Sign In Click redirect to Correct Page/URL
    def test_029(self):

        selenium = self.selenium
        selenium.get(self.urlSignUp)

        #Check Sign In Link href in Sign Up Page
        self.assertIn('/login',selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div[1]/a').get_attribute('href'))

        #Click on the Sign In Link and check redirected to Login Page
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div[1]/a').click()
        time.sleep(5)
        self.assertIn('https://indee.tv/login',selenium.current_url)


    #TC_030 :: Assert Email element presence on the Registration Page.
    def test_030(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)

        #Check the Login Page Signup Elements
        emailElement = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input').get_attribute("placeholder")
        #email = emailElement

        self.assertIn('Email',emailElement)


    #TC_031 :: Validates Email for invalid format. i.e., "[^@]+@[^@]+\.[^@]+" is not followed.
    def test_031(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input').send_keys('abc')
            email_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/div/p')
            print(email_error_status1.text)
            #print(email_error_status1)
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")

            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(3)
                email_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/div/p')
                print(email_error_status2.text)
                self.assertIn('Please enter a valid email address',email_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)

            except Exception as e:
                print(e)

    #TC_032 :: Validates Email for valid format. i.e., "[^@]+@[^@]+\.[^@]+" is followed.
    def test_032(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)
        try:

            #Input correct Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input').send_keys("abc"+str(random.randint(0,999))+"@def.com")
            email_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/div/p')
            email_error_status1.text
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")

            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(3)
                email_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/div/p')
                print(email_error_status2.text)

            except NoSuchElementException:
                print("The Input Email ID is correct")

    
    #TC_033 :: Assert Password element presence on the Login Page.
    def test_033(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)

        #Check the Login Page Signup Elements
        passwordElement = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/input').get_attribute("placeholder")

        self.assertIn('Password', passwordElement)

    
    #TC_034 :: Validate a invalid password of length less than 6 characters.
    def test_034(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/input').send_keys('pass')
            time.sleep(2)
            password_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/div/p')
            print(password_error_status1.text)
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")
            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(2)
                password_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/div/p')
                print(password_error_status2.text)
                self.assertIn('Passwords should have minimum 6 characters',password_error_status2.text)

            except Exception as e:
                print(e)

    #TC_035 :: Validate a valid password of length greater than or equal to 6 characters.
    def test_035(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)
        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/input').send_keys('password')
            time.sleep(2)
            password_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/div/p')
            print(password_error_status1.text)
            time.sleep(3)


        except NoSuchElementException:
            print("No such element exists")
            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(2)
                password_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/div/p')
                print(password_error_status2.text)
                #self.assertIn('Passwords should have minimum 6 characters.',password_error_status2.find_element_by_xpath("//p[@class='text-error regular-text']").text)

            except Exception as e:
                print("The entered password is correct")


    #TC_036 :: Assert Sign In Button element presence on the Login Page.
    def test_036(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)
        time.sleep(1)

        #Click on the Sign In Button
        self.assertTrue(selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[4]/button'))


    #TC_037 :: Validate Sign In Button without entering Email ID and Password.
    def test_037(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)

        #Click on the Sign In Button
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[4]/button').click()
        time.sleep(3)

        #Check for Error Messages.
        email_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/div/p')
        print(email_error_status1.text)
        self.assertTrue(email_error_status1)

        password_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/div/p')
        print(password_error_status1.text)
        self.assertTrue(password_error_status1)

        commonError_status = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/p[2]')
        print(commonError_status.text.encode('utf-8'))
        self.assertTrue(commonError_status)


    #TC_038 :: Validate Sign In Button entering Email ID and not Password.
    def test_038(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)


        #Enter Email ID
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input').send_keys("abc"+str(random.randint(0,999))+"@def.com")

        #Click on the Sign In Button
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[4]/button').click()
        time.sleep(3)

        #Check for Error Messages.

        password_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/div/p')
        print(password_error_status1.text)
        self.assertTrue(password_error_status1)

        commonError_status = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/p[2]')
        print(commonError_status.text.encode('utf-8'))
        self.assertTrue(commonError_status)


    #TC_039 :: Validate Sign In Button entering Password and not Email ID.
    def test_039(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)


        #Enter Password details
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/input').send_keys('password')

        #Click on the Sign In Button
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[4]/button').click()
        time.sleep(3)

        #Check for Error Messages.
        email_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/div/p')
        print(email_error_status1.text)
        self.assertTrue(email_error_status1)


        commonError_status = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/p[2]')
        print(commonError_status.text.encode('utf-8'))
        self.assertTrue(commonError_status)


    #TC_040 :: Validate Sign In Button entering registered Email ID and Password.
    def test_040(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)

        #Enter Email ID
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input').send_keys("e@mail.com")

        #Enter Password details
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[2]/input').send_keys('123456')

        #Click on the Sign In Button
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[4]/button').click()
        time.sleep(8)

        #Check for Page Redirection
        self.assertIn('https://indee.tv/app/projects',selenium.current_url)



    #TC_041 :: Assert Forgot Password Link presence on the Login Page.
    def test_041(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)

        #Check the Login Page Forgot Password Link
        forgotPasswordLink = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/p[1]').text
        print(forgotPasswordLink)

        self.assertIn('Forgot your password?',forgotPasswordLink)

    
    #TC_042 :: Validate Forgot Password Link when selected.
    def test_042(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)

        #Check the Login Page Forgot Password Link
        forgotPasswordLink = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/p[1]').click()
        time.sleep(3)

        #Assert Forgot Password Form
        self.assertTrue(selenium.find_element_by_class_name('forgot-pwd-holder'))
    
    #TC_043 :: Assert Email ID field in Forgot Password Form.
    def test_043(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)

        #Click the Login Page Forgot Password Link
        forgotPasswordLink = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/p[1]').click()
        time.sleep(3)

        #Assert Email ID in Forgot Password Form
        self.assertIn('Email (Username)', selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[1]/input').get_attribute("placeholder"))

    
    #TC_044 :: Validates Email for invalid format. i.e., "[^@]+@[^@]+\.[^@]+" is not followed.
    def test_044(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)

        #Click the Login Page Forgot Password Link
        forgotPasswordLink = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/p[1]').click()
        time.sleep(3)

        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[1]/input').send_keys('abc')
            email_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[1]/div/p')
            print(email_error_status1.text)
            #print(email_error_status1)
            time.sleep(2)


        except NoSuchElementException:
            print("No such element exists")

            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(3)
                email_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[1]/div/p')
                print(email_error_status2.text)
                self.assertIn('Please enter a valid email address',email_error_status2.text)

            except Exception as e:
                print(e)

    #TC_045 :: Validates Email for valid format. i.e., "[^@]+@[^@]+\.[^@]+" is followed.
    def test_045(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)

        #Click the Login Page Forgot Password Link
        forgotPasswordLink = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/p[1]').click()
        time.sleep(3)

        try:

            #Input Incorrect Email ID in the Text box
            selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[1]/input').send_keys('xyz@abc.com')
            email_error_status1 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[1]/div/p')
            print(email_error_status1.text)
            #print(email_error_status1)
            time.sleep(2)


        except NoSuchElementException:
            print("No such element exists")

            try:
                actions = ActionChains(selenium)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(3)
                email_error_status2 = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[1]/div/p')
                print(email_error_status2.text)
                self.assertIn("The entered email address is correct")

            except NoSuchElementException:
                print("The entered email id is correct")


    #TC_046 :: Assert Send Reset Link Button in Forgot Password Form.
    def test_046(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)

        #Click the Login Page Forgot Password Link
        forgotPasswordLink = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/p[1]').click()
        time.sleep(3)

        #Assert Send Reset Link Button is Forgot Password Form
        self.assertTrue(selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[2]/button'))


    #TC_047 :: Validate Send Reset Link Button without entering email ID.
    def test_047(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)

        #Click the Login Page Forgot Password Link
        forgotPasswordLink = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/p[1]').click()
        time.sleep(3)

        #Click Send Reset Link Button
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[2]/button').click()
        time.sleep(3)

        #Check for Errors
        self.assertTrue(selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[1]/div/p'))
        self.assertTrue(selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[2]/button').get_attribute("disabled"))


    #TC_048 :: Validate Send Reset Link Button entering email ID.
    def test_048(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)

        #Click the Login Page Forgot Password Link
        forgotPasswordLink = selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/p[1]').click()
        time.sleep(3)

        #Input Incorrect Email ID in the Text box
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[1]/input').send_keys('xyz@abc.com')

        #Click Send Reset Link Button
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[2]/button').click()
        time.sleep(3)

        #Assert successful mail sent event
        self.assertTrue(selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/p'))
        self.assertTrue(selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/p'))
        self.assertIn('THANK YOU',selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/form/div[2]/span').text)




    #TC_049 :: Assert Need Help Widget in Sign Up and Sign In Screens
    def test_049(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)
        time.sleep(5)

        #Assert Need Help Widget in Sign In Page
        self.assertTrue(selenium.find_element_by_xpath('//*[@id="olark-wrapper"]/button'))


        #CLick on Sign Up Link
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/a').click()
        time.sleep(5)

        #Assert Need Help Widget in Sign In Page
        self.assertTrue(selenium.find_element_by_xpath('//*[@id="olark-wrapper"]/button'))


    #TC_050 :: Validate Need Help Widget pop up on selection on both Sign Up and Sign In Screens
    def test_050(self):

        selenium = self.selenium
        selenium.get(self.urlSignIn)
        time.sleep(5)


        #Click the Need Help Widget Icon
        selenium.find_element_by_xpath('//*[@id="olark-wrapper"]/button').click()
        time.sleep(2)
        self.assertTrue(selenium.find_element_by_id('olark-container'))
        time.sleep(1)


        #CLick on Sign Up Link
        selenium.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/div/a').click()
        time.sleep(5)

        self.assertTrue(selenium.find_element_by_id('olark-container'))   
    
    


