**PROJECT TITLE - Solar Eclipse Classification**
        
<img src = "https://github.com/Regidan-codes/ML-ZOOMCAMP2022/blob/main/ML_ZOOMCAMP_MIDTERM_PROJECT/solareclipse.png" width="500">

**DATASET**

- The data was taken from [Kaggle](https://www.kaggle.com/datasets/nasa/solar-eclipses?select=solar.csv)
- There were 11898 solar eclipses during the five millennium period from 2000 BC to 3000 CE 

**Features**

| Heading | Descriptions | 
| ------ | ------ | 
| ΔT  | Sequential number of the eclipse |
| Luna Num  | Lunation Number is the number of synodic months since New Moon of 2000 Jan 06.|
| Saros-Number | Saros series number of eclipse. |
| Gamma  | Distance of the shadow cone axis from the center of Earth|
| Ecl. Mag | Eclipse magnitude is the fraction of the Sun's diameter obscured by the Moon. |
| Sun Alt  | Sun's altitude at greatest eclipse |
| Sun Azm  | Sun's azimuth at greatest eclipse. |
| Path Width | Width of the path of totality or annularity at greatest eclipse  |
| Calendar Date  | Calendar Date at instant of Greatest Eclipse. |
| TD of Greatest Eclipse | Dynamical Time (TD) of Greatest Eclipse |

**CONTEXT** 

Eclipses of the sun can only occur when the moon is near one of its two orbital nodes during the new moon phase. 
It is then possible for the Moon's penumbral, umbral, or antumbral shadows to sweep across Earth's surface thereby producing an eclipse. 
There are four types of solar eclipses: a partial eclipse, during which the moon's penumbral shadow traverses Earth and umbral and antumbral 
shadows completely miss Earth; an annular eclipse, during which the moon's antumbral shadow traverses Earth but does not completely cover the sun;
a total eclipse, during which the moon's umbral shadow traverses Earth and completely covers the sun; and a hybrid eclipse, 
during which the moon's umbral and antumbral shadows traverse Earth and annular and total eclipses are visible in different locations. 
Earth will experience 11898 solar eclipses during the five millennium period -1999 to +3000 (2000 BCE to 3000 CE).

**GOAL** - The aim of this project is to classify among the main types of Solar eclipses, which are 

1) P = Partial Eclipse
2) A = Annular Eclipse
3) T = Total Eclipse
4) H = Hybrid or Annular/Total Eclipse.


**WHAT I HAVE DONE**

- Loading datasets
- Handling null values
- Dealing with the target variable and extracting only the main types of eclipses
- Dealing with the Calender Date column
- Extracting the year, month and date values
- Dealing with the Eclipse Time column
- Changing into Datetime format
- Extracting the hour, minutes and seconds
- Dealing with Latitude and Longitude Column
- Extracting the longitude and latitude numeric value and direction
- Dealing with the Central Duration column
- Extracting the minutes and seconds
- Performing One Hot Encoding on the categorical columns
- Performing Label Encoding on the categorical columns
- Converting the object data types into numeric data types
- Visualization of the independent features
- Heatmap of the correlation matrix

<img src = "https://github.com/Regidan-codes/ML-ZOOMCAMP2022/blob/main/ML_ZOOMCAMP_MIDTERM_PROJECT/correlationmatrix.png" width="500">

- Performing Feature Scaling
- Splitting the data
- Using Logistic Regression
- Using Random Forest Algorithm
- Using Support Vector Machine(SVM)
- Using XGBoost
- Hyperparameter Tuning using RandomisedSearchCV and Random Forest

**BENTOML**

- After choosing best model I saved the trained model with BentoML API in its model store (a local directory managed by BentoML). 
- You can check service.py for runner models and custom objects.
- Later ran the BentoML server using service.py 
- After service definition is finalized, I build the model and served into a bento. You can check below the files created automatically by bentoml.

<img src = "https://github.com/Regidan-codes/ML-ZOOMCAMP2022/blob/main/ML_ZOOMCAMP_MIDTERM_PROJECT/bentoml_tree.png" width="500">

- Later used Dockerfile created by bento to containerize the model.
- Uploaded the image to DockerHub

**Azure For Deployment**

- Uploaded docker image from docker hub to azure container registry
- Used the model saved in Azure registry to create a web app.
- You can check the web app below.


**MODELS USED**

- Logistic Regression - *A simple classification algorithm that measures the probability of a binary response as the value of response variable based on the mathematical equation relating it with the predictor variables.* 
- XGBoost - *Extreme Gradient Boost alsorithm is based on the Gradient Boosting model which uses the boosting technique of ensemble learning where the underfitted data of the weak learners are passed on to the strong learners to increase the strength and accuracy of the model.*
- Support Vector Machine - *SVM is a supervised machine learning algorithm used for both classification and regression. The objective of SVM algorithm is to find a hyperplane in an N-dimensional space that distinctly classifies the data points.*
- Random Forest - *This algorithm works on the concept of emsemble learning.It used bagging technique to train multiple predictors on the same sampled instances to achieve a higher degree of accuracy.*
- RandomisedSearchCV - *This is a hyperparameter optimistion algorithm that increases the model accuracy by tweaking the hyperparameters to their best values*


**LIBRARIES NEEDED**

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- datetime
- re
- scikit learn
- xgboost


**Conclusion**

| Algorithm | F1-SCORE | 
| ------ | ------ | 
| Logistic Regression  | 0.85 |
| Random Forest Algorithm | 0.96 |
| Support Vector Machine(SVM) | 0.89 |
| XGBoost | 0.98 |
| Hyperparameter Tuning using RandomisedSearchCV | 0.97 |

In this project we have performed a exploratory data analysis of the given dataset to extract all the numeric values from the dataframe, 
preprocess them and lastly feed them to different classifier models. As my hyper parameter tuned model using randomforest classifer wasn't better 
than XGBoost I chose XGBoost as my final model.
After performing the comaparative analysis we can conclude that XGBoost model performed best both on the training and testing set thus giving 
predictions with a validation accuracy of 98.12%.

**What you have to do**

**OPTION 1**

Clone repository and export conda environment:

```
conda env create -n ENVNAME --file environment.yml

```
- Run the [notebook](https://github.com/Regidan-codes/ML-ZOOMCAMP2022/blob/main/ML_ZOOMCAMP_MIDTERM_PROJECT/Solar_Eclipse_Classification.ipynb)
- Run [service.py](https://github.com/Regidan-codes/ML-ZOOMCAMP2022/blob/main/ML_ZOOMCAMP_MIDTERM_PROJECT/service.py) with updated tag locally.
- You can use the API by simply opening a browser to http://localhost:3000


**OPTION 2**

- Pull the image from docker hub
~~~
docker pull regidancodes/first_image
~~~

-Run it

~~~
docker run -it --rm -p 3000:3000 regidancodes/first_image serve --production
~~~

- You can test it by simply opening a browser to http://localhost:3000


**Option 3**

- You can test the web app I deployed to Azure [Web App](https://solareclipse.azurewebsites.net)
- Video link on how to test is [here](https://youtu.be/RU5SjAo1Zu8)












