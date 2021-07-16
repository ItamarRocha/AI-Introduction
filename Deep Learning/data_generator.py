import numpy as np
import random

def generate_losangles(data_size, quadrant):
  points = []
  for _ in range(data_size):
    if quadrant == 0:
      x = random.uniform(0,1)
      y = random.uniform(0,1-x)
      points.append([x,y,quadrant])

    if quadrant == 1:
      x = random.uniform(-1,0)
      y = random.uniform(0,x+1)
      points.append([x,y,quadrant])

    if quadrant == 2:
      x = random.uniform(0,1)
      y = random.uniform(-1+x, 0)
      points.append([x,y,quadrant])

    if quadrant == 3:
      x = random.uniform(-1,0)
      y = random.uniform(-1-x, 0)
      points.append([x,y,quadrant])

  return points

def generate_edges(data_size, quadrant):
  points = []

  for _ in range(data_size):

    if quadrant == 0:
      x = random.uniform(0,1)
      y = random.uniform(1-x, np.sqrt(1 - x**2))
      points.append([x,y,quadrant+4])

    if quadrant == 1:
      x = random.uniform(-1,0)
      y = random.uniform(1+x, np.sqrt(1 - x**2))
      points.append([x,y,quadrant+4])    

    if quadrant == 2:
      x = random.uniform(-1,0)
      y = random.uniform(-np.sqrt(1 - x**2), -1 - x)
      points.append([x,y,quadrant+4])        

    if quadrant == 3:
      x = random.uniform(0,1)
      y = random.uniform(-np.sqrt(1 - x**2), -1 + x)
      points.append([x,y,quadrant+4])    

  return points

def get_data(size=500, train_test_split=0.2):
    quadrants = [0,1,2,3]
    data_train = []
    data_test = []
    amount_test = int(size * train_test_split)
    amount_train = size - amount_test

    for quadrant in quadrants:
        data_train.extend(generate_losangles(amount_train,quadrant))
        data_test.extend(generate_losangles(amount_test,quadrant))
        data_train.extend(generate_edges(amount_train,quadrant))
        data_test.extend(generate_edges(amount_test,quadrant))

    data_train = np.array(data_train, dtype=np.float32)
    data_test = np.array(data_test, dtype=np.float32)

    X_train = data_train[:,[0,1]]
    y_train = data_train[:,2]
    X_test = data_test[:,[0,1]]
    y_test = data_test[:,2]

    return X_train, X_test, y_train, y_test