import numpy as np

class Searcher:
    def __init__(self, index):
        self.index = index
 
    def search(self, queryFeatures):
        results = {}
 
        # loop sobre el index
        for (k, features) in self.index.items():
            # Calcularemos la distancia chi-cuadrado entre las entidades
            # en nuestro Index y nuestras características de la querie - usando la
            # distancia de chi-cuadrado que se usa normalmente para comparar histogramas
            d = self.chi2_distance(features, queryFeatures)
 
            # Ahora que tenemos la distancia entre los dos vectores de características,
            # podemos actualizar el diccionario de resultados - el
            # ID de imagen actual sera el índice o key y el
            # valor sera la distancia que calculamos anteriormente, representando
            # qué tan 'similar' es la imagen del Index con nuestra imagen de querie
            results[k] = d
 
        # Ordenamos nuestros resultados, de modo que las distancias más pequeñas (es decir, las
        # las imágenes más relevantes están al principio de la lista)
        results = sorted([(v, k) for (k, v) in results.items()])
 
        return results
 
    def chi2_distance(self, histA, histB, eps = 1e-10):
        # calcular la distancia chi-cuadrado
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
            for (a, b) in zip(histA, histB)])
 
        # Devolver la distancia chi-cuadrado
        return d