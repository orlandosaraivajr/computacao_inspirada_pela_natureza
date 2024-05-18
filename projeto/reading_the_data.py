import pandas as pd
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X =  pd.read_pickle("./features.pkl")
y =  pd.read_pickle("./targets.pkl")

for rand_state in range(1,200):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=rand_state)
    perceptron = Perceptron(max_iter=1000, random_state=rand_state)
    perceptron.fit(X_train, y_train)

    y_pred_test = perceptron.predict(X_test)
    print("Random State: ", str(rand_state) + "   ", accuracy_score(y_test, y_pred_test) )

# dado = np.ndarray((1,4), buffer=np.array([152,276, 152, 276]),dtype=int)
# dado = np.ndarray((1,4), buffer=np.array([152,276, 152, 276]),dtype=int)