# File: B (Python 2.2)

from pandac.PandaModules import *
from direct.actor import Actor
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPGlobals
import random
Props = ((5, 'feather', 'feather-mod', 'feather-chan'), (5, 'lips', 'lips'), (5, 'lipstick', 'lipstick'), (5, 'hat', 'hat'), (5, 'cane', 'cane'), (5, 'cubes', 'cubes-mod', 'cubes-chan'), (4, 'fishing-pole', 'fishing-pole-mod', 'fishing-pole-chan'), (5, '1dollar', '1dollar-bill-mod', '1dollar-bill-chan'), (5, 'big-magnet', 'magnet'), (5, 'hypno-goggles', 'hypnotize-mod', 'hypnotize-chan'), (5, 'banana', 'banana-peel-mod', 'banana-peel-chan'), (5, 'rake', 'rake-mod', 'rake-chan'), (5, 'marbles', 'marbles-mod', 'marbles-chan'), (5, 'tnt', 'tnt-mod', 'tnt-chan'), (5, 'trapdoor', 'trapdoor'), (5, 'quicksand', 'quicksand'), (5, 'megaphone', 'megaphone'), (3.5, 'creampie', 'tart'), (5, 'fruitpie-slice', 'fruit-pie-slice'), (5, 'creampie-slice', 'cream-pie-slice'), (5, 'birthday-cake', 'birthday-cake-mod', 'birthday-cake-chan'), (3.5, 'squirting-flower', 'squirting-flower'), (5, 'glass', 'glass-mod', 'glass-chan'), (5, 'water-gun', 'water-gun'), (3.5, 'bottle', 'bottle'), (5, 'firehose', 'firehose-mod', 'firehose-chan'), (5, 'hydrant', 'battle_hydrant'), (4, 'stormcloud', 'stormcloud-mod', 'stormcloud-chan'), (3.5, 'button', 'button'), (5, 'flowerpot', 'flowerpot-mod', 'flowerpot-chan'), (5, 'sandbag', 'sandbag-mod', 'sandbag-chan'), (4, 'anvil', 'anvil-mod', 'anvil-chan'), (5, 'weight', 'weight-mod', 'weight-chan'), (5, 'safe', 'safe-mod', 'safe-chan'), (5, 'piano', 'piano-mod', 'piano-chan'), (5, 'rake-react', 'rake-step-mod', 'rake-step-chan'), (5, 'pad', 'pad'), (5, 'propeller', 'propeller-mod', 'propeller-chan'), (5, 'calculator', 'calculator-mod', 'calculator-chan'), (5, 'rollodex', 'roll-o-dex'), (5, 'rubber-stamp', 'rubber-stamp'), (5, 'rubber-stamp-pad', 'rubber-stamp-pad-mod', 'rubber-stamp-pad-chan'), (5, 'smile', 'smile-mod', 'smile-chan'), (5, 'golf-club', 'golf-club'), (5, 'golf-ball', 'golf-ball'), (5, 'redtape', 'redtape'), (5, 'redtape-tube', 'redtape-tube'), (5, 'bounced-check', 'bounced-check'), (5, 'calculator', 'calculator-mod', 'calculator-chan'), (3.5, 'clip-on-tie', 'clip-on-tie-mod', 'clip-on-tie-chan'), (5, 'pen', 'pen'), (5, 'pencil', 'pencil'), (3.5, 'phone', 'phone'), (3.5, 'receiver', 'receiver'), (5, 'sharpener', 'sharpener'), (3.5, 'shredder', 'shredder'), (3.5, 'shredder-paper', 'shredder-paper-mod', 'shredder-paper-chan'), (5, 'watercooler', 'watercooler'), (5, 'dagger', 'dagger'), (5, 'card', 'card'), (5, 'baseball', 'baseball'), (5, 'bird', 'bird'), (5, 'can', 'can'), (5, 'cigar', 'cigar'), (5, 'evil-eye', 'evil-eye'), (5, 'gavel', 'gavel'), (5, 'half-windsor', 'half-windsor'), (5, 'lawbook', 'lawbook'), (5, 'newspaper', 'newspaper'), (5, 'pink-slip', 'pink-slip'), (5, 'teeth', 'teeth-mod', 'teeth-chan'), (5, 'power-tie', 'power-tie'), (3.5, 'spray', 'spray'), (3.5, 'splash', 'splash'), (3.5, 'splat', 'splat-mod', 'splat-chan'), (3.5, 'stun', 'stun-mod', 'stun-chan'), (3.5, 'glow', 'glow'), (3.5, 'suit_explosion', 'suit_explosion-mod', 'suit_explosion-chan'), (3.5, 'suit_explosion_dust', 'dust_cloud'), (4, 'ripples', 'ripples'), (4, 'wake', 'wake'), (4, 'splashdown', 'SZ_splashdown-mod', 'SZ_splashdown-chan'))
CreampieColor = VBase4(250.0 / 255.0, 241.0 / 255.0, 24.0 / 255.0, 1.0)
FruitpieColor = VBase4(55.0 / 255.0, 40.0 / 255.0, 148.0 / 255.0, 1.0)
BirthdayCakeColor = VBase4(253.0 / 255.0, 119.0 / 255.0, 220.0 / 255.0, 1.0)
Splats = {
    'tart': (0.29999999999999999, FruitpieColor),
    'fruitpie-slice': (0.5, FruitpieColor),
    'creampie-slice': (0.5, CreampieColor),
    'fruitpie': (0.69999999999999996, FruitpieColor),
    'creampie': (0.69999999999999996, CreampieColor),
    'birthday-cake': (0.90000000000000002, BirthdayCakeColor) }
