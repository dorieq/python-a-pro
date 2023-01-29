try:
    print(x)
except NameError:
    print('Name error')
except:
    print('Something else goes wrong')