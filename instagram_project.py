import instaloader

L = instaloader.Instaloader()


user = "NICKNAME_OF_YOUR_ACCOUNT"
passw = "PASSWORD_OF_YOUR_ACCOUNT"
USERNAME = "NICKNAME_OF_ACCOUNT_YOU_TAKE_DATA_FROM"

# Creating Instance
L.login(user, passw)

profile = instaloader.Profile.from_username(L.context, USERNAME)

follow_list = []

# Appending the list of followers
for follower in profile.get_followers():
    follow_list.append(follower.username)

print(follow_list)


for profile in follow_list:
    try:
        # Get the profile information using the Instaloader instance
        profile_obj = instaloader.Profile.from_username(L.context, profile)

        # Get the bio text and save it to a file
        bio_text = profile_obj.biography
        with open(f'{profile}_bio.txt', 'w') as f:
            f.write(bio_text)

        # Print the bio text
        print(f'{profile} bio: {bio_text}')
    except instaloader.exceptions.ProfileNotExistsException:
        print(f'Profile {profile} does not exist.')

