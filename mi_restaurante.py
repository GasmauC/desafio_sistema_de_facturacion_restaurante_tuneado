import customtkinter as ctk
from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

# --- CONFIGURACIÓN DE ESTILO ---
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("dark-blue")  

# Colores y Fuentes de Alto Impacto
COLOR_FONDO_PANEL = "#2b2b2b" # Gris oscuro para separar paneles
COLOR_ACENTO = "#00d2d3"      # Cian eléctrico para títulos
COLOR_BOTON_HOVER = "#0abde3" # Cian un poco más oscuro
FONT_TITULO = ("Roboto Medium", 50)
FONT_SUBTITULO = ("Roboto Medium", 20)
FONT_TEXTO = ("Roboto", 12)
FONT_MONO = ("Consolas", 12) # Para que el recibo se alinee perfecto

# --- LÓGICA DEL NEGOCIO ---
operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    try:
        resultado = str(eval(operador))
    except:
        resultado = "Error"
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    # Comida
    for x, c in enumerate(cuadros_comida):
        if variables_comida[x].get() == 1:
            cuadros_comida[x].configure(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].configure(state=DISABLED)
            texto_comida[x].set('0')

    # Bebida
    for x, c in enumerate(cuadros_bebida):
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].configure(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].configure(state=DISABLED)
            texto_bebida[x].set('0')

    # Postre
    for x, c in enumerate(cuadros_postre):
        if variables_postre[x].get() == 1:
            cuadros_postre[x].configure(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].configure(state=DISABLED)
            texto_postre[x].set('0')

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        valor = cantidad.get()
        num_cantidad = float(valor) if valor != '' else 0
        sub_total_comida = sub_total_comida + (num_cantidad * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        valor = cantidad.get()
        num_cantidad = float(valor) if valor != '' else 0
        sub_total_bebida = sub_total_bebida + (num_cantidad * precios_bebida[p])
        p += 1

    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        valor = cantidad.get()
        num_cantidad = float(valor) if valor != '' else 0
        sub_total_postre = sub_total_postre + (num_cantidad * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.07
    total_final = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postre.set(f'$ {round(sub_total_postre, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total_final, 2)}')

def recibo():
    texto_recibo.configure(state=NORMAL)
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 1999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    
    texto_recibo.insert(END, f'Datos: {num_recibo:<20}   Fecha: {fecha_recibo}\n')
    texto_recibo.insert(END, f'=' * 63 + '\n')
    texto_recibo.insert(END, f'{"Items":<25} | {"Cant.":<8} | {"Costo":<12}\n')
    texto_recibo.insert(END, f'-' * 63 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0' and comida.get() != '':
             costo = float(comida.get()) * precios_comida[x]
             texto_recibo.insert(END, f'{lista_comidas[x]:<25} | {comida.get():<8} | $ {costo:.2f}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0' and bebida.get() != '':
            costo = float(bebida.get()) * precios_bebida[x]
            texto_recibo.insert(END, f'{lista_bebidas[x]:<25} | {bebida.get():<8} | $ {costo:.2f}\n')
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != '0' and postre.get() != '':
            costo = float(postre.get()) * precios_postres[x]
            texto_recibo.insert(END, f'{lista_postres[x]:<25} | {postre.get():<8} | $ {costo:.2f}\n')
        x += 1

    texto_recibo.insert(END, f'=' * 63 + '\n')
    texto_recibo.insert(END, f'{"Sub-total":<35} : {var_subtotal.get()}\n')
    texto_recibo.insert(END, f'{"Impuestos (7%)":<35} : {var_impuesto.get()}\n')
    texto_recibo.insert(END, f'{"TOTAL":<35} : {var_total.get()}\n')
    texto_recibo.insert(END, f'=' * 63 + '\n')
    texto_recibo.insert(END, '\n*** Gracias por su visita ***')
    texto_recibo.configure(state=DISABLED)

def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if archivo:
        archivo.write(info_recibo)
        archivo.close()
        messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')

def resetear():
    texto_recibo.configure(state=NORMAL)
    texto_recibo.delete(0.1, END)
    texto_recibo.configure(state=DISABLED)
    
    for texto in texto_comida: texto.set('0')
    for texto in texto_bebida: texto.set('0')
    for texto in texto_postre: texto.set('0')

    for cuadro in cuadros_comida: cuadro.configure(state=DISABLED)
    for cuadro in cuadros_bebida: cuadro.configure(state=DISABLED)
    for cuadro in cuadros_postre: cuadro.configure(state=DISABLED)

    for v in variables_comida: v.set(0)
    for v in variables_bebida: v.set(0)
    for v in variables_postre: v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')
    
    visor_calculadora.delete(0, END)

# --- INICIO INTERFAZ GRÁFICA MODERNA ---
aplicacion = ctk.CTk()
aplicacion.geometry('1300x650') 
aplicacion.title('Sistema de Facturación - Moderno')

# VARIABLES
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# --- PANEL SUPERIOR (TÍTULO) ---
panel_superior = ctk.CTkFrame(aplicacion, fg_color=COLOR_FONDO_PANEL, corner_radius=0)
panel_superior.pack(side=TOP, fill=X)
titulo = ctk.CTkLabel(panel_superior, text="Sistema de Facturación", font=FONT_TITULO, text_color=COLOR_ACENTO)
titulo.pack(pady=10)

# --- PANEL IZQUIERDO (COMIDAS Y COSTOS) ---
panel_izquierdo = ctk.CTkFrame(aplicacion, fg_color="transparent")
panel_izquierdo.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

# Sub-panel para las listas de productos
panel_productos = ctk.CTkFrame(panel_izquierdo, fg_color="transparent")
panel_productos.pack(side=TOP, fill=BOTH, expand=True)

# Listas de Productos
lista_comidas = ['Pollo', 'Cordero', 'Asado', 'Merluza', 'Milanesa', 'Pizza', 'Empanadas', 'Pastas']
lista_bebidas = ['Gaseosa', 'Soda', 'Agua', 'Vino Tinto', 'Vino Blanco', 'Jugo', 'Cerveza', 'Licuado']
lista_postres = ['Helado', 'Fruta', 'Flan', 'Budín', 'Tiramisú', 'Torta', 'Brownies', 'Mousse']

# Función para crear paneles verticales de productos
def crear_panel_producto(parent, titulo, lista, variables, cuadros, textos, col):
    frame = ctk.CTkFrame(parent, fg_color=COLOR_FONDO_PANEL)
    frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
    
    ctk.CTkLabel(frame, text=titulo, font=FONT_SUBTITULO, text_color=COLOR_ACENTO).pack(pady=10)
    
    for i, item in enumerate(lista):
        var = IntVar()
        variables.append(var)
        texto = StringVar(value='0')
        textos.append(texto)
        
        # Fila contenedora
        row_frame = ctk.CTkFrame(frame, fg_color="transparent")
        row_frame.pack(fill=X, pady=2, padx=5)
        
        chk = ctk.CTkCheckBox(row_frame, text=item, variable=var, onvalue=1, offvalue=0, command=revisar_check, font=FONT_TEXTO)
        chk.pack(side=LEFT)
        
        entry = ctk.CTkEntry(row_frame, textvariable=texto, width=50, state=DISABLED, justify='center')
        entry.pack(side=RIGHT)
        cuadros.append(entry)

variables_comida, cuadros_comida, texto_comida = [], [], []
variables_bebida, cuadros_bebida, texto_bebida = [], [], []
variables_postre, cuadros_postre, texto_postre = [], [], []

crear_panel_producto(panel_productos, "Comida", lista_comidas, variables_comida, cuadros_comida, texto_comida, 0)
crear_panel_producto(panel_productos, "Bebidas", lista_bebidas, variables_bebida, cuadros_bebida, texto_bebida, 1)
crear_panel_producto(panel_productos, "Postres", lista_postres, variables_postre, cuadros_postre, texto_postre, 2)

# --- PANEL COSTOS (ABAJO A LA IZQUIERDA) ---
panel_costos = ctk.CTkFrame(panel_izquierdo, fg_color=COLOR_FONDO_PANEL, height=150)
panel_costos.pack(side=BOTTOM, fill=X, pady=(10, 0))

labels = ["Costo Comida", "Costo Bebida", "Costo Postre", "Subtotal", "Impuestos", "Total"]
vars_list = [var_costo_comida, var_costo_bebida, var_costo_postre, var_subtotal, var_impuesto, var_total]

# Grid de costos
for i in range(len(labels)):
    row = i % 3
    col = 0 if i < 3 else 2 
    
    ctk.CTkLabel(panel_costos, text=labels[i], font=FONT_TEXTO).grid(row=row, column=col, padx=10, pady=5, sticky="w")
    ctk.CTkEntry(panel_costos, textvariable=vars_list[i], state="readonly", width=100).grid(row=row, column=col+1, padx=10, pady=5)


# --- PANEL DERECHO (CALCULADORA, RECIBO Y BOTONES) ---
panel_derecho = ctk.CTkFrame(aplicacion, fg_color="transparent")
panel_derecho.pack(side=RIGHT, fill=BOTH, padx=10, pady=10)

# Calculadora
panel_calculadora = ctk.CTkFrame(panel_derecho, fg_color="transparent")
panel_calculadora.pack(side=TOP, fill=X)

visor_calculadora = ctk.CTkEntry(panel_calculadora, font=("Roboto", 24), justify=RIGHT)
visor_calculadora.pack(fill=X, pady=5)

grid_calc = ctk.CTkFrame(panel_calculadora, fg_color="transparent")
grid_calc.pack()

botones_calc = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'R', 'B', '0', '/']
r, c = 0, 0
for b in botones_calc:
    cmd = lambda x=b: click_boton(x)
    if b == 'R': cmd = obtener_resultado
    elif b == 'B': cmd = borrar
    elif b == 'x': cmd = lambda: click_boton('*')
    
    ctk.CTkButton(grid_calc, text=b, width=50, height=40, font=("Roboto", 18, "bold"), command=cmd, fg_color="#333").grid(row=r, column=c, padx=2, pady=2)
    c += 1
    if c > 3: c=0; r+=1

# Recibo
panel_recibo = ctk.CTkFrame(panel_derecho, fg_color="transparent")
panel_recibo.pack(side=TOP, fill=BOTH, expand=True, pady=10)
texto_recibo = ctk.CTkTextbox(panel_recibo, font=FONT_MONO, state=DISABLED)
texto_recibo.pack(fill=BOTH, expand=True)

# --- PANEL BOTONES (ABAJO A LA DERECHA) ---
panel_botones = ctk.CTkFrame(panel_derecho, fg_color="transparent")
panel_botones.pack(side=BOTTOM, fill=X)

botones_accion = ['Total', 'Recibo', 'Guardar', 'Resetear']
comandos = [total, recibo, guardar, resetear]
colores_btn = [COLOR_ACENTO, COLOR_ACENTO, "#27ae60", "#c0392b"] 

for i, btn_text in enumerate(botones_accion):
    ctk.CTkButton(panel_botones, 
                  text=btn_text, 
                  command=comandos[i], 
                  font=("Roboto", 14, "bold"), 
                  fg_color=colores_btn[i], 
                  hover_color=COLOR_BOTON_HOVER if i < 2 else None,
                  width=80, height=40).grid(row=0, column=i, padx=5, sticky="ew")

for i in range(4): panel_botones.grid_columnconfigure(i, weight=1)

aplicacion.mainloop()