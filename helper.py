import torch
from tqdm import tqdm 

class EarlyStopping:
    def __init__(self,path, patience=5, delta=0.01):
        self.patience = patience
        self.delta = delta
        self.path = path
        self.counter = 0
        self.best_loss = None
        self.early_stop = False

    def __call__(self, val_loss, model):
        if self.best_loss is None:
            self.best_loss = val_loss
            self.save_checkpoint(val_loss, model)
        elif val_loss > self.best_loss - self.delta:
            self.counter += 1
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_loss = val_loss
            self.save_checkpoint(val_loss, model)
            self.counter = 0

    def save_checkpoint(self, val_loss, model):
        torch.save(model.state_dict(), self.path)

class Trainer:
    def __init__(self, model, optimizer, criterion, device, early_stopping):
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.device = device
        self.early_stopping = early_stopping

    def train(self, train_loader, eval_loader, n_epochs):

        for i in tqdm(range(n_epochs)):
            train_loss = 0
            self.model.train()

            for input,target in train_loader:
                input = input.to(self.device)
                target = target.to(self.device)
                
                # forward pass
                self.optimizer.zero_grad()
                outputs = self.model(input)

                # calculate loss
                loss = self.criterion(outputs,target)
                train_loss +=loss.item()
                # backpropagation 
                loss.backward()
                self.optimizer.step()


            
            eval_loss = 0
            self.model.eval()
            with torch.no_grad():
                for input,target in eval_loader:
                    input = input.to(self.device)
                    target = target.to(self.device)
                    
                    # forward pass
                    outputs = self.model(input)

                    loss = self.criterion(outputs,target)
                    eval_loss+=loss.item()
                    # check for early stopping
            
            self.early_stopping(eval_loss, self.model)
            if self.early_stopping.early_stop:
                print("Early stopping")
                break
            
            # eval 
            print(train_loss,eval_loss)
        # return the saved model 
        self.model.load_state_dict(torch.load(self.early_stopping.path))

        return self.model

