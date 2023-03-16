from PIL import Image


def s16_126():
    mac = Image.open('example.jpg')
    # print(type(mac))
    # mac.show()

    print(mac.size)
    print(mac.filename)
    print(mac.format_description)

    # Cropping images
    # mac.crop((0,0,100,100)).show("Cropped image 100x100")
    pencils = Image.open('pencils.jpg')
    print(pencils.size)
    x = 0
    y = 0
    w = pencils.size[0] / 3
    h = pencils.size[1] / 10
    print(x, y, w, h)
    # pencils.crop((x,y,w,h)).show("Cropped pencils")

    # Bottom pencils
    x = 0
    y = pencils.size[1] * 0.84616  # 84.6%
    w = pencils.size[0] / 3
    h = pencils.size[1]
    # pencils.crop((x,int(y),int(w),h)).show("Cropped pencils")

    # Crop computer
    halfway = mac.size[0] / 2
    x = halfway - 200
    w = halfway + 200
    y = 800
    h = 1257
    print(x, y, w, h)
    computer = mac.crop((x, y, w, h))
    mac.paste(im=computer, box=(0, 0))
    # mac.show()
    # mac.resize((1000,300)).show()
    # mac.rotate(90).show()

    # Color transparency
    red = Image.open('red_color.jpg')
    # red.show()
    blue = Image.open('blue_color.png')
    print(type(blue))
    red.putalpha(128)
    # red.show()
    blue.paste(im=red,box=(0,0),mask=red)
    # blue.save('purple-2.png')


if __name__ == '__main__':
    s16_126()
