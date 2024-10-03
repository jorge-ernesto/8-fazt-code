import cv2

# Cargar el modelo preentrenado de Super-Resolution
sr = cv2.dnn_superres.DnnSuperResImpl_create()

# Cargar el archivo de pesos del modelo FSRCNN (más rápido)
path = "Recursos/1 Modelos/LapSRN_x4.pb"  # Necesitas descargar este archivo
sr.readModel(path)

# Establecer el modelo y el factor de escala
sr.setModel("lapsrn", 4)  # Cambiar a "fsrcnn" para velocidad

# Cargar la imagen original
image = cv2.imread("Recursos/3 Imagenes/1_453726189_122122787720341649_88385209316462114_n.jpg")

# Aplicar la super-resolución (ampliar la imagen)
result = sr.upsample(image)

# Guardar la imagen mejorada
cv2.imwrite("Recursos/3 Imagenes/imagen_mejorada_IA_rapido_lapsrn.jpg", result)

print("Imagen redimensionada con IA guardada rápidamente.")
