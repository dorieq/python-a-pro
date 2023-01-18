def message(s):

    def addWelcome():
        return "Welcome to "

    return addWelcome() + s

def site(site_name):
    return site_name

print(message(site('codify')))