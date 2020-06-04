# File: T (Python 2.2)

import whrandom
from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
import random
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from otp.avatar import AvatarDNA
notify = directNotify.newCategory('ToonDNA')
toonHeadTypes = [
    'dls',
    'dss',
    'dsl',
    'dll',
    'cls',
    'css',
    'csl',
    'cll',
    'hls',
    'hss',
    'hsl',
    'hll',
    'mls',
    'mss',
    'rls',
    'rss',
    'rsl',
    'rll',
    'fls',
    'fss',
    'fsl',
    'fll',
    'pls',
    'pss',
    'psl',
    'pll']
toonHeadAnimalIndices = [
    0,
    4,
    8,
    12,
    14,
    18,
    22]
toonTorsoTypes = [
    'ss',
    'ms',
    'ls',
    'sd',
    'md',
    'ld',
    's',
    'm',
    'l']
toonLegTypes = [
    's',
    'm',
    'l']
Shirts = [
    'phase_3/maps/desat_shirt_1.jpg',
    'phase_3/maps/desat_shirt_2.jpg',
    'phase_3/maps/desat_shirt_3.jpg',
    'phase_3/maps/desat_shirt_4.jpg',
    'phase_3/maps/desat_shirt_5.jpg',
    'phase_3/maps/desat_shirt_6.jpg',
    'phase_3/maps/desat_shirt_7.jpg',
    'phase_3/maps/desat_shirt_8.jpg',
    'phase_3/maps/desat_shirt_9.jpg',
    'phase_3/maps/desat_shirt_10.jpg',
    'phase_3/maps/desat_shirt_11.jpg',
    'phase_3/maps/desat_shirt_12.jpg',
    'phase_3/maps/desat_shirt_13.jpg',
    'phase_3/maps/desat_shirt_14.jpg',
    'phase_3/maps/desat_shirt_15.jpg',
    'phase_3/maps/desat_shirt_16.jpg',
    'phase_3/maps/desat_shirt_17.jpg',
    'phase_3/maps/desat_shirt_18.jpg',
    'phase_3/maps/desat_shirt_19.jpg',
    'phase_3/maps/desat_shirt_20.jpg',
    'phase_3/maps/desat_shirt_21.jpg',
    'phase_3/maps/desat_shirt_22.jpg',
    'phase_3/maps/desat_shirt_23.jpg',
    'phase_4/maps/female_shirt1b.jpg',
    'phase_4/maps/female_shirt2.jpg',
    'phase_4/maps/female_shirt3.jpg',
    'phase_4/maps/male_shirt1.jpg',
    'phase_4/maps/male_shirt2_palm.jpg',
    'phase_4/maps/male_shirt3c.jpg',
    'phase_4/maps/shirt_ghost.jpg',
    'phase_4/maps/shirt_pumkin.jpg',
    'phase_4/maps/holiday_shirt1.jpg',
    'phase_4/maps/holiday_shirt2b.jpg',
    'phase_4/maps/holidayShirt3b.jpg',
    'phase_4/maps/holidayShirt4.jpg',
    'phase_4/maps/female_shirt1b.jpg',
    'phase_4/maps/female_shirt5New.jpg',
    'phase_4/maps/shirtMale4B.jpg',
    'phase_4/maps/shirt6New.jpg',
    'phase_4/maps/shirtMaleNew7.jpg',
    'phase_4/maps/femaleShirtNew6.jpg',
    'phase_4/maps/Vday1Shirt5.jpg',
    'phase_4/maps/Vday1Shirt6SHD.jpg',
    'phase_4/maps/Vday1Shirt4.jpg',
    'phase_4/maps/Vday_shirt2c.jpg',
    'phase_4/maps/shirtTieDyeNew.jpg',
    'phase_4/maps/male_shirt1.jpg',
    'phase_4/maps/StPats_shirt1.jpg',
    'phase_4/maps/StPats_shirt2.jpg',
    'phase_4/maps/ContestfishingVestShirt2.jpg',
    'phase_4/maps/ContestFishtankShirt1.jpg',
    'phase_4/maps/ContestPawShirt1.jpg',
    'phase_4/maps/CowboyShirt1.jpg',
    'phase_4/maps/CowboyShirt2.jpg',
    'phase_4/maps/CowboyShirt3.jpg',
    'phase_4/maps/CowboyShirt4.jpg',
    'phase_4/maps/CowboyShirt5.jpg',
    'phase_4/maps/CowboyShirt6.jpg',
    'phase_4/maps/4thJulyShirt1.jpg',
    'phase_4/maps/4thJulyShirt2.jpg',
    'phase_4/maps/shirt_Cat7_01.jpg',
    'phase_4/maps/shirt_Cat7_02.jpg']
BoyShirts = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (8, 8),
    (9, 9),
    (10, 0),
    (11, 0),
    (14, 10),
    (16, 0),
    (17, 0),
    (18, 12),
    (19, 13)]
GirlShirts = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (5, 5),
    (6, 6),
    (7, 7),
    (9, 9),
    (12, 0),
    (13, 11),
    (15, 11),
    (16, 0),
    (20, 0),
    (21, 0),
    (22, 0)]

def isValidBoyShirt(index):
    for pair in BoyShirts:
        if index == pair[0]:
            return 1
        
    
    return 0


def isValidGirlShirt(index):
    for pair in GirlShirts:
        if index == pair[0]:
            return 1
        
    
    return 0

