# search method 
def search(what_to_search,number_result):
    # import modules
    import wikipedia
    # search on wikipedia api entered by user and store it in varible name x
    x=wikipedia.search(what_to_search,number_result)
    # return the x varibel with desired result
    return x
