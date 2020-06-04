# File: R (Python 2.2)

import Localizer
ValidChoices = [
    0,
    1,
    2,
    3,
    4]
NumberToWin = 14
InputTimeout = 20
ChanceRewards = (((1, 0), Localizer.RaceGameForwardOneSpace, 0), ((1, 0), Localizer.RaceGameForwardOneSpace, 0), ((1, 0), Localizer.RaceGameForwardOneSpace, 0), ((2, 0), Localizer.RaceGameForwardTwoSpaces, 0), ((2, 0), Localizer.RaceGameForwardTwoSpaces, 0), ((2, 0), Localizer.RaceGameForwardTwoSpaces, 0), ((3, 0), Localizer.RaceGameForwardThreeSpaces, 0), ((3, 0), Localizer.RaceGameForwardThreeSpaces, 0), ((3, 0), Localizer.RaceGameForwardThreeSpaces, 0), ((0, -3), Localizer.RaceGameOthersBackThree, 0), ((0, -3), Localizer.RaceGameOthersBackThree, 0), ((-1, 0), Localizer.RaceGameBackOneSpace, 0), ((-1, 0), Localizer.RaceGameBackOneSpace, 0), ((-2, 0), Localizer.RaceGameBackTwoSpaces, 0), ((-2, 0), Localizer.RaceGameBackTwoSpaces, 0), ((-3, 0), Localizer.RaceGameBackThreeSpaces, 0), ((-3, 0), Localizer.RaceGameBackThreeSpaces, 0), ((0, 3), Localizer.RaceGameOthersForwardThree, 0), ((0, 3), Localizer.RaceGameOthersForwardThree, 0), ((0, 0), Localizer.RaceGameJellybeans2, 2), ((0, 0), Localizer.RaceGameJellybeans2, 2), ((0, 0), Localizer.RaceGameJellybeans2, 2), ((0, 0), Localizer.RaceGameJellybeans2, 2), ((0, 0), Localizer.RaceGameJellybeans4, 4), ((0, 0), Localizer.RaceGameJellybeans4, 4), ((0, 0), Localizer.RaceGameJellybeans4, 4), ((0, 0), Localizer.RaceGameJellybeans4, 4), ((0, 0), Localizer.RaceGameJellybeans10, 10), ((0, 0), -1, 0), ((NumberToWin, 0), Localizer.RaceGameInstantWinner, 0))
