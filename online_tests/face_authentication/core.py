'''import dlib
from skimage import io
from scipy.spatial import distance

ENOUGH_DISTANCE = 0.55
sp = dlib.shape_predictor('/home/andrey/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('/home/andrey/dlib_face_recognition_resnet_model_v1.dat')

def findFace(image, detector, sp):
    dets = detector(image, 1)
    for k,d in enumerate(dets):
        shape = sp(image, d)

    return shape

def recognize(userFace, dbFaces):
    userImage = io.imread(userFace)
    detector = dlib.get_frontal_face_detector()
    shape = findFace(userImage, detector, sp)
    userFaceDescriptor = facerec.compute_face_descriptor(userImage, shape)

    distanceToDbFaces = []
    for dbFace in dbFaces:
        dbImage = io.imread(dbFace)
        shape = findFace(dbImage, detector, sp)
        dbFaceDescriptor = facerec.compute_face_descriptor(dbImage, shape)
        dist = distance.euclidean(userFaceDescriptor, dbFaceDescriptor)
        distanceToDbFaces.append(dist)
    return min(distanceToDbFaces) < ENOUGH_DISTANCE
'''
def recognize(a,b):
    return True
