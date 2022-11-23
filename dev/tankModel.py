import sys
from matplotlib import pyplot
# from keras.utils import to_categorical
from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dropout
from keras.layers import Dense
from keras.layers import Flatten
from tensorflow.keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator

import tensorflow as tf
print(tf.test.gpu_device_name())

from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from shutil import copyfile

img_height=224
img_width=224
batch_size=250
train_data_dir = './Images'
train_datagen = ImageDataGenerator(rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2) # set validation split
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training') # set as training data
validation_generator = train_datagen.flow_from_directory(
    train_data_dir, # same directory as training data
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation') # set as validation data

def define_model():
  # load model
  model = VGG16(include_top=False, input_shape=(224, 224, 3))
  # mark loaded layers as not trainable
  for layer in model.layers:
     layer.trainable = False
  # Stacking a new simple convolutional network on top of it    
  x = Conv2D(filters=64, kernel_size=(3, 3), activation='relu')(model.layers[-1].output)
  x = MaxPooling2D(pool_size=(2, 2))(x)
  x = Flatten()(x)
  x = Dense(256, activation='relu')(x)
  x = Dropout(0.5)(x)

  x = Dense(4, activation='softmax')(x)

  from keras.models import Model
  custom_model = Model(inputs=model.inputs, outputs=x)
  custom_model.compile(loss='categorical_crossentropy',
                     optimizer='rmsprop',
                     metrics=['accuracy'])
  return custom_model

tank_model = define_model()

if len(sys.argv) > 1:
    if sys.argv[1] == 'Yes' or 'y' or 'Y' or '1':
        tank_model.summary()
        
        def summarize_diagnostics(history):
            # plot loss
            pyplot.subplot(211)
            pyplot.title('Cross Entropy Loss')
            pyplot.plot(history.history['loss'], color='blue', label='train')
            pyplot.plot(history.history['val_loss'], color='orange', label='test')
            # plot accuracy
            pyplot.subplot(212)
            pyplot.title('Classification Accuracy')
            pyplot.plot(history.history['accuracy'], color='blue', label='train')
            pyplot.plot(history.history['val_accuracy'], color='orange', label='test')
            # save plot to file
            filename = sys.argv[0].split('/')[-1]
            pyplot.savefig(filename + '_plot.png')
            pyplot.close()
        
        history = tank_model.fit(train_generator, steps_per_epoch=len(train_generator),
        validation_data=validation_generator, validation_steps=len(validation_generator), epochs=10, verbose=1)
        
        _, acc = tank_model.evaluate(validation_generator, steps=len(validation_generator), verbose=0)
        print('> %.3f' % (acc * 100.0))