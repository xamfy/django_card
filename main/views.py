from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont
# Create your views here.


def test(request):

        # create Image object with the input image
    image = Image.open('media/images/download.jpeg')

    # initialise the drawing context with
    # the image object as background

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('main/static/fonts/Roboto-Bold.ttf', size=45)

    # starting position of the message

    (x, y) = (400, 400)
    message = "Happy Birthday!"
    color = 'rgb(0, 0, 0)'  # black color

    # draw the message on the background

    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (150, 150)
    name = 'asdfsdfsd'
    color = 'rgb(255, 255, 255)'  # white color
    draw.text((x, y), name, fill=color, font=font)
    # image.show()

    # save the edited image

    image.save('greeting_card.png')
