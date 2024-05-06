from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
# print(iris.metadata) 
  
# variable information 
# print(iris.variables) 

# Dividir o conjunto de dados em subconjuntos de treinamento, validação e testes
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=35)
X_validation, X_test, y_validation, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=35)

# Padronizar os recursos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_validation = scaler.transform(X_validation)

# Criar e treinar o Perceptron
perceptron = Perceptron(max_iter=1000, random_state=35)
perceptron.fit(X_train, y_train)

# Prever os rótulos das amostras de teste
y_pred_test = perceptron.predict(X_test)
y_pred_validation = perceptron.predict(X_validation)

# Avaliar a precisão do modelo
print("Acuracia nos testes: ", accuracy_score(y_test, y_pred_test) )
print("Acuracia: na validação", accuracy_score(y_validation, y_pred_validation) )
 
