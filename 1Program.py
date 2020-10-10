numberOfTimes= 5
anyName= 'Chuck'
'''
#Test 1
if True== True:
    print('True is True')
else:
    print('This is not true')
#Test 2
if True== 'True':
    print('True is True')
else:
    print('This is not true')
#Test 3
if 1== 1:
    print('True is True')
else:
    print('This is not true')
#Test 4
if 1+1 == 2:
    print('True is True')
else:
    print('This is not true')
'''
flag= True

while flag== True:
    anyName= input('What is your name? (Type "stop" to stop) ')
    if anyName.lower()!= "stop":
        print(f'hooray {anyName}')
    else:
        flag= False
        print('Have a nice day.')
    
    
