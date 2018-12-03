from myhdl import block, instance, Signal, ResetSignal, StopSimulation, instances, delay, intbv
import os

from axi.axis import Axis
# from myhdl_sim import clk_stim
from ESL_cezary import cezar


@block
def testbench(vhdl_output_path=None):

    reset = ResetSignal(0, active=0, async=False)
    clk = Signal(bool(0))
    key = Signal(bool(0))
    state = Signal(bool(0))
    message = Axis(32)
    out = Axis(32)
    period = 10
    state_period = 5*period
    #clk_gen = clk_stim(clk, period=10)

    low_time = int(period / 2)
    high_time = period - low_time
    state_low_time = int(state_period / 2)
    state_high_time = state_period - state_low_time

    @instance
    def drive_clk():
        while True:
            yield delay(low_time)
            clk.next = 1
            yield delay(high_time)
            clk.next = 0

    @instance
    def drive_state():
        while True:
            yield delay(state_low_time)
            state.next = 1
            yield delay(state_high_time)
            state.next = 0

    @instance
    def drive_key():
        while True:
            yield delay(state_low_time+2)
            key.next = 0
            yield delay(state_high_time+1)
            key.next = 1


    @instance
    def reset_gen():
        reset.next = 0
        yield delay(54)
        yield clk.negedge
        reset.next = 1

    # @instance
    # def mode_stim():
################################################################################

    @instance
    def write_stim():
        values = list(range(50, 100))
        i = 0
        yield reset.posedge
        while i < len(values):
            yield clk.negedge
            message.tvalid.next = 1
            message.tdata.next = values[i]
            if i == len(values) - 1:
                message.tlast.next = 1
            else:
                message.tlast.next = 0
            if message.tready == 1:
                i += 1
        yield clk.negedge
        message.tvalid.next = 0

    @instance
    def read_stim():
        yield reset.posedge
        yield delay(601)
        yield clk.negedge
        out.tready.next = 1
        while True:
            yield clk.negedge
            if out.tlast == 1:
                break

        for i in range(5):
            yield clk.negedge
        raise StopSimulation()
######################################################################################################################
    uut = cezar(clk, reset, out, message, state, key)

    if vhdl_output_path is not None:
        uut.convert(hdl='VHDL', path=vhdl_output_path)
    return instances()


if __name__ == '__main__':
    trace_save_path = 'C:/Users/student/Documents/MSDC/out/testbench/'
    vhdl_output_path = 'C:/Users/student/Documents/MSDC/out/vhdl/'
    os.makedirs(os.path.dirname(trace_save_path), exist_ok=True)
    os.makedirs(os.path.dirname(vhdl_output_path), exist_ok=True)

    tb = testbench(vhdl_output_path)
    tb.config_sim(trace=True, directory=trace_save_path, name='ESL_cezar_tb')
    tb.run_sim()
