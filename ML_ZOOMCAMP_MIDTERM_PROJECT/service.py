import numpy as np
import bentoml
from bentoml.io import NumpyNdarray
from bentoml.io import JSON

model_ref = bentoml.xgboost.get("solar_eclipse_classification:v62r4ms7n6weefja")

min_max_scaler = model_ref.custom_objects['minmaxscaler']
transformer = model_ref.custom_objects['normalizer']
le = model_ref.custom_objects['labelencoder']

model_runner = model_ref.to_runner()

svc = bentoml.Service("solar_eclipse_classification", runners=[model_runner])

@svc.api(input=NumpyNdarray(shape=(-1,21), enforce_shape=True), output=JSON())
def classify(application_data):
    vector = min_max_scaler.transform(application_data)
    vector2 = transformer.transform(vector)
    prediction = model_runner.predict.run(vector2)
    result = le.inverse_transform(prediction)
    final = result[0]
    if final == "A":
            return "Annular Eclipse"
    elif final == "P":
        return "Partial Eclipse"
    elif final == "T":
        return "Total Eclipse"
    else:
        return "Hybrid Eclipse"        