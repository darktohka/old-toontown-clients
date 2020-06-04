# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coderedemption\TTCodeRedemptionConsts.py
DefaultDbName = 'tt_code_redemption'
RedeemErrors = Enum('Success, CodeDoesntExist, CodeIsInactive, CodeAlreadyRedeemed, AwardCouldntBeGiven, TooManyAttempts, SystemUnavailable, ')
RedeemErrorStrings = {RedeemErrors.Success: 'Success', RedeemErrors.CodeDoesntExist: 'Invalid code', RedeemErrors.CodeIsInactive: 'Code is inactive', RedeemErrors.CodeAlreadyRedeemed: 'Code has already been redeemed', RedeemErrors.AwardCouldntBeGiven: 'Award could not be given', RedeemErrors.TooManyAttempts: 'Too many attempts, code ignored', RedeemErrors.SystemUnavailable: 'Code redemption is currently unavailable'}
MaxCustomCodeLen = config.GetInt('tt-max-custom-code-len', 16)