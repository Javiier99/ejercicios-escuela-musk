# * Lista de productos disponibles en producción
productos = [
    "Leche", "Pan", "Huevos", "Arroz", "Pasta", "Aceite de oliva",
    "Azúcar", "Sal", "Harina", "Tomates", "Cebollas", "Patatas",
    "Manzanas", "Plátanos", "Pollo", "Carne picada", "Atún en lata",
    "Queso", "Yogur", "Mantequilla", "Café", "Té", "Cereales",
    "Galletas", "Agua mineral", "Refresco de cola", "Detergente",
    "Papel higiénico", "Jabón de manos", "Pasta de dientes"
]

# --- 1. FÁBRICA ---
def fabrica():
    contador = 0
    # En lugar de while True, controlamos si quedan productos en la lista base
    while len(productos) > 0:
        contador += 1
        un_producto = productos.pop(0)
        print(f"[FÁBRICA] Fabricado producto Nº {contador}: {un_producto}")
        yield un_producto
    print("[FÁBRICA] ¡No quedan más materias primas! Fábrica cerrada.")

# --- 2. DISTRIBUIDOR ---
def distribuidor(generador_fabrica):
    distribuidor_objetos_guardados = []
    
    for producto in generador_fabrica:
        distribuidor_objetos_guardados.append(producto)
        
        # El distribuidor solo envía cuando tiene una carga de 5 productos
        if len(distribuidor_objetos_guardados) >= 5:
            print(f"[DISTRIBUIDOR] Lote de {len(distribuidor_objetos_guardados)} listo. Enviando carga...")
            # Enviamos todo el lote acumulado al supermercado
            yield distribuidor_objetos_guardados
            distribuidor_objetos_guardados = [] # Vaciamos el almacén del distribuidor
            
    # Si al cerrar la fábrica quedaron productos colgados (menos de 5), se envían igual
    if distribuidor_objetos_guardados:
        print(f"[DISTRIBUIDOR] Enviando último lote restante de {len(distribuidor_objetos_guardados)} productos.")
        yield distribuidor_objetos_guardados

# --- 3. SUPERMERCADO ---
productos_supermercados = []

def supermercado(generador_distribuidor):
    for lote in generador_distribuidor:
        print(f"[SUPERMERCADO] ¡Ha llegado un lote de productos! {lote}")
        for prod in lote:
            productos_supermercados.append(prod)
            print(f" -> Colocado en estantería: {prod}")
        # Ofrecemos las estanterías actualizadas al cliente
        yield productos_supermercados

# --- 4. CLIENTE (Simulación del proceso) ---
lista_cliente = ["Sal", "Harina", "Tomates", "Cebollas", "Patatas", "Manzanas", "Plátanos"]
objeto_guardado_carrito = []

# Inicializamos los eslabones de la cadena pasando el anterior como argumento
instancia_fabrica = fabrica()
instancia_distribuidor = distribuidor(instancia_fabrica)
instancia_supermercado = supermercado(instancia_distribuidor)

print("=== INICIO DE LA CADENA DE SUMINISTRO ===")

# Mientras el cliente tenga cosas que comprar y el supermercado reciba mercancía
for estanteria in instancia_supermercado:
    
    # Usamos una copia de la lista para poder remover elementos de la original de forma segura
    for prod_deseado in list(lista_cliente):
        if prod_deseado in estanteria:
            # El cliente lo compra
            lista_cliente.remove(prod_deseado)
            estanteria.remove(prod_deseado)
            objeto_guardado_carrito.append(prod_deseado)
            print(f"🛒 [CLIENTE] ¡Encontré y compré {prod_deseado}!")
            
    print(f"📋 Productos restantes en la lista de la compra: {lista_cliente}")
    print(f"🏪 Productos que quedan en el súper: {productos_supermercados}\n" + "-"*50)
    
    # Si la lista del cliente se vacía, rompemos el bucle sin esperar a que termine la fábrica
    if len(lista_cliente) == 0:
        break

# --- RESULTADO FINAL ---
print("\n=== PROCESO FINALIZADO ===")
if len(lista_cliente) == 0:
    print(f"🎉 ¡Éxito! El cliente completó su lista. Carrito final: {objeto_guardado_carrito}")
else:
    print(f"⚠️ El cliente no pudo encontrar todo. Faltó: {lista_cliente}. Carrito: {objeto_guardado_carrito}")