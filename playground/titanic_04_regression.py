import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


titanic = pd.read_csv('data/titanic.csv') 
pd.set_option('display.max_rows', 891)
# fares = titanic["Fare"]  
# high_fares = titanic[(titanic["Fare"] > 400)]                   
# print(high_fares)

# class_1 = titanic[titanic["Pclass"] == 1]                           
# class_23 = titanic[titanic["Pclass"].isin([2, 3])] 

filtered_titanic = titanic[titanic["Fare"] < 150]
print(filtered_titanic.shape[0])

X = np.array(filtered_titanic[["Fare"]]).reshape(-1, 1)
Y = np.array(filtered_titanic[["Survived"]])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)

model = LogisticRegression()
model.fit(X_train, Y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(Y_test, predictions)

beta_0 = model.intercept_[0]
beta_1 = model.coef_[0][0]

plt.scatter(filtered_titanic["Fare"], filtered_titanic["Survived"], alpha=0.5)
plt.xlabel("Fare") 
plt.ylabel("Survived")
plt.title("ticket price VS survival")
plt.plot(X, model.predict(X), color='red', linewidth=1)
plt.show()

plt.hist([filtered_titanic[filtered_titanic['Survived'] == 0]['Fare'], filtered_titanic[filtered_titanic['Survived'] == 1]['Fare']], 
         bins=30, alpha=0.5, label=['Not Survived', 'Survived'])
plt.xlabel("Fare")
plt.ylabel("Count")
plt.legend()
plt.title("Distribution of Fare for Survivors and Non-Survivors")
plt.show()

import seaborn as sns

sns.violinplot(x="Survived", y="Fare", data=filtered_titanic)
plt.title("Violin Plot of Fare for Survivors and Non-Survivors")
plt.show()




#    feels like there are probably better ways to show this data, and while the titanic dats is clearly a classic, 
#    i find myself a bit disenchanted with the limitations - iirc kaggle has slightly more data?  but tbh even so  


