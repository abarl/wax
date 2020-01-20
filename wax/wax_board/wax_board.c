#include <inttypes.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

struct game_state {
    uint64_t white_pawns;
    uint64_t white_king;
    uint64_t white_queen;
    uint64_t white_rooks;
    uint64_t white_knights;
    uint64_t white_bishops;
    uint64_t black_pawns;
    uint64_t black_king;
    uint64_t black_queen;
    uint64_t black_rooks;
    uint64_t black_knights;
    uint64_t black_bishops;
};

const struct game_state NEW_GAME = {
    (uint64_t)71776119061217280,
    (uint64_t)576460752303423488,
    (uint64_t)1152921504606846976,
    (uint64_t)9295429630892703744,
    (uint64_t)4755801206503243776,
    (uint64_t)2594073385365405696,
    (uint64_t)65280,
    (uint64_t)8,
    (uint64_t)16,
    (uint64_t)129,
    (uint64_t)66,
    (uint64_t)36
};

uint64_t bin_to_int(char* n) {
    uint64_t d = 0, i = 0;
    while (i <= strlen(n) - 1) {
        if (n[(strlen(n) - i - 1)] == '1')
        {
            d += pow(2, i);
        }
        ++i;
    }
    return d;
}

int main(void) {
    uint64_t i = bin_to_int("0000000000000000000000000000000000000000000000000000000000100100");
    printf("Int is: %llu\n", i);
    return 0;
}
