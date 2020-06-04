# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\actor\Actor.py
__all__ = [
 'Actor']
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import LODNode
import types, copy

class Actor(DirectObject, NodePath):
    __module__ = __name__
    notify = directNotify.newCategory('Actor')
    partPrefix = '__Actor_'
    modelLoaderOptions = LoaderOptions(LoaderOptions.LFSearch | LoaderOptions.LFReportErrors | LoaderOptions.LFConvertSkeleton)
    animLoaderOptions = LoaderOptions(LoaderOptions.LFSearch | LoaderOptions.LFReportErrors | LoaderOptions.LFConvertAnim)
    validateSubparts = ConfigVariableBool('validate-subparts', True)

    class PartDef:
        __module__ = __name__

        def __init__(self, partBundleNP, partBundleHandle, partModel):
            self.partBundleNP = partBundleNP
            self.partBundleHandle = partBundleHandle
            self.partModel = partModel

        def getBundle(self):
            return self.partBundleHandle.getBundle()

        def __repr__(self):
            return 'Actor.PartDef(%s, %s)' % (repr(self.partBundleNP), repr(self.partModel))

    class AnimDef:
        __module__ = __name__

        def __init__(self, filename=None, animBundle=None):
            self.filename = filename
            self.animBundle = None
            self.animControl = None
            return

        def makeCopy(self):
            return Actor.AnimDef(self.filename, self.animBundle)

        def __repr__(self):
            return 'Actor.AnimDef(%s)' % repr(self.filename)

    class SubpartDef:
        __module__ = __name__

        def __init__(self, truePartName, subset=PartSubset()):
            self.truePartName = truePartName
            self.subset = subset

        def makeCopy(self):
            return Actor.SubpartDef(self.truePartName, PartSubset(self.subset))

        def __repr__(self):
            return 'Actor.SubpartDef(%s, %s)' % (repr(self.truePartName), repr(self.subset))

    def __init__--- This code section failed: ---

 L. 152         0  SETUP_EXCEPT         15  'to 18'

 L. 153         3  LOAD_FAST             0  'self'
                6  LOAD_ATTR             1  'Actor_initialized'
                9  POP_TOP          

 L. 154        10  LOAD_CONST               None
               13  RETURN_VALUE     
               14  POP_BLOCK        
               15  JUMP_FORWARD         16  'to 34'
             18_0  COME_FROM             0  '0'

 L. 155        18  POP_TOP          
               19  POP_TOP          
               20  POP_TOP          

 L. 156        21  LOAD_CONST               1
               24  LOAD_FAST             0  'self'
               27  STORE_ATTR            1  'Actor_initialized'
               30  JUMP_FORWARD          1  'to 34'
               33  END_FINALLY      
             34_0  COME_FROM            30  '30'
             34_1  COME_FROM            15  '15'

 L. 159        34  LOAD_GLOBAL           2  'NodePath'
               37  LOAD_ATTR             3  '__init__'
               40  LOAD_FAST             0  'self'
               43  CALL_FUNCTION_1       1  None
               46  POP_TOP          

 L. 173        47  LOAD_FAST             8  'mergeLODBundles'
               50  LOAD_CONST               None
               53  COMPARE_OP            2  ==
               56  JUMP_IF_FALSE        28  'to 87'
               59  POP_TOP          

 L. 176        60  LOAD_GLOBAL           6  'base'
               63  LOAD_ATTR             7  'config'
               66  LOAD_ATTR             8  'GetBool'
               69  LOAD_CONST               'merge-lod-bundles'
               72  LOAD_GLOBAL           9  'True'
               75  CALL_FUNCTION_2       2  None
               78  LOAD_FAST             0  'self'
               81  STORE_ATTR            4  'mergeLODBundles'
               84  JUMP_FORWARD         10  'to 97'
             87_0  COME_FROM            56  '56'
               87  POP_TOP          

 L. 178        88  LOAD_FAST             8  'mergeLODBundles'
               91  LOAD_FAST             0  'self'
               94  STORE_ATTR            4  'mergeLODBundles'
             97_0  COME_FROM            84  '84'

 L. 184        97  LOAD_FAST             9  'allowAsyncBind'
              100  LOAD_CONST               None
              103  COMPARE_OP            2  ==
              106  JUMP_IF_FALSE        28  'to 137'
              109  POP_TOP          

 L. 185       110  LOAD_GLOBAL           6  'base'
              113  LOAD_ATTR             7  'config'
              116  LOAD_ATTR             8  'GetBool'
              119  LOAD_CONST               'allow-async-bind'
              122  LOAD_GLOBAL           9  'True'
              125  CALL_FUNCTION_2       2  None
              128  LOAD_FAST             0  'self'
              131  STORE_ATTR           10  'allowAsyncBind'
              134  JUMP_FORWARD         10  'to 147'
            137_0  COME_FROM           106  '106'
              137  POP_TOP          

 L. 187       138  LOAD_FAST             9  'allowAsyncBind'
              141  LOAD_FAST             0  'self'
              144  STORE_ATTR           10  'allowAsyncBind'
            147_0  COME_FROM           134  '134'

 L. 190       147  BUILD_MAP             0 
              150  LOAD_FAST             0  'self'
              153  STORE_ATTR           11  '__commonBundleHandles'

 L. 191       156  BUILD_MAP             0 
              159  LOAD_FAST             0  'self'
              162  STORE_ATTR           12  '__partBundleDict'

 L. 192       165  BUILD_MAP             0 
              168  LOAD_FAST             0  'self'
              171  STORE_ATTR           13  '__subpartDict'

 L. 193       174  BUILD_LIST_0          0 
              177  LOAD_FAST             0  'self'
              180  STORE_ATTR           14  '__sortedLODNames'

 L. 194       183  BUILD_MAP             0 
              186  LOAD_FAST             0  'self'
              189  STORE_ATTR           15  '__animControlDict'

 L. 196       192  LOAD_GLOBAL          16  'False'
              195  LOAD_FAST             0  'self'
              198  STORE_ATTR           17  '__subpartsComplete'

 L. 198       201  LOAD_CONST               None
              204  LOAD_FAST             0  'self'
              207  STORE_ATTR           18  '__LODNode'

 L. 199       210  LOAD_CONST               None
              213  LOAD_FAST             0  'self'
              216  STORE_ATTR           19  '__LODAnimation'

 L. 200       219  LOAD_GLOBAL          20  'Point3'
              222  LOAD_CONST               0
              225  LOAD_CONST               0
              228  LOAD_CONST               0
              231  CALL_FUNCTION_3       3  None
              234  LOAD_FAST             0  'self'
              237  STORE_ATTR           21  '__LODCenter'

 L. 201       240  LOAD_CONST               None
              243  LOAD_FAST             0  'self'
              246  STORE_ATTR           22  'switches'

 L. 203       249  LOAD_FAST             3  'other'
              252  LOAD_CONST               None
              255  COMPARE_OP            2  ==
              258  JUMP_IF_FALSE       987  'to 1248'
              261  POP_TOP          

 L. 207       262  LOAD_CONST               0
              265  LOAD_FAST             0  'self'
              268  STORE_ATTR           24  'gotName'

 L. 209       271  LOAD_FAST             6  'flattenable'
              274  JUMP_IF_FALSE        54  'to 331'
              277  POP_TOP          

 L. 213       278  LOAD_GLOBAL          26  'PandaNode'
              281  LOAD_CONST               'actor'
              284  CALL_FUNCTION_1       1  None
              287  STORE_FAST           15  'root'

 L. 214       290  LOAD_FAST             0  'self'
              293  LOAD_ATTR            28  'assign'
              296  LOAD_GLOBAL           2  'NodePath'
              299  LOAD_FAST            15  'root'
              302  CALL_FUNCTION_1       1  None
              305  CALL_FUNCTION_1       1  None
              308  POP_TOP          

 L. 215       309  LOAD_FAST             0  'self'
              312  LOAD_ATTR            29  'setGeomNode'
              315  LOAD_GLOBAL           2  'NodePath'
              318  LOAD_FAST             0  'self'
              321  CALL_FUNCTION_1       1  None
              324  CALL_FUNCTION_1       1  None
              327  POP_TOP          
              328  JUMP_FORWARD         73  'to 404'
            331_0  COME_FROM           274  '274'
              331  POP_TOP          

 L. 220       332  LOAD_GLOBAL          30  'ModelNode'
              335  LOAD_CONST               'actor'
              338  CALL_FUNCTION_1       1  None
              341  STORE_FAST           15  'root'

 L. 221       344  LOAD_FAST            15  'root'
              347  LOAD_ATTR            31  'setPreserveTransform'
              350  LOAD_CONST               1
              353  CALL_FUNCTION_1       1  None
              356  POP_TOP          

 L. 222       357  LOAD_FAST             0  'self'
              360  LOAD_ATTR            28  'assign'
              363  LOAD_GLOBAL           2  'NodePath'
              366  LOAD_FAST            15  'root'
              369  CALL_FUNCTION_1       1  None
              372  CALL_FUNCTION_1       1  None
              375  POP_TOP          

 L. 223       376  LOAD_FAST             0  'self'
              379  LOAD_ATTR            29  'setGeomNode'
              382  LOAD_FAST             0  'self'
              385  LOAD_ATTR            32  'attachNewNode'
              388  LOAD_GLOBAL          30  'ModelNode'
              391  LOAD_CONST               'actorGeom'
              394  CALL_FUNCTION_1       1  None
              397  CALL_FUNCTION_1       1  None
              400  CALL_FUNCTION_1       1  None
              403  POP_TOP          
            404_0  COME_FROM           328  '328'

 L. 225       404  LOAD_CONST               0
              407  LOAD_FAST             0  'self'
              410  STORE_ATTR           33  '__hasLOD'

 L. 237       413  LOAD_FAST             1  'models'
              416  JUMP_IF_FALSE       448  'to 867'
              419  POP_TOP          

 L. 239       420  LOAD_GLOBAL          35  'type'
              423  LOAD_FAST             1  'models'
              426  CALL_FUNCTION_1       1  None
              429  LOAD_GLOBAL          35  'type'
              432  BUILD_MAP             0 
              435  CALL_FUNCTION_1       1  None
              438  COMPARE_OP            2  ==
              441  JUMP_IF_FALSE       394  'to 838'
              444  POP_TOP          

 L. 241       445  LOAD_GLOBAL          35  'type'
              448  LOAD_FAST             1  'models'
              451  LOAD_FAST             1  'models'
              454  LOAD_ATTR            36  'keys'
              457  CALL_FUNCTION_0       0  None
              460  LOAD_CONST               0
              463  BINARY_SUBSCR    
              464  BINARY_SUBSCR    
              465  CALL_FUNCTION_1       1  None
              468  LOAD_GLOBAL          35  'type'
              471  BUILD_MAP             0 
              474  CALL_FUNCTION_1       1  None
              477  COMPARE_OP            2  ==
              480  JUMP_IF_FALSE       144  'to 627'
              483  POP_TOP          

 L. 243       484  LOAD_FAST             0  'self'
              487  LOAD_ATTR            37  'setLODNode'
              490  LOAD_CONST               'node'
              493  LOAD_FAST             5  'lodNode'
              496  CALL_FUNCTION_256   256  None
              499  POP_TOP          

 L. 246       500  LOAD_FAST             1  'models'
              503  LOAD_ATTR            36  'keys'
              506  CALL_FUNCTION_0       0  None
              509  STORE_FAST           11  'sortedKeys'

 L. 247       512  LOAD_FAST            11  'sortedKeys'
              515  LOAD_ATTR            40  'sort'
              518  CALL_FUNCTION_0       0  None
              521  POP_TOP          

 L. 248       522  SETUP_LOOP          310  'to 835'
              525  LOAD_FAST            11  'sortedKeys'
              528  GET_ITER         
              529  FOR_ITER             91  'to 623'
              532  STORE_FAST           12  'lodName'

 L. 251       535  LOAD_FAST             0  'self'
              538  LOAD_ATTR            42  'addLOD'
              541  LOAD_GLOBAL          43  'str'
              544  LOAD_FAST            12  'lodName'
              547  CALL_FUNCTION_1       1  None
              550  CALL_FUNCTION_1       1  None
              553  POP_TOP          

 L. 253       554  SETUP_LOOP           63  'to 620'
              557  LOAD_FAST             1  'models'
              560  LOAD_FAST            12  'lodName'
              563  BINARY_SUBSCR    
              564  LOAD_ATTR            36  'keys'
              567  CALL_FUNCTION_0       0  None
              570  GET_ITER         
              571  FOR_ITER             45  'to 619'
              574  STORE_FAST           13  'modelName'

 L. 254       577  LOAD_FAST             0  'self'
              580  LOAD_ATTR            45  'loadModel'
              583  LOAD_FAST             1  'models'
              586  LOAD_FAST            12  'lodName'
              589  BINARY_SUBSCR    
              590  LOAD_FAST            13  'modelName'
              593  BINARY_SUBSCR    

 L. 255       594  LOAD_FAST            13  'modelName'
              597  LOAD_FAST            12  'lodName'
              600  LOAD_CONST               'copy'
              603  LOAD_FAST             4  'copy'

 L. 256       606  LOAD_CONST               'okMissing'
              609  LOAD_FAST            10  'okMissing'
              612  CALL_FUNCTION_515   515  None
              615  POP_TOP          
              616  JUMP_BACK           571  'to 571'
              619  POP_BLOCK        
            620_0  COME_FROM           554  '554'
              620  JUMP_BACK           529  'to 529'
              623  POP_BLOCK        
              624  JUMP_ABSOLUTE       864  'to 864'
            627_0  COME_FROM           480  '480'
              627  POP_TOP          

 L. 258       628  LOAD_GLOBAL          35  'type'
              631  LOAD_FAST             2  'anims'
              634  LOAD_FAST             2  'anims'
              637  LOAD_ATTR            36  'keys'
              640  CALL_FUNCTION_0       0  None
              643  LOAD_CONST               0
              646  BINARY_SUBSCR    
              647  BINARY_SUBSCR    
              648  CALL_FUNCTION_1       1  None
              651  LOAD_GLOBAL          35  'type'
              654  BUILD_MAP             0 
              657  CALL_FUNCTION_1       1  None
              660  COMPARE_OP            2  ==
              663  JUMP_IF_FALSE        59  'to 725'
              666  POP_TOP          

 L. 260       667  SETUP_LOOP          165  'to 835'
              670  LOAD_FAST             1  'models'
              673  LOAD_ATTR            36  'keys'
              676  CALL_FUNCTION_0       0  None
              679  GET_ITER         
              680  FOR_ITER             38  'to 721'
              683  STORE_FAST           14  'partName'

 L. 262       686  LOAD_FAST             0  'self'
              689  LOAD_ATTR            45  'loadModel'
              692  LOAD_FAST             1  'models'
              695  LOAD_FAST            14  'partName'
              698  BINARY_SUBSCR    
              699  LOAD_FAST            14  'partName'

 L. 263       702  LOAD_CONST               'copy'
              705  LOAD_FAST             4  'copy'
              708  LOAD_CONST               'okMissing'
              711  LOAD_FAST            10  'okMissing'
              714  CALL_FUNCTION_514   514  None
              717  POP_TOP          
              718  JUMP_BACK           680  'to 680'
              721  POP_BLOCK        
              722  JUMP_ABSOLUTE       864  'to 864'
            725_0  COME_FROM           663  '663'
              725  POP_TOP          

 L. 266       726  LOAD_FAST             0  'self'
              729  LOAD_ATTR            37  'setLODNode'
              732  LOAD_CONST               'node'
              735  LOAD_FAST             5  'lodNode'
              738  CALL_FUNCTION_256   256  None
              741  POP_TOP          

 L. 268       742  LOAD_FAST             1  'models'
              745  LOAD_ATTR            36  'keys'
              748  CALL_FUNCTION_0       0  None
              751  STORE_FAST           11  'sortedKeys'

 L. 269       754  LOAD_FAST            11  'sortedKeys'
              757  LOAD_ATTR            40  'sort'
              760  CALL_FUNCTION_0       0  None
              763  POP_TOP          

 L. 270       764  SETUP_LOOP           97  'to 864'
              767  LOAD_FAST            11  'sortedKeys'
              770  GET_ITER         
              771  FOR_ITER             60  'to 834'
              774  STORE_FAST           12  'lodName'

 L. 271       777  LOAD_FAST             0  'self'
              780  LOAD_ATTR            42  'addLOD'
              783  LOAD_GLOBAL          43  'str'
              786  LOAD_FAST            12  'lodName'
              789  CALL_FUNCTION_1       1  None
              792  CALL_FUNCTION_1       1  None
              795  POP_TOP          

 L. 273       796  LOAD_FAST             0  'self'
              799  LOAD_ATTR            45  'loadModel'
              802  LOAD_FAST             1  'models'
              805  LOAD_FAST            12  'lodName'
              808  BINARY_SUBSCR    
              809  LOAD_CONST               'lodName'
              812  LOAD_FAST            12  'lodName'

 L. 274       815  LOAD_CONST               'copy'
              818  LOAD_FAST             4  'copy'
              821  LOAD_CONST               'okMissing'
              824  LOAD_FAST            10  'okMissing'
              827  CALL_FUNCTION_769   769  None
              830  POP_TOP          
              831  JUMP_BACK           771  'to 771'
              834  POP_BLOCK        
            835_0  COME_FROM           667  '667'
            835_1  COME_FROM           522  '522'
              835  JUMP_ABSOLUTE       868  'to 868'
            838_0  COME_FROM           441  '441'
              838  POP_TOP          

 L. 277       839  LOAD_FAST             0  'self'
              842  LOAD_ATTR            45  'loadModel'
              845  LOAD_FAST             1  'models'
              848  LOAD_CONST               'copy'
              851  LOAD_FAST             4  'copy'
              854  LOAD_CONST               'okMissing'
              857  LOAD_FAST            10  'okMissing'
              860  CALL_FUNCTION_513   513  None
              863  POP_TOP          
              864  JUMP_FORWARD          1  'to 868'
            867_0  COME_FROM           416  '416'
              867  POP_TOP          
            868_0  COME_FROM           864  '864'

 L. 281       868  LOAD_FAST             2  'anims'
              871  JUMP_IF_FALSE       370  'to 1244'
              874  POP_TOP          

 L. 282       875  LOAD_GLOBAL          50  'len'
              878  LOAD_FAST             2  'anims'
              881  CALL_FUNCTION_1       1  None
              884  LOAD_CONST               1
              887  COMPARE_OP            5  >=
              890  JUMP_IF_FALSE       347  'to 1240'
              893  POP_TOP          

 L. 284       894  LOAD_GLOBAL          35  'type'
              897  LOAD_FAST             2  'anims'
              900  LOAD_FAST             2  'anims'
              903  LOAD_ATTR            36  'keys'
              906  CALL_FUNCTION_0       0  None
              909  LOAD_CONST               0
              912  BINARY_SUBSCR    
              913  BINARY_SUBSCR    
              914  CALL_FUNCTION_1       1  None
              917  LOAD_GLOBAL          35  'type'
              920  BUILD_MAP             0 
              923  CALL_FUNCTION_1       1  None
              926  COMPARE_OP            2  ==
              929  JUMP_IF_FALSE       204  'to 1136'
              932  POP_TOP          

 L. 286       933  LOAD_GLOBAL          35  'type'
              936  LOAD_FAST             1  'models'
              939  CALL_FUNCTION_1       1  None
              942  LOAD_GLOBAL          35  'type'
              945  BUILD_MAP             0 
              948  CALL_FUNCTION_1       1  None
              951  COMPARE_OP            2  ==
              954  JUMP_IF_FALSE       175  'to 1132'
              957  POP_TOP          

 L. 287       958  LOAD_GLOBAL          35  'type'
              961  LOAD_FAST             1  'models'
              964  LOAD_FAST             1  'models'
              967  LOAD_ATTR            36  'keys'
              970  CALL_FUNCTION_0       0  None
              973  LOAD_CONST               0
              976  BINARY_SUBSCR    
              977  BINARY_SUBSCR    
              978  CALL_FUNCTION_1       1  None
              981  LOAD_GLOBAL          35  'type'
              984  BUILD_MAP             0 
              987  CALL_FUNCTION_1       1  None
              990  COMPARE_OP            2  ==
              993  JUMP_IF_FALSE        89  'to 1085'
              996  POP_TOP          

 L. 289       997  LOAD_FAST             1  'models'
             1000  LOAD_ATTR            36  'keys'
             1003  CALL_FUNCTION_0       0  None
             1006  STORE_FAST           11  'sortedKeys'

 L. 290      1009  LOAD_FAST            11  'sortedKeys'
             1012  LOAD_ATTR            40  'sort'
             1015  CALL_FUNCTION_0       0  None
             1018  POP_TOP          

 L. 291      1019  SETUP_LOOP          107  'to 1129'
             1022  LOAD_FAST            11  'sortedKeys'
             1025  GET_ITER         
             1026  FOR_ITER             52  'to 1081'
             1029  STORE_FAST           12  'lodName'

 L. 293      1032  SETUP_LOOP           43  'to 1078'
             1035  LOAD_FAST             2  'anims'
             1038  LOAD_ATTR            36  'keys'
             1041  CALL_FUNCTION_0       0  None
             1044  GET_ITER         
             1045  FOR_ITER             29  'to 1077'
             1048  STORE_FAST           14  'partName'

 L. 294      1051  LOAD_FAST             0  'self'
             1054  LOAD_ATTR            51  'loadAnims'
             1057  LOAD_FAST             2  'anims'
             1060  LOAD_FAST            14  'partName'
             1063  BINARY_SUBSCR    
             1064  LOAD_FAST            14  'partName'
             1067  LOAD_FAST            12  'lodName'
             1070  CALL_FUNCTION_3       3  None
             1073  POP_TOP          
             1074  JUMP_BACK          1045  'to 1045'
             1077  POP_BLOCK        
           1078_0  COME_FROM          1032  '1032'
             1078  JUMP_BACK          1026  'to 1026'
             1081  POP_BLOCK        
             1082  JUMP_ABSOLUTE      1133  'to 1133'
           1085_0  COME_FROM           993  '993'
             1085  POP_TOP          

 L. 298      1086  SETUP_LOOP           44  'to 1133'
             1089  LOAD_FAST             2  'anims'
             1092  LOAD_ATTR            36  'keys'
             1095  CALL_FUNCTION_0       0  None
             1098  GET_ITER         
             1099  FOR_ITER             26  'to 1128'
             1102  STORE_FAST           14  'partName'

 L. 299      1105  LOAD_FAST             0  'self'
             1108  LOAD_ATTR            51  'loadAnims'
             1111  LOAD_FAST             2  'anims'
             1114  LOAD_FAST            14  'partName'
             1117  BINARY_SUBSCR    
             1118  LOAD_FAST            14  'partName'
             1121  CALL_FUNCTION_2       2  None
             1124  POP_TOP          
             1125  JUMP_BACK          1099  'to 1099'
             1128  POP_BLOCK        
           1129_0  COME_FROM          1019  '1019'
             1129  JUMP_ABSOLUTE      1237  'to 1237'
           1132_0  COME_FROM           954  '954'
             1132  POP_TOP          
           1133_0  COME_FROM          1086  '1086'
             1133  JUMP_ABSOLUTE      1241  'to 1241'
           1136_0  COME_FROM           929  '929'
             1136  POP_TOP          

 L. 300      1137  LOAD_GLOBAL          35  'type'
             1140  LOAD_FAST             1  'models'
             1143  CALL_FUNCTION_1       1  None
             1146  LOAD_GLOBAL          35  'type'
             1149  BUILD_MAP             0 
             1152  CALL_FUNCTION_1       1  None
             1155  COMPARE_OP            2  ==
             1158  JUMP_IF_FALSE        62  'to 1223'
             1161  POP_TOP          

 L. 302      1162  LOAD_FAST             1  'models'
             1165  LOAD_ATTR            36  'keys'
             1168  CALL_FUNCTION_0       0  None
             1171  STORE_FAST           11  'sortedKeys'

 L. 303      1174  LOAD_FAST            11  'sortedKeys'
             1177  LOAD_ATTR            40  'sort'
             1180  CALL_FUNCTION_0       0  None
             1183  POP_TOP          

 L. 304      1184  SETUP_LOOP           50  'to 1237'
             1187  LOAD_FAST            11  'sortedKeys'
             1190  GET_ITER         
             1191  FOR_ITER             25  'to 1219'
             1194  STORE_FAST           12  'lodName'

 L. 305      1197  LOAD_FAST             0  'self'
             1200  LOAD_ATTR            51  'loadAnims'
             1203  LOAD_FAST             2  'anims'
             1206  LOAD_CONST               'lodName'
             1209  LOAD_FAST            12  'lodName'
             1212  CALL_FUNCTION_257   257  None
             1215  POP_TOP          
             1216  JUMP_BACK          1191  'to 1191'
             1219  POP_BLOCK        
             1220  JUMP_ABSOLUTE      1241  'to 1241'
           1223_0  COME_FROM          1158  '1158'
             1223  POP_TOP          

 L. 308      1224  LOAD_FAST             0  'self'
             1227  LOAD_ATTR            51  'loadAnims'
             1230  LOAD_FAST             2  'anims'
             1233  CALL_FUNCTION_1       1  None
             1236  POP_TOP          
           1237_0  COME_FROM          1184  '1184'
             1237  JUMP_ABSOLUTE      1245  'to 1245'
           1240_0  COME_FROM           890  '890'
             1240  POP_TOP          
             1241  JUMP_ABSOLUTE      1265  'to 1265'
           1244_0  COME_FROM           871  '871'
             1244  POP_TOP          
             1245  JUMP_FORWARD         17  'to 1265'
           1248_0  COME_FROM           258  '258'
             1248  POP_TOP          

 L. 311      1249  LOAD_FAST             0  'self'
             1252  LOAD_ATTR            52  'copyActor'
             1255  LOAD_FAST             3  'other'
             1258  LOAD_GLOBAL           9  'True'
             1261  CALL_FUNCTION_2       2  None
             1264  POP_TOP          
           1265_0  COME_FROM          1245  '1245'

 L. 313      1265  LOAD_FAST             7  'setFinal'
             1268  JUMP_IF_FALSE        26  'to 1297'
           1271_0  THEN                     1298
             1271  POP_TOP          

 L. 328      1272  LOAD_FAST             0  'self'
             1275  LOAD_ATTR            54  '__geomNode'
             1278  LOAD_ATTR            55  'node'
             1281  CALL_FUNCTION_0       0  None
             1284  LOAD_ATTR            53  'setFinal'
             1287  LOAD_CONST               1
             1290  CALL_FUNCTION_1       1  None
             1293  POP_TOP          
             1294  JUMP_FORWARD          1  'to 1298'
           1297_0  COME_FROM          1268  '1268'
             1297  POP_TOP          
           1298_0  COME_FROM          1294  '1294'
             1298  LOAD_CONST               None
             1301  RETURN_VALUE     

