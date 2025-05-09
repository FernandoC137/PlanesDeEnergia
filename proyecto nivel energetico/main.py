import customtkinter as ctk
import componentes as c

def actualizar_plan_actual():
    return c.obtener_plan_activo()

# Configuración de la ventana principal
ctk.set_appearance_mode("System")  # Modo claro/oscuro automático
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Consumo energético")
ventana.geometry("400x350")

# Etiqueta que muestra el plan actual
plan_actual = actualizar_plan_actual()
etiqueta = ctk.CTkLabel(
    ventana, 
    text=f"El plan de energía actual es: {plan_actual}",
    font=("Arial", 14)
)
etiqueta.pack(pady=20)

# Opciones disponibles para el Combobox
if c.obtener_guid_maximo_rendimiento():
    opciones = [
        "Economizador",
        "Equilibrado",
        "Alto rendimiento",
        "Máximo rendimiento"
    ]
else:
    opciones = [
        "Economizador",
        "Equilibrado",
        "Alto rendimiento"
    ]

# Crear el Combobox en modo solo lectura
combobox = ctk.CTkComboBox(
    ventana, 
    values=opciones,
    state="readonly",
    command=lambda _: al_seleccionar()
)
combobox.pack(pady=10)

# Etiqueta para mensajes de retroalimentación
etiqueta_feedback = ctk.CTkLabel(
    ventana, 
    text="", 
    font=("Arial", 10),
    text_color="green"
)
etiqueta_feedback.pack(pady=10)

def al_seleccionar():
    """
    Maneja la selección de un nuevo plan en el Combobox.
    Actualiza el plan según la selección y muestra feedback al usuario.
    """
    seleccion = combobox.get()
    
    if seleccion == "Economizador":
        mensaje = c.cambio_eco()
    elif seleccion == "Equilibrado":
        mensaje = c.cambio_equilibrado()
    elif seleccion == "Alto rendimiento":
        mensaje = c.cambio_alto_rendimiento()
    elif seleccion == "Máximo rendimiento":
        GUID = c.obtener_guid_maximo_rendimiento()
        if GUID:
            mensaje = c.activar_plan_por_guid(GUID)
        else:
            mensaje = "No se pudo obtener el GUID del plan 'Máximo rendimiento'."
    
    # Actualizar la etiqueta con el nuevo plan
    nuevo_plan = actualizar_plan_actual()
    etiqueta.configure(text=f"El plan de energía actual es: {nuevo_plan}")
    
    # Mostrar feedback y limpiar después de 3 segundos
    etiqueta_feedback.configure(text=mensaje)
    ventana.after(3000, lambda: etiqueta_feedback.configure(text=""))

# Crear botón para crear plan de máximo rendimiento
def crear_maximo_rendimiento():
    """Maneja la creación de un nuevo plan de máximo rendimiento."""
    resultado = c.crear_maximo_rendimiento()
    etiqueta_feedback.configure(
        text="Plan máximo rendimiento creado exitosamente",
        text_color="green"
    )
    ventana.after(3000, lambda: etiqueta_feedback.configure(text=""))

if c.obtener_guid_maximo_rendimiento() is None:
    boton_crear = ctk.CTkButton(
        ventana, 
        text="Crear Máximo Rendimiento",
        command=crear_maximo_rendimiento
    )
    boton_crear.pack(pady=10)

ventana.mainloop()