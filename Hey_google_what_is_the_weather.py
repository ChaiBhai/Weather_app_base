import random
print('Welcome to the weather app!')
print('------------------------------------------------------------')
weather = ["rainy", "sunny", "cloudy", "clear skies and hot", "clear skies and warm", "clear skies and cold"]
num = random.randint(0,5)
print('The weather today is ' + weather[num])
if weather[num] == 'rainy':
    print('You should consider brining a umbrella outside today')
else:
    if weather[num] == 'sunny' or weather[num] == 'clear skies and warm':
        print('You should consider bringing a pair of glasses today')
print('------------------------------------------------------------')




