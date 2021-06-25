from PIL import Image

size = (128, 128)
img = Image.open('1.jpg')
img.thumbnail(size)
# 旋转45度
img.rotate(45).show()