Sleeves = [
    'phase_3/maps/desat_sleeve_1.jpg',
    'phase_3/maps/desat_sleeve_2.jpg',
    'phase_3/maps/desat_sleeve_3.jpg',
    'phase_3/maps/desat_sleeve_4.jpg',
    'phase_3/maps/desat_sleeve_5.jpg',
    'phase_3/maps/desat_sleeve_6.jpg',
    'phase_3/maps/desat_sleeve_7.jpg',
    'phase_3/maps/desat_sleeve_8.jpg',
    'phase_3/maps/desat_sleeve_9.jpg',
    'phase_3/maps/desat_sleeve_10.jpg',
    'phase_3/maps/desat_sleeve_15.jpg',
    'phase_3/maps/desat_sleeve_16.jpg',
    'phase_3/maps/desat_sleeve_19.jpg',
    'phase_3/maps/desat_sleeve_20.jpg',
    'phase_4/maps/female_sleeve1b.jpg',
    'phase_4/maps/female_sleeve2.jpg',
    'phase_4/maps/female_sleeve3.jpg',
    'phase_4/maps/male_sleeve1.jpg',
    'phase_4/maps/male_sleeve2_palm.jpg',
    'phase_4/maps/male_sleeve3c.jpg',
    'phase_4/maps/shirt_Sleeve_ghost.jpg',
    'phase_4/maps/shirt_Sleeve_pumkin.jpg',
    'phase_4/maps/holidaySleeve1.jpg',
    'phase_4/maps/holidaySleeve3.jpg',
    'phase_4/maps/female_sleeve1b.jpg',
    'phase_4/maps/female_sleeve5New.jpg',
    'phase_4/maps/male_sleeve4New.jpg',
    'phase_4/maps/sleeve6New.jpg',
    'phase_4/maps/SleeveMaleNew7.jpg',
    'phase_4/maps/female_sleeveNew6.jpg',
    'phase_4/maps/Vday5Sleeve.jpg',
    'phase_4/maps/Vda6Sleeve.jpg',
    'phase_4/maps/Vday_shirt4sleeve.jpg',
    'phase_4/maps/Vday2cSleeve.jpg',
    'phase_4/maps/sleeveTieDye.jpg',
    'phase_4/maps/male_sleeve1.jpg',
    'phase_4/maps/StPats_sleeve.jpg',
    'phase_4/maps/StPats_sleeve2.jpg',
    'phase_4/maps/ContestfishingVestSleeve1.jpg',
    'phase_4/maps/ContestFishtankSleeve1.jpg',
    'phase_4/maps/ContestPawSleeve1.jpg',
    'phase_4/maps/CowboySleeve1.jpg',
    'phase_4/maps/CowboySleeve2.jpg',
    'phase_4/maps/CowboySleeve3.jpg',
    'phase_4/maps/CowboySleeve4.jpg',
    'phase_4/maps/CowboySleeve5.jpg',
    'phase_4/maps/CowboySleeve6.jpg',
    'phase_4/maps/4thJulySleeve1.jpg',
    'phase_4/maps/4thJulySleeve2.jpg',
    'phase_4/maps/shirt_sleeveCat7_01.jpg',
    'phase_4/maps/shirt_sleeveCat7_02.jpg']
BoyShorts = [
    'phase_3/maps/desat_shorts_1.jpg',
    'phase_3/maps/desat_shorts_2.jpg',
    'phase_3/maps/desat_shorts_4.jpg',
    'phase_3/maps/desat_shorts_6.jpg',
    'phase_3/maps/desat_shorts_7.jpg',
    'phase_3/maps/desat_shorts_8.jpg',
    'phase_3/maps/desat_shorts_9.jpg',
    'phase_3/maps/desat_shorts_10.jpg',
    'phase_4/maps/VdayShorts2.jpg',
    'phase_4/maps/shorts4.jpg',
    'phase_4/maps/shorts1.jpg',
    'phase_4/maps/shorts5.jpg',
    'phase_4/maps/CowboyShorts1.jpg',
    'phase_4/maps/CowboyShorts2.jpg',
    'phase_4/maps/4thJulyShorts1.jpg',
    'phase_4/maps/shortsCat7_01.jpg']
SHORTS = 0
SKIRT = 1
GirlBottoms = [
    ('phase_3/maps/desat_skirt_1.jpg', SKIRT),
    ('phase_3/maps/desat_skirt_2.jpg', SKIRT),
    ('phase_3/maps/desat_skirt_3.jpg', SKIRT),
    ('phase_3/maps/desat_skirt_4.jpg', SKIRT),
    ('phase_3/maps/desat_skirt_5.jpg', SKIRT),
    ('phase_3/maps/desat_shorts_1.jpg', SHORTS),
    ('phase_3/maps/desat_shorts_5.jpg', SHORTS),
    ('phase_3/maps/desat_skirt_6.jpg', SKIRT),
    ('phase_3/maps/desat_skirt_7.jpg', SKIRT),
    ('phase_3/maps/desat_shorts_10.jpg', SHORTS),
    ('phase_4/maps/female_skirt1.jpg', SKIRT),
    ('phase_4/maps/female_skirt2.jpg', SKIRT),
    ('phase_4/maps/female_skirt3.jpg', SKIRT),
    ('phase_4/maps/VdaySkirt1.jpg', SKIRT),
    ('phase_4/maps/skirtNew5.jpg', SKIRT),
    ('phase_4/maps/shorts5.jpg', SHORTS),
    ('phase_4/maps/CowboySkirt1.jpg', SKIRT),
    ('phase_4/maps/CowboySkirt2.jpg', SKIRT),
    ('phase_4/maps/4thJulySkirt1.jpg', SKIRT),
    ('phase_4/maps/skirtCat7_01.jpg', SKIRT)]
