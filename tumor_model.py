from keras.models import load_model
from keras.layers import Conv2D

model = load_model('tumorr.keras')
#model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(150, 150, 3)))
def pred_tumor(data):
    a=model.predict(data)
    indices = a.argmax()
    return indices 