from myhdl import block, always_seq, Signal, intbv, enum, instances,bin


@block
def cezar(clk, reset, out, message, state, key):
    # state_t = enum('enc', 'dec')
    # state = Signal(state_t.enc)
    # max_value = 15
    # min_value = 0

    @always_seq(clk.posedge, reset=reset)
    def cezar_proc():

        #out.tvalid.next = 0
        #out.tlast.next = 0
        # message.tready.next = 1
        # out.tdata.next = Signal(intbv(0)[32:])
        # max_value = 2**len(message.tdata)-1

        # if state == state_t.enc:
        if state == 1:
            out.tdata.next = message.tdata + key
            # while((out.tdata >= max_value)or (out.tdata <=min_value)):
            # if out.tdata > max_value:
            #     out.tdata.next = out.tdata - max_value
            # elif out.tdata < min_value:
            #     out.tdata.next = out.tdata + max_value
        # elif state == state_t.dec:
        elif state == 0:
            # key.tdata.next= -key.tdata
            out.tdata.next = message.tdata - key
            # while ((out.tdata >= max_value) or (out.tdata <= min_value)):
            # if out.tdata > max_value:
            #     out.tdata.next = out.tdata - max_value
            # elif out.tdata < min_value:
            #     out.tdata.next = out.tdata + max_value

        else:
            raise ValueError("Undefined state")

    return instances()