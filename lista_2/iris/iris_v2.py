import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import mean_squared_error
from ucimlrepo import fetch_ucirepo 

# Carregar o conjunto de dados Iris
iris = fetch_ucirepo(id=53) 
X = iris.data.features 
y = iris.data.targets 

# Convertendo rótulos das classes em valores numéricos
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Dividir o conjunto de dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=35)
X_validation, X_test, y_validation, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=35)

# Padronizar os recursos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_validation = scaler.transform(X_validation)

# Inicializar o Perceptron
perceptron = Perceptron(max_iter=1000, random_state=35)

# Listas para armazenar o histórico do MSE
mse_train_history = []
mse_test_history = []
mse_validation_history = []

# Treinamento do Perceptron e cálculo do MSE em cada época
for epoch in range(1, perceptron.max_iter + 1):
    perceptron.partial_fit(X_train, y_train, classes=np.unique(y))
    y_train_pred = perceptron.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_pred)
    mse_train_history.append(mse_train)

    y_validation_pred = perceptron.predict(X_validation)
    mse_test = mean_squared_error(y_validation, y_validation_pred)
    mse_validation_history.append(mse_test)
    
    y_test_pred = perceptron.predict(X_test)
    mse_test = mean_squared_error(y_test, y_test_pred)
    mse_test_history.append(mse_test)

# Plotar o MSE ao longo das épocas e salvar a imagem
plt.plot(range(1, perceptron.max_iter + 1), mse_train_history, label='Train MSE')
plt.plot(range(1, perceptron.max_iter + 1), mse_test_history, label='Test MSE')
plt.plot(range(1, perceptron.max_iter + 1), mse_validation_history, label='Validation MSE')
plt.xlabel('Época')
plt.ylabel('Erro quadrático médio')
plt.title('Erro quadrático médio sobre épocas')
plt.legend()
plt.grid(True)

# Salvar a imagem em um arquivo
plt.savefig('mse_plot.png')
