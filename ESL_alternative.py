from myhdl import block, instances, enum, delay, Simulation, always_seq, now, Signal, intbv,ResetSignal

# mode 0 - encrypt
# mode 1 - decrypt
# key_max - 1,2 or 3
# message - 2 bit signal


@block
def cezar( mode, key, out, message,clk,reset):



    @always_seq(clk.posedge, reset=reset)
    def getTrnMsg():

        a = intbv(message)
        if mode == 0:
            if a == 15:
                out.next = '0000'
                print("2_", out, a)
            elif a > 15 - key:
                out.next = bin(a + key)
                print("3_", out, a)
            elif a > 0 + key:
                out.next = bin(a+key)
            else:
                print("else")
        elif mode == 1:
            if a == 0:
                out.next = '1111'
            elif a > 15:
                out.next = bin(a - key)

        print(out)



    # def getTranslatedMessage():
    #     if mode == 0:
    #         if key == 1:
    #             if message == '00':
    #                 out.next = '01'
    #             elif message == '01':
    #                 out.next = '10'
    #             elif message == '10':
    #                 out.next = '11'
    #             elif message == '11':
    #                 out.next = '00'
    #         elif key == 2:
    #             if message == '00':
    #                 out.next = '10'
    #             elif message == '01':
    #                 out.next = '11'
    #             elif message == '10':
    #                 out.next = '00'
    #             elif message == '11':
    #                 out.next = '01'
    #         elif key == 3:
    #             if message == '00':
    #                 out.next = '11'
    #             elif message == '01':
    #                 out.next = '00'
    #             elif message == '10':
    #                 out.next = '01'
    #             elif message == '11':
    #                 out.next = '10'
    #         elif key:
    #             print("unexpected value of key")
    #     elif mode == 1:
    #         if key == 1:
    #             if message == '00':
    #                 out.next = '11'
    #             elif message == '01':
    #                 out.next = '00'
    #             elif message == '10':
    #                 out.next = '01'
    #             elif message == '11':
    #                 out.next = '10'
    #         elif key == 2:
    #             if message == '00':
    #                 out.next = '10'
    #             elif message == '01':
    #                 out.next = '11'
    #             elif message == '10':
    #                 out.next = '00'
    #             elif message == '11':
    #                 out.next = '01'
    #         elif key == 3:
    #             if message == '00':
    #                 out.next = '01'
    #             elif message == '01':
    #                 out.next = '10'
    #             elif message == '10':
    #                 out.next = '11'
    #             elif message == '11':
    #                 out.next = '00'
    #         elif key:
    #             print("unexpected value of key")
    #     elif mode:
    #         print("unexpected value of mode")
    #
    #         return out
        return getTrnMsg
        return instances()
cezar(mode=0, key=1, out='0000', message='1010')