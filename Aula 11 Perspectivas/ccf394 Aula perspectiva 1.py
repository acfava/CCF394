import cv2
import numpy as np
#perspectiva 1
# Função de callback para registrar os pontos clicados
def click_points(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Image", image)

# Carregar a imagem
image_path = 'computador.jpg'  # Substitua pelo caminho da sua imagem
image = cv2.imread(image_path)
height, width = image.shape[:2]

# Define a nova largura e calcula a nova altura para manter a proporção
new_width = 800
aspect_ratio = new_width / float(width)
new_height = int(height * aspect_ratio)

# Redimensiona a imagem
image = cv2.resize(image, (new_width, new_height), interpolation = cv2.INTER_AREA)


orig = image.copy()
cv2.imshow("Image", image)

points = []

# Configurar a janela para capturar os cliques do mouse
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", click_points)

# Esperar até que 4 pontos sejam clicados
while True:
    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Pressione 'Esc' para sair sem selecionar os pontos
        break
    if len(points) == 4:
        break

if len(points) == 4:
    # Definir os pontos de destino para a transformação de perspectiva
    width, height = 300, 400  # Ajuste o tamanho da nova perspectiva conforme necessário
    dst_points = np.array([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]
    ], dtype="float32")

    # Calcular a matriz de transformação de perspectiva
    src_points = np.array(points, dtype="float32")
    M = cv2.getPerspectiveTransform(src_points, dst_points)

    # Aplicar a transformação de perspectiva
    warped = cv2.warpPerspective(orig, M, (width, height))

    # Mostrar a imagem transformada
    cv2.imshow("Warped Image", warped)
    cv2.waitKey(0)

# Fechar todas as janelas
cv2.destroyAllWindows()
