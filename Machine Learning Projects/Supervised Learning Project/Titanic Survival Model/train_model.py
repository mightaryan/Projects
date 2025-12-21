import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# 1. Load Data
df = pd.read_csv('train.csv')

# 2. Feature Engineering (MUST Match app.py logic)
# Fill missing Age/Embarked
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Create Family Features
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = 1
df.loc[df['FamilySize'] > 1, 'IsAlone'] = 0

# Encode Sex (0 = Male, 1 = Female) to match App
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Encode Embarked manually to match App columns exactly
# We need specific columns: Embarked_Q and Embarked_S
df['Embarked_Q'] = 0
df.loc[df['Embarked'] == 'Q', 'Embarked_Q'] = 1

df['Embarked_S'] = 0
df.loc[df['Embarked'] == 'S', 'Embarked_S'] = 1

# 3. Define Predictors (X)
# We explicitly select ONLY the columns the App uses
predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'FamilySize', 'IsAlone', 'Embarked_Q', 'Embarked_S']

X = df[predictors]
y = df['Survived']

# 4. Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 5. Save Model
joblib.dump(model, 'titanic_survival_model.pkl')
print("✅ Success! Model overwritten with correct columns.")
print(f"Model expects these columns: {predictors}")