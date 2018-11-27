from myhdl import block, always_seq, Signal, intbv, enum, instances


@block
def cezar(clk, reset, y, x):
    state_t = enum('enc', 'dec')
    accumulator = Signal(intbv(0)[32:])
    counter = Signal(intbv(0)[32:])
    state = Signal(state_t.COUNT)
    message = Signal(intbv(0)[4:])
    key = Signal(intbv(0)[3:].signed())

    @always_seq(clk.posedge, reset=reset)
    def enc_proc():
        if state == state_t.dec:
            key.next = -key

        x.next =  message + key
        if x > 15:
            x.next = 0 + key
        elif x < 0:
            x.next = 15 + key

        elif state == state_t.enc:
            key.next = key
            x.next = message + key
            if x > 15:
                x.next = 0 + key
            elif x < 0:
                x.next = 15 + key


        else:
            raise ValueError("Undefined state")

    return instances()
