text = '''In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.

And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.'''
x = text.split()

def format_text(x, width):
    text, phrase, letters = [], [], 0
    for word in x:
        if letters + len(word) + len(phrase) > width:
            if len(phrase) == 1:
                text.append(phrase[0])
            else:
                spaces = ((width - letters)//(len(phrase) - 1 ))
                text.append((' ' * spaces).join(phrase))
            phrase, letters = [], 0
        phrase += [word]
        letters += len(word)
    text.append( ' '.join(phrase))
    return text

def justify_text(x, width):
    textj, phrase, letters = [], [], 0
    for word in x:
        if letters + len(word) + len(phrase) > width:
            if len(phrase) == 1:
                textj.append(phrase[0] + ' '*(width - letters))
            else:
                spaces, addspaces = divmod(width - letters, len(phrase) - 1 )
                for i in range(addspaces):
                    phrase[i] += ' '
                textj.append((' ' * spaces).join(phrase))
            phrase, letters = [], 0
        phrase += [word]
        letters += len(word)
    textj.append(' '.join(phrase) + ' ' * (width - letters - len(phrase)))
    return textj


print(x)
y = justify_text(x,40)
print('\n'.join(y))
y = format_text(x,40)
print('\n'.join(y))