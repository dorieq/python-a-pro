def decorate_msg(fun):

    def addWelcome(s):
        return "Welcome to " + fun(s)

    return addWelcome

@decorate_msg
def site(site_name):
    return site_name

print(site('aprostudio'))