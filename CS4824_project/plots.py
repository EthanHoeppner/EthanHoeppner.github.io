import matplotlib.pyplot as plt
import pickle
import numpy as np

# This function creates and saves a plot for the data in the provided dictionary. The dictionary should contain three lists, 'dlr', 'hyb', and 'ibs', which correspond to the accuracies at each epoch for training with Decreasing Learning Rate, Hybrid, and Increased Batch Size, respectively.
def plot_accuracy(accuracies, title, display_title):
  dlr=accuracies['dlr']
  hyb=accuracies['hyb']
  ibs=accuracies['ibs']
  plt.clf()
  epochs = len(dlr)
  x = [e + 1 for e in range(epochs)]
  
  plt.ylim(0.8,1)
  plt.plot(x,dlr)
  plt.plot(x,hyb)
  plt.plot(x,ibs)
  plt.ylabel('Test Accuracy')
  plt.xlabel('Number of Epochs')
  plt.title(display_title)
  plt.legend(("Decaying learning rate","Hybrid","Increasing batch size"), loc='lower right')
  plt.savefig(display_title+".png")

# Load the pickled dictionary containing accuracy information. The pickled file is produced by main.py
pickle_file=open("results.pickle", "rb")
accuracies_dict=pickle.load(pickle_file)
pickle_file.close()

# Use the data in the pickled dictionary to produce plots. The pickled dictionary should contain results for 3 different models, each tested with both sgd and adam optimization.
for i in range(3):
  for opt in ['sgd', 'adam']:
    name="Model "+str(i)+" "+opt
    display_name="Architecture "+str(i+1)+" ("+opt+")"
    plot_accuracy(accuracies_dict[name], name, display_name)

# To create plots showing the learning rate and batch size over time for each of the three training approaches, we first create the learning rate and batch size schedules.
learning_rate_schedule = []
batch_size_schedule = []
hyb_learning_rate_schedule = []
hyb_batch_size_schedule = []
for i in range(4):
  for i2 in range(3):
    learning_rate_schedule.append(1 / (5 ** i))
    batch_size_schedule.append(5 ** i)
    hyb_learning_rate_schedule.append(1 / (np.sqrt(5) ** i))
    hyb_batch_size_schedule.append(np.sqrt(5) ** i)

training_epochs = len(learning_rate_schedule)

# Create the plot for learning rate for each of the three approaches
plt.clf()

x = [e + 1 for e in range(training_epochs)]
plt.yscale("log")
plt.plot(x, learning_rate_schedule)
plt.plot(x, hyb_learning_rate_schedule)
plt.plot(x, [1] * training_epochs)
plt.ylabel('Learning Rate Factor')
plt.xlabel('Number of Epochs')
plt.title('Learning rate schedules')
plt.legend(("Decaying learning rate","Hybrid","Increasing batch size"), loc='center left')
plt.savefig("Learning rate schedules.png")

# Create the plot for batch size rate for each of the three approaches
plt.clf()

x = [e + 1 for e in range(training_epochs)]
plt.yscale("log")
plt.plot(x, [1] * training_epochs)
plt.plot(x, hyb_batch_size_schedule)
plt.plot(x, batch_size_schedule)
plt.ylabel('Batch Size Factor')
plt.xlabel('Number of Epochs')
plt.title('Batch size schedules')
plt.legend(("Decaying learning rate","Hybrid","Increasing batch size"), loc='upper left')
plt.savefig("Batch size schedules.png")