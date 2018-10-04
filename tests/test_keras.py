import json
from keras.applications.mobilenet import MobileNet
from imagetagger.worker import predict


def test_predict():
    model = MobileNet(weights='imagenet')
    with open('tests/data/aircraft.jpg', 'rb') as f:
        img = f.read()
    resp = predict(img, model)
    data = json.loads(resp.decode('utf-8'))
    assert data['success']
    assert data['predictions'][0]['label']
