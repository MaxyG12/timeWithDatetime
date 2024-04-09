import datetime

print("EVENT COUNTDOWN")
print()

event = input("Input the event > ")
year = int(input("Input the year > "))
month = int(input("Input the month > "))
day = int(input("Input the day > "))

today = datetime.date.today()
eventDate = datetime.date(year, month, day)
difference = eventDate - today
difference = difference.days

if difference > 0:
  print(f"{difference} days to go")
elif difference < 0:
    print(f"😭😭😭😭😭😭😭😭😭💀😭😭😭😭😭😭 You missed it by {difference} days!")
else:
    print("🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳 Today!")


  