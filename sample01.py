from base64 import b64encode
from sys import argv
import json
import requests
from PIL import Image,ImageFont,ImageDraw

def face_ditection(resp, im):
    LIKELIHOOD = {'UNKOWN': '%s不明',
           'VERY_UNLIKELY': '%s0点',
           'UNLIKELY': '%s25点',
           'POSSIBLE': '%s50点',
           'LIKELY': '%s75点',
           'VERY_LIKELY': '%s100点'}

    draw = ImageDraw.Draw(im)

    for fa in resp["faceAnnotations"]:
        v = fa["fdBoundingPoly"]

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
        draw.rectangle((min(x), min(y), max(x), max(y)), outline=(255, 255, 255),width=2)

        font = ImageFont.truetype("HGRGE.TTC", 14)

        draw.text((min(x) + 5, min(y) + 5),LIKELIHOOD[ fa["joyLikelihood"] ]%'楽しさ　',fill=(255,255,255) ,font=font)
        draw.text((min(x) + 5, min(y) + 5 + 15), LIKELIHOOD[fa["sorrowLikelihood"]] % '悲しさ　', fill=(255, 255, 255), font=font)
        draw.text((min(x) + 5, min(y) + 5 + 30), LIKELIHOOD[fa["angerLikelihood"]] % '怒り　　', fill=(255, 255, 255), font=font)
        draw.text((min(x) + 5, min(y) + 5 + 45), LIKELIHOOD[fa["surpriseLikelihood"]] % '驚き　　', fill=(255, 255, 255), font=font)

    im.show()

if __name__ == '__main__':

    ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
    API_KEY = ''
    FILE_NAME ="images/toshimio01.jpg"

    img_requests = []

    with open( FILE_NAME ,'rb' ) as f:
        ctxt = b64encode(f.read()).decode()

        img_requests.append({
            'image':{'content':ctxt},
            'features':[
                {
                    'type' : 'FACE_DETECTION',
                    'maxResults' : 5
                }
            ]
        })

    response = requests.post(ENDPOINT_URL,
                         data=json.dumps({'requests':img_requests}).encode(),
                         params={'key':API_KEY},
                         headers={'Content-Type':'application/json'})

    resp = response.json()['responses'][0]
    im = Image.open(FILE_NAME)
    face_ditection( resp , im )
