module tb_convert8b10b;

reg clock;
reg bit_in;
reg reset;
wire [2:0] HGF;
wire [4:0] EDCBA;

initial begin
    $from_myhdl(
        clock,
        bit_in,
        reset
    );
    $to_myhdl(
        HGF,
        EDCBA
    );
end

convert8b10b dut(
    clock,
    bit_in,
    reset,
    HGF,
    EDCBA
);

endmodule