ClothesColors = [
    VBase4(0.93359400000000003, 0.265625, 0.28125, 1.0),
    VBase4(0.86328099999999997, 0.40625, 0.41796899999999998, 1.0),
    VBase4(0.71093799999999996, 0.234375, 0.4375, 1.0),
    VBase4(0.99218799999999996, 0.48046899999999998, 0.16796900000000001, 1.0),
    VBase4(0.99609400000000003, 0.89843799999999996, 0.32031199999999999, 1.0),
    VBase4(0.55078099999999997, 0.82421900000000003, 0.32421899999999998, 1.0),
    VBase4(0.24218799999999999, 0.74218799999999996, 0.515625, 1.0),
    VBase4(0.43359399999999998, 0.90625, 0.83593799999999996, 1.0),
    VBase4(0.34765600000000002, 0.82031200000000004, 0.953125, 1.0),
    VBase4(0.19140599999999999, 0.5625, 0.77343799999999996, 1.0),
    VBase4(0.28515600000000002, 0.328125, 0.72656200000000004, 1.0),
    VBase4(0.46093800000000001, 0.37890600000000002, 0.82421900000000003, 1.0),
    VBase4(0.546875, 0.28125, 0.75, 1.0),
    VBase4(0.57031200000000004, 0.44921899999999998, 0.16406200000000001, 1.0),
    VBase4(0.640625, 0.35546899999999998, 0.26953100000000002, 1.0),
    VBase4(0.99609400000000003, 0.69531200000000004, 0.51171900000000003, 1.0),
    VBase4(0.83203099999999997, 0.5, 0.296875, 1.0),
    VBase4(0.99218799999999996, 0.48046899999999998, 0.16796900000000001, 1.0),
    VBase4(0.55078099999999997, 0.82421900000000003, 0.32421899999999998, 1.0),
    VBase4(0.43359399999999998, 0.90625, 0.83593799999999996, 1.0),
    VBase4(0.34765600000000002, 0.82031200000000004, 0.953125, 1.0),
    VBase4(0.96875, 0.69140599999999997, 0.69921900000000003, 1.0),
    VBase4(0.99609400000000003, 0.95703099999999997, 0.59765599999999997, 1.0),
    VBase4(0.85546900000000003, 0.93359400000000003, 0.49218800000000001, 1.0),
    VBase4(0.55859400000000003, 0.58984400000000003, 0.875, 1.0),
    VBase4(0.72656200000000004, 0.47265600000000002, 0.859375, 1.0),
    VBase4(0.89843799999999996, 0.61718799999999996, 0.90625, 1.0),
    VBase4(1.0, 1.0, 1.0, 1.0)]
ShirtStyles = {
    'bss1': [
        0,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (27, 27)]],
    'bss2': [
        1,
        1,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12)]],
    'bss3': [
        2,
        2,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12)]],
    'bss4': [
        3,
        3,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12)]],
    'bss5': [
        4,
        4,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12)]],
    'bss6': [
        5,
        5,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12)]],
    'bss7': [
        8,
        8,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (27, 27)]],
    'bss8': [
        9,
        9,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12)]],
    'bss9': [
        10,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (27, 27)]],
    'bss10': [
        11,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (27, 27)]],
    'bss11': [
        14,
        10,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12)]],
    'bss12': [
        16,
        0,
        [
            (27, 27),
            (27, 4),
            (27, 5),
            (27, 6),
            (27, 7),
            (27, 8),
            (27, 9)]],
    'bss13': [
        17,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12)]],
    'bss14': [
        18,
        12,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (27, 27)]],
    'bss15': [
        19,
        13,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (27, 27)]],
    'gss1': [
        0,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
            (27, 27)]],
    'gss2': [
        1,
        1,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26)]],
    'gss3': [
        2,
        2,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26)]],
    'gss4': [
        3,
        3,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26)]],
    'gss5': [
        5,
        5,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26)]],
    'gss6': [
        6,
        6,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26)]],
    'gss7': [
        7,
        7,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26)]],
    'gss8': [
        9,
        9,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26)]],
    'gss9': [
        12,
        0,
        [
            (27, 27)]],
    'gss10': [
        13,
        11,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26)]],
    'gss11': [
        15,
        11,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26)]],
    'gss12': [
        16,
        0,
        [
            (27, 27),
            (27, 4),
            (27, 5),
            (27, 6),
            (27, 7),
            (27, 8),
            (27, 9)]],
    'gss13': [
        20,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26)]],
    'gss14': [
        21,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26)]],
    'gss15': [
        22,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26)]],
    'c_ss1': [
        25,
        16,
        [
            (27, 27)]],
    'c_ss2': [
        27,
        18,
        [
            (27, 27)]],
    'c_ss3': [
        38,
        27,
        [
            (27, 27)]],
    'c_bss1': [
        26,
        17,
        [
            (27, 27)]],
    'c_bss2': [
        28,
        19,
        [
            (27, 27)]],
    'c_bss3': [
        37,
        26,
        [
            (27, 27)]],
    'c_bss4': [
        39,
        28,
        [
            (27, 27)]],
    'c_gss1': [
        23,
        14,
        [
            (27, 27)]],
    'c_gss2': [
        24,
        15,
        [
            (27, 27)]],
    'c_gss3': [
        35,
        24,
        [
            (27, 27)]],
    'c_gss4': [
        36,
        25,
        [
            (27, 27)]],
    'c_gss5': [
        40,
        29,
        [
            (27, 27)]],
    'c_ss4': [
        45,
        34,
        [
            (27, 27)]],
    'c_ss5': [
        46,
        35,
        [
            (27, 27)]],
    'c_ss6': [
        52,
        41,
        [
            (27, 27)]],
    'c_ss7': [
        53,
        42,
        [
            (27, 27)]],
    'c_ss8': [
        54,
        43,
        [
            (27, 27)]],
    'c_ss9': [
        55,
        44,
        [
            (27, 27)]],
    'c_ss10': [
        56,
        45,
        [
            (27, 27)]],
    'c_ss11': [
        57,
        46,
        [
            (27, 27)]],
    'hw_ss1': [
        29,
        20,
        [
            (27, 27)]],
    'hw_ss2': [
        30,
        21,
        [
            (27, 27)]],
    'wh_ss1': [
        31,
        22,
        [
            (27, 27)]],
    'wh_ss2': [
        32,
        22,
        [
            (27, 27)]],
    'wh_ss3': [
        33,
        23,
        [
            (27, 27)]],
    'wh_ss4': [
        34,
        23,
        [
            (27, 27)]],
    'vd_ss1': [
        41,
        30,
        [
            (27, 27)]],
    'vd_ss2': [
        42,
        31,
        [
            (27, 27)]],
    'vd_ss3': [
        43,
        32,
        [
            (27, 27)]],
    'vd_ss4': [
        44,
        33,
        [
            (27, 27)]],
    'sd_ss1': [
        47,
        36,
        [
            (27, 27)]],
    'sd_ss2': [
        48,
        37,
        [
            (27, 27)]],
    'tc_ss1': [
        49,
        38,
        [
            (27, 27)]],
    'tc_ss2': [
        50,
        39,
        [
            (27, 27)]],
    'tc_ss3': [
        51,
        40,
        [
            (27, 27)]],
    'j4_ss1': [
        58,
        47,
        [
            (27, 27)]],
    'j4_ss2': [
        59,
        48,
        [
            (27, 27)]],
    'c_ss12': [
        60,
        49,
        [
            (27, 27)]],
    'c_ss13': [
        61,
        50,
        [
            (27, 27)]] }
