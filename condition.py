temp = 22

if (temp > 30):
    print("It's warm!")
elif temp > 20:
    print("Nice!")
else:
    print("It's cold!")

age = 19

msg = "Eligible" if age >= 18 else "Not Eligible"
print(msg)


if 18 <= age <= 24:
    print("Eligible")
