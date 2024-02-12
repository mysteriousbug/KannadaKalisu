import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# Assuming mfcc_features is your 2D array of MFCC coefficients
mfcc_tensor = torch.tensor(mfcc_features, dtype=torch.float32)

# Reshape MFCC features to a flat vector
flat_mfcc_features = mfcc_tensor.view(-1)

# Create a simple neural network model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(len(flat_mfcc_features), 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)  # Assuming a binary classification problem

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return torch.sigmoid(x)

model = SimpleModel()

# Define loss and optimizer
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters())

# Train the model (provide appropriate labels/targets for training)
# train_loader = DataLoader(TensorDataset(flat_mfcc_features, labels), batch_size=32, shuffle=True)
# for epoch in range(10):
#     for inputs, targets in train_loader:
#         optimizer.zero_grad()
#         outputs = model(inputs)
#         loss = criterion(outputs, targets)
#         loss.backward()
#         optimizer.step()
