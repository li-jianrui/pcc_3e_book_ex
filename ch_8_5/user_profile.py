def user_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    profile = profile | user_info
    return profile

user_profile1 = user_profile('albert', 'einstein', location='princeton', field='physics')
user_profile2 = user_profile('marie', 'curie', location='paris', field='chemistry')
user_profile3 = user_profile('isaac', 'newton', location='cambridge', field='mathematics')
print(user_profile1)
print(user_profile2)
print(user_profile3)