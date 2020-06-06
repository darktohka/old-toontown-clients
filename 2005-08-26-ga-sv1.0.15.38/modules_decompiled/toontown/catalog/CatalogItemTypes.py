# File: C (Python 2.2)

import CatalogFurnitureItem
import CatalogChatItem
import CatalogClothingItem
import CatalogEmoteItem
import CatalogWallpaperItem
import CatalogFlooringItem
import CatalogWainscotingItem
import CatalogMouldingItem
import CatalogWindowItem
import CatalogPoleItem
import CatalogPetTrickItem
import CatalogInvalidItem
INVALID_ITEM = 0
FURNITURE_ITEM = 1
CHAT_ITEM = 2
CLOTHING_ITEM = 3
EMOTE_ITEM = 4
WALLPAPER_ITEM = 5
WINDOW_ITEM = 6
FLOORING_ITEM = 7
MOULDING_ITEM = 8
WAINSCOTING_ITEM = 9
POLE_ITEM = 10
PET_TRICK_ITEM = 11
CatalogItemTypes = {
    CatalogInvalidItem.CatalogInvalidItem: INVALID_ITEM,
    CatalogFurnitureItem.CatalogFurnitureItem: FURNITURE_ITEM,
    CatalogChatItem.CatalogChatItem: CHAT_ITEM,
    CatalogClothingItem.CatalogClothingItem: CLOTHING_ITEM,
    CatalogEmoteItem.CatalogEmoteItem: EMOTE_ITEM,
    CatalogWallpaperItem.CatalogWallpaperItem: WALLPAPER_ITEM,
    CatalogWindowItem.CatalogWindowItem: WINDOW_ITEM,
    CatalogFlooringItem.CatalogFlooringItem: FLOORING_ITEM,
    CatalogMouldingItem.CatalogMouldingItem: MOULDING_ITEM,
    CatalogWainscotingItem.CatalogWainscotingItem: WAINSCOTING_ITEM,
    CatalogPoleItem.CatalogPoleItem: POLE_ITEM,
    CatalogPetTrickItem.CatalogPetTrickItem: PET_TRICK_ITEM }
CatalogItemTypeMask = 31
CatalogItemSaleFlag = 128
