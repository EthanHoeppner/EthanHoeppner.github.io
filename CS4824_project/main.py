import numpy as np
import tensorflow as tf
import tensorflow.keras.layers as layers
import pickle

# Load MNIST data, and scale it properly
(x_train, y_train),(x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Reduce the size of the training data
training_samples=20000
x_train=x_train[:training_samples,:,:]
y_train=y_train[:training_samples]

# The file by this name is where the accuracies over the training epochs will be stored. This is used for both a readable text file, and a pickled file containing a dictionary
filename = "results"

#Open and close the file, to erase any previous data
file = open(filename + ".txt", "w")
file.close()

# This dict will be used to store the results, and will be pickled at the end of execution so the data can be loaded elsewhere.
results_dict = {}

# Define the default base learning rates for both sgd and adam optimizers. These values are the keras defaults
base_learning_rate = {
  "sgd" : 0.01,
  "adam" : 0.001
}

# Define a dict for sgb and adam optimizers so the functions can be retrieved from the name
optimizer_dict = {
  "sgd" : tf.keras.optimizers.SGD,
  "adam" : tf.keras.optimizers.Adam
}

# Define the base batch size. This doesn't change between optimizers
base_batch_size = 4

# Define the schedules for learning rate and batch size. These should be inverse of one another. Also define the alternate learning rate and batch size schedules for the hybrid training.
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

# Define models
def initializeModels():
  model1 = tf.keras.models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(300, activation=tf.nn.relu),
    layers.Dense(10, activation=tf.nn.softmax)])

  model2 = tf.keras.models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(500, activation=tf.nn.relu),
    layers.Dense(150, activation=tf.nn.relu),
    layers.Dense(10, activation=tf.nn.softmax)])

  model3 = tf.keras.models.Sequential([
    layers.Reshape((28,28,1), input_shape=(28,28)),
    layers.Conv2D(6, (5, 5), activation=tf.nn.relu),
    layers.AveragePooling2D(),
    layers.Conv2D(16, (5, 5), activation=tf.nn.relu),
    layers.AveragePooling2D(),
    layers.Flatten(),
    layers.Dense(120, activation=tf.nn.relu),
    layers.Dense(84, activation=tf.nn.relu),
    layers.Dense(10, activation=tf.nn.softmax)])
  return [model1, model2, model3]

# For each model, create two dicts for storing the accuracy value over time (one for sgd and one for adam). Each dict stores accuracy for each training approach (decreasing learning rate, increasing batch size, and hybrid).
models=initializeModels()
for optimizer_type in ['sgd','adam']:
  for i, model in enumerate(models):
    results_here_dict = {}
    results_here_dict["dlr"] = [0] * training_epochs
    results_here_dict["ibs"] = [0] * training_epochs
    results_here_dict["hyb"] = [0] * training_epochs
    results_dict["Model "+str(i)+" "+optimizer_type]=results_here_dict

# The entire process of training and tracking accuracies is repeated several times, and the average is taken, to ensure the variance is minimized.
trials = 1
for trial in range(trials):
  file = open(filename + ".txt", "a")
  file.write("\n\ntrial "+str(trial+1)+"/"+str(trials)+"\n")
  file.close()
  print("Trial",trial)

  # Models are re-initialized each trial so that the initial weights are randomized differently each time
  models=initializeModels()
  # Run each model once with normal stochastic gradient descent, and once with Adam
  for optimizer_type in ['sgd','adam']:
    file = open(filename + ".txt", "a")
    file.write("Using optimizer "+optimizer_type+"\n")
    file.close()
    # For each model, train on MNIST data using a decreasing learning rate (dlr), then an increasing batch size (ibs), and finally a hybrid approach (hyb)
    for i, model in enumerate(models):
      # Make three copies of the model: one for dlr learing, one for ibs learning, and one for hybryd learning
      dlr_model=tf.keras.models.clone_model(model)
      ibs_model=tf.keras.models.clone_model(model)
      hyb_model=tf.keras.models.clone_model(model)

      # Train model using decreasing learning rate
      print("\nTraining model",i,"with decreasing learning rates...")
      dlr_accuracies = [0] * training_epochs
      for i2 in range(training_epochs):
        # Compile the model. This is done each epoch because the learning rate changes
        dlr_model.compile(optimizer=optimizer_dict[optimizer_type](lr=base_learning_rate[optimizer_type]*learning_rate_schedule[i2]),
          loss='sparse_categorical_crossentropy',
          metrics=['accuracy'])

        dlr_model.fit(x_train, y_train, batch_size=base_batch_size)
        results = dlr_model.evaluate(x_test, y_test)
        dlr_accuracies[i2] = results[1]

      # Compile the model for the ibs training. Unlike the dlr training, learning rate doesn't change for ibs, so this only needs to be done once.
      ibs_model.compile(optimizer=optimizer_dict[optimizer_type](lr=base_learning_rate[optimizer_type]),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy'])

      # Train model using increasing batch size
      print("\nTraining model",i,"with increasing batch sizes...")
      ibs_accuracies = [0] * training_epochs
      for i2 in range(training_epochs):
        ibs_model.fit(x_train, y_train, batch_size=base_batch_size*batch_size_schedule[i2])
        results = ibs_model.evaluate(x_test, y_test)
        ibs_accuracies[i2] = results[1]

      # Train model using a hybrid approach, with both an increasing learning rate and decreasing batch size.
      print("\nTraining model",i,"with hybrid approach...")
      hyb_accuracies = [0] * training_epochs
      for i2 in range(training_epochs):
        # Compile the model. This is done each epoch because the learning rate changes
        hyb_model.compile(optimizer=optimizer_dict[optimizer_type](lr=base_learning_rate[optimizer_type]*hyb_learning_rate_schedule[i2]),
          loss='sparse_categorical_crossentropy',
          metrics=['accuracy'])

        hyb_model.fit(x_train, y_train, batch_size=int(base_batch_size*hyb_batch_size_schedule[i2]))
        results = hyb_model.evaluate(x_test, y_test)
        hyb_accuracies[i2] = results[1]

      print("\nDLR accuracies for model",i,":",dlr_accuracies)
      print("IBS accuracies for model",i,":",ibs_accuracies)
      print("HYB accuracies for model",i,":",hyb_accuracies,"\n")

      # Write accuracies to the output file
      file = open(filename + ".txt", "a")
      file.write("Model "+str(i)+"\ndlr: "+str(dlr_accuracies)+"\nibs: "+str(ibs_accuracies)+"\nhyb: "+str(hyb_accuracies)+"\n")
      file.close()

      # Fill the dictionary for this model with the relevant results
      results_here_dict = {}
      results_here_dict["dlr"] = dlr_accuracies
      results_here_dict["ibs"] = ibs_accuracies
      results_here_dict["hyb"] = hyb_accuracies
      results_dict["Model "+str(i)+" "+optimizer_type]=results_here_dict
      for i3 in range(training_epochs):
        results_dict["Model "+str(i)+" "+optimizer_type]['dlr'] += dlr_accuracies[i3]/trials
        results_dict["Model "+str(i)+" "+optimizer_type]['ibs'] += ibs_accuracies[i3]/trials
        results_dict["Model "+str(i)+" "+optimizer_type]['hyb'] += hyb_accuracies[i3]/trials

pickle_file = open(filename + ".pickle", "wb")
pickle.dump(results_dict, pickle_file)
pickle_file.close()