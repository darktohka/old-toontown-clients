# File: C (Python 2.2)

import CatalogFurnitureItem
import CatalogChatItem
import CatalogClothingItem
import CatalogEmoteItem
import CatalogWallpaperItem
import CatalogWindowItem
CatalogItemTypes = {
    CatalogFurnitureItem.CatalogFurnitureItem: 1,
    CatalogChatItem.CatalogChatItem: 2,
    CatalogClothingItem.CatalogClothingItem: 3,
    CatalogEmoteItem.CatalogEmoteItem: 4,
    CatalogWallpaperItem.CatalogWallpaperItem: 5,
    CatalogWindowItem.CatalogWindowItem: 6 }
FURNITURE_ITEM = CatalogItemTypes[CatalogFurnitureItem.CatalogFurnitureItem]
CHAT_ITEM = CatalogItemTypes[CatalogChatItem.CatalogChatItem]
CLOTHING_ITEM = CatalogItemTypes[CatalogClothingItem.CatalogClothingItem]
EMOTE_ITEM = CatalogItemTypes[CatalogEmoteItem.CatalogEmoteItem]
WALLPAPER_ITEM = CatalogItemTypes[CatalogWallpaperItem.CatalogWallpaperItem]
WINDOW_ITEM = CatalogItemTypes[CatalogWindowItem.CatalogWindowItem]
