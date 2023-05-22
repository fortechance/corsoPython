import datetime


msec = datetime.datetime.now()

print(msec.microsecond)

print("ora",msec.hour,"minuti",msec.minute,"secondi",msec.second)
print("giorno",msec.day,"mese",msec.month,"anno",msec.year)
