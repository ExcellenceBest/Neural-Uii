from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
model = Sequential()
model.add(Dense(32, input_dim=10))
model.add(Dense(5))
model.add(Dense(1))
model.compile()
weights = model.get_weights()  # Получим веса нашей модели (генерируются случайным образом)
# print(weights)
print(weights.ndim())
# model.summary()