BottomStyles = {
    'bbs1': [
        0,
        [
            0,
            1,
            2,
            4,
            6,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20]],
    'bbs2': [
        1,
        [
            0,
            1,
            2,
            4,
            6,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20]],
    'bbs3': [
        2,
        [
            0,
            1,
            2,
            4,
            6,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20]],
    'bbs4': [
        3,
        [
            0,
            1,
            2,
            4,
            6,
            8,
            9,
            11,
            12,
            13,
            15,
            16,
            17,
            18,
            19,
            20,
            27]],
    'bbs5': [
        4,
        [
            0,
            1,
            2,
            4,
            6,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20]],
    'bbs6': [
        5,
        [
            0,
            1,
            2,
            4,
            6,
            9,
            10,
            11,
            12,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            27]],
    'bbs7': [
        6,
        [
            0,
            1,
            2,
            4,
            6,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            20,
            27]],
    'bbs8': [
        7,
        [
            0,
            1,
            2,
            4,
            6,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            27]],
    'vd_bs1': [
        8,
        [
            27]],
    'c_bs1': [
        9,
        [
            27]],
    'c_bs2': [
        10,
        [
            27]],
    'c_bs5': [
        15,
        [
            27]],
    'sd_bs1': [
        11,
        [
            27]],
    'gsk1': [
        0,
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            21,
            22,
            23,
            24,
            25,
            26,
            27]],
    'gsk2': [
        1,
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            21,
            22,
            23,
            24,
            25,
            26]],
    'gsk3': [
        2,
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            21,
            22,
            23,
            24,
            25,
            26]],
    'gsk4': [
        3,
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            21,
            22,
            23,
            24,
            25,
            26]],
    'gsk5': [
        4,
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            21,
            22,
            23,
            24,
            25,
            26]],
    'gsk6': [
        7,
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            21,
            22,
            23,
            24,
            25,
            26,
            27]],
    'gsk7': [
        8,
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            21,
            22,
            23,
            24,
            25,
            26,
            27]],
    'gsh1': [
        5,
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            21,
            22,
            23,
            24,
            25,
            26,
            27]],
    'gsh2': [
        6,
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            21,
            22,
            23,
            24,
            25,
            26,
            27]],
    'gsh3': [
        9,
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            21,
            22,
            23,
            24,
            25,
            26,
            27]],
    'c_gsk1': [
        10,
        [
            27]],
    'c_gsk2': [
        11,
        [
            27]],
    'c_gsk3': [
        12,
        [
            27]],
    'vd_gs1': [
        13,
        [
            27]],
    'c_gsk4': [
        14,
        [
            27]],
    'sd_gs1': [
        15,
        [
            27]],
    'c_gsk5': [
        16,
        [
            27]],
    'c_gsk6': [
        17,
        [
            27]],
    'c_bs3': [
        12,
        [
            27]],
    'c_bs4': [
        13,
        [
            27]],
    'j4_bs1': [
        14,
        [
            27]],
    'j4_gs1': [
        18,
        [
            27]],
    'c_gsk7': [
        19,
        [
            27]] }
