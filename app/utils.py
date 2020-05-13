#f do usuwania znakow format
def remove_whitespaces(string):
    try:
        return string.replace("\n",", ").replace("\r",", ")
    except AttributeError:
        pass

