import os
from PIL import Image

# 填充新的 image
def fill_image(image):
    width, height = image.size
    _length = width
    if height > width:
        _length = height
    new_image = Image.new(image.mode, (_length, _length), color='white')
    if width > height:
        new_image.paste(image, (0, int((_length - height) / 2)))
    else:
        new_image.paste(image, (int((_length - width) / 2), 0))
    return new_image

# 裁剪 image
def cut_image(image):
    width, height = image.size
    _width = int(width / 3)
    box_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j * _width, i * _width, (j + 1) * _width, (i + 1) * _width)
            box_list.append(box)
            image_list = [image.crop(box) for box in box_list]
    return image_list

# 将 image 列表的里面的图片保存
def save_images(image_list, res_dir):
    index = 1
    if not os.path.exists(res_dir):
        os.mkdir(res_dir)
    for image in image_list:
        new_name = os.path.join(res_dir, str(index) + '.png')
        image.save(new_name, 'PNG')
        index += 1
    print('图片保存完毕！')


if __name__ == '__main__':
    image = Image.open('test.jpg')
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list, 'imgs')