# Nonstandard libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Location of csv file, probably needs to be altered
# depending on the machine trying to run this
data_location = '/Users/mariacontreras/Documents/Titanic/train.csv'
# load csv into dataframe
passenger_data = pd.DataFrame.from_csv(data_location)

# Add a column with sex converted to binary values
# FEATURE ENGINEERING!!!
passenger_data['SexBin'] = [ 0 if x[0] == 'm' else 1 for x in passenger_data['Sex'] ]

#Dummy variables for embarked
#passenger_data['EmbarkedC'] = [ 1 if x[0] == 'C' else 0 for x in passenger_data["Embarked"] ]
#passenger_data['EmbarkedQ'] = [ 1 if x[0] == 'Q' else 0 for x in passenger_data["Embarked"] ]
#passenger_data['EmbarkedS'] = [ 1 if x[0] == 'S' else 0 for x in passenger_data["Embarked"] ]

# Add a column with the total sum of a passenger's parents, children, spouses, and siblings
# FEATURE ENGINEERING!!!
passenger_data['Family'] = passenger_data['Parch'] + passenger_data['SibSp']

# SQUARE THE FARE!!!
# FEATURE ENGINEERING!!!
passenger_data['SquareFare'] = passenger_data['Fare']**2

#removing outliers
pass_no_outliers = passenger_data[np.abs(passenger_data.Fare-passenger_data.Fare.mean())<=(3*passenger_data.Fare.std())]

# Split passengers into survivors and nonsurvivors
survivors = pass_no_outliers.loc[passenger_data['Survived'] == 1]
nonsurvivors = pass_no_outliers.loc[passenger_data['Survived'] == 0]


## Alternatively you can do this
## It's commented out by default because lines 24 and 25 do the same thing
## It's more versatile though, since you can group people by class or port instead
## The way it works is by finding each unique value in a column
## Then separating them by those values
#values = passenger_data.Survived.unique()
#groups = []
#
## In this case value is either 0 or 1 denoting survival
#for value in values:
#    group = passenger_data.loc[passenger_data['Survived'] == value]
#    groups.append(group)
#
#survivors = groups[0]
#nonsurvivors = groups[1]

# Values we will plot against each other
X = 'Age'
Y = 'Fare'

# Label axes with plotted values
plt.xlabel(X)
plt.ylabel(Y)

# Graph survivors and nonsurvivors with dot size=1
plt.scatter(survivors[X], survivors[Y], s=1)
plt.scatter(nonsurvivors[X], nonsurvivors[Y], s=1)

# Just print the column names for convenience
print(list(pass_no_outliers))
plt.show()

