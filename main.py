import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del WebDriver
@pytest.fixture
def driver():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

# Función para escribir más lento en los campos de texto
def slow_typing(element, text, delay=0.3):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

# Prueba: Inicio de sesión exitoso con pausas
def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)  # Pausa para ver la carga de la página

    campo_usuario = driver.find_element(By.ID, "user-name")
    slow_typing(campo_usuario, "standard_user")
    
    campo_password = driver.find_element(By.ID, "password")
    slow_typing(campo_password, "secret_sauce")

    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)  # Pausa después del login

    assert "inventory" in driver.current_url

# Prueba: Intento de inicio de sesión con credenciales incorrectas
def test_login_fallido(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)

    campo_usuario = driver.find_element(By.ID, "user-name")
    slow_typing(campo_usuario, "usuario_invalido")

    campo_password = driver.find_element(By.ID, "password")
    slow_typing(campo_password, "clave_incorrecta")

    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    mensaje_error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username and password do not match" in mensaje_error

# Prueba: Agregar un producto al carrito
def test_agregar_producto_al_carrito(driver):
    test_login_exitoso(driver)
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Add to cart')]").click()
    time.sleep(3)  # Pausa para ver el botón siendo presionado

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "1"

# Prueba: Eliminar un producto del carrito
def test_eliminar_producto_del_carrito(driver):
    test_agregar_producto_al_carrito(driver)
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Remove')]").click()
    time.sleep(3)

    carrito = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(carrito) == 0

# Prueba: Completar una compra
def test_finalizar_compra(driver):
    test_agregar_producto_al_carrito(driver)
    time.sleep(3)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)

    driver.find_element(By.ID, "checkout").click()
    time.sleep(3)

    driver.find_element(By.ID, "first-name").send_keys("Juan")
    driver.find_element(By.ID, "last-name").send_keys("Pérez")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    time.sleep(3)

    driver.find_element(By.ID, "continue").click()
    time.sleep(3)

    driver.find_element(By.ID, "finish").click()
    time.sleep(3)

    mensaje_final = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you for your order!" in mensaje_final