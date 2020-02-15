import numpy as np
import cv2

class RGBHistogram:
    def __init__(self, bins):
        # almacenar el número de contenedores o bins que utilizará el histograma
        self.bins = bins
 
    def describe(self, image):
        # calcular un histograma 3D en el espacio de color RGB,
        # luego normalizaremos el histograma para que las imágenes
        # con el mismo contenido, pero escalado más grande
        # o menor tengan (aproximadamente) el mismo histograma
        hist = cv2.calcHist([image], [0, 1, 2],
            None, self.bins, [0, 256, 0, 256, 0, 256])

        hist = cv2.normalize(hist,hist)
 
        # Devolvemos el histograma 3D como un "flatten array"
        return hist.flatten()