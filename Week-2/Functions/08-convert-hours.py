# This script converts seconds into hours
def convert_hours(seconds):
    hours = seconds // 3600
    mins = (seconds - hours * 3600 ) // 60 # total mins remaining after hours is deducted
    remaining_secs = seconds - hours * 3600 - mins * 60
    return( hours, mins, remaining_secs)
hours, mins, seconds = convert_hours(76383)
print(hours, mins, seconds)


