from base64 import b64encode
from sys import argv
import json
import requests
from PIL import Image
from PIL import ImageDraw

def face_ditection( resp , im ):
    LIKELIHOOD = {'UNKOWN': '%sかわからない',
           'VERY_UNLIKELY': '全く%sでない',
           'UNLIKELY': '%sでない',
           'POSSIBLE': 'まぁまぁ%s',
           'LIKELY': '%s！',
           'VERY_LIKELY': 'とても%s'}

    draw = ImageDraw.Draw(im)

    for fa in resp["faceAnnotations"]:
        v = fa["boundingPoly"]

        v_list = v["vertices"]
        x = []
        y = []
        for item in v_list:
            try:
                x.append(item["x"])
            except KeyError:
                x.append( 0 )
            try:
                y.append(item["y"])
            except KeyError:
                y.append( 0 )
        draw.rectangle((min(x), min(y), max(x), max(y)), outline=(255, 0, 0))
        print( LIKELIHOOD[ fa["joyLikelihood"] ]%'楽しそう' )
        print( LIKELIHOOD[ fa["sorrowLikelihood"]]%'悲しそう' )
        print( LIKELIHOOD[ fa["angerLikelihood"]]%'怒ってそう' )
        print( LIKELIHOOD[ fa["surpriseLikelihood"]]%'驚いてそう' )

    im.show()

