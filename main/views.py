from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont
# Create your views here.

from .models import Pic


def test(request):

    temp = Pic.objects.all().first()
    print(temp.cover)

    # create Image object with the input image
    image = Image.open('media/'+str(temp.cover))

    # initialise the drawing context with
    # the image object as background

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('main/static/fonts/Roboto-Bold.ttf', size=45)

    # starting position of the message

    (x, y) = (temp.x, temp.y)
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