MAKE_A_TOON = 1
TAMMY_TAILOR = 2004
LONGJOHN_LEROY = 1007
TAILOR_HARMONY = 4008
BONNIE_BLOSSOM = 5007
WARREN_BUNDLES = 3008
WORNOUT_WAYLON = 9010
TailorCollections = {
    MAKE_A_TOON: [
        [
            'bss1',
            'bss2',
            'bss3',
            'bss4',
            'bss5',
            'bss6',
            'bss7',
            'bss8',
            'bss9',
            'bss11',
            'bss15'],
        [
            'gss1',
            'gss2',
            'gss3',
            'gss4',
            'gss5',
            'gss6',
            'gss8',
            'gss10',
            'gss11',
            'gss13',
            'gss15'],
        [
            'bbs1',
            'bbs2',
            'bbs3',
            'bbs4',
            'bbs6',
            'bbs8'],
        [
            'gsk1',
            'gsk3',
            'gsk4',
            'gsk5',
            'gsk7',
            'gsh1',
            'gsh2',
            'gsh3']],
    TAMMY_TAILOR: [
        [
            'bss1',
            'bss2',
            'bss3',
            'bss4',
            'bss5',
            'bss6',
            'bss7',
            'bss8',
            'bss9',
            'bss11',
            'bss15'],
        [
            'gss1',
            'gss2',
            'gss3',
            'gss4',
            'gss5',
            'gss6',
            'gss8',
            'gss10',
            'gss11',
            'gss13',
            'gss15'],
        [
            'bbs1',
            'bbs2',
            'bbs3',
            'bbs4',
            'bbs6',
            'bbs8'],
        [
            'gsk1',
            'gsk3',
            'gsk4',
            'gsk5',
            'gsk7',
            'gsh1',
            'gsh2',
            'gsh3']],
    LONGJOHN_LEROY: [
        [
            'bss14'],
        [
            'gss14'],
        [
            'bbs5'],
        [
            'gsk2']],
    TAILOR_HARMONY: [
        [
            'bss10'],
        [
            'gss9'],
        [
            'bbs7'],
        [
            'gsk6']],
    BONNIE_BLOSSOM: [
        [
            'bss12'],
        [
            'gss12'],
        [
            'bbs6'],
        [
            'gsh3']],
    WARREN_BUNDLES: [
        [
            'bss13'],
        [
            'gss7'],
        [
            'bbs3'],
        [
            'gsh1']],
    WORNOUT_WAYLON: [
        [
            'bss13'],
        [
            'gss7'],
        [
            'bbs3'],
        [
            'gsh1']] }
BOY_SHIRTS = 0
GIRL_SHIRTS = 1
BOY_SHORTS = 2
GIRL_BOTTOMS = 3
MakeAToonBoyBottoms = []
MakeAToonBoyShirts = []
MakeAToonGirlBottoms = []
MakeAToonGirlShirts = []
MakeAToonGirlSkirts = []
MakeAToonGirlShorts = []
for style in TailorCollections[MAKE_A_TOON][BOY_SHORTS]:
    index = BottomStyles[style][0]
    MakeAToonBoyBottoms.append(index)

for style in TailorCollections[MAKE_A_TOON][BOY_SHIRTS]:
    index = ShirtStyles[style][0]
    MakeAToonBoyShirts.append(index)

for style in TailorCollections[MAKE_A_TOON][GIRL_BOTTOMS]:
    index = BottomStyles[style][0]
    MakeAToonGirlBottoms.append(index)

for style in TailorCollections[MAKE_A_TOON][GIRL_SHIRTS]:
    index = ShirtStyles[style][0]
    MakeAToonGirlShirts.append(index)

for index in MakeAToonGirlBottoms:
    flag = GirlBottoms[index][1]
    if flag == SKIRT:
        MakeAToonGirlSkirts.append(index)
    elif flag == SHORTS:
        MakeAToonGirlShorts.append(index)
    else:
        notify.error('Invalid flag')


def getRandomTop(gender, tailorId = MAKE_A_TOON, generator = None):
    if generator == None:
        generator = whrandom
    
    collection = TailorCollections[tailorId]
    if gender == 'm':
        style = generator.choice(collection[BOY_SHIRTS])
    else:
        style = generator.choice(collection[GIRL_SHIRTS])
    styleList = ShirtStyles[style]
    colors = generator.choice(styleList[2])
    return (styleList[0], colors[0], styleList[1], colors[1])


def getRandomBottom(gender, tailorId = MAKE_A_TOON, generator = None, girlBottomType = None):
    if generator == None:
        generator = whrandom
    
    collection = TailorCollections[tailorId]
    if gender == 'm':
        style = generator.choice(collection[BOY_SHORTS])
    elif girlBottomType is None:
        style = generator.choice(collection[GIRL_BOTTOMS])
    elif girlBottomType == SKIRT:
        skirtCollection = filter(lambda style: GirlBottoms[BottomStyles[style][0]][1] == SKIRT, collection[GIRL_BOTTOMS])
        style = generator.choice(skirtCollection)
    elif girlBottomType == SHORTS:
        shortsCollection = filter(lambda style: GirlBottoms[BottomStyles[style][0]][1] == SHORTS, collection[GIRL_BOTTOMS])
        style = generator.choice(shortsCollection)
    else:
        notify.error('Bad girlBottomType: %s' % girlBottomType)
    styleList = BottomStyles[style]
    color = generator.choice(styleList[1])
    return (styleList[0], color)


def getRandomGirlBottom(type):
    bottoms = []
    index = 0
    for bottom in GirlBottoms:
        if bottom[1] == type:
            bottoms.append(index)
        
        index += 1
    
    return random.choice(bottoms)


def getRandomGirlBottomAndColor(type):
    bottoms = []
    if type == SHORTS:
        typeStr = 'gsh'
    else:
        typeStr = 'gsk'
    for bottom in BottomStyles.keys():
        if bottom.find(typeStr) >= 0:
            bottoms.append(bottom)
        
    
    style = BottomStyles[random.choice(bottoms)]
    return (style[0], random.choice(style[1]))


def getRandomizedTops(gender, tailorId = MAKE_A_TOON, generator = None):
    if generator == None:
        generator = whrandom
    
    collection = TailorCollections[tailorId]
    if gender == 'm':
        collection = collection[BOY_SHIRTS][:]
    else:
        collection = collection[GIRL_SHIRTS][:]
    tops = []
    random.shuffle(collection)
    for style in collection:
        colors = ShirtStyles[style][2][:]
        random.shuffle(colors)
        for color in colors:
            tops.append((ShirtStyles[style][0], color[0], ShirtStyles[style][1], color[1]))
        
    
    return tops


