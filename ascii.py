from PIL import Image


#CHARS = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
CHARS = '@%#*+=-:. '


def resize(im, width=0):
    w, h = im.size
    ratio = h / w / 1.65

    if not width:
        width = im.size[0]

    height = int(width*ratio)
    resized = im.resize((width, height))

    return resized


def show(im):
    pixels = list(im.getdata())
    output = ""
    for pixel_index in range(len(pixels)):
        if pixel_index % im.size[0] == 0:
            output += "\n"
        output += CHARS[round((pixels[pixel_index] / 255) * (len(CHARS) - 1))]
    print(output)


def main():
    im = Image.open(r"image path")
    grayscale = im.convert("L")
    resized = resize(grayscale)
    show(resized)


main()
