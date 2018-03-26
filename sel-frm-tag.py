def extract_from_tag(tag, line):
    ''' This function accepts a line with html like tags, enter a tag \
    name and you can find the word wrapped within the tag'''
    # the line.index function has 3 arguments,
    # 1st is the substring,
    # 2nd is the starting postiton (default is 0),
    # 3rd is end postiton (default is -1)
    open_tag = "<" + tag + ">"
    close_tag = "</" + tag + ">"
    try:
        i = line.index(open_tag)
        start = i + len(open_tag) # starts from the end of the opener
        stop = line.index(close_tag, start) # ends at the start of the closer
        return line[start : stop]
    except ValueError :
        print("Tag doesn't exist!")
        return None


# Demonstration of the function
new_line = "This line of text is <really>awesome</really>!"
new_tag = "really"

text_in_tag = extract_from_tag(new_tag, new_line)

# Results should be awesome
print(text_in_tag)