def getRandomizedBottoms(gender, tailorId = MAKE_A_TOON, generator = None):
    if generator == None:
        generator = whrandom
    
    collection = TailorCollections[tailorId]
    if gender == 'm':
        collection = collection[BOY_SHORTS][:]
    else:
        collection = collection[GIRL_BOTTOMS][:]
    bottoms = []
    random.shuffle(collection)
    for style in collection:
        colors = BottomStyles[style][1][:]
        random.shuffle(colors)
        for color in colors:
            bottoms.append((BottomStyles[style][0], color))
        
    
    return bottoms


def getTops(gender, tailorId = MAKE_A_TOON):
    if gender == 'm':
        collection = TailorCollections[tailorId][BOY_SHIRTS]
    else:
        collection = TailorCollections[tailorId][GIRL_SHIRTS]
    tops = []
    for style in collection:
        for color in ShirtStyles[style][2]:
            tops.append((ShirtStyles[style][0], color[0], ShirtStyles[style][1], color[1]))
        
    
    return tops


def getAllTops(gender):
    tops = []
    for style in ShirtStyles.keys():
        if gender == 'm':
            if style[0] == 'g' or style[:3] == 'c_g':
                continue
            
        elif style[0] == 'b' or style[:3] == 'c_b':
            continue
        
        for color in ShirtStyles[style][2]:
            tops.append((ShirtStyles[style][0], color[0], ShirtStyles[style][1], color[1]))
        
    
    return tops


def getBottoms(gender, tailorId = MAKE_A_TOON):
    if gender == 'm':
        collection = TailorCollections[tailorId][BOY_SHORTS]
    else:
        collection = TailorCollections[tailorId][GIRL_BOTTOMS]
    bottoms = []
    for style in collection:
        for color in BottomStyles[style][1]:
            bottoms.append((BottomStyles[style][0], color))
        
    
    return bottoms


def getAllBottoms(gender, output = 'both'):
    bottoms = []
    for style in BottomStyles.keys():
        if gender == 'm':
            if style[0] == 'g' and style[:3] == 'c_g' and style[:4] == 'vd_g' and style[:4] == 'sd_g' or style[:4] == 'j4_g':
                continue
            
        elif style[0] == 'b' and style[:3] == 'c_b' and style[:4] == 'vd_b' and style[:4] == 'sd_b' or style[:4] == 'j4_b':
            continue
        
        bottomIdx = BottomStyles[style][0]
        if gender == 'f':
            textureType = GirlBottoms[bottomIdx][1]
        else:
            textureType = SHORTS
        if not output == 'both':
            if output == 'skirts' and textureType == SKIRT and output == 'shorts' and textureType == SHORTS:
                for color in BottomStyles[style][1]:
                    bottoms.append((bottomIdx, color))
                
            
    
    return bottoms

allColorsList = [
    VBase4(1.0, 1.0, 1.0, 1.0),
    VBase4(0.96875, 0.69140599999999997, 0.69921900000000003, 1.0),
    VBase4(0.93359400000000003, 0.265625, 0.28125, 1.0),
    VBase4(0.86328099999999997, 0.40625, 0.41796899999999998, 1.0),
    VBase4(0.71093799999999996, 0.234375, 0.4375, 1.0),
    VBase4(0.57031200000000004, 0.44921899999999998, 0.16406200000000001, 1.0),
    VBase4(0.640625, 0.35546899999999998, 0.26953100000000002, 1.0),
    VBase4(0.99609400000000003, 0.69531200000000004, 0.51171900000000003, 1.0),
    VBase4(0.83203099999999997, 0.5, 0.296875, 1.0),
    VBase4(0.99218799999999996, 0.48046899999999998, 0.16796900000000001, 1.0),
    VBase4(0.99609400000000003, 0.89843799999999996, 0.32031199999999999, 1.0),
    VBase4(0.99609400000000003, 0.95703099999999997, 0.59765599999999997, 1.0),
    VBase4(0.85546900000000003, 0.93359400000000003, 0.49218800000000001, 1.0),
    VBase4(0.55078099999999997, 0.82421900000000003, 0.32421899999999998, 1.0),
    VBase4(0.24218799999999999, 0.74218799999999996, 0.515625, 1.0),
    VBase4(0.30468800000000001, 0.96875, 0.40234399999999998, 1.0),
    VBase4(0.43359399999999998, 0.90625, 0.83593799999999996, 1.0),
    VBase4(0.34765600000000002, 0.82031200000000004, 0.953125, 1.0),
    VBase4(0.19140599999999999, 0.5625, 0.77343799999999996, 1.0),
    VBase4(0.55859400000000003, 0.58984400000000003, 0.875, 1.0),
    VBase4(0.28515600000000002, 0.328125, 0.72656200000000004, 1.0),
    VBase4(0.46093800000000001, 0.37890600000000002, 0.82421900000000003, 1.0),
    VBase4(0.546875, 0.28125, 0.75, 1.0),
    VBase4(0.72656200000000004, 0.47265600000000002, 0.859375, 1.0),
    VBase4(0.89843799999999996, 0.61718799999999996, 0.90625, 1.0),
    VBase4(0.69999999999999996, 0.69999999999999996, 0.80000000000000004, 1.0),
    VBase4(0.29999999999999999, 0.29999999999999999, 0.34999999999999998, 1.0)]
defaultBoyColorList = [
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22]
defaultGirlColorList = [
    1,
    2,
    3,
    4,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    21,
    22,
    23,
    24]

