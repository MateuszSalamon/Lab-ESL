from myhdl import Signal, ResetSignal, modbv

from Cezar import Cezar

def convert_Cezar(hdl):
    """Convert inc block to Verilog or VHDL."""

    m = 127

    key = Signal(modbv(0)[m:])
    mode = Signal(bool(0))
    clk = Signal(bool(0))
    reset = ResetSignal(0, active=0, async=True)

    Cezar_1 = Cezar(clk, reset, mode, key)

    Cezar_1.convert(hdl=hdl)


convert_Cezar(hdl='Verilog')
convert_Cezar(hdl='VHDL')