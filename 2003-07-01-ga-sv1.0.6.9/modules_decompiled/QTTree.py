# File: Q (Python 2.2)

import QTNode
import QTQuestNode
import QTEmoteNode
import QTCustomNode
import Localizer
import ToonBase

def getLocalizedQTTree(localizer):
    tree = []
    if toonbase.emotionsMenuEnabled:
        tree += [
            [
                localizer.QTMenuEmotions,
                QTNode.QT_EMOTE_ROOT_NODE,
                localizer.EmoteList]]
    
    if toonbase.customMenuEnabled:
        tree += [
            [
                localizer.QTMenuCustom,
                QTNode.QT_CUSTOM_ROOT_NODE]]
    
    tree += [
        [
            localizer.QTMenuHello,
            localizer.QTHelloEntries],
        [
            localizer.QTMenuBye,
            localizer.QTByeEntries],
        [
            localizer.QTMenuHappy,
            localizer.QTHappyEntries],
        [
            localizer.QTMenuSad,
            localizer.QTSadEntries],
        [
            localizer.QTMenuFriendly,
            [
                [
                    localizer.QTFriendlyYou,
                    QTNode.QT_TEXT_MENU_NODE,
                    localizer.QTFriendlyYouEntries],
                [
                    localizer.QTFriendlyILike,
                    QTNode.QT_TEXT_MENU_NODE,
                    localizer.QTFriendlyILikeEntries]] + localizer.QTFriendlyEntries],
        [
            localizer.QTMenuSorry,
            localizer.QTSorryEntries],
        [
            localizer.QTMenuStinky,
            localizer.QTStinkyEntries],
        [
            localizer.QTMenuPlaces,
            [
                [
                    localizer.QTPlacesLetsGo,
                    QTNode.QT_TEXT_MENU_NODE,
                    localizer.QTPlacesLetsGoEntries]] + localizer.QTPlacesEntries],
        [
            localizer.QTMenuToontasks,
            [
                [
                    localizer.QTToontasksMyTasks,
                    QTNode.QT_QUEST_ROOT_NODE],
                [
                    localizer.QTToontasksYouShouldChoose,
                    QTNode.QT_TEXT_MENU_NODE,
                    localizer.QTYouShouldChooseEntries]] + localizer.QTToontasksEntries],
        [
            localizer.QTMenuBattle,
            [
                [
                    localizer.QTBattleLetsUse,
                    QTNode.QT_TEXT_MENU_NODE,
                    localizer.QTBattleLetsUseEntries]] + localizer.QTBattleEntries],
        [
            localizer.QTMenuGagShop,
            localizer.QTGagShopEntries]]
    tree += Localizer.QTTopEntries
    return tree

QTTree = getLocalizedQTTree(Localizer)
