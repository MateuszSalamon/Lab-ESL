from myhdl import block, instance, Signal, ResetSignal, StopSimulation, instances, delay
import os


from clk_stim import clk_stim
from ESL_encryptor_from_mysum import cezar


@block
def testbench(vhdl_output_path=None):

    reset = ResetSignal(0, active=0, async=False)
    clk = Signal(bool(0))
    x = Signal(0)
    y = Signal(0)


    clk_gen = clk_stim(clk, period=10)

    @instance
    def reset_gen():
        reset.next = 0
        yield delay(54)
        yield clk.negedge
        reset.next = 1

    @instance
    def write_stim():
        values = list(range(50, 100))
        i = 0
        yield reset.posedge
        while i < len(values):
            yield clk.negedge
            x.next = 1
            x.next = values[i]
            if i == len(values) - 1:
                x.next = 1
            else:
                x.next = 0
            if x == 1:
                i += 1
        yield clk.negedge
        x.next = 0

    @instance
    def read_stim():
        yield reset.posedge
        yield delay(601)
        yield clk.negedge
        y.next = 1
        while True:
            yield clk.negedge
            if y == 1:
                break

        for i in range(10):
            yield clk.negedge
        raise StopSimulation()

    uut = cezar(clk, reset, y, x)

    if vhdl_output_path is not None:
        uut.convert(hdl='VHDL', path=vhdl_output_path)
    return instances()


if __name__ == '__main__':
    trace_save_path = '../out/testbench/'
    vhdl_output_path = '../out/vhdl/'
    os.makedirs(os.path.dirname(trace_save_path), exist_ok=True)
    os.makedirs(os.path.dirname(vhdl_output_path), exist_ok=True)

    tb = testbench(vhdl_output_path)
    tb.config_sim(trace=True, directory=trace_save_path, name='my_sum_tb')
    tb.run_sim()