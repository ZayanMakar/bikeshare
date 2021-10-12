import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while  True:
        city = input('Would you like to see data for chicago,new york city or washington? ')
        if city.lower() in CITY_DATA:           
            break       
    
        

    # TO DO: get user input for month (all, january, february, ... , june)   
    while True:
        month = input('Which month? January,Febrary,March,April,May,June or all? ')
        if month.lower()=='all' or  month.lower() in ['january','february','march','april','may','june'] :
            break
       

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day =input('Which day? (all, Monday, Tuesday, ... Sunday). ')
        if day.lower()=='all' or  day.lower() in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday'] :
            break
       

    print('-' * 40)

    return city.lower(), month, day


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
    
    df = pd.read_csv(CITY_DATA.get(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    
    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1    
        df = df[df['month'] == month]
        
    if day.lower() != 'all':
         days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
         day = days.index(day.lower()) + 1    
         df = df[df['day'] == int(day)]
        
        
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    com_month = df['month'].mode()[0]
    print('The most common month: ', com_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday
    com_day = df['day'].mode()[0]
    print('The most common day: ', com_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    com_hour = df['hour'].mode()[0]
    print('The most common hour: ', com_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print('The most commonly used start station: ',start_station)
    
    # TO DO: display most commonly used end station
    End_Station= df['End Station'].mode()[0]
    print('The most commonly used End station: ', End_Station)
    
    # TO DO: display most frequent combination of start station and end station trip
    combination=(df['Start Station']+"  And  "+df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip: ', combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time : ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time : ', mean_travel_time)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Count of user type: ', user_type)

    # TO DO: Display counts of gender
    #Chicago and New York City only have Gender & Birthday Data
    if 'Gender' in df:
       gender = df['Gender'].value_counts()
       print('Count of gender: ', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    #earliest
       yearbirthearliest = df['Birth Year'].min()
       print('The earliest year of birth: ',int(yearbirthearliest))
    #recent
       yearbirthrecent = df['Birth Year'].max()
       print('The recent year of birth: ',int(yearbirthrecent))
    #most common
       yearbirthcommon = df['Birth Year'].mode()[0]
       print('The most common year of birth: ',int(yearbirthcommon))
    else:
        print('Gender & Birth Year Counts found only in Chicago and New York City')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    
    
def display_data_5_row(df):
    """ to disply 5 row of data based on user request """
    
    while True:
        index=0
        raw_data=input('Would you like to see 5 row of data?please enter yes or no. ')
        if raw_data.lower()=='yes':
            print(df.iloc[index:index+5])
            index += 5
            # response= input("Do you want to see the next 5 rows of data?:yes or no. ")
        if raw_data.lower()=='no':
            break
        # else:
        #     return 
        # elif response.lower()=='yes':
        #     return
        #     return
        # elif raw_data.lower()=='yes':
        #     return
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data_5_row(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()