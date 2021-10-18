module tb_newBit;

reg clock;
reg enable;
reg reset;
wire bit_in;

initial begin
    $from_myhdl(
        clock,
        enable,
        reset
    );
    $to_myhdl(
        bit_in
    );
end

newBit dut(
    clock,
    enable,
    reset,
    bit_in
);

endmodule
