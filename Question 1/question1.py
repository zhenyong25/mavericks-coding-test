from datetime import datetime 

def calculate(sorted_time_intervals):
    longest_break = None

    for i in range(len(sorted_time_intervals) - 1):

        interval1 = sorted_time_intervals[i]
        interval2 = sorted_time_intervals[i + 1]

        end_time1 = datetime.strptime(interval1.split('-')[1], '%I:%M%p')
        start_time2 = datetime.strptime(interval2.split('-')[0], '%I:%M%p')

        break_duration = (start_time2 - end_time1).total_seconds() / 60

        if longest_break is None or break_duration > longest_break:
            longest_break = break_duration

    if longest_break is not None:
        # Convert shortest_break to hours and minutes
        hours = int(longest_break // 60)
        minutes = int(longest_break % 60)
        return f"{hours:02d}:{minutes:02d}"
    else:
        return "N/A"  # Not enough intervals to calculate a break

time_intervals = input()
sorted_time_intervals = sorted(time_intervals, key=lambda x: datetime.strptime(x.split('-')[0], '%I:%M%p'))
longest_break = calculate(sorted_time_intervals)
  
# keep this function call here 
print(longest_break)