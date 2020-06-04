# File: T (Python 2.2)

from toontown.toonbase.ToontownGlobals import *
wainscottingBase = [
    Vec4(0.80000000000000004, 0.5, 0.29999999999999999, 1.0),
    Vec4(0.69899999999999995, 0.58599999999999997, 0.47299999999999998, 1.0),
    Vec4(0.47299999999999998, 0.69899999999999995, 0.48799999999999999, 1.0)]
wallpaperBase = [
    Vec4(1.0, 1.0, 0.69999999999999996, 1.0),
    Vec4(0.80000000000000004, 1.0, 0.69999999999999996, 1.0),
    Vec4(0.40000000000000002, 0.5, 0.40000000000000002, 1.0),
    Vec4(0.5, 0.69999999999999996, 0.59999999999999998, 1.0)]
wallpaperBorderBase = [
    Vec4(1.0, 1.0, 0.69999999999999996, 1.0),
    Vec4(0.80000000000000004, 1.0, 0.69999999999999996, 1.0),
    Vec4(0.40000000000000002, 0.5, 0.40000000000000002, 1.0),
    Vec4(0.5, 0.69999999999999996, 0.59999999999999998, 1.0)]
doorBase = [
    Vec4(1.0, 1.0, 0.69999999999999996, 1.0)]
floorBase = [
    Vec4(0.746, 1.0, 0.47699999999999998, 1.0),
    Vec4(1.0, 0.68400000000000005, 0.47699999999999998, 1.0)]
baseScheme = {
    'TI_wainscotting': wainscottingBase,
    'TI_wallpaper': wallpaperBase,
    'TI_wallpaper_border': wallpaperBorderBase,
    'TI_door': doorBase,
    'TI_floor': floorBase }
colors = {
    DonaldsDock: {
        'TI_wainscotting': wainscottingBase,
        'TI_wallpaper': wallpaperBase,
        'TI_wallpaper_border': wallpaperBorderBase,
        'TI_door': doorBase,
        'TI_floor': floorBase },
    ToontownCentral: {
        'TI_wainscotting': wainscottingBase,
        'TI_wallpaper': wallpaperBase,
        'TI_wallpaper_border': wallpaperBorderBase,
        'TI_door': doorBase + [
            Vec4(0.80000000000000004, 0.5, 0.29999999999999999, 1.0)],
        'TI_floor': floorBase },
    TheBrrrgh: baseScheme,
    MinniesMelodyland: baseScheme,
    DaisyGardens: baseScheme,
    DonaldsDreamland: {
        'TI_wainscotting': wainscottingBase,
        'TI_wallpaper': wallpaperBase,
        'TI_wallpaper_border': wallpaperBorderBase,
        'TI_door': doorBase,
        'TI_floor': floorBase },
    Tutorial: {
        'TI_wainscotting': wainscottingBase,
        'TI_wallpaper': wallpaperBase,
        'TI_wallpaper_border': wallpaperBorderBase,
        'TI_door': doorBase + [
            Vec4(0.80000000000000004, 0.5, 0.29999999999999999, 1.0)],
        'TI_floor': floorBase },
    MyEstate: baseScheme }