if __name__ == '__main__':
    resp = {'faceAnnotations': [{'boundingPoly': {
        'vertices': [{'x': 248, 'y': 229}, {'x': 415, 'y': 229}, {'x': 415, 'y': 422}, {'x': 248, 'y': 422}]},
                                 'fdBoundingPoly': {
                                     'vertices': [{'x': 259, 'y': 287}, {'x': 395, 'y': 287}, {'x': 395, 'y': 423},
                                                  {'x': 259, 'y': 423}]}, 'landmarks': [
            {'type': 'LEFT_EYE', 'position': {'x': 299.83426, 'y': 329.83255, 'z': 0.0011867527}},
            {'type': 'RIGHT_EYE', 'position': {'x': 357.74362, 'y': 330.87518, 'z': -0.79565316}},
            {'type': 'LEFT_OF_LEFT_EYEBROW', 'position': {'x': 288.45728, 'y': 318.53918, 'z': 1.5632429}},
            {'type': 'RIGHT_OF_LEFT_EYEBROW', 'position': {'x': 317.41415, 'y': 322.85184, 'z': -12.65791}},
            {'type': 'LEFT_OF_RIGHT_EYEBROW', 'position': {'x': 341.20587, 'y': 323.16382, 'z': -13.054339}},
            {'type': 'RIGHT_OF_RIGHT_EYEBROW', 'position': {'x': 370.5553, 'y': 319.78723, 'z': 0.3767877}},
            {'type': 'MIDPOINT_BETWEEN_EYES', 'position': {'x': 329.1133, 'y': 333.07224, 'z': -10.715899}},
            {'type': 'NOSE_TIP', 'position': {'x': 328.5967, 'y': 364.00595, 'z': -16.45281}},
            {'type': 'UPPER_LIP', 'position': {'x': 328.63007, 'y': 377.49994, 'z': -0.65718085}},
            {'type': 'LOWER_LIP', 'position': {'x': 328.68192, 'y': 392.47385, 'z': 7.4609346}},
            {'type': 'MOUTH_LEFT', 'position': {'x': 305.7939, 'y': 378.63, 'z': 15.187313}},
            {'type': 'MOUTH_RIGHT', 'position': {'x': 352.09778, 'y': 380.38782, 'z': 14.731333}},
            {'type': 'MOUTH_CENTER', 'position': {'x': 328.6772, 'y': 383.33582, 'z': 4.9306755}},
            {'type': 'NOSE_BOTTOM_RIGHT', 'position': {'x': 344.83292, 'y': 363.24332, 'z': 3.2518535}},
            {'type': 'NOSE_BOTTOM_LEFT', 'position': {'x': 311.8429, 'y': 362.78134, 'z': 3.8425305}},
            {'type': 'NOSE_BOTTOM_CENTER', 'position': {'x': 328.5181, 'y': 368.4146, 'z': -3.581519}},
            {'type': 'LEFT_EYE_TOP_BOUNDARY', 'position': {'x': 304.69797, 'y': 328.8072, 'z': -4.1870885}},
            {'type': 'LEFT_EYE_RIGHT_CORNER', 'position': {'x': 310.29538, 'y': 331.91776, 'z': 0.411874}},
            {'type': 'LEFT_EYE_BOTTOM_BOUNDARY', 'position': {'x': 299.7468, 'y': 333.2134, 'z': 0.55466366}},
            {'type': 'LEFT_EYE_LEFT_CORNER', 'position': {'x': 293.6, 'y': 329.45917, 'z': 4.870285}},
            {'type': 'LEFT_EYE_PUPIL', 'position': {'x': 303.89468, 'y': 331.45685, 'z': -1.3648899}},
            {'type': 'RIGHT_EYE_TOP_BOUNDARY', 'position': {'x': 353.90396, 'y': 329.5725, 'z': -4.888189}},
            {'type': 'RIGHT_EYE_RIGHT_CORNER', 'position': {'x': 364.77872, 'y': 330.82513, 'z': 3.8665755}},
            {'type': 'RIGHT_EYE_BOTTOM_BOUNDARY', 'position': {'x': 356.849, 'y': 334.82312, 'z': -0.13107164}},
            {'type': 'RIGHT_EYE_LEFT_CORNER', 'position': {'x': 346.54285, 'y': 333.31818, 'z': 0.018443458}},
            {'type': 'RIGHT_EYE_PUPIL', 'position': {'x': 354.2796, 'y': 332.30905, 'z': -2.1703992}},
            {'type': 'LEFT_EYEBROW_UPPER_MIDPOINT', 'position': {'x': 302.90363, 'y': 315.92957, 'z': -10.569097}},
            {'type': 'RIGHT_EYEBROW_UPPER_MIDPOINT', 'position': {'x': 356.00964, 'y': 316.6922, 'z': -11.326627}},
            {'type': 'LEFT_EAR_TRAGION', 'position': {'x': 274.00116, 'y': 336.0918, 'z': 66.10024}},
            {'type': 'RIGHT_EAR_TRAGION', 'position': {'x': 392.26053, 'y': 337.85696, 'z': 68.67234}},
            {'type': 'FOREHEAD_GLABELLA', 'position': {'x': 329.25293, 'y': 322.9822, 'z': -14.874377}},
            {'type': 'CHIN_GNATHION', 'position': {'x': 328.41492, 'y': 411.931, 'z': 20.091923}},
            {'type': 'CHIN_LEFT_GONION', 'position': {'x': 278.90634, 'y': 371.37848, 'z': 55.86849}},
            {'type': 'CHIN_RIGHT_GONION', 'position': {'x': 379.99863, 'y': 373.33087, 'z': 54.373734}}],
                                 'rollAngle': 0.6159847, 'panAngle': -0.8741758, 'tiltAngle': -16.380037,
                                 'detectionConfidence': 0.9332564, 'landmarkingConfidence': 0.5778821,
                                 'joyLikelihood': 'LIKELY', 'sorrowLikelihood': 'VERY_UNLIKELY',
                                 'angerLikelihood': 'VERY_UNLIKELY', 'surpriseLikelihood': 'VERY_UNLIKELY',
                                 'underExposedLikelihood': 'VERY_UNLIKELY', 'blurredLikelihood': 'VERY_UNLIKELY',
                                 'headwearLikelihood': 'VERY_UNLIKELY'}]}

    im = Image.open('images/mio02.jpg')
    face_ditection( resp , im )