import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.pop_mat_4_mat import MainMat4Mat

class TestMat_4_Mat_ref:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_adding_0_10_correct_answers(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        adding_0_10 = MainMat4Mat(self.driver)
        adding_0_10.adding_0_10_correct_answers()

    def test_adding_0_10_empty_answers(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        adding_0_10 = MainMat4Mat(self.driver)
        adding_0_10.adding_0_10_empty_answers()

    def test_adding_0_10_correct_answers_dot_and_coma(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        adding_0_10 = MainMat4Mat(self.driver)
        adding_0_10.adding_0_10_correct_answers_dot_and_coma()

    def test_adding_0_10_different_characters(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        adding_0_10 = MainMat4Mat(self.driver)
        adding_0_10.adding_0_10_different_characters()

    def test_adding_0_10_correct_answers_space_before_and_after_result(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        adding_0_10 = MainMat4Mat(self.driver)
        adding_0_10.adding_0_10_correct_answers_space_before_and_after_result()

    def test_adding_0_10_correct_answers_dot_2_place(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        adding_0_10 = MainMat4Mat(self.driver)
        adding_0_10.adding_0_10_correct_answers_dot_2_place()

    def test_adding_0_10_correct_answers_comma_1_place(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        adding_0_10 = MainMat4Mat(self.driver)
        adding_0_10.adding_0_10_correct_answers_comma_1_place()

    def test_adding_0_10_invalid_equivalence_class(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        adding_0_10 = MainMat4Mat(self.driver)
        adding_0_10.adding_0_10_invalid_equivalence_class()

    def test_adding_0_50_correct_answers(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        adding_0_50 = MainMat4Mat(self.driver)
        adding_0_50.adding_0_50_correct_answers()

    def test_adding_0_50_invalid_equivalence_class(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        adding_0_50 = MainMat4Mat(self.driver)
        adding_0_50.adding_0_50_invalid_equivalence_class()

    def test_adding_0_100_correct_answers(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        adding_0_100= MainMat4Mat(self.driver)
        adding_0_100.adding_0_100_correct_answers()

    def test_adding_0_100_invalid_equivalence_class(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        adding_0_100 = MainMat4Mat(self.driver)
        adding_0_100.adding_0_100_invalid_equivalence_class()

    def test_subtraction_0_10_correct_answers(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        subtraction_0_10 = MainMat4Mat(self.driver)
        subtraction_0_10.subtraction_0_10_correct_answers()

    def test_subtraction_0_10_invalid_equivalence_class_(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        subtraction_0_10 = MainMat4Mat(self.driver)
        subtraction_0_10.subtraction_0_10_invalid_equivalence_class()

    def test_subtraction_0_50_correct_answers(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        subtraction_0_50 = MainMat4Mat(self.driver)
        subtraction_0_50.subtraction_0_50_correct_answers()

    def test_subtraction_0_50_invalid_equivalence_class(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        subtraction_0_50 = MainMat4Mat(self.driver)
        subtraction_0_50.subtraction_0_50_invalid_equivalence_class()

    def test_subtraction_0_100_correct_answers(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        subtraction_0_50= MainMat4Mat(self.driver)
        subtraction_0_50.subtraction_0_100_correct_answers()

    def test_subtraction_0_100_invalid_equivalence_class(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        subtraction_0_100= MainMat4Mat(self.driver)
        subtraction_0_100.subtraction_0_100_invalid_equivalence_class()

    def test_multiplication_0_10_correct_answers(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        multiplication_0_10 = MainMat4Mat(self.driver)
        multiplication_0_10.multiplication_0_10_correct_answers()

    def test_multiplication_0_10_invalid_equivalence_class(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        multiplication_0_10 = MainMat4Mat(self.driver)
        multiplication_0_10.multiplication_0_10_invalid_equivalence_class()

    def test_multiplication_0_50_correct_answers(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        multiplication_0_50 = MainMat4Mat(self.driver)
        multiplication_0_50.multiplication_0_50_correct_answers()

    def test_multiplication_0_50_invalid_equivalence_class(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        multiplication_0_50 = MainMat4Mat(self.driver)
        multiplication_0_50.multiplication_0_50_invalid_equivalence_class()

    def test_multiplication_0_100_correct_answers(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        multiplication_0_50 = MainMat4Mat(self.driver)
        multiplication_0_50.multiplication_0_100_correct_answers()

    def test_multiplication_0_100_invalid_equivalence_class(self,setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        multiplication_0_100 = MainMat4Mat(self.driver)
        multiplication_0_100.multiplication_0_100_invalid_equivalence_class()

    def test_division_0_10_correct_answers(self, setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        division_0_10 = MainMat4Mat(self.driver)
        division_0_10.division_0_10_correct_answers()

    def test_division_0_10_invalid_equivalence_class(self, setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        division_0_10 = MainMat4Mat(self.driver)
        division_0_10.division_0_10_invalid_equivalence_class()

    def test_division_0_50_correct_answers(self, setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        division_0_50 = MainMat4Mat(self.driver)
        division_0_50.division_0_50_correct_answers()

    def test_division_0_50_invalid_equivalence_class(self, setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        division_0_50 = MainMat4Mat(self.driver)
        division_0_50.division_0_50_invalid_equivalence_class()

    def test_division_0_100_correct_answers(self, setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        division_0_50 = MainMat4Mat(self.driver)
        division_0_50.division_0_100_correct_answers()

    def test_division_0_100_invalid_equivalence_class(self, setup):
        self.driver.get("https://slawomirj.github.io/Mat4Mat/")
        division_0_100 = MainMat4MatRef(self.driver)
        division_0_100.division_0_100_invalid_equivalence_class()


   