"""
Question 1
Write a function that takes a list of strings an prints them, one per line, in a rectangular frame.
For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:

* * * * *
* Hello *
* World *
* In    *
* A     *
* Frame *
* * * * *
"""


def frame(ls):
    max_len = len(max(ls, key=len))
    if max_len % 2 == 0:
        max_len += 1
    print('* '*(max_len//2 + 2) + '*')
    for word in ls:
        print('* ' + word.capitalize() + ' '*(max_len-len(word)) + ' *')
    print('* ' * (max_len // 2 + 2) + '*')


"""
Question 02
Write a function that prints the song "99 bottles of beer on the wall". The formatting, paragraphing and punctuation should be same as the lyrics in the link below. Use as many loops as possible. The question will be marked according to the number of lines used for the solution. 
Less lines of code, more points.
Lyrics: http://www.99-bottles-of-beer.net/lyrics.html
"""


def sing():
    for i in range(99, -1, -1):
        if i == 0:
            print("No more bottles of beer on the wall, no more bottles of beer."
                  "\nGo to the store and buy some more, 99 bottles of beer on the wall.")
        else:
            print(f"{i} bottle{(i!=1) * 's'} of beer on the wall, {i} bottle{(i!=1) * 's'} of beer")
            if i == 1:
                print("Take one down and pass it around, no more bottles of beer on the wall.\n")
            else:
                print(f"Take one down and pass it around, {i-1} bottle{(i!=2) * 's'} of beer on the wall.\n")


frame(["Hello", "World", "in", "a", "frame"] )
sing()
