# Altos import jhow
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import skimage.io as io

import numpy as np
# import matplotlib.pyplot as plt

# import numpy as np
# import matplotlib.pyplot as plt
import skimage.exposure as skie
import seaborn as sns
# %matplotlib inline

# Carregar imagem
def load_image():
    # abrir em escala de cinza
    img = io.imread('simpsonsG.png')
    io.imshow(img)
    io.show()

    # Imagem padrão do skiimage
    from skimage import data, io
    image = data.camera()
    io.imshow(image, cmap=plt.cm.gray)
    io.show()

    # Histograma em escala de cinza
    img = io.imread('simpsonsG.png')
    plt.hist(img.ravel(),256,[0,256])
    plt.show()

    img = io.imread('simpsons.png')   
    io.imshow(img)
    io.show()


# Converter imagem RGB em escala de cinza
def convert_RGB_2_GRAY():

    def rgb2gray(rgb):
        return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

    img = io.imread('simpsons.png')     
    gray = rgb2gray(img)    
    plt.imshow(gray, cmap = plt.get_cmap('gray'))
    plt.show()


# Converter em escala de cinza e salvar a imagem
def convert_and_save():
    def rgb2gray(rgb):
        return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

    img = io.imread('simpsons.png')     
    gray = rgb2gray(img)    

    fig = plt.imshow(gray, cmap = plt.get_cmap('gray'))
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig('my2.png', transparent = True, bbox_inches='tight', pad_inches = 0)

    plt.show()

# Função auxiliar para exibir imagem e histograma
def show(img):
    # Alterar a quantidade de bins do histograma
    # show(skie.rescale_intensity(img, in_range=(0,255), out_range=(0, 30)))
    # Alterar a Exposição do histograma
    # show(skie.rescale_intensity(img, in_range=(110,220), out_range=(0, 255)))
    # Equalizando o Histograma
    # show(skie.equalize_adapthist(img))


    # Display the image.
    fig, (ax1, ax2) = plt.subplots(1, 2,
                                   figsize=(12, 3))

    ax1.imshow(img, cmap=plt.cm.gray)
    ax1.set_axis_off()

    # Display the histogram.
    ax2.hist(img.ravel(), lw=0, bins=256)
    ax2.set_xlim(0, img.max())
    ax2.set_yticks([])

    plt.show()


