import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

#Step 1 : Load the Dataset
#----------------------------------------------------
#Function Name : LoadData
#Description :   Load the Data
#Input :         Name of CSV File
#Output :        Dataframe
#Author :        Aarti Gorakshnath Wamane
#Date :          18/08/2026
#----------------------------------------------------
Border = "-"*60
def LoadData(filename):

    print(Border)
    print("Step 1 : Load the csv")
    print(Border)

    df = pd.read_csv(filename)

    print(df.head())

    return df

#Step 2 : Data Preprocessing
#----------------------------------------------------
#Function Name : DataPreprocessing
#Description :   Perform Data Analysis
#Input :         Dataframe
#Output :        Updated Dataframe
#Author :        Aarti Gorakshnath Wamane
#Date :          18/08/2026
#----------------------------------------------------
def DataPreprocessing(df):
    print(Border)
    print("Step 2 : Data Preprocessing")
    print(Border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns = ["Unnamed: 0"])

    print(df.head())

    print(Border)
    print("Total Missing Values : ")
    print(Border)
    print(df.isnull().sum())
    print(Border)

    print(Border)
    print("Statistical Summary : ")
    print(Border)
    print(df.describe())
    print(Border)

    print(Border)
    print("Correlation : ")
    print(Border)
    print(df.corr())
    print(Border)

    return df

#Step 3 : Data Spliting
#----------------------------------------------------
#Function Name : SplitData
#Description :   Perform Data Spliting activity
#Input :         Dataframe
#Output :        4 subset of training and testing data
#Author :        Aarti Gorakshnath Wamane
#Date :          18/08/2026
#----------------------------------------------------
def SplitData(df):
    print(Border)
    print("Step 3 : Data Spliting")
    print(Border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Independent variables : ")
    print(X.head())

    print(Border)

    print("Dependent Variables : ")
    print(Y.head())

    X_train,X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    print(Border)
    print("Training Data : ",X_train.shape)
    print("Testing Data : ",X_test.shape)

    return X_train,X_test,Y_train,Y_test

#Step 4 : Create and Train the Model
#----------------------------------------------------
#Function Name : TrainModel
#Description :   Perform Model Creation Training activity
#Input :         Training Features and Labels
#Output :        Trained Model
#Author :        Aarti Gorakshnath Wamane
#Date :          18/08/2026
#---------------------------------------------------
def TrainModel(X_train, Y_train):
    print(Border)
    print("Step 4 : Create and Train the Model")
    print(Border)

    model = LinearRegression()

    model = model.fit(X_train,Y_train)

    print("Model Trained Successfully")

    return model

#Step 5 : Test and Evaluate the Model
#----------------------------------------------------
#Function Name : EvaluateModel
#Description :   Perform Testing and Evaluation activity
#Input :         Model, Testing Features and Labels
#Output :        None
#Author :        Aarti Gorakshnath Wamane
#Date :          18/08/2026
#---------------------------------------------------
def EvaluateModel(model,X_test,Y_test):

    print(Border)
    print("Step 5 : Test and Evaluate the Model")
    print(Border)

    Y_pred = model.predict(X_test)

    print("Expected Answer : ")
    print(Y_test[:3])

    print(Border)
    print("Predicted Answer : ")
    print(Y_pred[:3])
    print(Border)

    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)

    print(Border)
    print("MSE : ",MSE)
    print("RMSE : ", RMSE)
    print("R2 : ",R2)
    print(Border)

#--------------------------------------------------------
#Function Name :main
#Description :  Entry Point function
#Input :        None
#Output :       None
#Author :       Aarti Gorakshnath Wamane
#Date :         18/08/2026
#--------------------------------------------------------
def main():
    df = LoadData("Advertising.csv")

    df = DataPreprocessing(df)

    X_train,X_test,Y_train,Y_test = SplitData(df)

    model = TrainModel(X_train,Y_train)

    EvaluateModel(model,X_test,Y_test)

#--------------------------------------------------------
#Function Description : Starter function
#--------------------------------------------------------
if __name__ == "__main__":
    main()