def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


myProfile = build_profile("Xun", "Ruan", age=26, dream="To apple", favoriteCharacter="Bully Maguire")
print(myProfile)