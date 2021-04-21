import numpy as np
import tensorflow as tf
from keras.preprocessing import image
import argparse

def preprocess(img_path):

    ''' Preprocessing the image for prediction '''

    test_image = image.load_img(img_path)
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis =0)
    return test_image

def predict(model, img_path):

    ''' Method for performing prediction with a model of the user's choice '''

    test_image = preprocess(img_path)
    prediction = model.predict(test_image)

    if prediction[0][0] == 1:
        print('Entered image is a Dog')
    
    else:
        print('Entered image is a Cat')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Image-Classification-using-CNN')

    parser.add_argument('--img', '-i', help='path to image')
    parser.add_argument('--model', '-m', help='path to model')

    args = parser.parse_args()

    model = tf.keras.models.load_model(args.model)

    ''' Calling method to perform prediction '''
    predict(model, args.img)
