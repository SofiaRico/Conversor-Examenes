# 📘 Conversor de Exámenes Word a Formato GIFT (Moodle)

## 🧰 Requisitos previos
Antes de ejecutar esta herramienta, asegúrate de tener instalado lo siguiente:

- **Python 3.8 o superior**
- Acceso a internet para instalar dependencias
- El archivo `app.py` incluido en este proyecto

---

## 🔧 Instalación paso a paso

### 1. Verifica si ya tienes Python instalado
Abre una terminal (PowerShell o CMD) y escribe:

```bash
python --version
```

Si te sale un error diciendo que "python no se reconoce...", sigue con el siguiente paso.

### 2. Instala Python
1. Ve al sitio oficial: https://www.python.org/downloads/
2. Descarga la versión recomendada para Windows.
3. Ejecuta el instalador y **marca la casilla que dice**:  
   ✅ *Add Python to PATH*
4. Termina la instalación y **reinicia la terminal**.

---

### 3. Verifica que `pip` ya funcione
En la terminal, escribe:

```bash
pip --version
```

Si ves un número de versión, todo está bien.

---

### 4. Instala las dependencias del proyecto

En la misma carpeta donde está el archivo `app.py`, ejecuta:

```bash
pip install streamlit python-docx
```

---

## 🚀 Cómo ejecutar la aplicación

Desde la terminal, estando dentro de la carpeta del proyecto, ejecuta:

```bash
streamlit run app.py
```

Se abrirá automáticamente en el navegador una interfaz donde puedes subir el archivo `.docx` del examen y descargar el archivo `.txt` en formato GIFT para Moodle.

---

## 📁 Estructura recomendada del archivo Word

- **Preguntas:** comienzan con número y punto (ej: `1. ¿Qué es...?`)
- **Opciones:** `a)`, `b)`, `c)`, `d)`...
- **Respuesta correcta:** línea que empiece por `Respuesta correcta: a`
- **Feedback (opcional):** línea que empiece por `Feedback: explicación`
