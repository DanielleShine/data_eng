"""Write a function that prints a profile, given values."""

def create_profile(given_name, *surnames, **details):
    """Print a user's profile."""
    print(f"\n{given_name} {' '.join(surnames)}")
    for key, value in details.items():
        print(f"{key.title()}: {value}")


if __name__ == '__main__':
    create_profile("Sam")
    create_profile("Martin", "Luther", "King", "Jr.", born=1929, died=1968)
    create_profile("Sebastian", "Thrun", cofounded="Udacity", experience="Stanford Professor")
