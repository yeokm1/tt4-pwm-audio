![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg)

# tt4-pwm-audio

A Verilog project that takes in 8-bit audio over a parallel (port) interface then generates an analog audio signal like a Covox Speech Thing.

## How it works?

2 DAC techniques are used to generate the audio
* Standard PWM on output pin 0
* First-order sigma-delta modulator on output pin 1

## Testing

### One time setup
I used Debian/Ubuntu WSL on Windows to run the tests.

```bash
sudo apt update
sudo apt install iverilog verilator python3-pip
pip3 install cocotb pytest
```

### Run

```bash
cd tt4-pwm-audio/src
make

# After done
make clean
```

### Actual FPGA

The code was also tested on a [Mimas A7 Artix 7 FPGA board](https://numato.com/product/mimas-a7-artix-7-fpga-development-board/). The Vivado project is placed into the `covox-pwm` directory.

<img src="images\mimas-a7-pwm.jpg" width="600">

This is the pinout and function list for the FPGA

#### Input table

| Module input | Module function        | FPGA pin name                          | FPGA pin description    |
|--------------|------------------------|----------------------------------------|-------------------------|
| ui_in[0...7] | Audio Bit 0 to 7 (LSB) | F19, E19, D20, C22, F18, C18, D17, B20 |                         |
| ena          | Enable pin active-high | P19                                    | Down Button             |
| clk          | Clock                  | H4                                     | 100Mhz oscillator input |
| rst_n        | Reset pin active-low   | P20                                    | Left Button             |
#### Output table


| Module output | Module function              | FPGA pin name | FPGA pin description |
|---------------|------------------------------|---------------|----------------------|
| uo_out[0]     | Standard PWM audio output    | B17           |                      |
| uo_out[1]     | Sigma-delta modulator output | A18           |                      |
| uo_out[2]     | From ena pin                 | L14           | LED LD3              |
| uo_out[3]     | From clk pin                 | L15           | LED LD4              |
| uo_out[4]     | From rst_n pin               | L16           | LED LD5              |
| uo_out[5]     | Static 1                     | K16           | LED LD6              |
| uo_out[6]     | Static 0                     | M15           | LED LD7              |
| uo_out[7]     | Static 1                     | M16           | LED LD8              |

Bidirectional related pins are not used on FPGA testing hence any related code is commented out.

## References
* Standard PWM: https://www.fpga4fun.com/PWM_DAC_1.html
* First-order sigma-delta modulator: https://www.fpga4fun.com/PWM_DAC_2.html
* Alternative Mimas A7 documentation: https://sharmavins23.github.io/Mimas-A7-Artix-7-Documentation/

------

# What is Tiny Tapeout?

TinyTapeout is an educational project that aims to make it easier and cheaper than ever to get your digital designs manufactured on a real chip!

Go to https://tinytapeout.com for instructions!

## How to change the Wokwi project

Edit the [info.yaml](info.yaml) and change the wokwi_id to match your project.

## How to enable the GitHub actions to build the ASIC files

Please see the instructions for:

- [Enabling GitHub Actions](https://tinytapeout.com/faq/#when-i-commit-my-change-the-gds-action-isnt-running)
- [Enabling GitHub Pages](https://tinytapeout.com/faq/#my-github-action-is-failing-on-the-pages-part)

## How does it work?

When you edit the info.yaml to choose a different ID, the [GitHub Action](.github/workflows/gds.yaml) will fetch the digital netlist of your design from Wokwi.

After that, the action uses the open source ASIC tool called [OpenLane](https://www.zerotoasiccourse.com/terminology/openlane/) to build the files needed to fabricate an ASIC.

## Resources

- [FAQ](https://tinytapeout.com/faq/)
- [Digital design lessons](https://tinytapeout.com/digital_design/)
- [Learn how semiconductors work](https://tinytapeout.com/siliwiz/)
- [Join the community](https://discord.gg/rPK2nSjxy8)

## What next?

- Share your GDS on Twitter, tag it [#tinytapeout](https://twitter.com/hashtag/tinytapeout?src=hashtag_click) and [link me](https://twitter.com/matthewvenn)!
