import os
import pandas as pd
import numpy as np

#this function recieves the monthly data, and randomly distributes the precipitation
#in a given number of days by a random quantity

def monthly_to_daily(meteo_dir,output_dir,num_of_events_per_month,var_name):

    df = pd.read_csv(meteo_dir)
    df['time'] = pd.to_datetime(df['time'])
    df = df.pivot(index='time', columns='NOMBRE')




    month_unique=np.unique(df.index)
    n=0
    for month in month_unique:

        data_1month=df[df.index==month]

        start_date = data_1month.index.min() - pd.DateOffset(day=1)
        end_date = data_1month.index.max() + pd.DateOffset(day=31)


        dates = pd.date_range(start_date, end_date, freq='D')
        dates.name = 'time'

        data_1month = data_1month.reindex(dates, method='ffill')

        #random event %
        random_event_perc=np.random.dirichlet(np.ones(num_of_events_per_month),size=1)
        

        #random days of the month
        random_days=np.array([])
        while len(random_days)!=num_of_events_per_month:
            random_days=np.random.randint(low=1, high=end_date.day+1, size=num_of_events_per_month, dtype=int)
            random_days=np.unique(random_days)
        random_days.sort()
        
        #how many stations
        num_of_stations=data_1month.iloc[0][var_name].shape[0]
        #
        random_event_perc=np.repeat(random_event_perc,num_of_stations).reshape(num_of_events_per_month,num_of_stations)

        
        changed_data=data_1month.loc[data_1month.index.day.isin(random_days)][var_name]*random_event_perc

        data_1month[var_name]=0

        data_1month[var_name]=changed_data

        data_1month[var_name]=data_1month[var_name].fillna(0)

        #data_1month[var_name].update(changed_data)


        data_1month = data_1month.stack('NOMBRE')
        data_1month = data_1month.sort_index(level=1)
        data_1month = data_1month.reset_index()
        
        if n==0:
            df_final=data_1month
        else:
            df_final=pd.concat([df_final,data_1month],ignore_index=True)
        
        n=n+1

    df_final.to_csv(os.path.join(output_dir,var_name+"_daily_from_monthly.csv"))

if __name__=="__main__":

    meteo_dir=r"C:\Users\Ash kan\Documents\watbalpy\waterball_test\modelito_for_paper_tests\8x_METEO_9stations.csv"
    output_dir=r"C:\Users\Ash kan\Documents\watbalpy\waterball_test\modelito_for_paper_tests"
    num_of_events_per_month=9
    var_name="Prec_Val"
    monthly_to_daily(meteo_dir,output_dir,num_of_events_per_month,var_name)