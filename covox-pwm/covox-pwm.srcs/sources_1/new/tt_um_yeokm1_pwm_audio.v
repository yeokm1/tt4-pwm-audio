//`default_nettype none
//`timescale 1ns / 1ps

module tt_um_yeokm1_pwm_audio #( parameter MAX_COUNT = 10_000_000 ) (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    //input  wire [7:0] uio_in,   // IOs: Input path
    //output wire [7:0] uio_out,  // IOs: Output path
    //output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // will go high when the design is enabled
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

// Set bidir pins all to output mode
//assign uio_oe = 8'hFF;

// Set input to bidir output
//assign uio_out = ui_in;

reg [7:0] pwm_cnt;
reg [8:0] fsdm_accumulator;

always @(posedge clk) begin

    if(rst_n == 0) begin
        pwm_cnt <= 0;
        fsdm_accumulator <= 0;
    end else if (ena) begin
        pwm_cnt <= pwm_cnt + 1;
        fsdm_accumulator <= fsdm_accumulator[7:0] + ui_in;
    end

end

// Alternate numbering to show output is active
assign uo_out[7] = 1;
assign uo_out[6] = 0;
assign uo_out[5] = 1;

// Pipe some inputs to output for debugging
assign uo_out[4] = rst_n;
assign uo_out[3] = clk;
assign uo_out[2] = ena;

assign uo_out[1] = fsdm_accumulator[8];
assign uo_out[0] = (ui_in > pwm_cnt);

// Sources
// Standard PWM
// https://www.fpga4fun.com/PWM_DAC_1.html

// First-order sigma-delta modulator
// https://www.fpga4fun.com/PWM_DAC_2.html

endmodule