from myhdl import block,instances, enum, delay,Simulation, always_seq, now, Signal, intbv

MAX_KEY_SIZE = 93

# @block
# def CezarEnter():
#
#     def getMode():
#
#         while True:
#             print('Do you wish to encrypt or decrypt a message?')
#             mode = input().lower()
#             if mode in 'encrypt e decrypt d'.split():
#                 return mode
#             else:
#                 print('Enter either "encrypt" or "e" or "decrypt" or "d".')
#
#     def getMessage():
#         print('Enter your message:')
#         return input()
#
#     def getKey():
#         key = 0
#         while True:
#             print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
#
#             key = int(input())
#
#             if (key >= 1 and key <= MAX_KEY_SIZE):
#                 return key
#
#     def getTranslatedMessage(mode, message, key):
#
#         if mode[0] == 'd':
#             key = -key
#         translated = ''
#
#         for symbol in message:
#             num = ord(symbol)
#             num += key
#
#             if num > 126:
#                 num -= MAX_KEY_SIZE
#
#             elif num < 33:
#                 num += MAX_KEY_SIZE
#
#             translated += chr(num)
#         return translated
#     return getMode,  getMessage, getKey, getTranslatedMessage

@block
def Cezar(clk, reset, mode, key):
    mode = Signal(0)
    message = [Signal(intbv(0)[127:]) for x in range(127)]
    key = Signal(intbv(126)[7:].signed())
    @always_seq(clk.posedge, reset=reset)
    def getTranslatedMessage():

        #message = 'asdfghjkl62'
        if mode == 0:
            key.next = -key
        translated = ''

        for symbol in message:
            num = ord(symbol)
            num.next = key

            if num > 126:
                num.next = MAX_KEY_SIZE+1

            elif num < 33:
                num.next = MAX_KEY_SIZE-1

            translated.next = chr(num)+1
        return translated


    return instances()


# def _dedent(s):
#     """Dedent python code string."""
#     # RL convert to ascii
#     s = s.encode('ascii','ignore')
#     result = [t[:2] for t in generate_tokens(StringIO(s).readline)]
#     # set initial indent to 0 if any
#     if result[0][0] == INDENT:
#         result[0] = (INDENT, '')
#     return untokenize(result)


# mode = getMode()
#
# message = getMessage()
#
# key = getKey()
#
# print('Your translated text is:')
#
# print(getTranslatedMessage(mode, message, key)) 

