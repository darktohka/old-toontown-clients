# File: O (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.distributed.MsgTypes import *
from direct.distributed.ClockDelta import *
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import ivalMgr
import sys
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import ClientRepository
import PotentialAvatar
import PotentialShard
from direct.fsm import ClassicFSM
from direct.fsm import State
from otp.login import TTAccount
from otp.login import AccountServerConstants
from otp.login import CreateAccountScreen
from otp.login import LoginScreen
from otp.avatar import Avatar
from direct.task import Task
from otp.otpgui import OTPDialog
import types
from otp.avatar import DistributedAvatar
from direct.distributed import DistributedSmoothNode
import time
from otp.otpbase import OTPLocalizer
from otp.login import LoginGSAccount
from otp.login import LoginGoAccount
from otp.login import LoginWebPlayTokenAccount
from otp.login import LoginTTAccount
from otp.login import HTTPUtil
from direct.showbase import PythonUtil
from direct.distributed import DelayDelete
import string
from otp.otpbase import OTPGlobals
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator

class OTPClientRepository(ClientRepository.ClientRepository):
    notify = DirectNotifyGlobal.directNotify.newCategory('OTPClientRepository')
    avatarLimit = 6
    
    def __init__(self, serverVersion, launcher = None, playGame = None):
        ClientRepository.ClientRepository.__init__(self)
        self.launcher = launcher
        base.launcher = launcher
        self._OTPClientRepository__currentAvId = 0
        self.productName = config.GetString('product-name', 'DisneyOnline-US')
        self.createAvatarClass = None
        self.systemMessageSfx = None
        if self.productName == 'DisneyOnline-US':
            if self.launcher and self.launcher.isDummy():
                if self.launcher.getDeployment() == 'UK':
                    self.productName = 'DisneyOnline-UK'
                
            elif self.launcher and not self.launcher.isDummy():
                if self.launcher.getRegistry('DEPLOYMENT') == 'UK':
                    self.productName = 'DisneyOnline-UK'
                
            
        
        self.blue = None
        if self.launcher:
            self.blue = self.launcher.getBlue()
        
        fakeBlue = config.GetString('fake-blue', '')
        if fakeBlue:
            self.blue = fakeBlue
        
        self.playToken = None
        if self.launcher:
            self.playToken = self.launcher.getPlayToken()
        
        fakePlayToken = config.GetString('fake-playtoken', '')
        if fakePlayToken:
            self.playToken = fakePlayToken
        
        self.requiredLogin = config.GetString('required-login', 'auto')
        if self.requiredLogin == 'auto':
            self.notify.info('required-login auto.')
        elif self.requiredLogin == 'green':
            self.notify.error('The green code is out of date')
        elif self.requiredLogin == 'blue':
            if not (self.blue):
                self.notify.error('The tcr does not have the required blue login')
            
        elif self.requiredLogin == 'playToken':
            if not (self.playToken):
                self.notify.error('The tcr does not have the required playToken login')
            
        elif self.requiredLogin == 'gameServer':
            self.notify.info('Using game server name/password.')
        else:
            self.notify.error('The required-login was not recognized.')
        self.computeValidateDownload()
        self.wantMagicWords = base.config.GetString('want-magic-words', '')
        if self.launcher and hasattr(self.launcher, 'http'):
            self.http = self.launcher.http
        else:
            self.http = HTTPClient()
        self.allocateDcFile()
        self.accountOldAuth = config.GetBool('account-old-auth', 0)
        if self.accountOldAuth:
            self.loginInterface = LoginGSAccount.LoginGSAccount(self)
            self.notify.info('loginInterface: LoginGSAccount')
        elif self.blue:
            self.loginInterface = LoginGoAccount.LoginGoAccount(self)
            self.notify.info('loginInterface: LoginGoAccount')
        elif self.playToken:
            self.loginInterface = LoginWebPlayTokenAccount.LoginWebPlayTokenAccount(self)
            self.notify.info('loginInterface: LoginWebPlayTokenAccount')
        else:
            self.loginInterface = LoginTTAccount.LoginTTAccount(self)
            self.notify.info('loginInterface: LoginTTAccount')
        self.secretChatAllowed = base.config.GetBool('allow-secret-chat', 0)
        if base.config.GetBool('secret-chat-needs-parent-password', 0) and self.launcher:
            pass
        self.secretChatNeedsParentPassword = self.launcher.getNeedPwForSecretKey()
        if base.config.GetBool('parent-password-set', 0) and self.launcher:
            pass
        self.parentPasswordSet = self.launcher.getParentPasswordSet()
        self.freeTimeExpiresAt = -1
        self._OTPClientRepository__isPaid = 0
        self.periodTimerExpired = 0
        self.periodTimerStarted = None
        self.periodTimerSecondsRemaining = None
        self.parentMgr.registerParent(OTPGlobals.SPRender, base.render)
        self.parentMgr.registerParent(OTPGlobals.SPHidden, base.hidden)
        self.setZonesRequested = 0
        self.setZonesReceived = 0
        self.timeManager = None
        self._OTPClientRepository__queryAvatarMap = { }
        self._OTPClientRepository__shards = { }
        self.serverVersion = serverVersion
        self.waitingForDatabase = None
        self.loginFSM = ClassicFSM.ClassicFSM('ClientRepositoryLogin', [
            State.State('loginOff', self.enterLoginOff, self.exitLoginOff, [
                'connect']),
            State.State('connect', self.enterConnect, self.exitConnect, [
                'login',
                'failedToConnect',
                'failedToGetServerConstants']),
            State.State('login', self.enterLogin, self.exitLogin, [
                'noConnection',
                'waitForShardList',
                'createAccount',
                'reject',
                'failedToConnect',
                'shutdown']),
            State.State('createAccount', self.enterCreateAccount, self.exitCreateAccount, [
                'noConnection',
                'waitForShardList',
                'login',
                'reject',
                'failedToConnect',
                'shutdown']),
            State.State('failedToConnect', self.enterFailedToConnect, self.exitFailedToConnect, [
                'connect',
                'shutdown']),
            State.State('failedToGetServerConstants', self.enterFailedToGetServerConstants, self.exitFailedToGetServerConstants, [
                'connect',
                'shutdown',
                'noConnection']),
            State.State('shutdown', self.enterShutdown, self.exitShutdown, [
                'loginOff']),
            State.State('waitForShardList', self.enterWaitForShardList, self.exitWaitForShardList, [
                'noConnection',
                'waitForAvatarList',
                'noShards']),
            State.State('noShards', self.enterNoShards, self.exitNoShards, [
                'noConnection',
                'waitForShardList',
                'shutdown']),
            State.State('reject', self.enterReject, self.exitReject, [
                'shutdown']),
            State.State('noConnection', self.enterNoConnection, self.exitNoConnection, [
                'login',
                'connect',
                'shutdown']),
            State.State('afkTimeout', self.enterAfkTimeout, self.exitAfkTimeout, [
                'waitForAvatarList',
                'shutdown']),
            State.State('periodTimeout', self.enterPeriodTimeout, self.exitPeriodTimeout, [
                'waitForAvatarList',
                'shutdown']),
            State.State('waitForAvatarList', self.enterWaitForAvatarList, self.exitWaitForAvatarList, [
                'noConnection',
                'chooseAvatar',
                'createAvatar',
                'shutdown']),
            State.State('chooseAvatar', self.enterChooseAvatar, self.exitChooseAvatar, [
                'noConnection',
                'createAvatar',
                'waitForSetAvatarResponse',
                'waitForAvatarList',
                'waitForDeleteAvatarResponse',
                'shutdown',
                'login']),
            State.State('createAvatar', self.enterCreateAvatar, self.exitCreateAvatar, [
                'noConnection',
                'chooseAvatar',
                'waitForSetAvatarResponse',
                'shutdown']),
            State.State('waitForDeleteAvatarResponse', self.enterWaitForDeleteAvatarResponse, self.exitWaitForDeleteAvatarResponse, [
                'noConnection',
                'chooseAvatar',
                'createAvatar']),
            State.State('waitForSetAvatarResponse', self.enterWaitForSetAvatarResponse, self.exitWaitForSetAvatarResponse, [
                'noConnection',
                'chooseAvatar',
                'waitForAvatarList',
                'login',
                'shutdown',
                'afkTimeout',
                'periodTimeout'])], 'loginOff', 'loginOff')
        self.gameFSM = ClassicFSM.ClassicFSM('ClientRepository', [
            State.State('gameOff', self.enterGameOff, self.exitGameOff, [
                'waitOnEnterResponses']),
            State.State('waitOnEnterResponses', self.enterWaitOnEnterResponses, self.exitWaitOnEnterResponses, [
                'playGame',
                'passThroughQuietZone',
                'gameOff']),
            State.State('passThroughQuietZone', self.enterPassThroughQuietZone, self.exitPassThroughQuietZone, [
                'playGame',
                'tutorialQuestion',
                'gameOff']),
            State.State('tutorialQuestion', self.enterTutorialQuestion, self.exitTutorialQuestion, [
                'playGame',
                'gameOff']),
            State.State('playGame', self.enterPlayGame, self.exitPlayGame, [
                'gameOff',
                'waitOnEnterResponses'])], 'gameOff', 'gameOff')
        self.loginFSM.getStateNamed('waitForSetAvatarResponse').addChild(self.gameFSM)
        self.loginFSM.enterInitialState()
        self.loginScreen = None
        self.music = None
        self.gameDoneEvent = 'playGameDone'
        self.playGame = playGame(self.gameFSM, self.gameDoneEvent)

    
    def enterLoginOff(self):
        self.handler = self.handleLoginOff

    
    def exitLoginOff(self):
        self.handler = None

    
    def handleLoginOff(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)

    
    def computeValidateDownload(self):
        if self.launcher:
            hash = HashVal()
            hash.mergeWith(launcher.launcherFileDbHash)
            hash.mergeWith(launcher.serverDbFileHash)
            self.validateDownload = hash.asHex()
        else:
            self.validateDownload = ''
            downloadParFilename = Filename.expandFrom('$TOONTOWN/src/configfiles/download.par')
            if downloadParFilename.exists():
                downloadPar = open(downloadParFilename.toOsSpecific())
                for line in downloadPar.readlines():
                    i = string.find(line, 'VALIDATE_DOWNLOAD=')
                    if i != -1:
                        self.validateDownload = string.strip(line[i + 18:])
                        break
                    
                
            

    
    def getServerVersion(self):
        return self.serverVersion

    
    def enterConnect(self, serverList):
        self.serverList = serverList
        self.setZonesReceived = self.setZonesRequested
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.connectingBox = dialogClass(message = OTPLocalizer.CRConnecting)
        self.connectingBox.show()
        self.renderFrame()
        self.handler = self.handleConnect
        self.connect(self.serverList, successCallback = self.gotoFirstScreen, failureCallback = self.failedToConnect)

    
    def failedToConnect(self, statusCode, statusString):
        self.loginFSM.request('failedToConnect', [
            statusCode,
            statusString])

    
    def exitConnect(self):
        self.connectingBox.cleanup()
        del self.connectingBox

    
    def handleConnect(self, msgType, di):
        if msgType == CLIENT_SERVER_UP:
            self.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)

    
    def handleSystemMessage(self, di):
        message = ClientRepository.ClientRepository.handleSystemMessage(self, di)
        whisper = WhisperPopup(message, OTPGlobals.getInterfaceFont(), WhisperPopup.WTSystem)
        whisper.manage(base.marginManager)
        if not (self.systemMessageSfx):
            self.systemMessageSfx = base.loadSfx('phase_3.5/audio/sfx/GUI_whisper_3.mp3')
        
        if self.systemMessageSfx:
            base.playSfx(self.systemMessageSfx)
        

    
    def gotoFirstScreen(self):
        
        try:
            self.accountServerConstants = AccountServerConstants.AccountServerConstants(self)
        except TTAccount.TTAccountException:
            e = None
            self.notify.debug(str(e))
            self.loginFSM.request('failedToGetServerConstants', [
                e])
            return None

        self.startReaderPollTask()
        self.startHeartbeat()
        newInstall = 0
        if launcher:
            newInstall = launcher.getIsNewInstallation()
        
        newInstall = base.config.GetBool('new-installation', newInstall)
        self.loginFSM.request('login')

    
    def enterLogin(self):
        self.sendSetAvatarIdMsg(0)
        self.loginDoneEvent = 'loginDone'
        self.loginScreen = LoginScreen.LoginScreen(self, self.loginDoneEvent)
        self.accept(self.loginDoneEvent, self._OTPClientRepository__handleLoginDone)
        self.loginScreen.load()
        self.loginScreen.enter()

    
    def _OTPClientRepository__handleLoginDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'success':
            self.setIsNotNewInstallation()
            self.loginFSM.request('waitForShardList')
        elif mode == 'getChatPassword':
            self.loginFSM.request('parentPassword')
        elif mode == 'freeTimeExpired':
            self.loginFSM.request('freeTimeInform')
        elif mode == 'createAccount':
            self.loginFSM.request('createAccount', [
                {
                    'back': 'login',
                    'backArgs': [] }])
        elif mode == 'reject':
            self.loginFSM.request('reject')
        elif mode == 'quit':
            self.loginFSM.request('shutdown')
        elif mode == 'failure':
            self.loginFSM.request('failedToConnect', [
                -1,
                '?'])
        else:
            self.notify.error('Invalid doneStatus mode from loginScreen: ' + str(mode))

    
    def exitLogin(self):
        if self.loginScreen:
            self.loginScreen.exit()
            self.loginScreen.unload()
            self.loginScreen = None
            self.renderFrame()
        
        self.ignore(self.loginDoneEvent)
        del self.loginDoneEvent
        self.handler = None

    
    def enterCreateAccount(self, createAccountDoneData = {
        'back': 'login',
        'backArgs': [] }):
        self.createAccountDoneData = createAccountDoneData
        self.createAccountDoneEvent = 'createAccountDone'
        self.createAccountScreen = None
        self.createAccountScreen = CreateAccountScreen.CreateAccountScreen(self, self.createAccountDoneEvent)
        self.accept(self.createAccountDoneEvent, self._OTPClientRepository__handleCreateAccountDone)
        self.createAccountScreen.load()
        self.createAccountScreen.enter()

    
    def _OTPClientRepository__handleCreateAccountDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'success':
            self.setIsNotNewInstallation()
            self.loginFSM.request('waitForShardList')
        elif mode == 'reject':
            self.loginFSM.request('reject')
        elif mode == 'cancel':
            self.loginFSM.request(self.createAccountDoneData['back'], self.createAccountDoneData['backArgs'])
        elif mode == 'failure':
            self.loginFSM.request(self.createAccountDoneData['back'], self.createAccountDoneData['backArgs'])
        elif mode == 'quit':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Invalid doneStatus mode from CreateAccountScreen: ' + str(mode))

    
    def exitCreateAccount(self):
        if self.createAccountScreen:
            self.createAccountScreen.exit()
            self.createAccountScreen.unload()
            self.createAccountScreen = None
            self.renderFrame()
        
        self.ignore(self.createAccountDoneEvent)
        del self.createAccountDoneEvent
        self.handler = None

    
    def enterFailedToConnect(self, statusCode, statusString):
        self.handler = self.handleFailedToConnect
        url = self.serverList[0]
        self.notify.warning('Failed to connect to %s (%s %s).  Notifying user.' % (url.cStr(), statusCode, statusString))
        if statusCode == 1403 and statusCode == 1405 or statusCode == 1400:
            message = OTPLocalizer.CRNoConnectProxyNoPort % (url.getServer(), url.getPort(), url.getPort())
            style = OTPDialog.CancelOnly
        else:
            message = OTPLocalizer.CRNoConnectTryAgain % (url.getServer(), url.getPort())
            style = OTPDialog.TwoChoice
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.failedToConnectBox = dialogClass(message = message, doneEvent = 'failedToConnectAck', text_wordwrap = 18, style = style)
        self.failedToConnectBox.show()
        self.notify.info(message)
        self.accept('failedToConnectAck', self._OTPClientRepository__handleFailedToConnectAck)

    
    def _OTPClientRepository__handleFailedToConnectAck(self):
        doneStatus = self.failedToConnectBox.doneStatus
        if doneStatus == 'ok':
            self.loginFSM.request('connect', [
                self.serverList])
        elif doneStatus == 'cancel':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))

    
    def handleFailedToConnect(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)

    
    def exitFailedToConnect(self):
        self.handler = None
        self.ignore('failedToConnectAck')
        self.failedToConnectBox.cleanup()
        del self.failedToConnectBox

    
    def enterFailedToGetServerConstants(self, e):
        self.handler = self.handleFailedToGetConstants
        url = AccountServerConstants.AccountServerConstants.getServerURL()
        statusCode = 0
        if isinstance(e, HTTPUtil.ConnectionError):
            statusCode = e.statusCode
            self.notify.warning('Got status code %s from connection to %s.' % (statusCode, url.cStr()))
        else:
            self.notify.warning("Didn't get status code from connection to %s." % url.cStr())
        if statusCode == 1403 or statusCode == 1400:
            message = OTPLocalizer.CRServerConstantsProxyNoPort % (url.cStr(), url.getPort())
            style = OTPDialog.CancelOnly
        elif statusCode == 1405:
            message = OTPLocalizer.CRServerConstantsProxyNoCONNECT % url.cStr()
            style = OTPDialog.CancelOnly
        else:
            message = OTPLocalizer.CRServerConstantsTryAgain % url.cStr()
            style = OTPDialog.TwoChoice
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.failedToGetConstantsBox = dialogClass(message = message, doneEvent = 'failedToGetConstantsAck', text_wordwrap = 18, style = style)
        self.failedToGetConstantsBox.show()
        self.accept('failedToGetConstantsAck', self._OTPClientRepository__handleFailedToGetConstantsAck)
        self.notify.warning('Failed to get account server constants. Notifying user.')

    
    def _OTPClientRepository__handleFailedToGetConstantsAck(self):
        doneStatus = self.failedToGetConstantsBox.doneStatus
        if doneStatus == 'ok':
            self.loginFSM.request('connect', [
                self.serverList])
        elif doneStatus == 'cancel':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))

    
    def handleFailedToGetConstants(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)

    
    def exitFailedToGetServerConstants(self):
        self.handler = None
        self.ignore('failedToGetConstantsAck')
        self.failedToGetConstantsBox.cleanup()
        del self.failedToGetConstantsBox

    
    def enterShutdown(self):
        self.handler = self.handleShutdown
        self.sendDisconnect()
        self.notify.info('Exiting cleanly')
        base.exitShow()

    
    def exitShutdown(self):
        self.handler = None

    
    def handleShutdown(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)

    
    def enterWaitForShardList(self):
        self.handler = self.handleWaitForGetShardListResponse
        self.sendGetShardListMsg()

    
    def sendGetShardListMsg(self):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_GET_SHARD_LIST)
        self.send(datagram)

    
    def exitWaitForShardList(self):
        self.handler = None

    
    def handleWaitForGetShardListResponse(self, msgType, di):
        if msgType == CLIENT_GET_SHARD_LIST_RESP:
            self.handleLoginGetShardListResponseMsg(di)
        elif msgType == CLIENT_SERVER_UP:
            self.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)

    
    def handleGetShardListResponseMsg(self, di):
        numberOfShards = di.getUint16()
        if numberOfShards == 0:
            return 0
        
        for i in range(numberOfShards):
            shardId = di.getUint32()
            shardName = di.getString()
            shardPop = di.getUint32()
            shardWVPop = di.getUint32()
            shardActive = di.getBool()
            if not self._OTPClientRepository__shards.has_key(shardId):
                shard = PotentialShard.PotentialShard(shardId)
                self._OTPClientRepository__shards[shardId] = shard
            else:
                shard = self._OTPClientRepository__shards[shardId]
            shard.name = shardName
            shard.population = shardPop
            shard.welcomeValleyPopulation = shardWVPop
            shard.active = shardActive
        
        messenger.send('shardInfoUpdated')
        return numberOfShards

    
    def handleLoginGetShardListResponseMsg(self, di):
        numberOfShards = self.handleGetShardListResponseMsg(di)
        if numberOfShards != 0:
            self.loginFSM.request('waitForAvatarList')
        else:
            self.loginFSM.request('noShards')

    
    def enterNoShards(self):
        self.handler = self.handleNoShards
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.noShardsBox = dialogClass(message = OTPLocalizer.CRNoDistrictsTryAgain, doneEvent = 'noShardsAck', style = OTPDialog.TwoChoice)
        self.noShardsBox.show()
        self.accept('noShardsAck', self._OTPClientRepository__handleNoShardsAck)
        self.notify.warning('No shards are available.')

    
    def _OTPClientRepository__handleNoShardsAck(self):
        doneStatus = self.noShardsBox.doneStatus
        print doneStatus
        if doneStatus == 'ok':
            self.loginFSM.request('waitForShardList')
        elif doneStatus == 'cancel':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))

    
    def handleNoShards(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)

    
    def exitNoShards(self):
        self.handler = None
        self.ignore('noShardsAck')
        self.noShardsBox.cleanup()
        del self.noShardsBox

    
    def enterReject(self):
        self.handler = self.handleReject
        self.notify.warning('Connection Rejected')
        if launcher:
            launcher.setPandaErrorCode(13)
        
        sys.exit()

    
    def exitReject(self):
        self.handler = None

    
    def handleReject(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)

    
    def enterNoConnection(self):
        self.handler = self.handleNoConnection
        self._OTPClientRepository__currentAvId = 0
        self.stopHeartbeat()
        self.stopReaderPollTask()
        if self.bootedIndex != None and OTPLocalizer.CRBootedReasons.has_key(self.bootedIndex):
            message = OTPLocalizer.CRBootedReasons[self.bootedIndex]
        elif self.bootedText != None:
            message = OTPLocalizer.CRBootedReasonUnknownCode % self.bootedIndex
        else:
            message = OTPLocalizer.CRLostConnection
        style = OTPDialog.Acknowledge
        if self.loginInterface.supportsRelogin():
            message += OTPLocalizer.CRTryConnectAgain
            style = OTPDialog.TwoChoice
        
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.lostConnectionBox = dialogClass(doneEvent = 'lostConnectionAck', message = message, text_wordwrap = 18, style = style)
        self.lostConnectionBox.show()
        self.accept('lostConnectionAck', self._OTPClientRepository__handleLostConnectionAck)
        self.notify.warning('Lost connection to server. Notifying user.')

    
    def _OTPClientRepository__handleLostConnectionAck(self):
        if self.lostConnectionBox.doneStatus == 'ok' and self.loginInterface.supportsRelogin():
            self.loginFSM.request('connect', [
                self.serverList])
        else:
            self.loginFSM.request('shutdown')

    
    def handleNoConnection(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)

    
    def exitNoConnection(self):
        self.handler = None
        self.ignore('lostConnectionAck')
        self.lostConnectionBox.cleanup()

    
    def enterAfkTimeout(self):
        self.sendSetAvatarIdMsg(0)
        msg = OTPLocalizer.AfkForceAcknowledgeMessage
        dialogClass = OTPGlobals.getDialogClass()
        self.afkDialog = dialogClass(text = msg, command = self._OTPClientRepository__handleAfkOk, style = OTPDialog.Acknowledge)
        self.handler = self.handleAfkMessage

    
    def _OTPClientRepository__handleAfkOk(self, value):
        self.loginFSM.request('waitForAvatarList')

    
    def exitAfkTimeout(self):
        if self.afkDialog:
            self.afkDialog.cleanup()
            self.afkDialog = None
        
        self.handler = None

    
    def handleAfkMessage(self, msgType, di):
        if msgType == CLIENT_SERVER_UP:
            self.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.handleServerDown(di)
        elif msgType == CLIENT_GET_STATE_RESP:
            pass
        else:
            self.handleUnexpectedMsgType(msgType, di)

    
    def enterPeriodTimeout(self):
        self.sendSetAvatarIdMsg(0)
        self.sendDisconnect()
        msg = OTPLocalizer.PeriodForceAcknowledgeMessage
        dialogClass = OTPGlobals.getDialogClass()
        self.periodDialog = dialogClass(text = msg, command = self._OTPClientRepository__handlePeriodOk, style = OTPDialog.Acknowledge)
        self.handler = self.handleShutdown

    
    def _OTPClientRepository__handlePeriodOk(self, value):
        base.exitShow()

    
    def exitPeriodTimeout(self):
        if self.periodDialog:
            self.periodDialog.cleanup()
            self.periodDialog = None
        
        self.handler = None

    
    def enterWaitForAvatarList(self):
        self.handler = self.handleWaitForAvatarList
        self.sendGetAvatarsMsg()
        self.waitForDatabaseTimeout(requestName = 'WaitForAvatarList')

    
    def sendGetAvatarsMsg(self):
        print self.createAvatarClass
        if self.createAvatarClass:
            className = self.createAvatarClass.__name__
            dclass = self.dclassesByName[className]
            print className
            if className != 'DistributedToon':
                datagram = PyDatagram()
                datagram.addUint16(CLIENT_SET_AVTYPE)
                datagram.addUint16(dclass.getNumber())
                self.send(datagram)
            
        
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_GET_AVATARS)
        self.send(datagram)

    
    def exitWaitForAvatarList(self):
        self.cleanupWaitingForDatabase()
        self.handler = None

    
    def handleWaitForAvatarList(self, msgType, di):
        if msgType == CLIENT_GET_AVATARS_RESP:
            self.handleGetAvatarsRespMsg(di)
        elif msgType == CLIENT_GET_AVATARS_RESP2:
            self.handleGetAvatarsResp2Msg(di)
        elif msgType == CLIENT_SERVER_UP:
            self.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)

    
    def handleGetAvatarsRespMsg(self, di):
        returnCode = di.getUint8()
        if returnCode == 0:
            avatarTotal = di.getUint16()
            avList = []
            for i in range(0, avatarTotal):
                avNum = di.getUint32()
                avNames = [
                    '',
                    '',
                    '',
                    '']
                avNames[0] = di.getString()
                avNames[1] = di.getString()
                avNames[2] = di.getString()
                avNames[3] = di.getString()
                avDNA = di.getString()
                avPosition = di.getUint8()
                aname = di.getUint8()
                potAv = PotentialAvatar.PotentialAvatar(avNum, avNames, avDNA, avPosition, aname)
                avList.append(potAv)
            
            self.avList = avList
            self.loginFSM.request('chooseAvatar', [
                self.avList])
        else:
            self.notify.error('Bad avatar list return code: ' + str(returnCode))
            self.loginFSM.request('shutdown')

    
    def handleGetAvatarsResp2Msg(self, di):
        returnCode = di.getUint8()
        if returnCode == 0:
            avatarTotal = di.getUint16()
            avList = []
            for i in range(0, avatarTotal):
                avNum = di.getUint32()
                avNames = [
                    '',
                    '',
                    '',
                    '']
                avNames[0] = di.getString()
                avDNA = None
                avPosition = di.getUint8()
                aname = None
                potAv = PotentialAvatar.PotentialAvatar(avNum, avNames, avDNA, avPosition, aname)
                avList.append(potAv)
            
            self.avList = avList
            self.loginFSM.request('chooseAvatar', [
                self.avList])
        else:
            self.notify.error('Bad avatar list return code: ' + str(returnCode))
            self.loginFSM.request('shutdown')

    
    def enterChooseAvatar(self, avList):
        pass

    
    def exitChooseAvatar(self):
        pass

    
    def enterCreateAvatar(self, avList, index, newDNA = None):
        pass

    
    def exitCreateAvatar(self):
        pass

    
    def sendCreateAvatarMsg(self, avDNA, avName, avPosition):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_CREATE_AVATAR)
        datagram.addUint16(0)
        datagram.addString(avDNA.makeNetString())
        datagram.addUint8(avPosition)
        self.newName = avName
        self.newDNA = avDNA
        self.newPosition = avPosition
        self.send(datagram)

    
    def sendCreateAvatar2Msg(self, avClass, avDNA, avName, avPosition):
        className = avClass.__name__
        dclass = self.dclassesByName[className]
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_AVTYPE)
        datagram.addUint16(dclass.getNumber())
        self.send(datagram)
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_CREATE_AVATAR2)
        datagram.addUint16(0)
        datagram.addUint8(avPosition)
        datagram.addUint16(dclass.getNumber())
        self.newName = avName
        self.newDNA = avDNA
        self.newPosition = avPosition
        self.send(datagram)

    
    def enterWaitForDeleteAvatarResponse(self, potAv):
        self.handler = self.handleWaitForDeleteAvatarResponse
        self.sendDeleteAvatarMsg(potAv.id)
        self.waitForDatabaseTimeout(requestName = 'WaitForDeleteAvatarResponse')

    
    def sendDeleteAvatarMsg(self, avId):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_DELETE_AVATAR)
        datagram.addUint32(avId)
        self.send(datagram)

    
    def exitWaitForDeleteAvatarResponse(self):
        self.cleanupWaitingForDatabase()
        self.handler = None

    
    def handleWaitForDeleteAvatarResponse(self, msgType, di):
        if msgType == CLIENT_DELETE_AVATAR_RESP:
            self.handleGetAvatarsRespMsg(di)
        elif msgType == CLIENT_SERVER_UP:
            self.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)

    
    def enterWaitForSetAvatarResponse(self, potAv):
        self.handler = self.handleWaitForSetAvatarResponse
        self.sendSetAvatarMsg(potAv)
        self.waitForDatabaseTimeout(requestName = 'WaitForSetAvatarResponse')

    
    def exitWaitForSetAvatarResponse(self):
        pass

    
    def sendSetAvatarMsg(self, potAv):
        self.sendSetAvatarIdMsg(potAv.id)
        self.avData = potAv

    
    def sendSetAvatarIdMsg(self, avId):
        if avId != self._OTPClientRepository__currentAvId:
            self._OTPClientRepository__currentAvId = avId
            datagram = PyDatagram()
            datagram.addUint16(CLIENT_SET_AVATAR)
            datagram.addUint32(avId)
            self.send(datagram)
            if avId == 0:
                self.stopPeriodTimer()
            else:
                self.startPeriodTimer()
        

    
    def handleWaitForSetAvatarResponse(self, msgType, di):
        if msgType == CLIENT_GET_AVATAR_DETAILS_RESP:
            self.handleAvatarResponseMsg(di)
        elif msgType == CLIENT_GET_PET_DETAILS_RESP:
            self.handleAvatarResponseMsg(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_RESP:
            self.handleGetFriendsList(di)
        elif msgType == CLIENT_FRIEND_ONLINE:
            self.handleFriendOnline(di)
        elif msgType == CLIENT_FRIEND_OFFLINE:
            self.handleFriendOffline(di)
        elif msgType == CLIENT_SERVER_UP:
            self.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)

    
    def getAvatarDetails(self, avatar, func, *args):
        print 'Avatar type is ' + str(avatar.__class__)
        task = Task.Task(func)
        task.args = args
        task.avatar = avatar
        task.delayDelete = DelayDelete.DelayDelete(avatar)
        avId = avatar.doId
        self._OTPClientRepository__queryAvatarMap[avId] = task
        self._OTPClientRepository__sendGetAvatarDetails(avId)

    
    def cancelAvatarDetailsRequest(self, avatar):
        avId = avatar.doId
        if self._OTPClientRepository__queryAvatarMap.has_key(avId):
            del self._OTPClientRepository__queryAvatarMap[avId]
        

    
    def _OTPClientRepository__sendGetAvatarDetails(self, avId):
        datagram = PyDatagram()
        avatar = self._OTPClientRepository__queryAvatarMap[avId].avatar
        datagram.addUint16(avatar.getRequestID())
        datagram.addUint32(avId)
        self.send(datagram)

    
    def handleGetAvatarDetailsResp(self, di):
        avId = di.getUint32()
        returnCode = di.getUint8()
        self.notify.info('Got query response for avatar %d, code = %d.' % (avId, returnCode))
        
        try:
            task = self._OTPClientRepository__queryAvatarMap[avId]
        except:
            self.notify.warning('Received unexpected or outdated details for avatar %d.' % avId)
            return None

        del self._OTPClientRepository__queryAvatarMap[avId]
        gotData = 0
        if returnCode != 0:
            self.notify.warning('No information available for avatar %d.' % avId)
        elif str(task.avatar.__class__) == 'toontown.toon.DistributedToon.DistributedToon':
            dclass = self.dclassesByName['DistributedToon']
        elif str(task.avatar.__class__) == 'toontown.pets.DistributedPet.DistributedPet':
            dclass = self.dclassesByName['DistributedPet']
        else:
            self.notify.warning('This avatar type is invalid.')
            return None
        task.avatar.updateAllRequiredFields(dclass, di)
        gotData = 1
        if isinstance(task.__call__, types.StringType):
            messenger.send(task.__call__, list((gotData, task.avatar) + task.args))
        else:
            apply(task.__call__, (gotData, task.avatar) + task.args)

    
    def handleChooseAvatar(self, msgType, di):
        if msgType == CLIENT_SERVER_UP:
            self.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.handleServerDown(di)
        elif msgType == CLIENT_GET_STATE_RESP:
            pass
        else:
            self.handleUnexpectedMsgType(msgType, di)

    
    def enterGameOff(self):
        self.handler = self.handleGameOff
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def exitGameOff(self):
        self.handler = None

    
    def handleGameOff(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)

    
    def enterWaitOnEnterResponses(self, shardId, hoodId, zoneId, avId):
        self.handler = self.handleWaitOnEnterResponses
        self.handlerArgs = {
            'hoodId': hoodId,
            'zoneId': zoneId,
            'avId': avId }
        self.notify.info('Entering shard %s' % shardId)
        self.sendSetShardMsg(shardId)
        base.localAvatar.defaultShard = shardId
        time.sleep(1)
        self.waitForDatabaseTimeout(requestName = 'WaitOnEnterResponses')

    
    def handleWaitOnEnterResponses(self, msgType, di):
        if msgType == CLIENT_GET_STATE_RESP:
            self.handleSetShardResponse(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_RESP:
            self.handleGetFriendsList(di)
        elif msgType == CLIENT_FRIEND_ONLINE:
            self.handleFriendOnline(di)
        elif msgType == CLIENT_FRIEND_OFFLINE:
            self.handleFriendOffline(di)
        elif msgType == CLIENT_SERVER_UP:
            self.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)

    
    def handleSetShardResponse(self, di):
        self.cleanupWaitingForDatabase()
        hoodId = self.handlerArgs['hoodId']
        zoneId = self.handlerArgs['zoneId']
        avId = self.handlerArgs['avId']
        self.gameFSM.request('passThroughQuietZone', [
            hoodId,
            zoneId,
            avId])
        return None

    
    def exitWaitOnEnterResponses(self):
        self.cleanupWaitingForDatabase()
        self.handler = None
        self.handlerArgs = None

    
    def enterTutorialQuestion(self, hoodId, zoneId, avId):
        pass

    
    def exitTutorialQuestion(self):
        pass

    
    def enterPlayGame(self, hoodId, zoneId, avId):
        if self.music:
            self.music.stop()
            self.music = None
        
        self.handler = self.handlePlayGame
        self.accept(self.gameDoneEvent, self.handleGameDone)
        base.transitions.noFade()
        self.playGame.load()
        
        try:
            loader.endBulkLoad('localAvatarPlayGame')
        except:
            pass

        self.playGame.enter(hoodId, zoneId, avId)
        
        def checkScale(task):
            return Task.cont


    
    def handleGameDone(self):
        if self.timeManager:
            self.timeManager.setDisconnectReason(OTPGlobals.DisconnectSwitchShards)
        
        doneStatus = self.playGame.getDoneStatus()
        how = doneStatus['how']
        shardId = doneStatus['shardId']
        hoodId = doneStatus['hoodId']
        zoneId = doneStatus['zoneId']
        avId = doneStatus['avId']
        if how == 'teleportIn':
            self.gameFSM.request('waitOnEnterResponses', [
                shardId,
                hoodId,
                zoneId,
                avId])
        else:
            self.notify.error('Exited shard with unexpected mode %s' % how)

    
    def exitPlayGame(self):
        taskMgr.remove('globalScaleCheck')
        self.handler = None
        self.playGame.exit()
        self.playGame.unload()
        self.disableAllBetweenShards()
        self.ignore(self.gameDoneEvent)

    
    def enterPassThroughQuietZone(self, hoodId, zoneId, avId):
        globalClockDelta.clear()
        self.handler = self.handlePassThroughQuietZone
        self.handlerArgs = {
            'hoodId': hoodId,
            'zoneId': zoneId,
            'avId': avId }
        self.sendSetZoneMsg(OTPGlobals.QuietZone)
        self.waitForDatabaseTimeout(20, requestName = 'PassThroughQuietZone')
        return None

    
    def handlePassThroughQuietZone(self, msgType, di):
        if msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            self.handleQuietZoneGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            self.handleQuietZoneGenerateWithRequiredOther(di)
        elif msgType == CLIENT_OBJECT_UPDATE_FIELD:
            self.handleUpdateField(di)
        elif msgType == CLIENT_OBJECT_DISABLE_RESP:
            self.handleDisable(di)
        elif msgType == CLIENT_OBJECT_DELETE_RESP:
            self.handleDelete(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_RESP:
            self.handleGetFriendsList(di)
        elif msgType == CLIENT_FRIEND_ONLINE:
            self.handleFriendOnline(di)
        elif msgType == CLIENT_FRIEND_OFFLINE:
            self.handleFriendOffline(di)
        elif msgType == CLIENT_GET_AVATAR_DETAILS_RESP:
            self.handleGetAvatarDetailsResp(di)
        elif msgType == CLIENT_GET_PET_DETAILS_RESP:
            self.handleGetAvatarDetailsResp(di)
        elif msgType == CLIENT_SERVER_UP:
            self.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.handleServerDown(di)
        elif msgType == CLIENT_GET_STATE_RESP:
            pass
        elif msgType == CLIENT_DONE_SET_ZONE_RESP:
            zoneId = di.getInt32()
            if zoneId == OTPGlobals.QuietZone:
                self.reachedQuietZone()
            
        else:
            self.handleUnexpectedMsgType(msgType, di)

    
    def reachedQuietZone(self):
        self._OTPClientRepository__gotTimeSync = 0
        self.cleanupWaitingForDatabase()
        if self.timeManager == None:
            self.notify.info('TimeManager is not present.')
            DistributedSmoothNode.activateSmoothing(0, 0)
            self.gotTimeSync()
        else:
            DistributedSmoothNode.activateSmoothing(1, 0)
            if self.timeManager.synchronize('startup'):
                self.accept('gotTimeSync', self.gotTimeSync)
                self.waitForDatabaseTimeout(requestName = 'reachedQuietZone-timeSync')
            else:
                self.notify.info('No sync from TimeManager.')
                self.gotTimeSync()

    
    def gotTimeSync(self):
        self.notify.info('gotTimeSync')
        self.ignore('gotTimeSync')
        self._OTPClientRepository__gotTimeSync = 1
        self.moveOnFromQuietZone()

    
    def moveOnFromQuietZone(self):
        if not (self._OTPClientRepository__gotTimeSync):
            self.notify.info('Waiting for time sync.')
            return None
        
        hoodId = self.handlerArgs['hoodId']
        zoneId = self.handlerArgs['zoneId']
        avId = self.handlerArgs['avId']
        if not (self.SupportTutorial) or base.localAvatar.tutorialAck:
            self.gameFSM.request('playGame', [
                hoodId,
                zoneId,
                avId])
        elif base.config.GetBool('force-tutorial', 1):
            self.gameFSM.request('tutorialQuestion', [
                hoodId,
                zoneId,
                avId])
        else:
            self.gameFSM.request('playGame', [
                hoodId,
                zoneId,
                avId])
        return None

    
    def exitPassThroughQuietZone(self):
        self.cleanupWaitingForDatabase()
        self.ignore('gotTimeSync')
        self.handler = None
        self.handlerArgs = None
        return None

    
    def handlePlayGame(self, msgType, di):
        if self.notify.getDebug():
            self.notify.debug('handle play game got message type: ' + `msgType`)
        
        if msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            self.handleGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            self.handleGenerateWithRequiredOther(di)
        elif msgType == CLIENT_OBJECT_UPDATE_FIELD:
            self.handleUpdateField(di)
        elif msgType == CLIENT_OBJECT_DISABLE_RESP:
            self.handleDisable(di)
        elif msgType == CLIENT_OBJECT_DELETE_RESP:
            self.handleDelete(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_RESP:
            self.handleGetFriendsList(di)
        elif msgType == CLIENT_FRIEND_ONLINE:
            self.handleFriendOnline(di)
        elif msgType == CLIENT_FRIEND_OFFLINE:
            self.handleFriendOffline(di)
        elif msgType == CLIENT_GET_AVATAR_DETAILS_RESP:
            self.handleGetAvatarDetailsResp(di)
        elif msgType == CLIENT_GET_PET_DETAILS_RESP:
            self.handleGetAvatarDetailsResp(di)
        elif msgType == CLIENT_SERVER_UP:
            self.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.handleServerDown(di)
        elif msgType == CLIENT_GET_SHARD_LIST_RESP:
            self.handleGetShardListResponseMsg(di)
        elif msgType == CLIENT_GET_STATE_RESP:
            di.skipBytes(12)
            zoneId = di.getInt32()
        elif msgType == CLIENT_DONE_SET_ZONE_RESP:
            zoneId = di.getInt32()
        else:
            self.handleUnexpectedMsgType(msgType, di)

    
    def sendQuietZoneRequest(self):
        self.disableAll()
        self.sendSetZoneMsg(OTPGlobals.QuietZone)

    
    def disableAll(self):
        distObjs = self.doId2do.values()
        for distObj in distObjs:
            if distObj.getNeverDisable():
                pass
            1
            self.disableDoId(distObj.doId)
        

    
    def disableAllBetweenShards(self):
        distObjs = self.doId2do.values()
        for distObj in distObjs:
            if distObj.doId == base.localAvatar.doId:
                pass
            1
            if distObj.doId == GLOBAL_ID_FRIEND_MANAGER:
                pass
            1
            self.disableDoId(distObj.doId)
        

    
    def needParentPasswordForSecretChat(self):
        if self.isPaid() and self.secretChatNeedsParentPassword and self.productName == 'Terra-DMC' and self.isBlue():
            pass
        return self.secretChatAllowed

    
    def isFreeTimeExpired(self):
        if self.accountOldAuth:
            return 0
        
        if base.config.GetBool('free-time-expired', 0):
            return 1
        
        if base.config.GetBool('unlimited-free-time', 0):
            return 0
        
        if self.freeTimeExpiresAt == -1:
            return 0
        
        if self.freeTimeExpiresAt == 0:
            return 1
        
        if self.freeTimeExpiresAt < -1:
            self.notify.warning('freeTimeExpiresAt is less than -1 (%s)' % self.freeTimeExpiresAt)
        
        if self.freeTimeExpiresAt < time.time():
            return 1
        else:
            return 0

    
    def freeTimeLeft(self):
        if self.freeTimeExpiresAt == -1 or self.freeTimeExpiresAt == 0:
            return 0
        
        secsLeft = self.freeTimeExpiresAt - time.time()
        return max(0, secsLeft)

    
    def isWebPlayToken(self):
        return self.playToken != None

    
    def isBlue(self):
        return self.blue != None

    
    def isPaid(self):
        paidStatus = base.config.GetString('force-paid-status', '')
        if paidStatus == 'paid':
            return 1
        
        if paidStatus == 'unpaid':
            return 0
        
        return self._OTPClientRepository__isPaid

    
    def setIsPaid(self, isPaid):
        self._OTPClientRepository__isPaid = isPaid

    
    def allowFreeNames(self):
        return base.config.GetInt('allow-free-names', 1)

    
    def allowSecretChat(self):
        if self.isPaid() and self.secretChatAllowed and self.productName == 'Terra-DMC' and self.isBlue():
            pass
        return self.secretChatAllowed

    
    def isParentPasswordSet(self):
        return self.parentPasswordSet

    
    def logAccountInfo(self):
        self.notify.info('*** ACCOUNT INFO ***')
        self.notify.info('username: %s' % self.userName)
        if self.blue:
            self.notify.info('paid: %s (blue)' % self.isPaid())
        else:
            self.notify.info('paid: %s' % self.isPaid())
        if not self.isPaid():
            if self.isFreeTimeExpired():
                self.notify.info('free time is expired')
            else:
                secs = self.freeTimeLeft()
                self.notify.info('free time left: %s' % PythonUtil.formatElapsedSeconds(secs))
        
        if self.periodTimerSecondsRemaining != None:
            self.notify.info('period time left: %s' % PythonUtil.formatElapsedSeconds(self.periodTimerSecondsRemaining))
        

    
    def getShardName(self, shardId):
        
        try:
            return self._OTPClientRepository__shards[shardId].name
        except:
            return None


    
    def isShardAvailable(self, shardId):
        
        try:
            return self._OTPClientRepository__shards[shardId].available
        except:
            return 0


    
    def listActiveShards(self):
        list = []
        for s in self._OTPClientRepository__shards.values():
            if s.available and s.active:
                list.append((s.id, s.name, s.population, s.welcomeValleyPopulation))
            
        
        return list

    
    def handleServerUp(self, di):
        shardId = di.getUint32()
        shardName = di.getString()
        potShard = PotentialShard.PotentialShard(shardId)
        potShard.name = shardName
        self._OTPClientRepository__shards[shardId] = potShard
        self.notify.info('shard %s is now available.' % shardName)
        messenger.send('shardInfoUpdated')

    
    def handleServerDown(self, di):
        shardId = di.getUint32()
        
        try:
            potShard = self._OTPClientRepository__shards[shardId]
            potShard.available = 0
            self.notify.info('shard %s is no longer available.' % potShard.name)
        except:
            self.notify.info('Unknown shard %d is no longer available.' % shardId)

        messenger.send('shardInfoUpdated')

    
    def allocateDcFile(self):
        dcName = 'Shard %s cannot be found.'
        hash = HashVal()
        hash.hashString(dcName)
        self.http.setClientCertificatePassphrase(hash.asHex())

    
    def lostConnection(self):
        ClientRepository.ClientRepository.lostConnection(self)
        self.loginFSM.request('noConnection')

    
    def sendSetZoneMsg(self, *args, **kwargs):
        ClientRepository.ClientRepository.sendSetZoneMsg(self, *args, **args)
        self.setZonesRequested += 1

    
    def getSetZoneDoneEvent(self, setZoneId):
        return 'TCRSetZoneDone-%s' % setZoneId

    
    def getNextSetZoneDoneEvent(self):
        return self.getSetZoneDoneEvent(self.setZonesRequested)

    
    def handleSetZoneDone(self):
        messenger.send(self.getSetZoneDoneEvent(self.setZonesReceived))
        self.setZonesReceived += 1

    
    def waitForDatabaseTimeout(self, extraTimeout = 0, requestName = 'unknown'):
        OTPClientRepository.notify.debug('waiting for database timeout %s at %s' % (requestName, globalClock.getFrameTime()))
        taskMgr.remove('waitingForDatabase')
        globalClock.tick()
        taskMgr.doMethodLater(OTPGlobals.DatabaseDialogTimeout + extraTimeout, self._OTPClientRepository__showWaitingForDatabase, 'waitingForDatabase', extraArgs = [
            requestName])

    
    def _OTPClientRepository__showWaitingForDatabase(self, requestName):
        OTPClientRepository.notify.info('timed out waiting for %s at %s' % (requestName, globalClock.getFrameTime()))
        dialogClass = OTPGlobals.getDialogClass()
        self.waitingForDatabase = dialogClass(text = OTPLocalizer.CRToontownUnavailable, dialogName = 'WaitingForDatabase', buttonTextList = [
            OTPLocalizer.CRToontownUnavailableCancel], style = OTPDialog.CancelOnly, command = self._OTPClientRepository__handleCancelWaiting)
        self.waitingForDatabase.show()
        taskMgr.remove('waitingForDatabase')
        taskMgr.doMethodLater(OTPGlobals.DatabaseGiveupTimeout, self._OTPClientRepository__giveUpWaitingForDatabase, 'waitingForDatabase', extraArgs = [
            requestName])
        return Task.done

    
    def _OTPClientRepository__giveUpWaitingForDatabase(self, requestName):
        OTPClientRepository.notify.info('giving up waiting for %s at %s' % (requestName, globalClock.getFrameTime()))
        self.cleanupWaitingForDatabase()
        self.loginFSM.request('noConnection')
        return Task.done

    
    def cleanupWaitingForDatabase(self):
        if self.waitingForDatabase != None:
            self.waitingForDatabase.hide()
            self.waitingForDatabase.cleanup()
            self.waitingForDatabase = None
        
        taskMgr.remove('waitingForDatabase')

    
    def _OTPClientRepository__handleCancelWaiting(self, value):
        self.loginFSM.request('shutdown')

    
    def setIsNotNewInstallation(self):
        if launcher:
            launcher.setIsNotNewInstallation()
        

    
    def renderFrame(self):
        base.graphicsEngine.renderFrame()

    
    def refreshAccountServerDate(self, forceRefresh = 0):
        
        try:
            self.accountServerDate.grabDate(force = forceRefresh)
        except TTAccount.TTAccountException:
            e = None
            self.notify.debug(str(e))
            return 1


    
    def resetPeriodTimer(self, secondsRemaining):
        self.periodTimerExpired = 0
        self.periodTimerSecondsRemaining = secondsRemaining

    
    def recordPeriodTimer(self, task):
        freq = 60.0
        elapsed = globalClock.getRealTime() - self.periodTimerStarted
        self.runningPeriodTimeRemaining = self.periodTimerSecondsRemaining - elapsed
        self.notify.debug('periodTimeRemaining: %s' % self.runningPeriodTimeRemaining)
        launcher.recordPeriodTimeRemaining(self.runningPeriodTimeRemaining)
        taskMgr.doMethodLater(freq, self.recordPeriodTimer, 'periodTimerRecorder')
        return Task.done

    
    def startPeriodTimer(self):
        if self.periodTimerStarted == None and self.periodTimerSecondsRemaining != None:
            self.periodTimerStarted = globalClock.getRealTime()
            taskMgr.doMethodLater(self.periodTimerSecondsRemaining, self._OTPClientRepository__periodTimerExpired, 'periodTimerCountdown')
            for warning in OTPGlobals.PeriodTimerWarningTime:
                if self.periodTimerSecondsRemaining > warning:
                    taskMgr.doMethodLater(self.periodTimerSecondsRemaining - warning, self._OTPClientRepository__periodTimerWarning, 'periodTimerCountdown')
                
            
            self.runningPeriodTimeRemaining = self.periodTimerSecondsRemaining
            self.recordPeriodTimer(None)
        

    
    def stopPeriodTimer(self):
        if self.periodTimerStarted != None:
            elapsed = globalClock.getRealTime() - self.periodTimerStarted
            self.periodTimerSecondsRemaining -= elapsed
            self.periodTimerStarted = None
        
        taskMgr.remove('periodTimerCountdown')
        taskMgr.remove('periodTimerRecorder')

    
    def _OTPClientRepository__periodTimerWarning(self, task):
        base.localAvatar.setSystemMessage(0, OTPLocalizer.PeriodTimerWarning)
        return Task.done

    
    def _OTPClientRepository__periodTimerExpired(self, task):
        self.notify.info("User's period timer has just expired!")
        self.stopPeriodTimer()
        self.periodTimerExpired = 1
        self.periodTimerStarted = None
        self.periodTimerSecondsRemaining = None
        messenger.send('periodTimerExpired')
        return Task.done


