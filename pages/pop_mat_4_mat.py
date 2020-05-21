# -*- coding: utf-8 -*-
import logging
from selenium.webdriver.support.select import Select

class MainMat4Mat:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.range_of_calculations_xpath = "//*[@id='sel1']"
        self.type_off_calculation_xpath = "//*[@id='sel2']"
        self.gen_button_xpath = "//*[@id='footer_buttons']/button[1]"
        self.check_button_xpath = "//*[@id='footer_buttons']/button[2]"

    def correct_result(self):
        z = 0
        for i in range(8):
            y = self.driver.find_element_by_xpath("//*[@id='face" + str(i + 1) + "']").text
            if (y == "😀"):
                z = z + 1
        assert z == 8, "Błędna ilość prawidłowych obliczeń"

    def incorrect_result(self):
        z = 0
        for i in range(8):
            y = self.driver.find_element_by_xpath("//*[@id='face" + str(i + 1) + "']").text
            if (y == "😕"):
                z = z + 1
        assert z == 8, "Błędna ilość nie prawidłowych obliczeń"

    def adding_0_10_correct_answers(self):
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 10, podaje wynik prawidłowy")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_"+ str(i+1)+"").text
            v2 = self.driver.find_element_by_id("second_value_"+ str(i+1)+"").text
            v3 = int(v1)+int(v2)
            self.driver.find_element_by_id("ans"+ str(i+1)+"").send_keys(v3)
            if i == 7:
                self.logger.info("{value1} + {value2} = {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def adding_0_10_empty_answers(self):
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 10, nie podaje żadnego wyniku")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def adding_0_10_different_characters(self):
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 10, podaje wynik prawidłowy z zapisem wyniku za pomocą kropki i 1 miejsca po przecinku (np.: 6.0)")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        v3 = ["abc", "ABC", "!", "@", "AbC", "1abc", "abc1", "#"]
        for i in range(8):
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3[i])
            self.logger.info("Podaje wartość {}".format(v3[i]))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def adding_0_10_correct_answers_dot_and_coma(self):
        global v5
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 10, podaje wynik prawidłowy z zapisem wyniku za pomocą kropki i 1 miejsca po przecinku")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        number_of_0="0"
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_"+ str(i+1)+"").text
            v2 = self.driver.find_element_by_id("second_value_"+ str(i+1)+"").text
            v3 = int(v1)+int(v2)
            x = number_of_0.zfill(i)
            if i < 4:
                v3_str = str(v3) + "."
                v4 = v3_str + x
                self.driver.find_element_by_id("ans"+ str(i+1)+"").send_keys(v4)
                if i == 0:
                    v4_len = len(v4)
                    v4 = v4[0: v4_len - 1]
                if i == 4:
                    self.logger.info("{value1} + {value2} = {result}".format(value1=v1, value2=v2, result=v4))
            else:
                v3_str = str(v3) + ","
                v4 = v3_str + x
                if i > 4:
                    v4_len = len(v4)
                    v4 = v4[0: v4_len - 5]
                self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v4)
                if i == 4:
                    self.logger.info("{value1} + {value2} = {result}".format(value1=v1, value2=v2, result=v4))

    def adding_0_10_correct_answers_space_before_and_after_result(self):
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 10, podaje wynik prawidłowy ze spacją przed wynikiem")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_"+ str(i+1)+"").text
            v2 = self.driver.find_element_by_id("second_value_"+ str(i+1)+"").text
            v3 = int(v1)+int(v2)
            v3_str = str(v3)
            if i <4:
                v4 = " " + v3_str
            else:
                v4 = v3_str + " "
            self.driver.find_element_by_id("ans"+ str(i+1)+"").send_keys(v4)
            if i == 3 or i == 7:
                self.logger.info("{value1} + {value2} = {result}".format(value1=v1, value2=v2, result=v4))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def adding_0_10_correct_answers_space_after_result(self):
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 10, podaje wynik prawidłowy ze spacją po wyniku")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_"+ str(i+1)+"").text
            v2 = self.driver.find_element_by_id("second_value_"+ str(i+1)+"").text
            v3 = int(v1)+int(v2)
            v3_str = str(v3)
            v4 = v3_str + " "
            self.driver.find_element_by_id("ans"+ str(i+1)+"").send_keys(v4)
            if i == 7:
                self.logger.info("{value1} + {value2} = {result}".format(value1=v1, value2=v2, result=v4))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def adding_0_10_correct_answers_dot_2_place(self):
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 10, podaje wynik prawidłowy z zapisem wyniku za pomocą kropki i 2 zerami. ")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_"+ str(i+1)+"").text
            v2 = self.driver.find_element_by_id("second_value_"+ str(i+1)+"").text
            v3 = int(v1)+int(v2)
            v3_str = str(v3)
            v4 = v3_str + ".00"
            self.driver.find_element_by_id("ans"+ str(i+1)+"").send_keys(v4)
            if i == 7:
                self.logger.info("{value1} + {value2} = {result}".format(value1=v1, value2=v2, result=v4))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def adding_0_10_correct_answers_comma_1_place(self):
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 10, podaje wynik prawidłowy z zapisem wyniku za pomocą przecinka i 1 miejsca po przecinku")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            v3 = int(v1) + int(v2)
            v3_str = str(v3)
            v4 = v3_str + ",0"
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v4)
            if i == 7:
                self.logger.info("{value1} plus {value2} = {result}".format(value1=v1, value2=v2, result=v4))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def adding_0_10_invalid_equivalence_class(self):
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 10, podaje wynik nieprawidłowy, 4 pierwsze wyniki powiększone o pozostałe 4 pomniejszone o 1.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            if i <4:
                v3 = int(v1) + int(v2) + 1
            else:
                v3 = int(v1) + int(v2) - 1
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            if i == 3 or i == 7:
                self.logger.info("{value1} + {value2} != {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def adding_0_50_correct_answers(self):
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 50, podaje wynik prawidłowy.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("50")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            v3 = int(v1) + int(v2)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            self.logger.info("{value1} + {value2} = {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def adding_0_50_invalid_equivalence_class(self):
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 50, podaje wynik nieprawidłowy, 4 pierwsze wyniki powiększone o pozostałe 4 pomniejszone o 1")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("50")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            if i < 4:
                v3 = int(v1) + int(v2) + 1
            else:
                v3 = int(v1) + int(v2) - 1
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            if i == 3 or i == 7:
                self.logger.info("{value1} + {value2} != {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def adding_0_100_correct_answers(self):
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 100, podaje wynik prawidłowy.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("100")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            v3 = int(v1) + int(v2)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            self.logger.info("{value1} + {value2} = {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def adding_0_100_invalid_equivalence_class(self):
        self.logger.info("Użytkownik dodaje 2 liczb, od 0 do 100, podaje wynik nieprawidłowy, 4 pierwsze wyniki powiększone o pozostałe 4 pomniejszone o 1")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("100")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("+")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            if i < 4:
                v3 = int(v1) + int(v2) + 1
            else:
                v3 = int(v1) + int(v2) - 1
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            if i == 3 or i == 7:
                self.logger.info("{value1} - {value2} != {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def subtraction_0_10_correct_answers(self):
        self.logger.info("Użytkownik odejmuje 2 liczb, od 0 do 10, podaje wynik prawidłowy.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("-")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            v3 = int(v1) - int(v2)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            self.logger.info("{value1} - {value2} = {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def subtraction_0_10_invalid_equivalence_class(self):
        self.logger.info("Użytkownik odejmuje 2 liczb, od 0 do 10, podaje wynik nieprawidłowy, 4 pierwsze wyniki powiększone o pozostałe 4 pomniejszone o 1")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("-")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            if i < 4:
                v3 = int(v1) - int(v2) + 1
            else:
                v3 = int(v1) - int(v2) - 1
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            if i == 3 or i == 7:
                self.logger.info("{value1} - {value2} != {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def subtraction_0_50_correct_answers(self):
        self.logger.info("Użytkownik odejmuje 2 liczb, od 0 do 50, podaje wynik prawidłowy.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("50")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("-")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            v3 = int(v1) - int(v2)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            self.logger.info("{value1} - {value2} = {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def subtraction_0_50_invalid_equivalence_class(self):
        self.logger.info("Użytkownik odejmuje 2 liczb, od 0 do 50, podaje wynik nieprawidłowy, 4 pierwsze wyniki powiększone o pozostałe 4 pomniejszone o 1")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("50")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("-")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            if i < 4:
                v3 = int(v1) - int(v2) + 1
            else:
                v3 = int(v1) - int(v2) - 1
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            if i == 3 or i == 7:
                self.logger.info("{value1} - {value2} != {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def subtraction_0_100_correct_answers(self):
        self.logger.info("Użytkownik odejmuje 2 liczb, od 0 do 100, podaje wynik prawidłowy.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("100")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("-")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            v3 = int(v1) - int(v2)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            self.logger.info("{value1} - {value2} = {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def subtraction_0_100_invalid_equivalence_class(self):
        self.logger.info("Użytkownik odejmuje 2 liczb, od 0 do 100, podaje wynik nieprawidłowy, 4 pierwsze wyniki powiększone o pozostałe 4 pomniejszone o 1")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("100")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("-")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            if i < 4:
                v3 = int(v1) - int(v2) + 1
            else:
                v3 = int(v1) - int(v2) - 1
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            if i == 3 or i == 7:
                self.logger.info("{value1} - {value2} != {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def multiplication_0_10_correct_answers(self):
        self.logger.info("Użytkownik mnoży 2 liczb, od 0 do 10, podaje wynik prawidłowy.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("*")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            v3 = int(v1) * int(v2)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            if i == 7:
                self.logger.info("{value1} * {value2} = {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def multiplication_0_10_invalid_equivalence_class(self):
        self.logger.info("Użytkownik mnoży 2 liczb, od 0 do 10 podaje wynik nieprawidłowy, 4 pierwsze wyniki powiększonych o pozostałe 4 pomniejszone o 1.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("*")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            if i < 4:
                v3 = int(v1) * int(v2) + 1
            else:
                v3 = int(v1) * int(v2) - 1
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            if i == 3 or i == 7:
                self.logger.info("{value1} * {value2} != {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def multiplication_0_50_correct_answers(self):
        self.logger.info("Użytkownik mnoży 2 liczb, od 0 do 50, podaje wynik prawidłowy.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("50")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("*")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            v3 = int(v1) * int(v2)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            if i == 7:
                self.logger.info("{value1} * {value2} = {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def multiplication_0_50_invalid_equivalence_class(self):
        self.logger.info("Użytkownik mnoży 2 liczb, od 0 do 50 podaje wynik nieprawidłowy, 4 pierwsze wyniki powiększonych o pozostałe 4 pomniejszone o 1.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("50")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("*")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            if i < 4:
                v3 = int(v1) * int(v2) + 1
            else:
                v3 = int(v1) * int(v2) - 1
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            if i == 3 or i == 7:
                self.logger.info("{value1} * {value2} != {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def multiplication_0_100_correct_answers(self):
        self.logger.info("Użytkownik mnoży 2 liczb, od 0 do 100, podaje wynik prawidłowy.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("100")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("*")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            v3 = int(v1) * int(v2)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            if i == 7:
                self.logger.info("{value1} * {value2} = {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def multiplication_0_100_invalid_equivalence_class(self):
        self.logger.info("Użytkownik mnoży 2 liczb, od 0 do 100 podaje wynik nieprawidłowy, 4 pierwsze wyniki powiększonych o pozostałe 4 pomniejszone o 1.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("100")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("*")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            if i < 4:
                v3 = int(v1) * int(v2) + 1
            else:
                v3 = int(v1) * int(v2) - 1
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v3)
            if i == 3 or i == 7:
                self.logger.info("{value1} * {value2} != {result}".format(value1=v1, value2=v2, result=v3))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def division_0_10_correct_answers(self):
        self.logger.info("Użytkownik dzieli 2 liczb, od 0 do 10, podaje wynik prawidłowy.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("/")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            v3 = int(v1) / int(v2)
            v4 = round(v3, 2)
            v5 = str(v4)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v5)
            if i == 7:
                self.logger.info("{value1} / {value2} = {result}".format(value1=v1, value2=v2, result=v5))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)


    def division_0_10_invalid_equivalence_class(self):
        self.logger.info("Użytkownik dzieli 2 liczb, od 0 do 10 podaje wynik nieprawidłowy,  4 pierwsze wyniki powiększonych o pozostałe 4 pomniejszone o 1.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("10")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("/")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            if i < 4:
                v3 = int(v1) / int(v2) +1
            else:
                v3 = int(v1) / int(v2) - 1
            v4 = round(v3, 2)
            v5 = str(v4)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v5)
            if i == 3 or i == 7:
                self.logger.info("{value1} / {value2} != {result}".format(value1=v1, value2=v2, result=v5))
            self.driver.find_element_by_xpath(self.check_button_xpath).click()
            MainMat4Mat.incorrect_result(self)

    def division_0_50_correct_answers(self):
        self.logger.info("Użytkownik dzieli 2 liczb, od 0 do 50 podaje wynik nieprawidłowy,  4 pierwsze wyniki powiększonych o pozostałe 4 pomniejszone o 1.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("50")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("/")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            v3 = int(v1) / int(v2)
            v4 = round(v3, 2)
            v5 = str(v4)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v5)
            if i == 7:
                self.logger.info("{value1} / {value2} = {result}".format(value1=v1, value2=v2, result=v5))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)
        

    def division_0_50_invalid_equivalence_class(self):
        self.logger.info("Użytkownik dzieli 2 liczb, od 0 do 100 podaje wynik nieprawidłowy,  4 pierwsze wyniki powiększonych o pozostałe 4 pomniejszone o 1.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("50")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("/")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            if i < 4:
                v3 = int(v1) / int(v2) + 1
            else:
                v3 = int(v1) / int(v2) - 1
            v4 = round(v3, 2)
            v5 = str(v4)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v5)
            if i == 3 or i == 7:
                self.logger.info("{value1} / {value2} != {result}".format(value1=v1, value2=v2, result=v5))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

    def division_0_100_correct_answers(self):
        self.logger.info("Użytkownik dzieli 2 liczb, od 0 do 100, podaje wynik prawidłowy.")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("100")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("/")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            v3 = int(v1) / int(v2)
            v4 = round(v3, 2)
            v5 = str(v4)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v5)
            if i == 7:
                self.logger.info("{value1} / {value2} = {result}".format(value1=v1, value2=v2, result=v5))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.correct_result(self)

    def division_0_100_invalid_equivalence_class(self):
        self.logger.info("Użytkownik dzieli 2 liczb, od 0 do 100 podaje wynik nieprawidłowy, powiększony o 1")
        Select(self.driver.find_element_by_xpath(self.range_of_calculations_xpath)).select_by_value("100")
        Select(self.driver.find_element_by_xpath(self.type_off_calculation_xpath)).select_by_value("/")
        self.driver.find_element_by_xpath(self.gen_button_xpath).click()
        for i in range(8):
            v1 = self.driver.find_element_by_id("first_value_" + str(i + 1) + "").text
            v2 = self.driver.find_element_by_id("second_value_" + str(i + 1) + "").text
            if i < 4:
                v3 = int(v1) / int(v2) + 1
            else:
                v3 = int(v1) / int(v2) - 1
            v4 = round(v3, 2)
            v5 = str(v4)
            self.driver.find_element_by_id("ans" + str(i + 1) + "").send_keys(v5)
            if i == 3 or i == 7:
                self.logger.info("{value1} / {value2} != {result}".format(value1=v1, value2=v2, result=v5))
        self.driver.find_element_by_xpath(self.check_button_xpath).click()
        MainMat4Mat.incorrect_result(self)

