#	Write a script that formats the dates this way, of course your date will not be mine
#	as in the example but it must be formatted the same.

#  Expected output:
#	$>python format_ft_time.py | cat -e
#	Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
#	Oct 21 2022$
#	$>

import datetime

def main():
	# Get the current date and time
	now = datetime.datetime.now()

	# Display the current date and time
	print("Seconds since January 1, 1970:" + \
	   " {:,.4f} or {:.2e} in scientific notation" \
	   .format(now.timestamp(), now.timestamp()))
	print(now.strftime("%b %d %Y"))

if __name__ == '__main__':
	main()