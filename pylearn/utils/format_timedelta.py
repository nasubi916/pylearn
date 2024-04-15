def format_timedelta(timedelta):
  total_sec = timedelta.total_seconds()
  # hours
  hours = total_sec // 3600
  # remaining seconds
  remain = total_sec - (hours * 3600)
  # minutes
  minutes = remain // 60
  # remaining seconds
  seconds = remain - (minutes * 60)
  # total time
  return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))