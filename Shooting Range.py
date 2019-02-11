def shot(wall1, wall2, shot_point, later_point):
    wall1_x, wall1_y = wall1
    wall2_x, wall2_y = wall2
    sp_x, sp_y = shot_point
    lp_x, lp_y = later_point

    i = wall2_x - wall1_x
    j = wall2_y - wall1_y
    if i:
        wa = -j / i
        wb = 1
        wc = wall1_x * j / i - wall1_y
    else:
        wa = 1
        wb = 0
        wc = -wall1_x
    di = lp_x - sp_x
    dj = lp_y - sp_y
    if di:
        sa = -dj / di
        sb = 1
        sc = sp_x * dj / di - sp_y
    else:
        sa = 1
        sb = 0
        sc = - sp_x

    if (wa, wb) == (sa, sb):
        return -1
    if sa: wa, wb, wc, sa, sb, sc = sa, sb, sc, wa, wb, wc
    if wa and sa:
        sb -= wb * sa / wa
        sc -= wc * sa / wa
    y = -sc / sb
    x = -(wc + wb * y) / wa
    if ((x - sp_x) * (lp_x - sp_x) + (y - sp_y) * (lp_y - sp_y)) < 0:
        return -1
    if wall2_x - wall1_x:
        cf = (x - wall1_x) / (wall2_x - wall1_x)
    else:
        cf = (y - wall1_y) / (wall2_y - wall1_y)
    if 0 <= cf <= 1:
        return int(100 * (1 - abs(2 * cf - 1)) + .5)
    return -1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"
