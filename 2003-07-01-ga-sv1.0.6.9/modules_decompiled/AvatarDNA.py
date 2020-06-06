# File: A (Python 2.2)

import whrandom
from PandaModules import *
from DirectNotifyGlobal import *
import Localizer
import random
notify = directNotify.newCategory('AvatarDNA')
classTypes = [
    't',
    's',
    'c']
toonType = classTypes[0]
suitType = classTypes[1]
charType = classTypes[2]
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
    'fll']
toonHeadAnimalIndices = [
    0,
    4,
    8,
    12,
    14,
    18]
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
    'phase_3/maps/desat_shirt_23.jpg']
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
    (22, 0),
    (23, 0)]

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
    'phase_3/maps/desat_sleeve_20.jpg']
BoyShorts = [
    'phase_3/maps/desat_shorts_1.jpg',
    'phase_3/maps/desat_shorts_2.jpg',
    'phase_3/maps/desat_shorts_4.jpg',
    'phase_3/maps/desat_shorts_6.jpg',
    'phase_3/maps/desat_shorts_7.jpg',
    'phase_3/maps/desat_shorts_8.jpg',
    'phase_3/maps/desat_shorts_9.jpg',
    'phase_3/maps/desat_shorts_10.jpg']
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
    ('phase_3/maps/desat_shorts_10.jpg', SHORTS)]

def getRandomGirlBottom(type):
    bottoms = []
    index = 0
    for bottom in GirlBottoms:
        if bottom[1] == type:
            bottoms.append(index)
        
        index += 1
    
    return random.choice(bottoms)

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
            (26, 26)]] }
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
            27]] }
MAKE_A_TOON = 1
CATALOG = 2
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
    CATALOG: [
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


def getRandomBottom(gender, tailorId = MAKE_A_TOON, generator = None):
    if generator == None:
        generator = whrandom
    
    collection = TailorCollections[tailorId]
    if gender == 'm':
        style = generator.choice(collection[BOY_SHORTS])
    else:
        style = generator.choice(collection[GIRL_BOTTOMS])
    styleList = BottomStyles[style]
    color = generator.choice(styleList[1])
    return (styleList[0], color)


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

charTypes = [
    'mk',
    'mn',
    'g',
    'd',
    'dw',
    'p']
suitHeadTypes = [
    'f',
    'p',
    'ym',
    'mm',
    'ds',
    'hh',
    'cr',
    'tbc',
    'bf',
    'b',
    'dt',
    'ac',
    'bs',
    'sd',
    'le',
    'bw',
    'sc',
    'pp',
    'tw',
    'bc',
    'nc',
    'mb',
    'ls',
    'rb',
    'cc',
    'tm',
    'nd',
    'gh',
    'ms',
    'tf',
    'm',
    'mh']
suitATypes = [
    'ym',
    'hh',
    'tbc',
    'dt',
    'bs',
    'le',
    'bw',
    'pp',
    'nc',
    'rb',
    'nd',
    'tf',
    'm',
    'mh']
suitBTypes = [
    'p',
    'ds',
    'b',
    'ac',
    'sd',
    'bc',
    'ls',
    'tm',
    'ms']
suitCTypes = [
    'f',
    'mm',
    'cr',
    'bf',
    'sc',
    'tw',
    'mb',
    'cc',
    'gh']
suitDepts = [
    'c',
    'l',
    'm',
    's']
suitDeptFullnames = {
    'c': Localizer.Bossbot,
    'l': Localizer.Lawbot,
    'm': Localizer.Cashbot,
    's': Localizer.Sellbot }
corpPolyColor = VBase4(0.94999999999999996, 0.75, 0.75, 1.0)
legalPolyColor = VBase4(0.75, 0.75, 0.94999999999999996, 1.0)
moneyPolyColor = VBase4(0.65000000000000002, 0.94999999999999996, 0.84999999999999998, 1.0)
salesPolyColor = VBase4(0.94999999999999996, 0.75, 0.94999999999999996, 1.0)
suitsPerLevel = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1]
suitsPerDept = 8

def getSuitBodyType(name):
    if name in suitATypes:
        return 'a'
    elif name in suitBTypes:
        return 'b'
    elif name in suitCTypes:
        return 'c'
    else:
        print 'Unknown body type for suit name: ', name


def getSuitDept(name):
    index = suitHeadTypes.index(name)
    if index < suitsPerDept:
        return suitDepts[0]
    elif index < suitsPerDept * 2:
        return suitDepts[1]
    elif index < suitsPerDept * 3:
        return suitDepts[2]
    elif index < suitsPerDept * 4:
        return suitDepts[3]
    else:
        print 'Unknown dept for suit name: ', name


def getDeptFullname(dept):
    return suitDeptFullnames[dept]


def getSuitDeptFullname(name):
    return suitDeptFullnames[getSuitDept(name)]


def getSuitType(name):
    index = suitHeadTypes.index(name)
    return index % suitsPerDept + 1

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
    VBase4(0.69999999999999996, 0.69999999999999996, 0.80000000000000004, 1.0)]
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

