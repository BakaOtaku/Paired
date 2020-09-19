import tensorflow as tf
import cv2
import os
import skimage
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt

path="asl_alphabet_test/asl_alphabet_test"
for a in os.listdir(path):
    print(a)


image_shape=(64,64,3)
data=[]
label=[]
# loading stuff , put in script
labels_dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,
                   'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,
                   'Z':25,'space':26,'del':27,'nothing':28}
reverse_label_dict={value:key for key,value in labels_dict.items()}

model=tf.keras.models.load_model("asl_predictor.h5")
cap=cv2.VideoCapture(0)
counter=0
lis=[]
counter=0
while(True):

    ret,frame=cap.read()
    data=cv2.rectangle(frame, (50, 50), (300, 300), (0, 255, 0), 0)
    # data=data=[]

    #
    roi_gray=cv2.cvtColor(frame[50:300,50:300],cv2.COLOR_BGR2RGB)
    data_=resize(frame[50:300,50:300],(64,64,3))
    # data_=data_/np.max(data)
    ans=model.predict(data_.reshape(1,64,64,3))
    print(reverse_label_dict[np.argmax(ans)])
    cv2.imshow(f"frame> predicted", data)
    cv2.imshow("other frame",data_)

    # if counter==100000:
    #     break
    # counter+=1

    #
    # # # s=x
    # runner=resize(roi_gray,(64,64,3))
    # s=np.argmax(model.predict(np.reshape(runner,(1,64,64,3))))
    # lis.append(s)
    #
    # cv2.imshow(f"{reverse_label_dict[s]} > predicted value",runner)
    # counter+=1
    # if(counter==500):
    #     l=np.bincount(lis).argmax()
    #     writer=open("hello_world.txt","a")
    #     writer.write(str(l)+" ")
    #     break
# except:
    #     print("the code ended")
    #     # print(np.bincount(lis).argmax())
    #     l = np.bincount(lis).argmax()
    #     writer = open("hello_world.txt", "w+")
    #     writer.write(str(l)+" ")
    #     break

    if(cv2.waitKey(20)&0xFF==ord("q")):
        break
#
# counter+=1
#
# cap.release()
#
#
#
# # reverse_label_dict
#
# # testing shit
# for a in os.listdir(path):
#     label_=list(a.split("_"))[0]
#     image_file=cv2.imread(path+f"/{a}",cv2.COLOR_BGR2RGB)
#     data.append(resize(image_file,output_shape=image_shape))
#     label.append(label_)
#
#
# data=np.asarray(data)
#
#
# tf.keras.utils.plot_model(model,show_shapes=True,to_file="model.png")
#

