import bentoml

from bentoml.io import NumpyNdarray

model_ref2 = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")

model_runner2 = model_ref2.to_runner()

svc_b = bentoml.Service("mlzoomcamp_homework5b", runners = [model_runner2])

@svc_b.api(input=NumpyNdarray(), output=NumpyNdarray())
async def classify_b(vector):
    prediction = await model_runner2.predict.async_run(vector)
    return prediction