# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\catalog\CatalogSurfaceColors.py
CT_WHITE = (1.0, 1.0, 1.0, 1.0)
CT_RED = (1.0, 0.5, 0.5, 1.0)
CT_BROWN = (0.641, 0.355, 0.27, 1.0)
CT_CANTELOPE = (0.839, 0.651, 0.549, 1.0)
CT_TAN = (0.996, 0.695, 0.512, 1.0)
CT_ORANGE = (0.992, 0.48, 0.168, 1.0)
CT_CORAL = (0.832, 0.5, 0.297, 1.0)
CT_PEACH = (1.0, 0.82, 0.7, 1.0)
CT_BEIGE = (1.0, 0.8, 0.6, 1.0)
CT_TAN2 = (0.808, 0.678, 0.51, 1.0)
CT_SIENNA = (0.57, 0.449, 0.164, 1.0)
CT_YELLOW = (0.996, 0.898, 0.32, 1.0)
CT_CREAM = (0.996, 0.957, 0.598, 1.0)
CT_BEIGE2 = (1.0, 1.0, 0.6, 1.0)
CT_YELLOW2 = (1.0, 1.0, 0.7, 1.0)
CT_CITRINE = (0.855, 0.934, 0.492, 1.0)
CT_FOREST_GREEN = (0.5, 0.586, 0.4, 1.0)
CT_LINE = (0.551, 0.824, 0.324, 1.0)
CT_PALE_GREEN = (0.789, 1.0, 0.7, 1.0)
CT_GREEN = (0.305, 0.969, 0.402, 1.0)
CT_TEAL = (0.6, 1.0, 0.8, 1.0)
CT_SEA_GREEN = (0.242, 0.742, 0.516, 1.0)
CT_LIGHT_BLUE = (0.434, 0.906, 0.836, 1.0)
CT_AQUA = (0.348, 0.82, 0.953, 1.0)
CT_BLUE = (0.191, 0.563, 0.773, 1.0)
CT_LIGHT_BLUE2 = (0.875, 0.937, 1.0, 1.0)
CT_PERIWINKLE = (0.559, 0.59, 0.875, 1.0)
CT_ROYAL_BLUE = (0.285, 0.328, 0.727, 1.0)
CT_GREY = (0.7, 0.7, 0.8, 1.0)
CT_BLUE2 = (0.6, 0.6, 1.0, 1.0)
CT_SLATE_BLUE = (0.461, 0.379, 0.824, 1.0)
CT_PURPLE = (0.547, 0.281, 0.75, 1.0)
CT_LAVENDER = (0.727, 0.473, 0.859, 1.0)
CT_PINK = (0.898, 0.617, 0.906, 1.0)
CT_PINK2 = (1.0, 0.6, 1.0, 1.0)
CT_MAROON = (0.711, 0.234, 0.438, 1.0)
CT_PEACH2 = (0.969, 0.691, 0.699, 1.0)
CT_RED2 = (0.863, 0.406, 0.418, 1.0)
CT_BRIGHT_RED = (0.934, 0.266, 0.281, 1.0)
CT_DARK_WOOD = (0.69, 0.741, 0.71, 1.0)
CT_DARK_WALNUT = (0.549, 0.412, 0.259, 1.0)
CT_GENERIC_DARK = (0.443, 0.333, 0.176, 1.0)
CT_PINE = (1.0, 0.812, 0.49, 1.0)
CT_CHERRY = (0.71, 0.408, 0.267, 1.0)
CT_BEECH = (0.961, 0.659, 0.4, 1.0)
CTFlatColor = [
 CT_BEIGE, CT_TEAL, CT_BLUE2, CT_PINK2, CT_BEIGE2, CT_RED]
CTValentinesColors = [
 CT_PINK2, CT_RED]
CTUnderwaterColors = [
 CT_WHITE, CT_TEAL, CT_SEA_GREEN, CT_LIGHT_BLUE, CT_PALE_GREEN, CT_AQUA, CT_CORAL, CT_PEACH]
CTFlatColorDark = []
tint = 0.75
for color in CTFlatColor:
    CTFlatColorDark.append((color[0] * tint, color[1] * tint, color[2] * tint, 1.0))

CTFlatColorAll = CTFlatColor + CTFlatColorDark
CTBasicWoodColorOnWhite = [
 CT_DARK_WALNUT, CT_GENERIC_DARK, CT_PINE, CT_CHERRY, CT_BEECH]
CTWhite = [
 CT_WHITE]