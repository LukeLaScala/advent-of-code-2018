lines = open('input.txt').readlines()
timestamps = sorted(lines, key=lambda x: str(x).strip())

active = 0
minutes = {}
fell_asleep = ""
for stamp in timestamps:
    if "Guard" in stamp:
        active = int(stamp.split()[3][1:])
    elif "wakes up" in stamp:
        if not active in minutes:
            minutes[active] = [0, [0 for x in range(60)]]
        if active in minutes:
            woke = int(stamp[stamp.index(']')-2:stamp.index(']')])
            asleep = int(fell_asleep[fell_asleep.index(']')-2:fell_asleep.index(']')]) 
            minutes[active][0] += woke - asleep
            for x in range(asleep, woke, 1):
                minutes[active][1][x] += 1
    elif "falls asleep" in stamp:
        fell_asleep = stamp

max_mins = 0
max_min_guard_id = 0
for guard in minutes:
    for mins in minutes[guard][1]:
        if mins > max_mins:
            max_mins = mins
            minute = minutes[guard][1].index(mins)
            max_min_guard_id = guard

print(max_min_guard_id)
print(minute)