// File: convert10b.v
// Generated by MyHDL 0.11
// Date: Mon Oct 18 00:30:20 2021


`timescale 1ns/10ps

module convert10b (
    clock,
    reset,
    HGF,
    EDCBA,
    fghj,
    abcdei
);


input clock;
input reset;
input [2:0] HGF;
input [4:0] EDCBA;
output [3:0] fghj;
reg [3:0] fghj;
output [5:0] abcdei;
reg [5:0] abcdei;

reg [2:0] i;



always @(negedge clock, negedge reset) begin: CONVERT10B_SEQ
    if (reset == 0) begin
        i <= 0;
        fghj <= 0;
        abcdei <= 0;
    end
    else begin
        if ((i == 2)) begin
            case (HGF)
                'h0: begin
                    fghj <= 4;
                end
                'h1: begin
                    fghj <= 9;
                end
                'h2: begin
                    fghj <= 5;
                end
                'h3: begin
                    fghj <= 3;
                end
                'h4: begin
                    fghj <= 2;
                end
                'h5: begin
                    fghj <= 10;
                end
                'h6: begin
                    fghj <= 6;
                end
                'h7: begin
                    fghj <= 1;
                end
            endcase
        end
        if ((i == 7)) begin
            case (EDCBA)
                'h0: begin
                    abcdei <= 39;
                end
                'h1: begin
                    abcdei <= 29;
                end
                'h2: begin
                    abcdei <= 45;
                end
                'h3: begin
                    abcdei <= 49;
                end
                'h4: begin
                    abcdei <= 53;
                end
                'h5: begin
                    abcdei <= 41;
                end
                'h6: begin
                    abcdei <= 25;
                end
                'h7: begin
                    abcdei <= 56;
                end
                'h8: begin
                    abcdei <= 57;
                end
                'h9: begin
                    abcdei <= 37;
                end
                'ha: begin
                    abcdei <= 21;
                end
                'hb: begin
                    abcdei <= 52;
                end
                'hc: begin
                    abcdei <= 13;
                end
                'hd: begin
                    abcdei <= 44;
                end
                'he: begin
                    abcdei <= 28;
                end
                'hf: begin
                    abcdei <= 23;
                end
                'h10: begin
                    abcdei <= 27;
                end
                'h11: begin
                    abcdei <= 35;
                end
                'h12: begin
                    abcdei <= 19;
                end
                'h13: begin
                    abcdei <= 50;
                end
                'h14: begin
                    abcdei <= 11;
                end
                'h15: begin
                    abcdei <= 42;
                end
                'h16: begin
                    abcdei <= 26;
                end
                'h17: begin
                    abcdei <= 58;
                end
                'h18: begin
                    abcdei <= 51;
                end
                'h19: begin
                    abcdei <= 38;
                end
                'h1a: begin
                    abcdei <= 22;
                end
                'h1b: begin
                    abcdei <= 54;
                end
                'h1c: begin
                    abcdei <= 14;
                end
                'h1d: begin
                    abcdei <= 46;
                end
                'h1e: begin
                    abcdei <= 30;
                end
                'h1f: begin
                    abcdei <= 43;
                end
            endcase
        end
        i <= (i + 1);
    end
end

endmodule
