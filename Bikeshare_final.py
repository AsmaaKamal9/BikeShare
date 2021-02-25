import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['January', 'February', 'March', 'April', 'May' , 'June' , 'All']
day_of_week = ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    city_que,month_que,day_que = False, False,False

    while True:
# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        if not city_que:
            city = input("Would you like to see data for Chicago, New York or Washington?")
            city=city.lower()
            if city not in CITY_DATA:
                print("\nCity is not found,Please enter a valid city: Chicago, New York or Washington?")
                continue
            else:
                city_que = True
#get from user the filtering (whether by months , days)

        if not month_que:
            month = input("\nChoose a month: January, February, March, April, May, June or All?")
            month = month.title()
            if month not in months:
                print("\nPlease Enter a valid month: January, February, March, April, May, June or All? ")
                continue
            else:
                month_que = True

        if not day_que:
            day= input('\nChoose a week day to filter with: Friday, Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday or All?')
            day=day.title()
            if day not in day_of_week:
                print("\nPlease Enter a valid day: Friday, Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday or All?")
                continue
            else:
                break

    print('Your Data is being filtered for {} and {}'.format(month,day))
    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df= pd.read_csv(CITY_DATA[city])

    df['Start Time']= pd.to_datetime(df['Start Time'])

    df['Start Month'] = df['Start Time'].dt.month_name()
    df['Start Day'] = df['Start Time'].dt.day_name()
    df['Start Hour']= df['Start Time'].dt.hour

    if month != 'All':
        df = df[df['Start Month'] == month]

    if day != 'All':
        df = df[df['Start Day'] == day]

    print('Your Data is being filtered !')
    return df

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Month']= df['Start Time'].dt.month_name()
    df['Start Day'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour

        # display the most common month
    if month == 'All':
        most_common_month = df['Start Month'].dropna()
        most_common_month = most_common_month.mode()[0]
        print('Most common Month is : {}'.format(most_common_month))
    else:
        print('\n Please select All, to get accurate filtered Data!')

        # display the most common day of week
    if day == 'All':
        most_common_day_ofweek = df['Start Day'].dropna()
        most_common_day_ofweek = most_common_day_ofweek.mode()[0]
        print('Most common Day is : {}'.format(most_common_day_ofweek))
    else:
        print('\n Please select All, to get accurate filtered Data!')

        # display the most common start hour
    most_common_hour = df['Start Hour'].dropna()
    most_common_hour = most_common_hour.mode()[0]


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].dropna().mode()[0]

    # display most commonly used end station
    common_end_station = df['End Station'].dropna().mode()[0]

    # display most frequent combination of start station and end station trip
    most_start_end = (df['Start Station'] + ';' + df['End Station']).dropna().mode()[0]

    print('Most common used Start Station is {} , \nMost Common used End Station is {} , \nand the most frequent combination of both of them is {} '
    .format(common_start_station,common_end_station,most_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    time_total = df['Trip Duration'].fillna(0)
    total_travel = time_total.sum()

     #display mean travel time
    mean_travel = time_total.mean()

    print('Total time traveled by bikes: {} sec, \nMean Duration traveled: {} sec'.format(total_travel,mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Users Details are {}: '.format(user_types))

    # Display counts of gender
    if "Gender" in df:
        count_gender = df['Gender'].dropna()
        count_gender = count_gender.value_counts()
        print('\nGender Count is: {}'.format(count_gender))
    else:
        print('\nGender count is not in the filtered Data')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        Birth_Year = df['Birth Year'].dropna()
        earliest_year = Birth_Year.min()
        recent = Birth_Year.max()
        common_year = Birth_Year.mode()[0]
        print('\nEarliest Year of birth is: {}, \nMost Recent is: {}, \nMost Common Year: {}'.format(earliest_year,recent,common_year))
    else:
        print('\nBirth Year data is not in the filtered Data')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def showing_rows(df):
    #showing the first 5 rows of the filter
    showing_rows = input('\n Would you like to see 5 lines of your filtered Data? Enter yes or no. \n')
    count = 0
    if showing_rows.lower() == 'yes':
        print('\nThe first 5 rows of the filtered Data:', df.head(5))
        while showing_rows.lower() == 'yes':
            showing_rows2=input('\nDo you like to see 5 more? Enter yes or no. \n')
            count +=5
            if showing_rows2.lower() == 'yes':
                print(df.iloc[(count):(count+5) , :])
            else :
                break

def main():
    while True:
        city,month,day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        showing_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
