# 💎 Sistema de Facturación - Modern UI Edition

**Sistema de Facturación v2.0** es una reimaginación visual del clásico sistema de punto de venta (POS). Desarrollado en **Python** utilizando **CustomTkinter**, esta versión abandona la estética tradicional para ofrecer una interfaz moderna, oscura y elegante, optimizada para una mejor experiencia de usuario.

Este proyecto combina lógica de negocio robusta con un diseño de interfaz de alto impacto visual.

![Estado del Proyecto](https://img.shields.io/badge/Estado-Finalizado-success)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![UI](https://img.shields.io/badge/Interfaz-CustomTkinter-blueviolet)
![Theme](https://img.shields.io/badge/Tema-Dark_Mode-black)

## 📸 Interfaz Moderna
*(¡Tu captura de pantalla va aquí! Muestra ese elegante modo oscuro)*
![Screenshot del Sistema](C:\Users\Usuario\Desktop\python_total\sitema_facturacion\app.jpg)

## ✨ Novedades Visuales (UI/UX)

A diferencia de las interfaces estándar de Tkinter, esta edición incluye:
* **Modo Oscuro Nativo:** Utiliza `ctk.set_appearance_mode("Dark")` para reducir la fatiga visual.
* **Paleta de Colores Cyberpunk:** Tonos gris oscuro (`#2b2b2b`) con acentos en Cian Eléctrico (`#00d2d3`).
* **Tipografía Moderna:** Implementación de fuentes **Roboto** para una lectura limpia y **Consolas** para la alineación perfecta de recibos digitales.
* **Componentes Estilizados:** Botones con efectos *hover*, entradas redondeadas y bordes suavizados.

## 📋 Funcionalidades del Negocio

El sistema mantiene toda la potencia lógica bajo una nueva piel:

* **🔢 Panel de Control de Productos:**
    * Selección de Comidas, Bebidas y Postres mediante *checkboxes* estilizados.
    * Activación inteligente de campos de entrada.
* **💵 Motor de Facturación:**
    * Cálculo de subtotales por categoría.
    * Cálculo automático de impuestos (7%).
    * Suma total precisa y redondeo de decimales.
* **🧾 Generador de Recibos:**
    * Visualización de tickets en tiempo real en un panel de texto monoespaciado.
    * Detalle de ítems, cantidades y precios unitarios.
* **💾 Persistencia:**
    * Exportación de recibos a archivos `.txt` mediante cuadros de diálogo nativos del sistema operativo.
* **🧮 Calculadora Integrada:**
    * Herramienta matemática completa incorporada en la interfaz derecha.

## 🛠️ Tecnologías

* **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter):** Librería principal para el diseño UI moderno.
* **Python Standard Library:**
    * `tkinter`: Backend base de la interfaz.
    * `random`, `datetime`: Para la unicidad y temporalidad de los recibos.
    * `filedialog`: Para la gestión de guardado.

## ⚙️ Instalación

Este proyecto requiere la librería `customtkinter`.

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/facturacion-modern-ui.git](https://github.com/tu-usuario/facturacion-modern-ui.git)
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install customtkinter
    ```

## 🚀 Ejecución

Ejecuta el script principal para lanzar la interfaz:

```bash
python main.py
