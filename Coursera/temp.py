print("Hello", "World.",  sep=' '*8, end="\n")
# you don't need to specify end, if you don't want to, but I wanted you to know it was also an option
#if you wanted to have an 8 space prefix, and did not wish to use tabs for some reason, you could do the following.
print("%sHello World." % (' '*8))
