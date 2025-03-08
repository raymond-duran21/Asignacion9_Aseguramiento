# 🚀 Pruebas Automatizadas con Selenium y Pytest

Este repositorio contiene pruebas automatizadas para el sitio web **SauceDemo** utilizando **Selenium** y **Pytest** en Python.

## 📌 Tecnologías Utilizadas
- 🐍 **Python 3.x**
- 🌐 **Selenium** (Automatización de navegador)
- 🧪 **Pytest** (Framework de pruebas)
- 📊 **Pytest-HTML** (Generación de reportes)

## 🛠 Configuración del Entorno

### 1️⃣ Clonar el repositorio:
```bash
git clone https://github.com/TU-USUARIO/Actividad-9-Selenium.git
cd Actividad-9-Selenium
```

### 2️⃣ Crear un entorno virtual (Opcional pero recomendado):
```bash
python -m venv venv
```

### 3️⃣ Activar el entorno virtual:
- **En Windows**:
  ```bash
  venv\Scriptsctivate
  ```
- **En Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Instalar dependencias necesarias:
```bash
pip install -r requirements.txt
```

## 🚀 Ejecutar las Pruebas

Para ejecutar todas las pruebas, usa el siguiente comando:
```bash
pytest test_saucedemo.py --html=report.html
```
Esto generará un reporte en **HTML** llamado `report.html`.

## 📋 Escenarios de Prueba Automatizados

✅ **Inicio de sesión exitoso**  
✅ **Intento de inicio de sesión con credenciales incorrectas**  
✅ **Agregar un producto al carrito**  
✅ **Eliminar un producto del carrito**  
✅ **Completar una compra**  

## 📊 Generación de Reportes

Puedes ver los resultados en un reporte HTML después de ejecutar las pruebas:
```bash
pytest --html=report.html
```
Abre `report.html` en tu navegador para ver el resumen.
