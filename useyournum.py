from PIL import Image
import numpy as np
from Neuronal_Network import neuralNetwork
import matplotlib.pyplot as plt
import imageio

# número de nodos de entrada, ocultos y de salida
input_nodes = 784  # 28*28
hidden_nodes = 100
output_nodes = 10

# la tasa de aprendizaje es 0.3
learning_rate = 0.1

# crear instancia de red neuronal
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# cambiar el valor de píxel
file_in = 'yournum/6.png'
width = 28
height = 28
file_out = 'yournum/yournum_c.png'
image = Image.open(file_in)
resized_image = image.resize((width, height), Image.ANTIALIAS)
resized_image.save(file_out)

save_wih_file = "save_model/wih.npy"
save_who_file = "save_model/who.npy"
n.wih = np.load(save_wih_file)
n.who = np.load(save_who_file)

# probar la red neuronal

image_file_name = "yournum/yournum_c.png"
img_array = imageio.imread(image_file_name, as_gray=True)

img_data = 255.0 - img_array.reshape(784)
img_data = (img_data / 255.0 * 0.99) + 0.01
# consultar la red
outputs = n.query(img_data)
for i in range(10):
    print(i, " ", outputs[i])
result = np.argmax(outputs)
print("La red neuronal predice ", result)
image_array = np.asfarray(img_data).reshape((28, 28))
plt.imshow(image_array, cmap='Greys', interpolation='None')
plt.show()