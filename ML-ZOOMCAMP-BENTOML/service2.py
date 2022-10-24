import bentoml

from bentoml.io import NumpyNdarray

model_ref1 = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")

model_runner1 = model_ref1.to_runner()

svc_a = bentoml.Service("mlzoomcamp_homework5", runners = [model_runner1])

@svc_a.api(input=NumpyNdarray(), output=NumpyNdarray())
async def classify_a(vector):
    prediction = await model_runner1.predict.async_run(vector)
    return prediction