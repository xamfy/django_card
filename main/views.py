from django.shortcuts import render, reverse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

# 3rd party libraries
from PIL import Image, ImageDraw, ImageFont

from django.http import HttpResponseRedirect, HttpResponse

from .models import Pic, Category

import secrets
import string

from main import forms


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
    if request.method == "POST":
        form = forms.GenerateForm(request.POST)
        pic = Pic.objects.filter(id=pic).first()
        if form.is_valid():
            name = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                           for _ in range(10))
            image = Image.open('media/'+str(pic.cover))

            draw = ImageDraw.Draw(image)

            aux_font = 'main/static/fonts/'+str(pic.font)+'.ttf'
            # print(aux_font)

            font = ImageFont.truetype(
                aux_font, size=pic.size)

            print(font)

            (x, y) = (pic.x, pic.y)

            message = form.cleaned_data['name']

            # color = 'rgb(0, 0, 0)'  # black color

            draw.text((x, y), message, fill=pic.color, font=font)
            image.save('media/generated/'+name+'.jpg')
            print(name)

        form = forms.GenerateForm()
        src = 'media/generated/'+name
        # return reverse('generate', kwargs={'pic': name})
        return HttpResponseRedirect(reverse('generate', kwargs={'pic': name}))

    else:
        image = Pic.objects.filter(id=pic).first()
        form = forms.GenerateForm()
        return render(request, "edit.html", {'form': form, 'image': image})


def generate(request, pic):
    pic = '/media/generated/'+pic+'.jpg'
    return render(request, "generated.html", {'src': pic})
