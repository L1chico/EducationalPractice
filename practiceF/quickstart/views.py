from django.shortcuts import render
from .models import user_image
from django.views.generic import CreateView
from .forms import user_image_form

from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import json
from tensorflow import Graph

img_height, img_width=224,224
with open('practiceF\quickstart\models\imagenet_classes.json','r') as f:
    labelInfo=f.read()

labelInfo=json.loads(labelInfo)

model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model=load_model('practiceF\quickstart\models\MobileNetModelImagenet.h5')

# Create your views here.
class user_image_create(CreateView):
    model = user_image
    form_class = user_image_form
    extra_context = {'all_user_image': user_image.objects.all()}
    template_name = 'userimagecreate.html'
    success_url = '/'

def index_page(request):

    print (request)
    print (request.POST.dict())

    

    all_user_image = user_image.objects.all()

    predictedLabel = []
    predictedLabelresult = []

    """ testimage = 'practiceF'+all_user_image[1].image_downloaded.url

    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x=x/255
    x=x.reshape(1,img_height, img_width,3)
    with model_graph.as_default():
        with tf_session.as_default():
            predi=model.predict(x)

    import numpy as np
    predictedLabel=labelInfo[str(np.argmax(predi[0]))] """

    for i in all_user_image:


        testimage = 'practiceF'+i.image_downloaded.url

        img = image.load_img(testimage, target_size=(img_height, img_width))
        x = image.img_to_array(img)
        x=x/255
        x=x.reshape(1,img_height, img_width,3)
        with model_graph.as_default():
            with tf_session.as_default():
                predi=model.predict(x)

        import numpy as np
        predictedLabel.append(labelInfo[str(np.argmax(predi[0]))])
    
    for i in predictedLabel:
            predictedLabelresult.append(i[1])

    print(predictedLabel)
    print(predictedLabelresult)

    data = {
        'all_user_image': all_user_image
    }

    return render(request, 'index.html', {'data':data,'predictedLabelresult':predictedLabelresult})