Parse error at or near `JUMP_ABSOLUTE' instruction at offset 1237

    def delete(self):
        try:
            self.Actor_deleted
            return
        except:
            self.Actor_deleted = 1
            self.cleanup()

    def copyActor(self, other, overwrite=False):
        self.gotName = other.gotName
        if overwrite:
            otherCopy = other.copyTo(NodePath())
            otherCopy.detachNode()
            self.assign(otherCopy)
        else:
            otherCopy = other.copyTo(self)
        if other.getGeomNode().getName() == other.getName():
            self.setGeomNode(otherCopy)
        else:
            self.setGeomNode(otherCopy.getChild(0))
        self.switches = other.switches
        self.__LODNode = self.find('**/+LODNode')
        self.__hasLOD = 0
        if not self.__LODNode.isEmpty():
            self.__hasLOD = 1
        self.__copyPartBundles(other)
        self.__copySubpartDict(other)
        self.__subpartsComplete = other.__subpartsComplete
        self.__copyAnimControls(other)

    def __cmp__(self, other):
        if self is other:
            return 0
        else:
            return 1

    def __str__(self):
        return 'Actor %s, parts = %s, LODs = %s, anims = %s' % (self.getName(), self.getPartNames(), self.getLODNames(), self.getAnimNames())

    def listJoints(self, partName='modelRoot', lodName='lodRoot'):
        if self.mergeLODBundles:
            partBundleDict = self.__commonBundleHandles
        else:
            partBundleDict = self.__partBundleDict.get(lodName)
            if not partBundleDict:
                Actor.notify.error('no lod named: %s' % lodName)
        subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
        partDef = partBundleDict.get(subpartDef.truePartName)
        if partDef == None:
            Actor.notify.error('no part named: %s' % partName)
        self.__doListJoints(0, partDef.getBundle(), subpartDef.subset.isIncludeEmpty(), subpartDef.subset)
        return

    def __doListJoints(self, indentLevel, part, isIncluded, subset):
        name = part.getName()
        if subset.matchesInclude(name):
            isIncluded = True
        elif subset.matchesExclude(name):
            isIncluded = False
        if isIncluded:
            value = ''
            if hasattr(part, 'outputValue'):
                lineStream = LineStream.LineStream()
                part.outputValue(lineStream)
                value = lineStream.getLine()
            print ' ' * indentLevel, part.getName(), value
        for i in range(part.getNumChildren()):
            self.__doListJoints(indentLevel + 2, part.getChild(i), isIncluded, subset)

    def getActorInfo(self):
        lodInfo = []
        for (lodName, partDict) in self.__animControlDict.items():
            if self.mergeLODBundles:
                lodName = self.__sortedLODNames[0]
            partInfo = []
            for partName in partDict.keys():
                subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
                partBundleDict = self.__partBundleDict.get(lodName)
                partDef = partBundleDict.get(subpartDef.truePartName)
                partBundle = partDef.getBundle()
                animDict = partDict[partName]
                animInfo = []
                for animName in animDict.keys():
                    file = animDict[animName].filename
                    animControl = animDict[animName].animControl
                    animInfo.append([animName, file, animControl])

                partInfo.append([partName, partBundle, animInfo])

            lodInfo.append([lodName, partInfo])

        return lodInfo

    def getAnimNames(self):
        animNames = []
        for (lodName, lodInfo) in self.getActorInfo():
            for (partName, bundle, animInfo) in lodInfo:
                for (animName, file, animControl) in animInfo:
                    if animName not in animNames:
                        animNames.append(animName)

        return animNames

    def pprint(self):
        for (lodName, lodInfo) in self.getActorInfo():
            print 'LOD:', lodName
            for (partName, bundle, animInfo) in lodInfo:
                print '  Part:', partName
                print '  Bundle:', repr(bundle)
                for (animName, file, animControl) in animInfo:
                    print '    Anim:', animName
                    print '      File:', file
                    if animControl == None:
                        print ' (not loaded)'
                    else:
                        print '      NumFrames: %d PlayRate: %0.2f' % (animControl.getNumFrames(), animControl.getPlayRate())

        return

    def cleanup(self):
        self.stop(None)
        self.clearPythonData()
        self.flush()
        if self.__geomNode:
            self.__geomNode.removeNode()
            self.__geomNode = None
        if not self.isEmpty():
            self.removeNode()
        return

    def removeNode(self):
        if self.__geomNode and self.__geomNode.getNumChildren() > 0:
            pass
        NodePath.removeNode(self)

    def clearPythonData(self):
        self.__commonBundleHandles = {}
        self.__partBundleDict = {}
        self.__subpartDict = {}
        self.__sortedLODNames = []
        self.__animControlDict = {}

    def flush(self):
        self.clearPythonData()
        if self.__LODNode and not self.__LODNode.isEmpty():
            self.__LODNode.removeNode()
            self.__LODNode = None
        if self.__geomNode:
            self.__geomNode.removeChildren()
        self.__hasLOD = 0
        return

    def getAnimControlDict(self):
        return self.__animControlDict

    def removeAnimControlDict(self):
        self.__animControlDict = {}

    def getPartBundleDict(self):
        return self.__partBundleDict

    def getPartBundles(self, partName=None):
        bundles = []
        for (lodName, partBundleDict) in self.__partBundleDict.items():
            if partName == None:
                for partDef in partBundleDict.values():
                    bundles.append(partDef.getBundle())

            else:
                subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
                partDef = partBundleDict.get(subpartDef.truePartName)
                if partDef != None:
                    bundles.append(partDef.getBundle())
                else:
                    Actor.notify.warning("Couldn't find part: %s" % partName)

        return bundles

    def __updateSortedLODNames(self):
        self.__sortedLODNames = self.__partBundleDict.keys()

        def sortFunc(x, y):
            if not str(x).isdigit():
                smap = {'h': 3, 'm': 2, 'l': 1, 'f': 0}
                return cmp(smap[y[0]], smap[x[0]])
            else:
                return cmp(int(y), int(x))

        self.__sortedLODNames.sort(sortFunc)

    def getLODNames(self):
        return self.__sortedLODNames

    def getPartNames(self):
        partNames = []
        if self.__partBundleDict:
            partNames = self.__partBundleDict.values()[0].keys()
        return partNames + self.__subpartDict.keys()

    def getGeomNode(self):
        return self.__geomNode

    def setGeomNode(self, node):
        self.__geomNode = node

    def getLODNode(self):
        return self.__LODNode.node()

    def setLODNode(self, node=None):
        if node == None:
            node = LODNode.makeDefaultLod('lod')
        if self.__LODNode:
            self.__LODNode = node
        else:
            self.__LODNode = self.__geomNode.attachNewNode(node)
            self.__hasLOD = 1
            self.switches = {}
        return

    def useLOD(self, lodName):
        child = self.__LODNode.find(str(lodName))
        index = self.__LODNode.node().findChild(child.node())
        self.__LODNode.node().forceSwitch(index)

    def printLOD(self):
        sortedKeys = self.__sortedLODNames
        for eachLod in sortedKeys:
            print 'python switches for %s: in: %d, out %d' % (eachLod, self.switches[eachLod][0], self.switches[eachLod][1])

        switchNum = self.__LODNode.node().getNumSwitches()
        for eachSwitch in range(0, switchNum):
            print 'c++ switches for %d: in: %d, out: %d' % (eachSwitch, self.__LODNode.node().getIn(eachSwitch), self.__LODNode.node().getOut(eachSwitch))

    def resetLOD(self):
        self.__LODNode.node().clearForceSwitch()

    def addLOD(self, lodName, inDist=0, outDist=0, center=None):
        self.__LODNode.attachNewNode(str(lodName))
        self.switches[lodName] = [
         inDist, outDist]
        self.__LODNode.node().addSwitch(inDist, outDist)
        if center != None:
            self.setCenter(center)
        return

    def setLOD(self, lodName, inDist=0, outDist=0):
        self.switches[lodName] = [
         inDist, outDist]
        self.__LODNode.node().setSwitch(self.getLODIndex(lodName), inDist, outDist)

    def getLODIndex(self, lodName):
        return list(self.__LODNode.getChildren()).index(self.getLOD(lodName))

    def getLOD(self, lodName):
        if self.__LODNode:
            lod = self.__LODNode.find(str(lodName))
            if lod.isEmpty():
                return
            else:
                return lod
        else:
            return
        return

    def hasLOD(self):
        return self.__hasLOD

    def setCenter(self, center):
        if center == None:
            center = Point3(0, 0, 0)
        self.__LODCenter = center
        if self.__LODNode:
            self.__LODNode.node().setCenter(self.__LODCenter)
        if self.__LODAnimation:
            self.setLODAnimation(*self.__LODAnimation)
        return

    def setLODAnimation(self, farDistance, nearDistance, delayFactor):
        self.__LODAnimation = (
         farDistance, nearDistance, delayFactor)
        for lodData in self.__partBundleDict.values():
            for partData in lodData.values():
                char = partData.partBundleNP
                char.node().setLodAnimation(self.__LODCenter, farDistance, nearDistance, delayFactor)

    def clearLODAnimation(self):
        self.__LODAnimation = None
        for lodData in self.__partBundleDict.values():
            for partData in lodData.values():
                char = partData.partBundleNP
                char.node().clearLodAnimation()

        return

    def update(self, lod=0, partName=None, lodName=None, force=False):
        if lodName == None:
            lodNames = self.getLODNames()
        else:
            lodNames = [
             lodName]
        anyChanged = False
        if lod < len(lodNames):
            lodName = lodNames[lod]
            if partName == None:
                partBundleDict = self.__partBundleDict[lodName]
                partNames = partBundleDict.keys()
            else:
                partNames = [
                 partName]
            for partName in partNames:
                partBundle = self.getPartBundle(partName, lodNames[lod])
                if force:
                    if partBundle.forceUpdate():
                        anyChanged = True
                elif partBundle.update():
                    anyChanged = True

        else:
            self.notify.warning('update() - no lod: %d' % lod)
        return anyChanged

    def getFrameRate(self, animName=None, partName=None):
        lodName = self.__animControlDict.keys()[0]
        controls = self.getAnimControls(animName, partName)
        if len(controls) == 0:
            return
        return controls[0].getFrameRate()

    def getBaseFrameRate(self, animName=None, partName=None):
        lodName = self.__animControlDict.keys()[0]
        controls = self.getAnimControls(animName, partName)
        if len(controls) == 0:
            return
        return controls[0].getAnim().getBaseFrameRate()

    def getPlayRate(self, animName=None, partName=None):
        if self.__animControlDict:
            lodName = self.__animControlDict.keys()[0]
            controls = self.getAnimControls(animName, partName)
            if controls:
                return controls[0].getPlayRate()
        return

    def setPlayRate(self, rate, animName, partName=None):
        for control in self.getAnimControls(animName, partName):
            control.setPlayRate(rate)

    def getDuration(self, animName=None, partName=None, fromFrame=None, toFrame=None):
        lodName = self.__animControlDict.keys()[0]
        controls = self.getAnimControls(animName, partName)
        if len(controls) == 0:
            return
        animControl = controls[0]
        if fromFrame is None:
            fromFrame = 0
        if toFrame is None:
            toFrame = animControl.getNumFrames() - 1
        return (toFrame + 1 - fromFrame) / animControl.getFrameRate()

    def getNumFrames(self, animName=None, partName=None):
        lodName = self.__animControlDict.keys()[0]
        controls = self.getAnimControls(animName, partName)
        if len(controls) == 0:
            return
        return controls[0].getNumFrames()

    def getFrameTime(self, anim, frame, partName=None):
        numFrames = self.getNumFrames(anim, partName)
        animTime = self.getDuration(anim, partName)
        frameTime = animTime * float(frame) / numFrames
        return frameTime

    def getCurrentAnim(self, partName=None):
        if len(self.__animControlDict.items()) == 0:
            return
        (lodName, animControlDict) = self.__animControlDict.items()[0]
        if partName == None:
            (partName, animDict) = animControlDict.items()[0]
        else:
            animDict = animControlDict.get(partName)
            if animDict == None:
                Actor.notify.warning("couldn't find part: %s" % partName)
                return
        for (animName, anim) in animDict.items():
            if anim.animControl and anim.animControl.isPlaying():
                return animName

        return

    def getCurrentFrame(self, animName=None, partName=None):
        (lodName, animControlDict) = self.__animControlDict.items()[0]
        if partName == None:
            (partName, animDict) = animControlDict.items()[0]
        else:
            animDict = animControlDict.get(partName)
            if animDict == None:
                Actor.notify.warning("couldn't find part: %s" % partName)
                return
        if animName:
            anim = animDict.get(animName)
            if not anim:
                Actor.notify.warning("couldn't find anim: %s" % animName)
            elif anim.animControl:
                return anim.animControl.getFrame()
        for (animName, anim) in animDict.items():
            if anim.animControl and anim.animControl.isPlaying():
                return anim.animControl.getFrame()

        return

    def getPart(self, partName, lodName='lodRoot'):
        partBundleDict = self.__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return
        subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
        partDef = partBundleDict.get(subpartDef.truePartName)
        if partDef != None:
            return partDef.partBundleNP
        return

    def getPartBundle(self, partName, lodName='lodRoot'):
        partBundleDict = self.__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return
        subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
        partDef = partBundleDict.get(subpartDef.truePartName)
        if partDef != None:
            return partDef.getBundle()
        return

    def removePart(self, partName, lodName='lodRoot'):
        partBundleDict = self.__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return
        if partBundleDict.has_key(partName):
            partBundleDict[partName].partBundleNP.removeNode()
            del partBundleDict[partName]
        if self.mergeLODBundles:
            lodName = 'common'
        partDict = self.__animControlDict.get(lodName)
        if not partDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return
        if partDict.has_key(partName):
            del partDict[partName]

    def hidePart(self, partName, lodName='lodRoot'):
        partBundleDict = self.__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return
        partDef = partBundleDict.get(partName)
        if partDef:
            partDef.partBundleNP.hide()
        else:
            Actor.notify.warning('no part named %s!' % partName)

    def showPart(self, partName, lodName='lodRoot'):
        partBundleDict = self.__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return
        partDef = partBundleDict.get(partName)
        if partDef:
            partDef.partBundleNP.show()
        else:
            Actor.notify.warning('no part named %s!' % partName)

    def showAllParts(self, partName, lodName='lodRoot'):
        partBundleDict = self.__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return
        partDef = partBundleDict.get(partName)
        if partDef:
            partDef.partBundleNP.show()
            partDef.partBundleNP.getChildren().show()
        else:
            Actor.notify.warning('no part named %s!' % partName)

    def exposeJoint(self, node, partName, jointName, lodName='lodRoot', localTransform=0):
        partBundleDict = self.__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return
        subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
        partDef = partBundleDict.get(subpartDef.truePartName)
        if partDef:
            bundle = partDef.getBundle()
        else:
            Actor.notify.warning('no part named %s!' % partName)
            return
        joint = bundle.findChild(jointName)
        if node == None:
            node = self.attachNewNode(jointName)
        if joint:
            if localTransform:
                joint.addLocalTransform(node.node())
            else:
                joint.addNetTransform(node.node())
        else:
            Actor.notify.warning('no joint named %s!' % jointName)
        return node

    def stopJoint(self, partName, jointName, lodName='lodRoot'):
        partBundleDict = self.__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return
        subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
        partDef = partBundleDict.get(subpartDef.truePartName)
        if partDef:
            bundle = partDef.getBundle()
        else:
            Actor.notify.warning('no part named %s!' % partName)
            return
        joint = bundle.findChild(jointName)
        if joint:
            joint.clearNetTransforms()
            joint.clearLocalTransforms()
        else:
            Actor.notify.warning('no joint named %s!' % jointName)
        return

    def getJoints(self, partName=None, jointName='*', lodName=None):
        joints = []
        pattern = GlobPattern(jointName)
        if lodName == None and self.mergeLODBundles:
            partBundleDicts = [self.__commonBundleHandles]
        elif lodName == None:
            partBundleDicts = self.__partBundleDict.values()
        else:
            partBundleDict = self.__partBundleDict.get(lodName)
            if not partBundleDict:
                Actor.notify.warning("couldn't find lod: %s" % lodName)
                return []
            partBundleDicts = [
             partBundleDict]
        for partBundleDict in partBundleDicts:
            parts = []
            if partName:
                subpartDef = self.__subpartDict.get(partName, None)
                if not subpartDef:
                    subset = None
                    partDef = partBundleDict.get(partName)
                else:
                    subset = subpartDef.subset
                    partDef = partBundleDict.get(subpartDef.truePartName)
                if not partDef:
                    Actor.notify.warning('no part named %s!' % partName)
                    return []
                parts = [
                 partDef]
            else:
                subset = None
                parts = partBundleDict.values()
            for partData in parts:
                partBundle = partData.getBundle()
                if not pattern.hasGlobCharacters() and not subset:
                    joint = partBundle.findChild(jointName)
                    if joint:
                        joints.append(joint)
                else:
                    isIncluded = True
                    if subset:
                        isIncluded = subset.isIncludeEmpty()
                    self.__getPartJoints(joints, pattern, partBundle, subset, isIncluded)

        return joints

    def getOverlappingJoints(self, partNameA, partNameB, jointName='*', lodName=None):
        jointsA = set(self.getJoints(partName=partNameA, jointName=jointName, lodName=lodName))
        jointsB = set(self.getJoints(partName=partNameB, jointName=jointName, lodName=lodName))
        return jointsA & jointsB

    def __getPartJoints(self, joints, pattern, partNode, subset, isIncluded):
        name = partNode.getName()
        if subset:
            if subset.matchesInclude(name):
                isIncluded = True
            elif subset.matchesExclude(name):
                isIncluded = False
        if isIncluded and pattern.matches(name) and isinstance(partNode, MovingPartBase):
            joints.append(partNode)
        for child in partNode.getChildren():
            self.__getPartJoints(joints, pattern, child, subset, isIncluded)

    def getJointTransform(self, partName, jointName, lodName='lodRoot'):
        partBundleDict = self.__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return
        subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
        partDef = partBundleDict.get(subpartDef.truePartName)
        if partDef:
            bundle = partDef.getBundle()
        else:
            Actor.notify.warning('no part named %s!' % partName)
            return
        joint = bundle.findChild(jointName)
        if joint == None:
            Actor.notify.warning('no joint named %s!' % jointName)
            return
        return joint.getDefaultValue()

    def controlJoint(self, node, partName, jointName, lodName='lodRoot'):
        subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
        trueName = subpartDef.truePartName
        anyGood = False
        for bundleDict in self.__partBundleDict.values():
            bundle = bundleDict[trueName].getBundle()
            if node == None:
                node = self.attachNewNode(ModelNode(jointName))
                joint = bundle.findChild(jointName)
                if joint:
                    if isinstance(joint, MovingPartMatrix):
                        node.setMat(joint.getDefaultValue())
            elif bundle.controlJoint(jointName, node.node()):
                anyGood = True

        if not anyGood:
            self.notify.warning('Cannot control joint %s' % jointName)
        return node

    def freezeJoint(self, partName, jointName, transform=None, pos=Vec3(0, 0, 0), hpr=Vec3(0, 0, 0), scale=Vec3(1, 1, 1)):
        if transform == None:
            transform = TransformState.makePosHprScale(pos, hpr, scale)
        subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
        trueName = subpartDef.truePartName
        anyGood = False
        for bundleDict in self.__partBundleDict.values():
            if bundleDict[trueName].getBundle().freezeJoint(jointName, transform):
                anyGood = True

        if not anyGood:
            self.notify.warning('Cannot freeze joint %s' % jointName)
        return

    def releaseJoint(self, partName, jointName):
        subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
        trueName = subpartDef.truePartName
        for bundleDict in self.__partBundleDict.values():
            bundleDict[trueName].getBundle().releaseJoint(jointName)

    def instance(self, path, partName, jointName, lodName='lodRoot'):
        partBundleDict = self.__partBundleDict.get(lodName)
        if partBundleDict:
            subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
            partDef = partBundleDict.get(subpartDef.truePartName)
            if partDef:
                joint = partDef.partBundleNP.find('**/' + jointName)
                if joint.isEmpty():
                    Actor.notify.warning('%s not found!' % jointName)
                else:
                    return path.instanceTo(joint)
            else:
                Actor.notify.warning('no part named %s!' % partName)
        else:
            Actor.notify.warning('no lod named %s!' % lodName)

    def attach(self, partName, anotherPartName, jointName, lodName='lodRoot'):
        partBundleDict = self.__partBundleDict.get(lodName)
        if partBundleDict:
            subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
            partDef = partBundleDict.get(subpartDef.truePartName)
            if partDef:
                anotherPartDef = partBundleDict.get(anotherPartName)
                if anotherPartDef:
                    joint = anotherPartDef.partBundleNP.find('**/' + jointName)
                    if joint.isEmpty():
                        Actor.notify.warning('%s not found!' % jointName)
                    else:
                        partDef.partBundleNP.reparentTo(joint)
                else:
                    Actor.notify.warning('no part named %s!' % anotherPartName)
            else:
                Actor.notify.warning('no part named %s!' % partName)
        else:
            Actor.notify.warning('no lod named %s!' % lodName)

    def drawInFront(self, frontPartName, backPartName, mode, root=None, lodName=None):
        if lodName != None:
            lodRoot = self.__LODNode.find(str(lodName))
            if root == None:
                root = lodRoot
            else:
                root = lodRoot.find('**/' + root)
        elif root == None:
            root = self
        frontParts = root.findAllMatches('**/' + frontPartName)
        if mode > 0:
            numFrontParts = frontParts.getNumPaths()
            for partNum in range(0, numFrontParts):
                frontParts[partNum].setBin('fixed', mode)

            return
        if mode == -2:
            numFrontParts = frontParts.getNumPaths()
            for partNum in range(0, numFrontParts):
                frontParts[partNum].setDepthWrite(0)
                frontParts[partNum].setDepthTest(0)

        backPart = root.find('**/' + backPartName)
        if backPart.isEmpty():
            Actor.notify.warning('no part named %s!' % backPartName)
            return
        if mode == -3:
            backPart.node().setEffect(DecalEffect.make())
        else:
            backPart.reparentTo(backPart.getParent(), -1)
        frontParts.reparentTo(backPart)
        return

    def fixBounds(self, partName=None):
        if partName == None:
            for lodData in self.__partBundleDict.values():
                for partData in lodData.values():
                    char = partData.partBundleNP
                    char.node().update()
                    geomNodes = char.findAllMatches('**/+GeomNode')
                    numGeomNodes = geomNodes.getNumPaths()
                    for nodeNum in xrange(numGeomNodes):
                        thisGeomNode = geomNodes.getPath(nodeNum)
                        numGeoms = thisGeomNode.node().getNumGeoms()
                        for geomNum in xrange(numGeoms):
                            thisGeom = thisGeomNode.node().getGeom(geomNum)
                            thisGeom.markBoundsStale()

                        thisGeomNode.node().markInternalBoundsStale()

        for lodData in self.__partBundleDict.values():
            partData = lodData.get(partName)
            if partData:
                char = partData.partBundleNP
                char.node().update()
                geomNodes = char.findAllMatches('**/+GeomNode')
                numGeomNodes = geomNodes.getNumPaths()
                for nodeNum in xrange(numGeomNodes):
                    thisGeomNode = geomNodes.getPath(nodeNum)
                    numGeoms = thisGeomNode.node().getNumGeoms()
                    for geomNum in xrange(numGeoms):
                        thisGeom = thisGeomNode.node().getGeom(geomNum)
                        thisGeom.markBoundsStale()

                    thisGeomNode.node().markInternalBoundsStale()

        return

    def fixBounds_old(self, part=None):
        if part == None:
            part = self
        charNodes = part.findAllMatches('**/+Character')
        numCharNodes = charNodes.getNumPaths()
        for charNum in range(0, numCharNodes):
            charNodes.getPath(charNum).node().update()

        geomNodes = part.findAllMatches('**/+GeomNode')
        numGeomNodes = geomNodes.getNumPaths()
        for nodeNum in range(0, numGeomNodes):
            thisGeomNode = geomNodes.getPath(nodeNum)
            numGeoms = thisGeomNode.node().getNumGeoms()
            for geomNum in range(0, numGeoms):
                thisGeom = thisGeomNode.node().getGeom(geomNum)
                thisGeom.markBoundsStale()

            thisGeomNode.node().markInternalBoundsStale()

        return

    def showAllBounds(self):
        geomNodes = self.__geomNode.findAllMatches('**/+GeomNode')
        numGeomNodes = geomNodes.getNumPaths()
        for nodeNum in range(0, numGeomNodes):
            geomNodes.getPath(nodeNum).showBounds()

    def hideAllBounds(self):
        geomNodes = self.__geomNode.findAllMatches('**/+GeomNode')
        numGeomNodes = geomNodes.getNumPaths()
        for nodeNum in range(0, numGeomNodes):
            geomNodes.getPath(nodeNum).hideBounds()

    def animPanel(self):
        from direct.showbase import TkGlobal
        from direct.tkpanels import AnimPanel
        return AnimPanel.AnimPanel(self)

    def stop(self, animName=None, partName=None):
        for control in self.getAnimControls(animName, partName):
            control.stop()

    def play(self, animName, partName=None, fromFrame=None, toFrame=None):
        if fromFrame == None:
            for control in self.getAnimControls(animName, partName):
                control.play()

        else:
            for control in self.getAnimControls(animName, partName):
                if toFrame == None:
                    control.play(fromFrame, control.getNumFrames() - 1)
                else:
                    control.play(fromFrame, toFrame)

        return

    def loop(self, animName, restart=1, partName=None, fromFrame=None, toFrame=None):
        if fromFrame == None:
            for control in self.getAnimControls(animName, partName):
                control.loop(restart)

        else:
            for control in self.getAnimControls(animName, partName):
                if toFrame == None:
                    control.loop(restart, fromFrame, control.getNumFrames() - 1)
                else:
                    control.loop(restart, fromFrame, toFrame)

        return

    def pingpong(self, animName, restart=1, partName=None, fromFrame=None, toFrame=None):
        if fromFrame == None:
            fromFrame = 0
        for control in self.getAnimControls(animName, partName):
            if toFrame == None:
                control.pingpong(restart, fromFrame, control.getNumFrames() - 1)
            else:
                control.pingpong(restart, fromFrame, toFrame)

        return

    def pose(self, animName, frame, partName=None, lodName=None):
        for control in self.getAnimControls(animName, partName, lodName):
            control.pose(frame)

    def setBlend(self, animBlend=None, frameBlend=None, blendType=None, partName=None):
        for bundle in self.getPartBundles(partName=partName):
            if blendType != None:
                bundle.setBlendType(blendType)
            if animBlend != None:
                bundle.setAnimBlendFlag(animBlend)
            if frameBlend != None:
                bundle.setFrameBlendFlag(frameBlend)

        return

    def enableBlend(self, blendType=PartBundle.BTNormalizedLinear, partName=None):
        self.setBlend(animBlend=True, blendType=blendType, partName=partName)

    def disableBlend(self, partName=None):
        self.setBlend(animBlend=False, partName=partName)

    def setControlEffect(self, animName, effect, partName=None, lodName=None):
        for control in self.getAnimControls(animName, partName, lodName):
            control.getPart().setControlEffect(control, effect)

    def getAnimFilename(self, animName, partName='modelRoot'):
        if self.mergeLODBundles:
            lodName = 'common'
        elif self.switches:
            lodName = str(self.switches.keys()[0])
        else:
            lodName = 'lodRoot'
        try:
            return self.__animControlDict[lodName][partName][animName].filename
        except:
            return

        return

    def getAnimControl(self, animName, partName=None, lodName=None, allowAsyncBind=True):
        if not partName:
            partName = 'modelRoot'
        if self.mergeLODBundles:
            lodName = 'common'
        elif not lodName:
            if self.switches:
                lodName = str(self.switches.keys()[0])
            else:
                lodName = 'lodRoot'
        partDict = self.__animControlDict.get(lodName)
        animDict = partDict.get(partName)
        if animDict == None:
            Actor.notify.warning("couldn't find part: %s" % partName)
        else:
            anim = animDict.get(animName)
            if anim == None:
                pass
            else:
                if not anim.animControl:
                    self.__bindAnimToPart(animName, partName, lodName, allowAsyncBind=allowAsyncBind)
                elif not allowAsyncBind:
                    anim.animControl.waitPending()
                return anim.animControl
        return

    def getAnimControls(self, animName=None, partName=None, lodName=None, allowAsyncBind=True):
        if partName == None and self.__subpartsComplete:
            partName = self.__subpartDict.keys()
        controls = []
        if lodName == None or self.mergeLODBundles:
            animControlDictItems = self.__animControlDict.items()
        else:
            partDict = self.__animControlDict.get(lodName)
            if partDict == None:
                Actor.notify.warning("couldn't find lod: %s" % lodName)
                animControlDictItems = []
            else:
                animControlDictItems = [
                 (
                  lodName, partDict)]
        for (lodName, partDict) in animControlDictItems:
            if partName == None:
                animDictItems = []
                for (thisPart, animDict) in partDict.items():
                    if not self.__subpartDict.has_key(thisPart):
                        animDictItems.append((thisPart, animDict))

            elif isinstance(partName, types.StringTypes):
                partNameList = [
                 partName]
            else:
                partNameList = partName
            animDictItems = []
            for pName in partNameList:
                animDict = partDict.get(pName)
                if animDict == None:
                    subpartDef = self.__subpartDict.get(pName)
                    if subpartDef:
                        animDict = {}
                        partDict[pName] = animDict
                if animDict == None:
                    Actor.notify.warning("couldn't find part: %s" % pName)
                else:
                    animDictItems.append((pName, animDict))

            if animName is None:
                for (thisPart, animDict) in animDictItems:
                    for anim in animDict.values():
                        if anim.animControl and anim.animControl.isPlaying():
                            controls.append(anim.animControl)

            else:
                if isinstance(animName, types.StringTypes):
                    animNameList = [animName]
                else:
                    animNameList = animName
                for (thisPart, animDict) in animDictItems:
                    names = animNameList
                    if animNameList is True:
                        names = animDict.keys()
                    for animName in names:
                        anim = animDict.get(animName)
                        if anim == None and partName != None:
                            for pName in partNameList:
                                subpartDef = self.__subpartDict.get(pName)
                                if subpartDef:
                                    truePartName = subpartDef.truePartName
                                    anim = partDict[truePartName].get(animName)
                                    if anim:
                                        anim = anim.makeCopy()
                                        animDict[animName] = anim

                        if anim == None:
                            pass
                        else:
                            animControl = anim.animControl
                            if animControl == None:
                                animControl = self.__bindAnimToPart(animName, thisPart, lodName, allowAsyncBind=allowAsyncBind)
                            elif not allowAsyncBind:
                                animControl.waitPending()
                            if animControl:
                                controls.append(animControl)

        return controls

    def loadModel(self, modelPath, partName='modelRoot', lodName='lodRoot', copy=True, okMissing=None, autoBindAnims=True):
        if isinstance(modelPath, NodePath):
            if copy:
                model = modelPath.copyTo(NodePath())
            else:
                model = modelPath
        else:
            loaderOptions = self.modelLoaderOptions
            if not copy:
                loaderOptions = LoaderOptions(loaderOptions)
                loaderOptions.setFlags(loaderOptions.getFlags() & ~LoaderOptions.LFNoRamCache)
            model = loader.loadModel(modelPath, loaderOptions=loaderOptions, okMissing=okMissing)
        if model == None:
            raise StandardError, 'Could not load Actor model %s' % modelPath
        if model.node().isOfType(Character.getClassType()):
            bundleNP = model
        else:
            bundleNP = model.find('**/+Character')
        if bundleNP.isEmpty():
            Actor.notify.warning('%s is not a character!' % modelPath)
            model.reparentTo(self.__geomNode)
        else:
            if autoBindAnims:
                acc = AnimControlCollection()
                autoBind(model.node(), acc, -1)
                numAnims = acc.getNumAnims()
            else:
                numAnims = 0
            if lodName != 'lodRoot':
                bundleNP.reparentTo(self.__LODNode.find(str(lodName)))
            else:
                bundleNP.reparentTo(self.__geomNode)
            self.__prepareBundle(bundleNP, model.node(), partName, lodName)
            bundleNP.node().setName('%s%s' % (Actor.partPrefix, partName))
            if numAnims != 0:
                Actor.notify.info('model contains %s animations.' % numAnims)
                if self.mergeLODBundles:
                    lodName = 'common'
                self.__animControlDict.setdefault(lodName, {})
                self.__animControlDict[lodName].setdefault(partName, {})
                for i in range(numAnims):
                    animControl = acc.getAnim(i)
                    animName = acc.getAnimName(i)
                    animDef = Actor.AnimDef()
                    animDef.animControl = animControl
                    self.__animControlDict[lodName][partName][animName] = animDef

        return

    def __prepareBundle(self, bundleNP, partModel, partName='modelRoot', lodName='lodRoot'):
        if not self.gotName:
            self.node().setName(bundleNP.node().getName())
            self.gotName = 1
        bundleDict = self.__partBundleDict.get(lodName, None)
        if bundleDict == None:
            bundleDict = {}
            self.__partBundleDict[lodName] = bundleDict
            self.__updateSortedLODNames()
        node = bundleNP.node()
        bundleHandle = node.getBundleHandle(0)
        if self.mergeLODBundles:
            loadedBundleHandle = self.__commonBundleHandles.get(partName, None)
            if loadedBundleHandle:
                node.mergeBundles(bundleHandle, loadedBundleHandle)
                bundleHandle = loadedBundleHandle
            else:
                self.__commonBundleHandles[partName] = bundleHandle
        bundleDict[partName] = Actor.PartDef(bundleNP, bundleHandle, partModel)
        return

    def makeSubpart(self, partName, includeJoints, excludeJoints=[], parent='modelRoot', overlapping=False):
        subpartDef = self.__subpartDict.get(parent, Actor.SubpartDef(''))
        subset = PartSubset(subpartDef.subset)
        for name in includeJoints:
            subset.addIncludeJoint(GlobPattern(name))

        for name in excludeJoints:
            subset.addExcludeJoint(GlobPattern(name))

        self.__subpartDict[partName] = Actor.SubpartDef(parent, subset)
        if __dev__ and not overlapping and self.validateSubparts.getValue():
            for (otherPartName, otherPartDef) in self.__subpartDict.items():
                if otherPartName != partName and otherPartDef.truePartName == parent:
                    joints = self.getOverlappingJoints(partName, otherPartName)
                    if joints:
                        raise StandardError, 'Overlapping joints: %s and %s' % (partName, otherPartName)

    def setSubpartsComplete(self, flag):
        self.__subpartsComplete = flag
        if __dev__ and self.__subpartsComplete and self.validateSubparts.getValue():
            if self.__subpartDict:
                self.verifySubpartsComplete()

    def getSubpartsComplete(self):
        return self.__subpartsComplete

    def verifySubpartsComplete(self, partName=None, lodName=None):
        if partName:
            partNames = [partName]
        elif lodName:
            partNames = self.__partBundleDict[lodName].keys()
        else:
            partNames = self.__partBundleDict.values()[0].keys()
        for partName in partNames:
            subJoints = set()
            for (subPartName, subPartDef) in self.__subpartDict.items():
                if subPartName != partName and subPartDef.truePartName == partName:
                    subJoints |= set(self.getJoints(partName=subPartName, lodName=lodName))

            allJoints = set(self.getJoints(partName=partName, lodName=lodName))
            diff = allJoints.difference(subJoints)
            if diff:
                self.notify.warning('Uncovered joints: %s' % list(diff))

    def loadAnims(self, anims, partName='modelRoot', lodName='lodRoot'):
        reload = True
        if self.mergeLODBundles:
            lodNames = [
             'common']
        elif lodName == 'all':
            reload = False
            lodNames = self.switches.keys()
            lodNames.sort()
            for i in range(0, len(lodNames)):
                lodNames[i] = str(lodNames[i])

        else:
            lodNames = [
             lodName]
        firstLoad = True
        if not reload:
            try:
                self.__animControlDict[lodNames[0]][partName]
                firstLoad = False
            except:
                pass

        for lName in lodNames:
            if firstLoad:
                self.__animControlDict.setdefault(lName, {})
                self.__animControlDict[lName].setdefault(partName, {})

        for (animName, filename) in anims.items():
            for lName in lodNames:
                if firstLoad:
                    self.__animControlDict[lName][partName][animName] = Actor.AnimDef()
                if isinstance(filename, NodePath):
                    if filename.node().isOfType(AnimBundleNode.getClassType()):
                        animBundleNP = filename
                    else:
                        animBundleNP = filename.find('**/+AnimBundleNode')
                    self.__animControlDict[lName][partName][animName].animBundle = animBundleNP.node().getBundle()
                else:
                    self.__animControlDict[lName][partName][animName].filename = filename

    def initAnimsOnAllLODs(self, partNames):
        if self.mergeLODBundles:
            lodNames = [
             'common']
        else:
            lodNames = self.__partBundleDict.keys()
        for lod in lodNames:
            for part in partNames:
                self.__animControlDict.setdefault(lod, {})
                self.__animControlDict[lod].setdefault(part, {})

    def loadAnimsOnAllLODs(self, anims, partName='modelRoot'):
        if self.mergeLODBundles:
            lodNames = [
             'common']
        else:
            lodNames = self.__partBundleDict.keys()
        for (animName, filename) in anims.items():
            for lod in lodNames:
                self.__animControlDict[lod][partName][animName] = Actor.AnimDef(filename)

    def postFlatten(self):
        if self.mergeLODBundles:
            self.__commonBundleHandles = {}
            for (lodName, bundleDict) in self.__partBundleDict.items():
                for (partName, partDef) in bundleDict.items():
                    loadedBundleHandle = self.__commonBundleHandles.get(partName, None)
                    node = partDef.partBundleNP.node()
                    if loadedBundleHandle:
                        node.mergeBundles(partDef.partBundleHandle, loadedBundleHandle)
                        partDef.partBundleHandle = loadedBundleHandle
                    else:
                        self.__commonBundleHandles[partName] = partDef.partBundleHandle

        self.unloadAnims()
        return

    def unloadAnims(self, anims=None, partName=None, lodName=None):
        if lodName == None or self.mergeLODBundles:
            lodNames = self.__animControlDict.keys()
        else:
            lodNames = [
             lodName]
        if partName == None:
            if len(lodNames) > 0:
                partNames = self.__animControlDict[lodNames[0]].keys()
            else:
                partNames = []
        else:
            partNames = [
             partName]
        if anims == None:
            for lodName in lodNames:
                for partName in partNames:
                    for animDef in self.__animControlDict[lodName][partName].values():
                        if animDef.animControl != None:
                            animDef.animControl.getPart().clearControlEffects()
                            animDef.animControl = None

        for lodName in lodNames:
            for partName in partNames:
                for anim in anims:
                    animDef = self.__animControlDict[lodName][partName].get(anim)
                    if animDef and animDef.animControl != None:
                        animDef.animControl.getPart().clearControlEffects()
                        animDef.animControl = None

        return

    def bindAnim(self, animName, partName=None, lodName=None, allowAsyncBind=False):
        self.getAnimControls(animName=animName, partName=partName, lodName=lodName, allowAsyncBind=allowAsyncBind)

    def bindAllAnims(self, allowAsyncBind=False):
        self.getAnimControls(animName=True, allowAsyncBind=allowAsyncBind)

    def waitPending(self, partName=None):
        for bundle in self.getPartBundles(partName=partName):
            bundle.waitPending()

    def __bindAnimToPart(self, animName, partName, lodName, allowAsyncBind=True):
        subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
        partDict = self.__animControlDict[lodName]
        animDict = partDict.get(partName)
        if animDict == None:
            animDict = {}
            partDict[partName] = animDict
        anim = animDict.get(animName)
        if anim == None:
            anim = partDict[subpartDef.truePartName].get(animName)
            anim = anim.makeCopy()
            animDict[animName] = anim
        if anim == None:
            Actor.notify.error('actor has no animation %s', animName)
        if anim.animControl:
            return anim.animControl
        if self.mergeLODBundles:
            bundle = self.__commonBundleHandles[subpartDef.truePartName].getBundle()
        else:
            bundle = self.__partBundleDict[lodName][subpartDef.truePartName].getBundle()
        if anim.animBundle:
            animControl = bundle.bindAnim(anim.animBundle, -1, subpartDef.subset)
        else:
            animControl = bundle.loadBindAnim(loader.loader, Filename(anim.filename), -1, subpartDef.subset, allowAsyncBind and self.allowAsyncBind)
        if not animControl:
            return
        anim.animControl = animControl
        return animControl

    def __copyPartBundles(self, other):
        for lodName in other.__partBundleDict.keys():
            if lodName == 'lodRoot':
                partLod = self
            else:
                partLod = self.__LODNode.find(str(lodName))
            if partLod.isEmpty():
                Actor.notify.warning('no lod named: %s' % lodName)
                return
            for (partName, partDef) in other.__partBundleDict[lodName].items():
                bundleNP = partLod.find('**/%s%s' % (Actor.partPrefix, partName))
                if bundleNP != None:
                    self.__prepareBundle(bundleNP, partDef.partModel, partName, lodName)
                else:
                    Actor.notify.error('lod: %s has no matching part: %s' % (lodName, partName))

        return

    def __copySubpartDict(self, other):
        self.__subpartDict = {}
        for (partName, subpartDef) in other.__subpartDict.items():
            subpartDefCopy = subpartDef
            if subpartDef:
                subpartDef = subpartDef.makeCopy()
            self.__subpartDict[partName] = subpartDef

    def __copyAnimControls(self, other):
        for lodName in other.__animControlDict.keys():
            self.__animControlDict[lodName] = {}
            for partName in other.__animControlDict[lodName].keys():
                self.__animControlDict[lodName][partName] = {}
                for animName in other.__animControlDict[lodName][partName].keys():
                    anim = other.__animControlDict[lodName][partName][animName]
                    anim = anim.makeCopy()
                    self.__animControlDict[lodName][partName][animName] = anim

    def actorInterval(self, *args, **kw):
        from direct.interval import ActorInterval
        return ActorInterval.ActorInterval(self, *args, **kw)

    def getAnimBlends(self, animName=None, partName=None, lodName=None):
        result = []
        if animName is None:
            animNames = self.getAnimNames()
        else:
            animNames = [
             animName]
        if lodName is None:
            lodNames = self.getLODNames()
            if self.mergeLODBundles:
                lodNames = lodNames[:1]
        else:
            lodNames = [
             lodName]
        if partName == None and self.__subpartsComplete:
            partNames = self.__subpartDict.keys()
        else:
            partNames = [
             partName]
        for lodName in lodNames:
            animList = []
            for animName in animNames:
                blendList = []
                for partName in partNames:
                    control = self.getAnimControl(animName, partName, lodName)
                    if control:
                        part = control.getPart()
                        effect = part.getControlEffect(control)
                        if effect > 0.0:
                            blendList.append((partName, effect))

                if blendList:
                    animList.append((animName, blendList))

            if animList:
                result.append((lodName, animList))

        return result

    def printAnimBlends(self, animName=None, partName=None, lodName=None):
        for (lodName, animList) in self.getAnimBlends(animName, partName, lodName):
            print 'LOD %s:' % lodName
            for (animName, blendList) in animList:
                list = []
                for (partName, effect) in blendList:
                    list.append('%s:%.3f' % (partName, effect))

                print '  %s: %s' % (animName, (', ').join(list))

    def osdAnimBlends(self, animName=None, partName=None, lodName=None):
        if not onScreenDebug.enabled:
            return
        if animName is None:
            animNames = self.getAnimNames()
        else:
            animNames = [
             animName]
        for animName in animNames:
            if animName is 'nothing':
                continue
            thisAnim = ''
            totalEffect = 0.0
            controls = self.getAnimControls(animName, partName, lodName)
            for control in controls:
                part = control.getPart()
                name = part.getName()
                effect = part.getControlEffect(control)
                if effect > 0.0:
                    totalEffect += effect
                    thisAnim += '%s:%.3f, ' % (name, effect)

            thisAnim += '\n'
            for control in controls:
                part = control.getPart()
                name = part.getName()
                rate = control.getPlayRate()
                thisAnim += '%s:%.1f, ' % (name, rate)

            itemName = 'anim %s' % animName
            if totalEffect > 0.0:
                onScreenDebug.add(itemName, thisAnim)
            elif onScreenDebug.has(itemName):
                onScreenDebug.remove(itemName)

        return

    def faceAwayFromViewer(self):
        self.getGeomNode().setH(180)

    def faceTowardsViewer(self):
        self.getGeomNode().setH(0)

    def renamePartBundles(self, partName, newBundleName):
        subpartDef = self.__subpartDict.get(partName, Actor.SubpartDef(partName))
        for partBundleDict in self.__partBundleDict.values():
            partDef = partBundleDict.get(subpartDef.truePartName)
            partDef.getBundle().setName(newBundleName)