import time
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)
'''
In this project, you will make use of Python to explore data related to
bike share systems for three major cities in the United States—
Chicago, New York City, and Washington.
'''
CITY_DATA = { 'CH': 'chicago.csv',
              'NYC': 'new_york_city.csv',
              'WA': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    while True:
        city=(input("please select city \n(chicago=CH, new york city=NYC, washington=WA)\n")).upper()
        if(city== "CH" or city== "NYC" or city== "WA"):
            break
        else:
            print("wrong input please try agen")
    # get user input for month (all, january, february, ... , june)
    while True:
        month=(input("please Enter month \n(all, January, February, March, April, May, June)\n")).title()
        if month in ['January', 'February', 'March', 'April', 'May', 'June','All']:
            break
        else:
            print("wrong input please try agen")   
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=(input("please Enter day of week \n(all, saturday, sunday, monday, tuesday, wednesday, thursday, friday)\n")).title()
        if day in ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','All']:
            break
        else:
            print("wrong input please try agen")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = CITY_DATA[city]

    # load data file into a dataframe
    df = pd.read_csv(filename)
    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
   
        # filter by month to create the new dataframe
        df = df[df["month"] ==month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]

    # display the most common day of week
    popular_day = df["day_of_week"].mode()[0]

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    popular_hour = df['hour'].mode()[0]
    print("****************************************")
    print("the most common month :         {}\n".format( popular_month))
    print("the most common day of week:    {}\n".format(popular_day))
    print("the most common start hour:     {}\n".format(popular_hour))
    print("****************************************")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print("***********************************************************")
    # display most commonly used start station
    most_commonly_start_station= df['Start Station'].mode()[0]
    print("Most commonly used start station:\n{}\n".format(most_commonly_start_station))

    # display most commonly used end station
    most_commonly_end_station= df['End Station'].mode()[0]
    print("Most commonly used end station:\n{}\n".format(most_commonly_end_station))

    # display most frequent combination of start station and end station trip
    most_frequent_combination_station=df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1)
        
    print('Most frequent combination of Start and End Station trip:\n{}\n'.format(most_frequent_combination_station))
    print("***********************************************************")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print ("************************************")
    # display total travel time
    total_travel_time=df["Trip Duration"].sum()
    print("total travel time: {}\n".format(total_travel_time))

    # display mean travel time
    mean_travel_time=df["Trip Duration"].mean()
    print("mean travel time:  {}\n".format(mean_travel_time))
    print ("************************************")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print("*********************************")
    # Display counts of user types
    user_types =df["User Type"].value_counts()
    print("Counts of user types:\n{}\n".format(user_types))
    
    if (city=="CH" or city=="NYC"):
        # Display counts of gender
        counts_of_gender =df["Gender"].value_counts()
        print("Gender Year Stats:\n{}\n".format(counts_of_gender))
        # Display earliest, most recent, and most common year of birth 
        earliest=df["Birth Year"].min()
        most_recent=df["Birth Year"].max()
        most_common_year =df["Birth Year"].mode()[0]
        print('------------------------------\n')
        print('Birth Year Stats:\n')
        print("Earliest Year:     {}".format(int(earliest)))
        print("Most Recent Year:: {}".format(int(most_recent)))
        print("Most Common Year:  {}\n".format(int(most_common_year)))
    print("*********************************")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_data(df):
    """Displays Data Frame"""
    # start and end of Displays Data
    start_data=0
    end_data=5
    #print Displays Data
    while True:
        print(df.iloc[start_data:end_data]) 
        # input do you want more data or no??
        while True:
            more_data=(input("do you want more data?? \nEnter yes or no\n")).lower()
            if more_data=="yes" or more_data=="no":            
                break
            else:
                print ("wrong input!!\n")
        if more_data=="yes": 
            start_data=end_data
            end_data+=5
        else:
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        print_data(df)
        
        restart = (input('\nWould you like to restart? Enter yes or no.\n')).lower()
      
        if restart != 'yes':
            break
if __name__ == "__main__":
	main()
