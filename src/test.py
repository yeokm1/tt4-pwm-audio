import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

PERIOD_CYCLES = 256


@cocotb.test()
async def test_tt_um_yeokm1_pwm_audio(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 10, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Applying reset")
    # dut._log.info("uo out " + str(dut.uo_out.value))
    dut.rst_n.value = 0
    dut.ena.value = 0
    # dut._log.info("uo out " + str(dut.uo_out.value))
    await ClockCycles(dut.clk, 10)

    dut._log.info("Releasing reset")
    # dut._log.info("uo out " + str(dut.uo_out.value))
    dut.rst_n.value = 1
    dut.ena.value = 1

    # Check bidir pins are set as output
    assert str(dut.uio_oe.value) == "11111111"

    dut._log.info("Testing Ton and Toff range")

    # Only the test the standard PWM algorithm
    for i in range(PERIOD_CYCLES):

        dut.ui_in.value = i

        # dut._log.info("Testing Tonn " + str(i))

        for j in range(PERIOD_CYCLES):
            await ClockCycles(dut.clk, 1)

            # Check bidir output pins are exactly the same as input
            assert int(dut.uio_out.value) == i

            # For debug use
            # if i <= 1 and j <= 1:
            #     dut._log.info("i " + str(i) + " j " + str(j))
            #     dut._log.info("ui in " + str(dut.ui_in.value))
            #     dut._log.info("uio out " + str(dut.uio_out.value))
            #     dut._log.info("uio oe " + str(dut.uio_oe.value))
            #     dut._log.info("uo out " + str(dut.uo_out.value))

            # Verify correct ratio of Ton and Toff for PWM, FSDM is not tested
            if j < i:
                assert str(dut.uo_out.value[7]) == "1"
            else:
                assert str(dut.uo_out.value[7]) == "0"
