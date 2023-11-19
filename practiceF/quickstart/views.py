from django.shortcuts import render
from .models import user_image
from django.views.generic import CreateView
from .forms import user_image_form
""" from .objrecog import resize_image, recognize_func """


# Create your views here.
class user_image_create(CreateView):
    model = user_image
    form_class = user_image_form
    extra_context = {'all_user_image': user_image.objects.all()}
    template_name = 'userimagecreate.html'
    success_url = '/'

def index_page(request):



    data = user_image.objects.all()
    """ object_names = recognize_func() """

    """ data = {
        'all_user_image': all_user_image
    }
 """
    return render(request, 'index.html', {'data': data})

