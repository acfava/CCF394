import cv2
import numpy as np

# Função de callback para lidar com os cliques do mouse
def click_event(event, x, y, flags, param):
    global points, counter

    # Verifica se o botão esquerdo do mouse foi pressionado
    if event == cv2.EVENT_LBUTTONDOWN:
        # Marca o ponto na imagem
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow('Image', img)

        # Adiciona o ponto à lista de pontos
        points.append((x, y))
        counter += 1

        # Verifica se todos os pontos foram marcados
        if counter == 4:
            # Converte os pontos em um array numpy
            pts1 = np.float32(points)

            # Define os pontos de destino para a transformação de perspectiva
            width, height = 300, 400
            pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

            # Calcula a matriz de transformação de perspectiva
            M = cv2.getPerspectiveTransform(pts1, pts2)

            # Aplica a transformação de perspectiva na imagem
            transformed_img = cv2.warpPerspective(img, M, (width, height))
            new_width = int(width * 1.5)
            new_height = int(height * 1.5)

            # Redimensiona a imagem
            resized_img = cv2.resize(transformed_img, (new_width, new_height))

            # Exibe a imagem transformada
            cv2.imshow('Transformed Image', resized_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# Carrega a imagem
print(" clique nos cantos superior esquerdo, superior direito, inferior direito, inferior esquerdo")
img = cv2.imread('computador.jpg')

# Cria uma janela para exibir a imagem
cv2.namedWindow('Image')

# Inicializa a lista de pontos e o contador
points = []
counter = 0

# Define a função de callback para o evento de clique do mouse
cv2.setMouseCallback('Image', click_event)

# Exibe a imagem
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