class ToonDNA(AvatarDNA.AvatarDNA):
    
    def __init__(self, str = None, type = None, dna = None, r = None, b = None, g = None):
        if str != None:
            self.makeFromNetString(str)
        elif type != None:
            if type == 't':
                if dna == None:
                    self.newToonRandom(r, g, b)
                else:
                    self.newToonFromProperties(*dna.asTuple())
            
        else:
            self.type = 'u'

    
    def __str__(self):
        string = 'type = toon\n'
        string = string + 'gender = %s\n' % self.gender
        string = string + 'head = %s, torso = %s, legs = %s\n' % (self.head, self.torso, self.legs)
        string = string + 'arm color = %d\n' % self.armColor
        string = string + 'glove color = %d\n' % self.gloveColor
        string = string + 'leg color = %d\n' % self.legColor
        string = string + 'head color = %d\n' % self.headColor
        string = string + 'top texture = %d\n' % self.topTex
        string = string + 'top texture color = %d\n' % self.topTexColor
        string = string + 'sleeve texture = %d\n' % self.sleeveTex
        string = string + 'sleeve texture color = %d\n' % self.sleeveTexColor
        string = string + 'bottom texture = %d\n' % self.botTex
        string = string + 'bottom texture color = %d\n' % self.botTexColor
        return string

    
    def makeNetString(self):
        dg = PyDatagram()
        dg.addFixedString(self.type, 1)
        if self.type == 't':
            headIndex = toonHeadTypes.index(self.head)
            torsoIndex = toonTorsoTypes.index(self.torso)
            legsIndex = toonLegTypes.index(self.legs)
            dg.addUint8(headIndex)
            dg.addUint8(torsoIndex)
            dg.addUint8(legsIndex)
            if self.gender == 'm':
                dg.addUint8(1)
            else:
                dg.addUint8(0)
            dg.addUint8(self.topTex)
            dg.addUint8(self.topTexColor)
            dg.addUint8(self.sleeveTex)
            dg.addUint8(self.sleeveTexColor)
            dg.addUint8(self.botTex)
            dg.addUint8(self.botTexColor)
            dg.addUint8(self.armColor)
            dg.addUint8(self.gloveColor)
            dg.addUint8(self.legColor)
            dg.addUint8(self.headColor)
        elif self.type == 'u':
            notify.error('undefined avatar')
        else:
            notify.error('unknown avatar type: ', self.type)
        return dg.getMessage()

    
    def makeFromNetString(self, string):
        dg = PyDatagram(string)
        dgi = PyDatagramIterator(dg)
        self.type = dgi.getFixedString(1)
        if self.type == 't':
            headIndex = dgi.getUint8()
            torsoIndex = dgi.getUint8()
            legsIndex = dgi.getUint8()
            self.head = toonHeadTypes[headIndex]
            self.torso = toonTorsoTypes[torsoIndex]
            self.legs = toonLegTypes[legsIndex]
            gender = dgi.getUint8()
            if gender == 1:
                self.gender = 'm'
            else:
                self.gender = 'f'
            self.topTex = dgi.getUint8()
            self.topTexColor = dgi.getUint8()
            self.sleeveTex = dgi.getUint8()
            self.sleeveTexColor = dgi.getUint8()
            self.botTex = dgi.getUint8()
            self.botTexColor = dgi.getUint8()
            self.armColor = dgi.getUint8()
            self.gloveColor = dgi.getUint8()
            self.legColor = dgi.getUint8()
            self.headColor = dgi.getUint8()
        else:
            notify.error('unknown avatar type: ', self.type)
        return None

    
    def defaultColor(self):
        return 25

    
    def _ToonDNA__defaultColors(self):
        color = self.defaultColor()
        self.armColor = color
        self.gloveColor = 0
        self.legColor = color
        self.headColor = color

    
    def newToon(self, dna, color = None):
        if len(dna) == 4:
            self.type = 't'
            self.head = dna[0]
            self.torso = dna[1]
            self.legs = dna[2]
            self.gender = dna[3]
            self.topTex = 0
            self.topTexColor = 0
            self.sleeveTex = 0
            self.sleeveTexColor = 0
            self.botTex = 0
            self.botTexColor = 0
            if color == None:
                color = self.defaultColor()
            
            self.armColor = color
            self.legColor = color
            self.headColor = color
            self.gloveColor = 0
        else:
            notify.error("tuple must be in format ('%s', '%s', '%s', '%s')")

    
    def newToonFromProperties(self, head, torso, legs, gender, armColor, gloveColor, legColor, headColor, topTexture, topTextureColor, sleeveTexture, sleeveTextureColor, bottomTexture, bottomTextureColor):
        self.type = 't'
        self.head = head
        self.torso = torso
        self.legs = legs
        self.gender = gender
        self.armColor = armColor
        self.gloveColor = gloveColor
        self.legColor = legColor
        self.headColor = headColor
        self.topTex = topTexture
        self.topTexColor = topTextureColor
        self.sleeveTex = sleeveTexture
        self.sleeveTexColor = sleeveTextureColor
        self.botTex = bottomTexture
        self.botTexColor = bottomTextureColor
        return None

    
    def updateToonProperties(self, head = None, torso = None, legs = None, gender = None, armColor = None, gloveColor = None, legColor = None, headColor = None, topTexture = None, topTextureColor = None, sleeveTexture = None, sleeveTextureColor = None, bottomTexture = None, bottomTextureColor = None, shirt = None, bottom = None):
        if head:
            self.head = head
        
        if torso:
            self.torso = torso
        
        if legs:
            self.legs = legs
        
        if gender:
            self.gender = gender
        
        if armColor:
            self.armColor = armColor
        
        if gloveColor:
            self.gloveColor = gloveColor
        
        if legColor:
            self.legColor = legColor
        
        if headColor:
            self.headColor = headColor
        
        if topTexture:
            self.topTex = topTexture
        
        if topTextureColor:
            self.topTexColor = topTextureColor
        
        if sleeveTexture:
            self.sleeveTex = sleeveTexture
        
        if sleeveTextureColor:
            self.sleeveTexColor = sleeveTextureColor
        
        if bottomTexture:
            self.botTex = bottomTexture
        
        if bottomTextureColor:
            self.botTexColor = bottomTextureColor
        
        if shirt:
            (str, colorIndex) = shirt
            defn = ShirtStyles[str]
            self.topTex = defn[0]
            self.topTexColor = defn[2][colorIndex][0]
            self.sleeveTex = defn[1]
            self.sleeveTexColor = defn[2][colorIndex][1]
        
        if bottom:
            (str, colorIndex) = bottom
            defn = BottomStyles[str]
            self.botTex = defn[0]
            self.botTexColor = defn[1][colorIndex]
        
        return None

    
    def newToonRandom(self, seed = None, gender = 'm', npc = 0):
        if seed:
            (seedx, seedy) = divmod(seed, 100)
            seedz = seed & 255
            generator = whrandom.whrandom()
            generator.seed(seedx, seedy, seedz)
        else:
            generator = whrandom
        self.type = 't'
        self.legs = generator.choice(toonLegTypes + [
            'm',
            'l',
            'l',
            'l'])
        self.gender = gender
        if not npc:
            self.head = generator.choice(toonHeadTypes)
        else:
            self.head = generator.choice(toonHeadTypes[:22])
        (top, topColor, sleeve, sleeveColor) = getRandomTop(gender, generator = generator)
        (bottom, bottomColor) = getRandomBottom(gender, generator = generator)
        if gender == 'm':
            self.torso = generator.choice(toonTorsoTypes[:3])
            self.topTex = top
            self.topTexColor = topColor
            self.sleeveTex = sleeve
            self.sleeveTexColor = sleeveColor
            self.botTex = bottom
            self.botTexColor = bottomColor
            color = generator.choice(defaultBoyColorList)
            self.armColor = color
            self.legColor = color
            self.headColor = color
        else:
            self.torso = generator.choice(toonTorsoTypes[:6])
            self.topTex = top
            self.topTexColor = topColor
            self.sleeveTex = sleeve
            self.sleeveTexColor = sleeveColor
            if self.torso[1] == 'd':
                (tex, color) = getRandomGirlBottomAndColor(SKIRT)
                self.botTex = tex
                self.botTexColor = color
            else:
                (tex, color) = getRandomGirlBottomAndColor(SKIRT)
                self.botTex = tex
                self.botTexColor = color
            color = generator.choice(defaultGirlColorList)
            self.armColor = color
            self.legColor = color
            self.headColor = color
        self.gloveColor = 0

    
    def asTuple(self):
        return (self.head, self.torso, self.legs, self.gender, self.armColor, self.gloveColor, self.legColor, self.headColor, self.topTex, self.topTexColor, self.sleeveTex, self.sleeveTexColor, self.botTex, self.botTexColor)

    
    def getType(self):
        if self.type == 't':
            type = self.getAnimal()
        else:
            notify.error('Invalid DNA type: ', self.type)
        return type

    
    def getAnimal(self):
        if self.head[0] == 'd':
            return 'dog'
        elif self.head[0] == 'c':
            return 'cat'
        elif self.head[0] == 'm':
            return 'mouse'
        elif self.head[0] == 'h':
            return 'horse'
        elif self.head[0] == 'r':
            return 'rabbit'
        elif self.head[0] == 'f':
            return 'duck'
        elif self.head[0] == 'p':
            return 'monkey'
        else:
            notify.error('unknown headStyle: ', self.head[0])

    
    def getHeadSize(self):
        if self.head[1] == 'l':
            return 'long'
        elif self.head[1] == 's':
            return 'short'
        else:
            notify.error('unknown head size: ', self.head[1])

    
    def getMuzzleSize(self):
        if self.head[2] == 'l':
            return 'long'
        elif self.head[2] == 's':
            return 'short'
        else:
            notify.error('unknown muzzle size: ', self.head[2])

    
    def getTorsoSize(self):
        if self.torso[0] == 'l':
            return 'long'
        elif self.torso[0] == 'm':
            return 'medium'
        elif self.torso[0] == 's':
            return 'short'
        else:
            notify.error('unknown torso size: ', self.torso[0])

    
    def getLegSize(self):
        if self.legs == 'l':
            return 'long'
        elif self.legs == 'm':
            return 'medium'
        elif self.legs == 's':
            return 'short'
        else:
            notify.error('unknown leg size: ', self.legs)

    
    def getGender(self):
        return self.gender

    
    def getClothes(self):
        if len(self.torso) == 1:
            return 'naked'
        elif self.torso[1] == 's':
            return 'shorts'
        elif self.torso[1] == 'd':
            return 'dress'
        else:
            notify.error('unknown clothing type: ', self.torso[1])

    
    def getArmColor(self):
        
        try:
            return allColorsList[self.armColor]
        except:
            return allColorsList[0]


    
    def getLegColor(self):
        
        try:
            return allColorsList[self.legColor]
        except:
            return allColorsList[0]


    
    def getHeadColor(self):
        
        try:
            return allColorsList[self.headColor]
        except:
            return allColorsList[0]


    
    def getGloveColor(self):
        
        try:
            return allColorsList[self.gloveColor]
        except:
            return allColorsList[0]


    
    def getBlackColor(self):
        
        try:
            return allColorsList[26]
        except:
            return allColorsList[0]



