// File: newBit.v
// Generated by MyHDL 0.11
// Date: Mon Oct 18 00:30:20 2021


`timescale 1ns/10ps

module newBit (
    clock,
    enable,
    reset,
    bit_in
);


input clock;
input enable;
input reset;
output bit_in;
reg bit_in;

reg [2:0] counter;



always @(posedge clock, negedge reset) begin: NEWBIT_SEQ
    reg [0-1:0] data;
    if (reset == 0) begin
        counter <= 7;
        bit_in <= 0;
    end
    else begin
        if (enable) begin
            bit_in <= data[(counter + 1)-1:counter];
        end
        counter <= (counter - 1);
    end
end

endmodule
