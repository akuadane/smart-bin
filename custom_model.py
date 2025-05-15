# Create the model here
import torch


class CustomModel(torch.nn.Module):
    def __init__(self, n_cls):
        super(CustomModel, self).__init__()
        self.n_cls = n_cls
        
        # Convolutional Layers
        self.conv_block1 = torch.nn.Sequential(
            torch.nn.Conv2d(3, 16, kernel_size=3, padding=1),
            torch.nn.BatchNorm2d(16),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),  # Output: 16x112x112
            torch.nn.Dropout(0.3)
        )
        
        self.conv_block2 = torch.nn.Sequential(
            torch.nn.Conv2d(16, 32, kernel_size=3, padding=1),
            torch.nn.BatchNorm2d(32),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),  # Output: 32x56x56
            torch.nn.Dropout(0.3)
        )
        
        self.conv_block3 = torch.nn.Sequential(
            torch.nn.Conv2d(32, 64, kernel_size=3, padding=1),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),  # Output: 64x28x28
            torch.nn.Dropout(0.3)
        )
        
        self.conv_block4 = torch.nn.Sequential(
            torch.nn.Conv2d(64, 128, kernel_size=3, padding=1),
            torch.nn.BatchNorm2d(128),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),  # Output: 128x14x14
            torch.nn.Dropout(0.3)
        )

        # Fully Connected Layers
        self.fc_block = torch.nn.Sequential(
            torch.nn.Flatten(),
            torch.nn.Linear(128 * 14 * 14, 8192),
            torch.nn.BatchNorm1d(8192),
            torch.nn.ReLU(),
            torch.nn.Linear(8192, 4096),
            torch.nn.BatchNorm1d(4096),
            torch.nn.ReLU(),
            torch.nn.Linear(4096, 512),
            torch.nn.BatchNorm1d(512),
            torch.nn.ReLU(),
            torch.nn.Linear(512, self.n_cls)
        )

    def forward(self, x):
        # Pass through convolutional blocks
        x = self.conv_block1(x)
        x = self.conv_block2(x)
        x = self.conv_block3(x)
        x = self.conv_block4(x)
        
        # Pass through fully connected layers
        x = self.fc_block(x)
        return x
  