// File: convert8b10b.v
// Generated by MyHDL 0.11
// Date: Mon Oct 18 00:30:20 2021


`timescale 1ns/10ps

module convert8b10b (
    clock,
    bit_in,
    reset,
    HGF,
    EDCBA
);


input clock;
input bit_in;
input reset;
output [2:0] HGF;
reg [2:0] HGF;
output [4:0] EDCBA;
reg [4:0] EDCBA;

reg [2:0] i;



always @(posedge clock, negedge reset) begin: CONVERT8B10B_SEQ
    if (reset == 0) begin
        i <= 0;
        EDCBA <= 0;
        HGF <= 0;
    end
    else begin
        if ((i < 3)) begin
            if (bit_in) begin
                case (i)
                    'h0: begin
                        HGF <= (HGF + 4);
                    end
                    'h1: begin
                        HGF <= (HGF + 2);
                    end
                    'h2: begin
                        HGF <= (HGF + 1);
                    end
                endcase
            end
        end
        else begin
            if (bit_in) begin
                case (i)
                    'h3: begin
                        EDCBA <= (EDCBA + 16);
                    end
                    'h4: begin
                        EDCBA <= (EDCBA + 8);
                    end
                    'h5: begin
                        EDCBA <= (EDCBA + 4);
                    end
                    'h6: begin
                        EDCBA <= (EDCBA + 2);
                    end
                    'h7: begin
                        EDCBA <= (EDCBA + 1);
                    end
                endcase
            end
        end
        if ((i >= 8)) begin
            i <= 0;
        end
        i <= (i + 1);
    end
end

endmodule
