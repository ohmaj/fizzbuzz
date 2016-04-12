def divisableCheck(number,factor,alertWord):
    if number % factor:
        response=str(number)
    elif number < 1:
        response=str(number)
    else:
        response=alertWord
    return (response)
def rangeFizzBuzz (start,stop,rate):
    for number in range (start,stop,rate):
        if  'fizzbuzz' == (divisableCheck(number,3,'fizz'))+(divisableCheck(number,5,'buzz')):
            yield ('fizz buzz')
        elif 'buzz' == (divisableCheck(number,5,'buzz')):
            yield 'buzz'
        elif 'fizz' == (divisableCheck(number,3,'fizz')):
            yield 'fizz'
        else:
            yield number
runFizzBuzz = rangeFizzBuzz(1,10001,1)
for fizzBuzz in runFizzBuzz:
    print (fizzBuzz)

