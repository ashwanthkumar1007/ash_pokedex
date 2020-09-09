from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import pickle
from django_projects.settings import MEDIAFILES_FOLDER
from tensorflow import Graph
from  tensorflow.compat.v1 import Session
import cv2


model_graph = Graph()
tf_session=Session()

img_height,img_width=96,96
lb = pickle.loads(open("./models/new_lb.pickle", "rb").read())
print(lb)
print(lb.classes_)

model_graph = Graph()
with model_graph.as_default():
    tf_session=Session()
    with tf_session.as_default():
        model=load_model('./models/new_pokedex.MODEL')
       

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        uploaded_file=request.FILES['photo']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        url=fs.url(name)
        file_path=fs.url(name)
        print("**********************")
        print("THE URL ID")
        print(url)
        
        print(name)
        print(file_path)
        test=MEDIAFILES_FOLDER+ file_path
        print("****************")
        print(test)
        print(MEDIAFILES_FOLDER)
        img = cv2.imread(test)
        print("IMAGE READ SUCCESSFULLY")
        print(img)
        img=cv2.resize(img, (96,96))
        x=img_to_array(img)
        x=x.astype("float")/255.0
        x = np.expand_dims(x, axis=0)
        print(x.shape)
        with model_graph.as_default():
            with tf_session.as_default():
                predictions = model.predict(x)
        print(predictions)
        idx = np.argmax(predictions)
        print(lb.classes_)
        label = lb.classes_[idx]
        print(label)
        img_name=label+".png"
        url="media/"+img_name
        print(url)
        print("SUCCESS")
        print(idx)
    return render(request, 'result.html',{'filepath' : url , 'label':label} )

        