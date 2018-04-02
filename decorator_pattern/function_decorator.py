def open_app(f):
    def new_f(*args):
        print("Entering %s" % f.__name__)
        f(*args)
        print("Exiting %s" % f.__name__)
    new_f.__name__ = f.__name__
    return new_f

@open_app
def edit_setting(a, b, c):
    print("Editing project Settings")
    print("Setting args: %s, %s, %s" % (a, b, c))


edit_setting("path", "to", "store project")
