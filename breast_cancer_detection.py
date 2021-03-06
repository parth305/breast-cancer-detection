from sklearn.datasets import load_breast_cancer
Data=load_breast_cancer()

print(Data)

features=Data.data
target=Data.target

print(features.shape)
print(target.shape)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(features,target,test_size=0.2)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

from keras.models import Sequential
from keras.layers import Dense

model=Sequential()
model.add(Dense(32,input_dim=30,activation='relu'))
model.add(Dense(64,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.summary()

model.fit(x_train,y_train,epochs=10)

score=model.evaluate(x_test,y_test)
print(score)

predictions=model.predict(x_train)

for p in predictions:
  if p>=0.5:
    print("Malignent")
  else:
    print("Benign")
