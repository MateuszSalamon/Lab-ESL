from myhdl import block, instances, enum, delay, Simulation, always_seq, now, Signal, intbv

#mode 0 - encrypt
#mode 1 - decrypt
#key_max - 1,2 or 3
#message - 2 bit signal

@block
def Cezar(clk, reset, mode, key, message):
    clk = Signal(0)
    reset = Signal(0)
    mode = Signal(0)
    key = int
    message = Signal(2)
    out = Signal(2)


    @always_seq(clk.posedge, reset=reset)
    def getTranslatedMessage():
        if mode == 0:
            if key == 1:
                if message == '00':
                    out.next = '01'
                elif message == '01':
                    out.next = '10'
                elif message == '10':
                    out.next = '11'
                elif message == '11':
                    out.next = '00'
            elif key == 2:
                if message == '00':
                    out.next = '10'
                elif message == '01':
                    out.next = '11'
                elif message == '10':
                    out.next = '00'
                elif message == '11':
                    out.next = '01'
            elif key == 3:
                if message == '00':
                    out.next = '11'
                elif message == '01':
                    out.next = '00'
                elif message == '10':
                    out.next = '01'
                elif message == '11':
                    out.next = '10'
            elif key:
                print("unexpected value of key")
        elif mode == 1:
            if key == 1:
                if message == '00':
                    out.next = '11'
                elif message == '01':
                    out.next = '00'
                elif message == '10':
                    out.next = '01'
                elif message == '11':
                    out.next = '10'
            elif key == 2:
                if message == '00':
                    out.next = '10'
                elif message == '01':
                    out.next = '11'
                elif message == '10':
                    out.next = '00'
                elif message == '11':
                    out.next = '01'
            elif key == 3:
                if message == '00':
                    out.next = '01'
                elif message == '01':
                    out.next = '10'
                elif message == '10':
                    out.next = '11'
                elif message == '11':
                    out.next = '00'
            elif key:
                print("unexpected value of key")
        elif mode:
            print("unexpected value of mode")

            return out
        return instances()
