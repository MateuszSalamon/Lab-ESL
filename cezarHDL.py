from myhdl import block, delay, always_comb, now, instance

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

key = 7
@block
def CezarEnter(key):



    @always_comb
    def getTranslatedMessage():

        message = 'asdfghjkl62'
        translated = ''

        for symbol in message:
            num = ord(symbol)
            num += key

            if num > 126:
                num -= MAX_KEY_SIZE

            elif num < 33:
                num += MAX_KEY_SIZE

            translated += chr(num)
        return translated
    return getTranslatedMessage


# mode = getMode()
#
# message = getMessage()
#
# key = getKey()
#
# print('Your translated text is:')
#
# print(getTranslatedMessage(mode, message, key))

inst = CezarEnter()
inst.run_sim(50)



