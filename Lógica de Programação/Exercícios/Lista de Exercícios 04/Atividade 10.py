for celsius in range(0, 41, 2):

    fahrenheit = (celsius * 9/5) + 32

    print("{:.1f} ºC = {:.1f} ºF".format(celsius, fahrenheit))
