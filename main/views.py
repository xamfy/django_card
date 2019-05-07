from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

# 3rd party libraries
from PIL import Image, ImageDraw, ImageFont

from .models import Pic, Category


class HomePageView(ListView):
    template_name = "home.html"
    model = Category
    context_object_name = 'categories'
    queryset = Category.objects.all()


class CategoryView(DetailView):
    template_name = "category.html"
    model = Category
    # context_object_name = 'images'
    # queryset = Category.images.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = self.object.images.all()
        context['images'] = images
        return context


def edit(request, pic):

    image = Pic.objects.filter(id=pic).first()
    return render(request, "edit.html", {'image': image})


def generate(request):
    pass
    # print(temp.cover)

    # create Image object with the input image
    # image = Image.open('media/'+str(temp.cover))

    # initialise the drawing context with
    # the image object as background

    # draw = ImageDraw.Draw(image)

    # font = ImageFont.truetype('main/static/fonts/Roboto-Bold.ttf', size=45)

    # starting position of the message

    # (x, y) = (temp.x, temp.y)
    # message = "Happy Birthday!"
    # color = 'rgb(0, 0, 0)'  # black color

    # draw the message on the background

    # draw.text((x, y), message, fill=color, font=font)
    # image.save('greeting_card.png')

    # (x, y) = (150, 150)
    # name = 'asdfsdfsd'
    # color = 'rgb(255, 255, 255)'  # white color
    # draw.text((x, y), name, fill=color, font=font)
    # # image.show()

    # save the edited image
