#Ejercicio numero 1 de introduccion a cadenas#
def extraer_palabras(oracion):
  """Extrae la primera y última palabra de una oración."""
  palabras = oracion.split()
  primera_palabra = palabras[0]
  ultima_palabra = palabras[-1]
  return primera_palabra, ultima_palabra

#2do ejercicio de intorducción a cadenas#
def eliminar_espacios_repetidos(cadena):
  """Elimina los espacios repetidos en una cadena."""
  palabras = cadena.split()
  cadena_limpia = " ".join(palabras)
  return cadena_limpia

#3er ejercicio#
def extraer_dominio(correo):
  """Extrae el dominio de un correo electrónico."""
  dominio = correo.split("@")[1]
  return dominio

#4to ejercicio#
def verificar_extension(archivo, extension_esperada):
  """Verifica si un archivo tiene la extensión correcta."""
  return archivo.endswith(extension_esperada)

# Ejemplos de uso del 4to ejericio de Dado un nombre de archivo, verifica si tiene la extensión correcta (ej. .pdf). 
archivo1 = "documento.pdf"
archivo2 = "imagen.jpg"
print(verificar_extension(archivo1, ".pdf"))  # True
print(verificar_extension(archivo2, ".pdf"))  # False


#5to ejercicio#
def invertir_palabras(texto):
  """Invierte el orden de las palabras en un texto."""
  palabras = texto.split()
  palabras_invertidas = palabras[::-1]
  texto_invertido = " ".join(palabras_invertidas)
  return texto_invertido

#6to ejercicio#
def responder_texto(texto):
  """Detecta palabras clave en un texto y responde."""

  # Cadenas con palabras clave
  poema = "Podrá nublarse el sol eternamente;\nPodrá secarse en un instante el mar;\nPodrá romperse el eje de la tierra\nComo un débil cristal."
  canto = "Eres como la noche, callada y constelada.\nTu silencio es de estrella, tan lejano y sencillo.\nMe gustas cuando callas porque estás como ausente.\nDistante y dolorosa como si hubieras muerto."

  # Convertir texto a minúsculas para comparación
  texto_lower = texto.lower()

  if "poema" in texto_lower and "amor" in texto_lower:
    return poema
  elif "canción" in texto_lower and "alegría" in texto_lower:
    return canto
  else:
    return "No se encontraron palabras clave en el texto."

# Ejemplo para explicar el ejercicio 6#
texto1 = "necesito que me escribas un poema de amor."
texto2 = "escribe una canción de alegría."
texto3 = "hola mundo"

print(responder_texto(texto1))
print(responder_texto(texto2))
print(responder_texto(texto3))