import dlib
from skimage import io
from scipy.spatial import distance
from PIL import Image
import os
import pickle


ENOUGH_DISTANCE = 0.55
PATH = 'C:/Users/jasfe/Desktop/django-face-authentication-master/online_tests/'

sp = dlib.shape_predictor(PATH + 'shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1(PATH + 'dlib_face_recognition_resnet_model_v1.dat')

detector = dlib.get_frontal_face_detector()

def get_descriptor(image_name):
    image = io.imread(image_name)
    dets = detector(image, 1)
    shape = None
    for k, d in enumerate(dets):
        shape = sp(image, d)

    if shape is None:
        return None

    descriptor = facerec.compute_face_descriptor(image, shape)
    
    return descriptor

def recognize(image_name, db_path):
    user_descriptor = get_descriptor(image_name)
    if user_descriptor is None:
        return False

    dir_names = os.listdir(PATH + '/tmp/accepted/')
    for name in dir_names:
        if '.desc' not in name:
            continue
        cur_descriptor = pickle.load(open(PATH + '/tmp/accepted/' + name, 'rb'))

        dist = distance.euclidean(user_descriptor, cur_descriptor)

        if dist < ENOUGH_DISTANCE:
            return True

    return False

def save_descriptors():
    dir_names = os.listdir(PATH + '/tmp/accepted/')
    for name in dir_names:
        if '.desc' in name:
            continue
        cur_descriptor = get_descriptor(PATH + '/tmp/accepted/' + name)
        pickle.dump(cur_descriptor, open(PATH + '/tmp/accepted/' + name + '.desc', 'wb'))

if __name__ == '__main__':
    save_descriptors()