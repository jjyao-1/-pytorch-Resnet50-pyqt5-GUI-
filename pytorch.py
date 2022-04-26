import torch
import torchvision
from torchvision import datasets, models, transforms
import os
from torch.autograd import Variable
import matplotlib.pyplot as plt
import time
from PIL import Image

#data_dir = '/home/jjyao/下载/archive/test/test'
class Classification:

    def __init__(self,image):
        self.image = image


    def Main(self):

        data_transform = transforms.Compose(
            [transforms.Resize([224,224]),transforms.ToTensor(),transforms.Normalize(mean=[0.5,0.5,0.5],std=[0.5,0.5,0.5])]
        )

        # img_path = '/home/jjyao/下载/archive/test/test/16.jpg'
        # img = Image.open(img_path)

        img = self.image

        img_ = data_transform(img).unsqueeze(0) #拓展维度

        cvd = ['cat','dog']
        #X_example = img_
        #img1 = img_

        # img1 = torchvision.utils.make_grid(img_)
        # img1 = img1.numpy().transpose([1,2,0])

        # plt.imshow(img1)
        # plt.show()

        model = models.resnet50(pretrained= True)
        model.fc = torch.nn.Linear(2048,2)

        model.load_state_dict(torch.load('/home/jjyao/python_files/gui/test/save.pt',map_location=torch.device('cpu')))
        # model.load_state_dict(torch.load(PATH))
        model.eval()

        X = img_
        outputs = model(X)

        _, pred = torch.max(outputs,1)

        #print(cvd[pred])
        return cvd[pred]