Variants = ('tart', 'fruitpie', 'splat-tart', 'dust', 'kapow', 'double-windsor', 'splat-fruitpie-slice', 'splat-creampie-slice', 'splat-fruitpie', 'splat-creampie', 'splat-birthday-cake', 'splash-from-splat', 'clip-on-tie', 'lips', 'small-magnet', '5dollar', '10dollar', 'suit_explosion', 'quicksand', 'trapdoor')

class PropPool:
    notify = DirectNotifyGlobal.directNotify.newCategory('PropPool')
    
    def __init__(self):
        self.props = { }
        self.propCache = []
        self.propStrings = { }
        self.propTypes = { }
        self.maxPoolSize = base.config.GetInt('prop-pool-size', 8)
        for p in Props:
            phase = p[0]
            propName = p[1]
            modelName = p[2]
            if len(p) == 4:
                animName = p[3]
                propPath = self.getPath(phase, modelName)
                animPath = self.getPath(phase, animName)
                self.propTypes[propName] = 'actor'
                self.propStrings[propName] = (propPath, animPath)
            else:
                propPath = self.getPath(phase, modelName)
                self.propTypes[propName] = 'model'
                self.propStrings[propName] = (propPath,)
        
        propName = 'tart'
        self.propStrings[propName] = (self.getPath(3.5, 'tart'),)
        self.propTypes[propName] = 'model'
        propName = 'fruitpie'
        self.propStrings[propName] = (self.getPath(3.5, 'tart'),)
        self.propTypes[propName] = 'model'
        propName = 'double-windsor'
        self.propStrings[propName] = (self.getPath(5, 'half-windsor'),)
        self.propTypes[propName] = 'model'
        splatAnimFileName = self.getPath(3.5, 'splat-chan')
        for splat in Splats.keys():
            propName = 'splat-' + splat
            self.propStrings[propName] = (self.getPath(3.5, 'splat-mod'), splatAnimFileName)
            self.propTypes[propName] = 'actor'
        
        propName = 'splash-from-splat'
        self.propStrings[propName] = (self.getPath(3.5, 'splat-mod'), splatAnimFileName)
        self.propTypes[propName] = 'actor'
        propName = 'small-magnet'
        self.propStrings[propName] = (self.getPath(5, 'magnet'),)
        self.propTypes[propName] = 'model'
        propName = '5dollar'
        self.propStrings[propName] = (self.getPath(5, '1dollar-bill-mod'), self.getPath(5, '1dollar-bill-chan'))
        self.propTypes[propName] = 'actor'
        propName = '10dollar'
        self.propStrings[propName] = (self.getPath(5, '1dollar-bill-mod'), self.getPath(5, '1dollar-bill-chan'))
        self.propTypes[propName] = 'actor'
        propName = 'dust'
        self.propStrings[propName] = (self.getPath(5, 'dust-mod'), self.getPath(5, 'dust-chan'))
        self.propTypes[propName] = 'actor'
        propName = 'kapow'
        self.propStrings[propName] = (self.getPath(5, 'kapow-mod'), self.getPath(5, 'kapow-chan'))
        self.propTypes[propName] = 'actor'

    
    def getPath(self, phase, model):
        return 'phase_%s/models/props/%s' % (phase, model)

    
    def makeVariant(self, name):
        if name == 'tart':
            self.props[name].setScale(0.5)
        elif name == 'fruitpie':
            self.props[name].setScale(0.75)
        elif name == 'double-windsor':
            self.props[name].setScale(1.5)
        elif name[:6] == 'splat-':
            prop = self.props[name]
            scale = prop.getScale() * Splats[name[6:]][0]
            prop.setScale(scale)
            prop.setColor(Splats[name[6:]][1])
        elif name == 'splash-from-splat':
            self.props[name].setColor(0.75, 0.75, 1.0, 1.0)
        elif name == 'clip-on-tie':
            tie = self.props[name]
            tie.getChild(0).setHpr(23.859999999999999, -16.030000000000001, 9.1799999999999997)
        elif name == 'small-magnet':
            self.props[name].setScale(0.5)
        elif name == 'shredder-paper':
            paper = self.props[name]
            paper.setPosHpr(2.2200000000000002, -0.94999999999999996, 1.1599999999999999, -48.609999999999999, 26.57, -111.51000000000001)
            paper.flattenMedium()
        elif name == 'lips':
            lips = self.props[name]
            lips.setPos(0, 0, -3.04)
            lips.flattenMedium()
        elif name == '5dollar':
            tex = loader.loadTexture('phase_5/maps/dollar_5.jpg')
            tex.setMinfilter(Texture.FTLinearMipmapLinear)
            tex.setMagfilter(Texture.FTLinear)
            self.props[name].setTexture(tex, 1)
        elif name == '10dollar':
            tex = loader.loadTexture('phase_5/maps/dollar_10.jpg')
            tex.setMinfilter(Texture.FTLinearMipmapLinear)
            tex.setMagfilter(Texture.FTLinear)
            self.props[name].setTexture(tex, 1)
        elif name == 'dust':
            bin = 110
            for cloudNum in range(1, 12):
                cloudName = '**/cloud' + str(cloudNum)
                cloud = self.props[name].find(cloudName)
                cloud.setBin('fixed', bin)
                bin -= 10
            
        elif name == 'kapow':
            l = self.props[name].find('**/letters')
            l.setBin('fixed', 20)
            e = self.props[name].find('**/explosion')
            e.setBin('fixed', 10)
        elif name == 'suit_explosion':
            print 'making suit exp variant'
            joints = [
                '**/joint-scale-POW',
                '**/joint-scale-BLAM',
                '**/joint-scale-BOOM']
            joint = random.choice(joints)
            self.props[name].find(joint).hide()
            joints.remove(joint)
            joint = random.choice(joints)
            self.props[name].find(joint).hide()
        elif name == 'quicksand' or name == 'trapdoor':
            p = self.props[name]
            p.setBin('shadow', -5)
            p.setDepthWrite(0)
            p.getChild(0).setPos(0, 0, OTPGlobals.FloorOffset)
        

    
    def unloadProps(self):
        for p in self.props.values():
            if type(p) != type(()):
                self._PropPool__delProp(p)
            
        
        self.props = { }
        self.propCache = []

    
    def getProp(self, name):
        return self._PropPool__getPropCopy(name)

    
    def _PropPool__getPropCopy(self, name):
        if self.propTypes[name] == 'actor':
            if not self.props.has_key(name):
                prop = Actor.Actor()
                prop.loadModel(self.propStrings[name][0])
                animDict = { }
                animDict[name] = self.propStrings[name][1]
                prop.loadAnims(animDict)
                prop.name = name
                self.storeProp(name, prop)
                if name in Variants:
                    self.makeVariant(name)
                
            
            return Actor.Actor(other = self.props[name])
        elif not self.props.has_key(name):
            prop = loader.loadModel(self.propStrings[name][0])
            prop.name = name
            self.storeProp(name, prop)
            if name in Variants:
                self.makeVariant(name)
            
        
        return self.props[name].copyTo(hidden)

    
    def storeProp(self, name, prop):
        self.props[name] = prop
        self.propCache.append(prop)
        if len(self.props) > self.maxPoolSize:
            oldest = self.propCache.pop(0)
            del self.props[oldest.name]
            self._PropPool__delProp(oldest)
        
        self.notify.debug('props = %s' % self.props)
        self.notify.debug('propCache = %s' % self.propCache)

    
    def getPropType(self, name):
        return self.propTypes[name]

    
    def _PropPool__delProp(self, prop):
        if prop == None:
            self.notify.warning('tried to delete null prop!')
            return None
        
        if isinstance(prop, Actor.Actor):
            prop.cleanup()
        else:
            prop.removeNode()


globalPropPool = PropPool()
