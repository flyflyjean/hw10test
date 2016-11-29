from bs4 import BeautifulSoup
from urllib.request import urlopen
import argparse


def calculate(strings, return_float=False):
    str_split = strings.split(' ')
    new_str = "%20".join(word for word in str_split)
    response = urlopen('http://api.wolframalpha.com/v2/query?input={}&appid=UAGAWR-3X6Y8W777Q'.format(new_str)) 
    html_data = response.read()
    response.close()
    soup = BeautifulSoup(html_data,'xml')
    queryresult = soup.findAll('queryresult')
    if queryresult[0]['success'] == 'false':
        return 'Error1: The string you passed is invalid'
    else:
        item = soup.findAll('pod')
        if item[1]['id'] == 'Result':
            result = item[1].find('plaintext')
            answer = result.get_text()
            if return_float:
                return float_conv(answer)
            else:
                return answer
        else:
            return 'Error2: The string you passed is not calculable'

def float_conv(answer):
    if answer.isdigit():
        fanswer = float(answer)
        return fanswer
    else:
        value = answer.split(' ')[0].split('×')
        num = float(value[0])
        base = int(value[1].split('^')[0])
        power = int(value[1].split('^')[1])
        fanswer = num*(base**power)
        return fanswer

if __name__== "__main__":
    parser = argparse.ArgumentParser(description='CalCalc')
    parser.add_argument('-s', action='store', dest='string',
                    help='Enter anything you want to calculate')
    parser.add_argument('-f', action='store_true', default=False,
                    dest='boolean_switch',
                    help='Set true if you want to conver the result to a float')
    results = parser.parse_args()
    strings = results.string
    return_float = results.boolean_switch
    print(calculate(strings, return_float))



def test_simple():
    assert calculate('12*12') == '144'

def test_float():
    assert abs(calculate('12*12', return_float = True) - 144) < 0.001

def test_error1():
    assert calculate('dsfdfsdggf43523') == 'Error1: The string you passed is invalid'

def test_error2():
    assert calculate('carbon') == 'Error2: The string you passed is not calculable'

def test_float2():
    assert calculate('mass of the moon in kg', return_float = True) == 7.3459e+22
