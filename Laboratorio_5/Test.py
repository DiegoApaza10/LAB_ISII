 #"D:\\SOFTWARE_2\\PYTHON\\msedgedriver.exe"
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HtmlTestRunner 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPercentCalculator(unittest.TestCase):

    def setUp(self):
        # Configurar el controlador del navegador Microsoft Edge
        self.driver = webdriver.Edge()
        self.driver.get("https://www.calculator.net/percent-calculator.html")
        self.driver.implicitly_wait(20)

    def test_porcentage_1(self):
        # Ingresar valores en los campos necesarios
        number_field = self.driver.find_element(By.XPATH, '//*[@id="cpar1"]')
        number_field.clear()
        number_field.send_keys("10")

        percent_field = self.driver.find_element(By.XPATH, '//*[@id="cpar2"]')
        percent_field.clear()
        percent_field.send_keys("50")

        # Hacer clic en el botón de calcular
        calculate_button = self.driver.find_element(By.XPATH, "//input[@value='Calculate']")
        calculate_button.click()

        # Verificar el resultado esperado
        result = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/p[2]/font/b")
        actual_result = result.text
        expected_result = "5"

        # Comparar el resultado
        self.assertEqual(actual_result, expected_result)
        # Comparacion
        if actual_result == expected_result:
            print("Éxito: La prueba ha pasado exitosamente")
        else:
            print("Fracaso: Resultado actual: {actual_result}, Resultado esperado: {expected_result}")


    def test_porcentage_2(self): #Número = -5, Porcentaje = 30 | -1.5  
        # Ingresar valores en los campos necesarios
        number_field = self.driver.find_element(By.XPATH, '//*[@id="cpar1"]')
        number_field.clear()
        number_field.send_keys("30")

        percent_field = self.driver.find_element(By.XPATH, '//*[@id="cpar2"]')
        percent_field.clear()
        percent_field.send_keys("-5")

        # Hacer clic en el botón de calcular
        calculate_button = self.driver.find_element(By.XPATH, "//input[@value='Calculate']")
        calculate_button.click()

        # Verificar el resultado esperado
        result = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/p[2]/font/b")
        actual_result = result.text
        expected_result = "-1.5"

        # Comparar el resultado
        self.assertEqual(actual_result, expected_result)
        # Comparacion
        if actual_result == expected_result:
            print("Éxito: La prueba ha pasado exitosamente")
        else:
            print("Fracaso: Resultado actual: {actual_result}, Resultado esperado: {expected_result}")
            
    def test_porcentage_3(self):
        # Ingresar valores en los campos necesarios
        number_field = self.driver.find_element(By.XPATH, '//*[@id="cpar1"]')
        number_field.clear()
        number_field.send_keys(" ")

        percent_field = self.driver.find_element(By.XPATH, '//*[@id="cpar2"]')
        percent_field.clear()
        percent_field.send_keys(" ")

        # Hacer clic en el botón de calcular
        calculate_button = self.driver.find_element(By.XPATH, "//input[@value='Calculate']")
        calculate_button.click()

        # Verificar el resultado esperado
        result = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/p[2]/font/b")
        actual_result = result.text
        expected_result = ""

        # Comparar el resultado
        self.assertEqual(actual_result, expected_result)
        # Comparacion
        if actual_result == expected_result:
            print("Éxito: La prueba ha pasado exitosamente")
        else:
            print("Fracaso: Resultado actual: {actual_result}, Resultado esperado: {expected_result}")
            


    def test_porcentage_4(self):  #Número = 'abc', Porcentaje = 'xyz' | Mensaje de Error o NaN   |
        # Ingresar valores en los campos necesarios
        number_field = self.driver.find_element(By.XPATH, '//*[@id="cpar1"]')
        number_field.clear()
        number_field.send_keys("xyz")

        percent_field = self.driver.find_element(By.XPATH, '//*[@id="cpar2"]')
        percent_field.clear()
        percent_field.send_keys("abc")

        # Hacer clic en el botón de calcular
        calculate_button = self.driver.find_element(By.XPATH, "//input[@value='Calculate']")
        calculate_button.click()

        # Verificar el resultado esperado
        result = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/p[2]/font/b")
        actual_result = result.text
        expected_result = " "

        # Comparar el resultado
        self.assertEqual(actual_result, expected_result)
        # Comparacion
        if actual_result == expected_result:
            print("Éxito: La prueba ha pasado exitosamente")
        else:
            print("Fracaso: Resultado actual: {actual_result}, Resultado esperado: {expected_result}")
    def test_porcentage_5(self):  #Número = 9999999999999, Porcentaje = 100 | 9999999999999 
        # Ingresar valores en los campos necesarios
        number_field = self.driver.find_element(By.XPATH, '//*[@id="cpar1"]')
        number_field.clear()
        number_field.send_keys("100")

        percent_field = self.driver.find_element(By.XPATH, '//*[@id="cpar2"]')
        percent_field.clear()
        percent_field.send_keys("9999999999999")

        # Hacer clic en el botón de calcular
        calculate_button = self.driver.find_element(By.XPATH, "//input[@value='Calculate']")
        calculate_button.click()

        # Verificar el resultado esperado
        result = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/p[2]/font/b")
        actual_result = result.text
        expected_result = "9999999999999"

        # Comparar el resultado
        self.assertEqual(actual_result, expected_result)
        # Comparacion
        if actual_result == expected_result:
            print("Éxito: La prueba ha pasado exitosamente")
        else:
            print("Fracaso: Resultado actual: {actual_result}, Resultado esperado: {expected_result}")
           
    def tearDown(self):
        # Cerrar el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reporte_pruebas'))
