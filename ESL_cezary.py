from myhdl import block, always_seq, Signal, intbv, enum, instances,bin


@block
def cezar(clk, reset, out, message, state, key):
    # state_t = enum('enc', 'dec')
    # state = Signal(state_t.enc)


    @always_seq(clk.posedge, reset=reset)
    def cezar_proc():
        out.tvalid.next = 0
        out.tlast.next = 0
        # message.tready.next = 1
        out.tdata.next = Signal(intbv(0)[32:])
        # if state == state_t.enc:
        if state == 1:
            out.tdata.next = message.tdata + key
            if out.tdata  > 15:
                out.tdata.next = 0 + key
            elif out.tdata  < 0:
                out.tdata.next = 15+ key
        # elif state == state_t.dec:
        elif state == 0:
            # key.next= -key
            out.tdata.next = message.tdata - key
            if out.tdata  > 15:
                out.tdata.next = 0 - key
            elif out.tdata  < 0:
                out.tdata.next = 15 - key

        else:
            raise ValueError("Undefined state")

    return instances()
