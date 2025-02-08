import pandas as pd
import time
from IPython.display import display

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?').lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Invalid input. Please enter a valid city name.')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month - January, February, March, April, May, or June?').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Invalid input. Please enter a valid month name.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Invalid input. Please enter a valid day of the week.')

    print('-'*40)
    
    print("Your chosen City, Month(s) and Day(s) are:")
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
    df = pd.read_csv(CITY_DATA[city])
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def display_data(df):
    """
    Asks the user if they want to see 5 rows of data and keeps iterating until the user says 'no'.
    """
    start_row = 0
    while True:
        show_data = input("\nWould you like to see 5 rows of data? Enter 'yes' or 'no': ").strip().lower()
        if show_data == 'yes':
            # display(df.iloc[start_row:start_row+5])  # Display next 5 rows
            # print(df.head(start_row:start_row+5))
            print(df[start_row:start_row+5].head())
            start_row += 5
            if start_row >= len(df):  # Stop if there are no more rows to display
                print("\n🚀 End of data reached.")
                break
        elif show_data == 'no':
            print("\n✅ Data display stopped.")
            break
        else:
            print("❌ Invalid input. Please enter 'yes' or 'no'.")

# Run the script
city, month, day = get_filters()
df = load_data(city, month, day)
display_data(df)  # Ask user if they want to display rows