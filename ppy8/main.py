import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

url = "iris.csv"
headers = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv(url, names=headers)

print(df.describe())
print("\n==========\n")

lista = df.iloc[:, :-1].values
etykieta = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(lista, etykieta, test_size=0.25, random_state=2023)

# Użyjemy klasyfikatora Random Forest z 100 drzewami
rf = RandomForestClassifier(n_estimators=100, random_state=2023)

rf.fit(x_train, y_train)

from sklearn.model_selection import KFold, GridSearchCV

param_grid = {'n_estimators': [100, 200, 300], 'max_depth': [None, 5, 10]}

grid_search = GridSearchCV(rf, param_grid, cv=KFold(n_splits=5, random_state=2023, shuffle=True))
grid_search.fit(x_train, y_train)

results = pd.DataFrame(grid_search.cv_results_)

print(results["mean_test_score"])

print("Najlepszy model: ", grid_search.best_params_)
print("Najlepszy wynik: ", grid_search.best_score_)
best_model = grid_search.best_estimator_

best_predict = best_model.predict(x_test)
print("Dokładność modelu: ", accuracy_score(y_test, best_predict))
