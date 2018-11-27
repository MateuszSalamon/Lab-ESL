import myhdl
from myhdl import block, always, instance, Signal, ResetSignal, delay, StopSimulation
from ESL_alternative import cezar

ACTIVE_LOW = 0

@block
def testbench():

    mode = Signal(bool(0))
    key = Signal(bool(0))
    clk = Signal(bool(0))
    reset = ResetSignal(1, active=ACTIVE_LOW,async=0)
    message = Signal()
    out = Signal()

    cezar_0 = cezar(mode, key,out, message, clk, reset)

    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
        for i in range(3):
            yield clk.negedge
        for n in (12, 8, 8, 4):
            mode.next = 1
            yield clk.negedge
            mode.next = 0
            for i in range(n-1):
                yield clk.negedge
        raise StopSimulation()

    return cezar_0, clkgen, stimulus

tb = testbench()
tb.config_sim(trace=True)
tb.run_sim()