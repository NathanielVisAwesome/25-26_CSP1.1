milliseconds = 10000123
hours = int(milliseconds / 3600000)
secondsLeft = milliseconds % 36000
minutesLeft = int(secondsLeft / 600)
timeSecondsLeft = (secondsLeft % 60) - 3
millisecondsLeft = int(secondsLeft / 1000)


print("Lab03, 80 Point Version")
print("Starting milliseconds:", milliseconds)
print("Time left:", hours,"hours", minutesLeft,"minutes", timeSecondsLeft,"seconds", millisecondsLeft,"milliseconds","remaining")