class AvatarDNA:
    
    def __init__(self, str = None, type = None, dna = None, r = None, b = None, g = None):
        if str != None:
            self.makeFromNetString(str)
        elif type != None:
            if type == 't':
                if dna == None:
                    self.newToonRandom(r, g, b)
                else:
                    self.newToon(dna, r, g, b)
            elif type == 's':
                self.newSuit()
            elif type == 'c':
                self.newChar(dna)
            
        else:
            self.type = 'u'

    
    def __str__(self):
        if self.type == 't':
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
        elif self.type == 's':
            return 'type = %s\nbody = %s, dept = %s, name = %s' % ('suit', self.body, self.dept, self.name)
        elif self.type == 'c':
            return 'type = char, name = %s' % self.name
        else:
            return 'type undefined'

    
    def makeNetString(self):
        dg = Datagram()
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
        elif self.type == 's':
            dg.addFixedString(self.name, 3)
            dg.addFixedString(self.dept, 1)
        elif self.type == 'c':
            dg.addFixedString(self.name, 2)
        elif self.type == 'u':
            notify.error('undefined avatar')
        else:
            notify.error('unknown avatar type: ', self.type)
        return dg.getMessage()

    
    def printNetString(self):
        string = self.makeNetString()
        dg = Datagram(string)
        dg.dumpHex(ostream)

    
    def makeFromNetString(self, string):
        dg = Datagram(string)
        dgi = DatagramIterator(dg)
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
        elif self.type == 's':
            self.name = dgi.getFixedString(3)
            self.dept = dgi.getFixedString(1)
            self.body = getSuitBodyType(self.name)
        elif self.type == 'c':
            self.name = sgi.getFixedString(2)
        else:
            notify.error('unknown avatar type: ', self.type)
        return None

    
    def defaultColor(self):
        return 25

    
    def _AvatarDNA__defaultColors(self):
        color = self.defaultColor()
        self.armColor = color
        self.gloveColor = 0
        self.legColor = color
        self.headColor = color

    
    def _AvatarDNA__defaultChar(self):
        self.type = 'c'
        self.name = charTypes[0]

    
    def _AvatarDNA__defaultSuit(self):
        self.type = 's'
        self.name = 'ds'
        self.dept = getSuitDept(self.name)
        self.body = getSuitBodyType(self.name)

    
    def newChar(self, name = None):
        if name == None:
            self._AvatarDNA__defaultChar()
        else:
            self.type = 'c'
            if name in charTypes:
                self.name = name
            else:
                notify.error('unknown avatar type: ', name)

    
    def newSuit(self, name = None):
        if name == None:
            self._AvatarDNA__defaultSuit()
        else:
            self.type = 's'
            self.name = name
            self.dept = getSuitDept(self.name)
            self.body = getSuitBodyType(self.name)

    
    def newSuitRandom(self, level = None, dept = None):
        self.type = 's'
        if level == None:
            level = whrandom.choice(range(1, len(suitsPerLevel)))
        elif level < 0 or level > len(suitsPerLevel):
            notify.error('Invalid suit level: %d' % level)
        
        if dept == None:
            dept = whrandom.choice(suitDepts)
        
        self.dept = dept
        index = suitDepts.index(dept)
        base = index * suitsPerDept
        offset = 0
        if level > 1:
            for i in range(1, level):
                offset = offset + suitsPerLevel[i - 1]
            
        
        bottom = base + offset
        top = bottom + suitsPerLevel[level - 1]
        self.name = suitHeadTypes[whrandom.choice(range(bottom, top))]
        self.body = getSuitBodyType(self.name)

    
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

    
    def newToonRandom(self, seed = None, gender = 'm'):
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
        self.head = generator.choice(toonHeadTypes)
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
                self.botTex = getRandomGirlBottom(SKIRT)
            else:
                self.botTex = getRandomGirlBottom(SHORTS)
            self.botTexColor = bottomColor
            color = generator.choice(defaultGirlColorList)
            self.armColor = color
            self.legColor = color
            self.headColor = color
        self.gloveColor = self.defaultColor()

    
    def asTuple(self):
        return (self.head, self.torso, self.legs, self.gender, self.armColor, self.gloveColor, self.legColor, self.headColor, self.topTex, self.topTexColor, self.sleeveTex, self.sleeveTexColor, self.botTex, self.botTexColor)

    
    def getType(self):
        if self.type == 't':
            type = self.getAnimal()
        elif self.type == 's':
            type = 'suit'
        elif self.type == 'c':
            type = self.getCharName()
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
            return 'fowl'
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
        return allColorsList[self.armColor]

    
    def getLegColor(self):
        return allColorsList[self.legColor]

    
    def getHeadColor(self):
        return allColorsList[self.headColor]

    
    def getGloveColor(self):
        return allColorsList[self.gloveColor]

    
    def getCharName(self):
        if self.name == 'mk':
            return 'mickey'
        elif self.name == 'mn':
            return 'minnie'
        elif self.name == 'g':
            return 'goofy'
        elif self.name == 'd':
            return 'donald'
        elif self.name == 'dw':
            return 'donald-wheel'
        elif self.name == 'p':
            return 'pluto'
        else:
            notify.error('unknown char type: ', self.name)


