import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from PIL import Image
from torchvision.datasets import ImageFolder

data_dir = 'Braille Dataset'
dataset = ImageFolder(data_dir, transform=transforms.Compose([
    transforms.Resize((28, 28)), transforms.ToTensor()]))
img = dataset[1550][0]
print(img.shape)

def braille(e):
    criterion = nn.CrossEntropyLoss()

    # optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.conv1 = nn.Conv2d(3, 6, 5)  # 1 convolutional layer
            self.fc1 = nn.Linear(6 * 24 * 24, 24)  # 1/2 linear layers
            self.fc2 = nn.Linear(24, 26)  # 2/2 linear layers

        def forward(self, x):
            x = (F.relu(self.conv1(x)))
            print(x.shape)
            x = x.view(1560, 6 * 24 * 24)
            x = F.relu(self.fc1(x))
            x = self.fc2(x)
            return x

    net = Net()
    optimizer = optim.Adam(net.parameters(), lr=0.001)
    inputs = []
    inputs = torch.tensor(inputs)
    labels = [];
    for item in dataset:
        inputs = torch.cat((inputs, item[0]))
        labels.append(item[1])

    # inputs = torch.Tensor(inputs)
    inputs = inputs.reshape(1560, 3, 28, 28)
    labels = torch.Tensor(labels)
    labels = labels.type(torch.LongTensor)
    print(labels.shape)
    for epoch in range(e):  # iterations over the training data
        running_loss = 0.0
        running_corrects = 0

        # zero the parameter gradients
        optimizer.zero_grad()

        # change the weights
        outputs = net(inputs)
        _, preds = torch.max(outputs, 1)
        print(outputs.shape)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # print stats
        running_loss += loss.item()
        running_corrects += torch.sum(preds == labels).item()
        if epoch % 10 == 0:
            print('[%d] accuracy: %3.2f %%' % (epoch + 1, 100 * running_corrects / len(labels)))

    print('Finished Training')
braille(100)



