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
import CatalogInvalidItem
CatalogItemTypes = {
    CatalogInvalidItem.CatalogInvalidItem: 0,
    CatalogFurnitureItem.CatalogFurnitureItem: 1,
    CatalogChatItem.CatalogChatItem: 2,
    CatalogClothingItem.CatalogClothingItem: 3,
    CatalogEmoteItem.CatalogEmoteItem: 4,
    CatalogWallpaperItem.CatalogWallpaperItem: 5,
    CatalogWindowItem.CatalogWindowItem: 6,
    CatalogFlooringItem.CatalogFlooringItem: 7,
    CatalogMouldingItem.CatalogMouldingItem: 8,
    CatalogWainscotingItem.CatalogWainscotingItem: 9,
    CatalogPoleItem.CatalogPoleItem: 10 }
FURNITURE_ITEM = CatalogItemTypes[CatalogFurnitureItem.CatalogFurnitureItem]
CHAT_ITEM = CatalogItemTypes[CatalogChatItem.CatalogChatItem]
CLOTHING_ITEM = CatalogItemTypes[CatalogClothingItem.CatalogClothingItem]
EMOTE_ITEM = CatalogItemTypes[CatalogEmoteItem.CatalogEmoteItem]
WALLPAPER_ITEM = CatalogItemTypes[CatalogWallpaperItem.CatalogWallpaperItem]
WINDOW_ITEM = CatalogItemTypes[CatalogWindowItem.CatalogWindowItem]
FLOORING_ITEM = CatalogItemTypes[CatalogFlooringItem.CatalogFlooringItem]
MOULDING_ITEM = CatalogItemTypes[CatalogMouldingItem.CatalogMouldingItem]
WAINSCOTING_ITEM = CatalogItemTypes[CatalogWainscotingItem.CatalogWainscotingItem]
POLE_ITEM = CatalogItemTypes[CatalogPoleItem.CatalogPoleItem]
