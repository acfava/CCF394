import time as t
import tensorflow as tf
import keras
import cv2
import numpy as np
import process, sudoku
import model_wrapper
import preprocess
# nomes das imagens: 1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg
print("Versão do TensorFlow:", tf.__version__)
print("Versão do Keras:", keras.__version__)
print("Versão do Numpy:", np.__version__)
print("Versão do Opencv:", cv2.__version__)

# Versão do TensorFlow: 2.15.0
# Versão do Keras: 2.15.0
# Versão do Numpy: 1.26.4
# Versão do Opencv: 4.9.0
def resize_image(image, new_width):
    # Obtém as dimensões originais da imagem
    height, width,c = image.shape[:3]
    
    # Verifica se a largura é maior que o novo_width
    if width > new_width:
        # Calcula a razão de redimensionamento
        ratio = new_width / float(width)
        
        # Calcula a nova altura mantendo a proporção
        new_height = int(height * ratio)
        
        # Redimensiona a imagem
        resized_image = cv2.resize(image, (new_width, new_height))
        
        return resized_image
    else:
        # Se a largura já é menor ou igual ao novo_width, retorna a imagem original
        return image


# load the model with weights
my_model = model_wrapper.model_wrapper(None, False, None, "model.hdf5")

prev = 0

seen = dict()


imagem=input("Digite nome da imagem para resolver...")
imagem='./test_imgs/'+imagem
img=cv2.imread(imagem)
time_elapsed = t.time() - prev
if time_elapsed > 1. / 30:
    prev = t.time()

    img_result = img.copy()
    img_corners = img.copy()

    processed_img = preprocess.preprocess(img)
    corners = process.find_contours(processed_img, img_corners)

    if corners:
        warped, matrix = process.warp_image(corners, img)
        warped_processed = preprocess.preprocess(warped)

        vertical_lines, horizontal_lines = process.get_grid_lines(warped_processed)
        mask = process.create_grid_mask(vertical_lines, horizontal_lines)
        numbers = cv2.bitwise_and(warped_processed, mask)

        squares = process.split_into_squares(numbers)
        squares_processed = process.clean_squares(squares)

        squares_guesses = process.recognize_digits(squares_processed, my_model)

        # if it is impossible, continue
        if squares_guesses in seen and seen[squares_guesses] is True:
            print("impossivel resolver")
            sys.exit()


        # if we already solved this puzzle, just fetch the solution
        if squares_guesses in seen:
            process.draw_digits_on_warped(warped, seen[squares_guesses][0], squares_processed)
            img_result = process.unwarp_image(warped, img_result, corners, seen[squares_guesses][1])

        else:
            solved_puzzle, time = sudoku.solve_wrapper(squares_guesses)
            if solved_puzzle is not None:
                process.draw_digits_on_warped(warped, solved_puzzle, squares_processed)
                img_result = process.unwarp_image(warped, img_result, corners, time)
                seen[squares_guesses] = [solved_puzzle, time]

            else:
                seen[squares_guesses] = False

# Define a nova largura desejada
new_width = 1000
# Redimensiona a imagem se necessário
resized_image = resize_image(img_result, new_width)

cv2.imshow('window', resized_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

