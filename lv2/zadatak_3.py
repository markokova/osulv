import numpy as np
import matplotlib.pylab as plt
import PIL
from PIL import Image

image = Image.open('road.jpg')
image.show()

imageAsArray = np.asarray(image)

brightImageAsArray = imageAsArray + 50
brightImageAsArray[brightImageAsArray > 255] = 255

brightImage = Image.fromarray(brightImageAsArray)
brightImage.show()
#b)
quarter = imageAsArray[0:int((image.height/2)), int((image.width/2)):int((image.width))]
quarterImage = Image.fromarray(quarter)
quarterImage.show()
#c)
rotatedImage = image.rotate(-90, expand=True)
rotatedImage.show()
#d)
mirroredImage = image.transpose(method=Image.FLIP_LEFT_RIGHT)
mirroredImage.show()