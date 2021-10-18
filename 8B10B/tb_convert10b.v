module tb_convert10b;

reg clock;
reg reset;
reg [2:0] HGF;
reg [4:0] EDCBA;
wire [3:0] fghj;
wire [5:0] abcdei;

initial begin
    $from_myhdl(
        clock,
        reset,
        HGF,
        EDCBA
    );
    $to_myhdl(
        fghj,
        abcdei
    );
end

convert10b dut(
    clock,
    reset,
    HGF,
    EDCBA,
    fghj,
    abcdei
);

endmodule
