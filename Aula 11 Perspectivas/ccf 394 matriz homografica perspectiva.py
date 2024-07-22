
import numpy as np
import cv2
# Pontos correspondentes
pts_src = np.array([[1, 1], [4, 1], [4, 4], [1, 4]], dtype='float32')
pts_dst = np.array([[2, 2], [6, 2], [5, 5], [2, 6]], dtype='float32')
# Calcular a matriz homográfica H,
status = cv2.findHomography(pts_src, pts_dst)
print("Matriz Homográfica:")
print(H)
# Carregar a imagem i
mg_src = cv2.imread('computador.jpg')
# Aplicar a transformação homográfica
height, width = img_src.shape[:2]
img_dst = cv2.warpPerspective(img_src, H, (width, height))
# Mostrar a imagem original e a imagem transformada
cv2.imshow('Imagem Original', img_src)
cv2.imshow('Imagem Transformada', img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows() # Salvar a imagem transformada
cv2.imwrite('transformed_image.jpg', img_dst) 
