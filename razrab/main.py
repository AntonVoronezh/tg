from PIL import Image, ImageDraw, ImageFont

def text_color(output_path):
    image = Image.open(output_path)
    draw = ImageDraw.Draw(image)

    # text_isx = 'Любой вид взаимоотношений – как песок, который вы держите в руке. Держите свободно, в открытой руке – и песок остается в ней. В тот момент, когда вы сожмете крепко руку, песок начнет высыпаться сквозь ваши пальцы. Таким образом вы можете удержать немного песка, но большая часть просыплется.'
    # text_isx = 'Когда ты бросил меня, я в телефоне переименовала тебя в НИКТО, только жаль что с сердцем такое проделать нельзя…'
    text_isx = 'Когда не знаешь как поступить – поступи по-человечески.'
    print(len(text_isx))
    if len(text_isx) > 250:
        size = 35
        chunk = 20
        text_left = 350
        text_top = 50

    if len(text_isx) >100 and len(text_isx) < 150:
        size = 50
        chunk = 10
        text_left = 170
        text_top = 30

    if len(text_isx) < 100:
        size = 65
        chunk = 5
        text_left = 10
        text_top = 70

    font = ImageFont.truetype("comicz.ttf", size=size)
    text = text_isx.split(' ')
    arr = [[]]
    count = 0

    for i ,f in enumerate(text):
        # print(i, f)
        if (count + len(f)) <= chunk:
            arr[-1].append(f)
            count = count + len(f)
        else:
            count = 0
            arr.append([f'\n {f}'])

    text_out = ' '.join([j for i in arr for j in i])
    print(text_out)
    # f5b105
    draw.text((text_left,text_top), f' {text_out}', '#000', font, align ="left")
    image_crop = image.crop((0, 0, 800, 600))
    image_crop.save(f'{output_path}.png', "PNG")


text_color("back_1.jpg")