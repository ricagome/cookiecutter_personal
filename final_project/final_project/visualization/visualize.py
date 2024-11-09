## AQUI SE COLOCAN LOS IMPORTS PARA SU EJECUCION
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def country_time_series(df: pd.DataFrame):
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series");

## Luego de esto ya se puede abstraer directo alproycto