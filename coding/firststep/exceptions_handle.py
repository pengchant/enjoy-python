try:
    text = input('enter something-->')
except EOFError:
    print('why did you do an eof one me?')
except KeyboardInterrupt:
    print('You cancelled the operation')
else:
    print('you entered {}'.format(text))

