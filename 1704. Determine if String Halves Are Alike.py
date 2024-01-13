def halvesAreAlike(s):
    first_half_count = 0
    second_half_count = 0
    half = int(len(s)/2)
    first_half = s[0:half]
    second_half = s[half:]
    vowels = 'AaEeIiOoUu'
    for i in first_half:
        if i in vowels:
            first_half_count += 1
    for i in second_half:
        if i in vowels:
            second_half_count += 1
    if first_half_count == second_half_count:
        return True
    else:
        return False
output = halvesAreAlike("Ieai")
print(output)