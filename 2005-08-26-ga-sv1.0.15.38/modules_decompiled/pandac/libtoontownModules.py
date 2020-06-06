# File: l (Python 2.2)

import libdtoolconfig
import libtoontown
from GeomBindType import *
from NotifySeverity import *
from DCSubatomicType import *
from ErrorUtilCode import *
from ChatFlags import *
from CoordinateSystem import *
from DCPackType import *
from libtoontownDowncasts import *
import AccumulatedAttribs
import AngularIntegrator
import AnimControlCollection
import AsyncUtility
import BamFile
import BaseParticle
import BitMask32
import BoundedObject
import Buffer
import ButtonHandle
import ButtonRegistry
import CConnectionRepository
import CDistributedSmoothNodeBase
import CIntervalManager
import CPTAFloat
import CPetBrain
import CString
import ClickablePopup
import ClockObject
import ComputedVertices
import ConfigConfigureGetConfigConfigShowbase
import ConfigDeclaration
import ConfigExpress
import ConfigFlags
import ConfigPage
import ConfigPageManager
import ConfigVariableCore
import ConfigVariableManager
import CullBinManager
import CullableObject
import CurveFitter
import DCDeclaration
import DCFile
import DCPackData
import DCPacker
import DCPackerInterface
import DNALoader
import DNAStorage
import DSearchPath
import DataGraphTraverser
import DataNodeTransmit
import DatagramIterator
import Decompressor
import DocumentSpec
import DownloadDb
import DrawableRegion
import EggAttributes
import EggMaterialCollection
import EggRenderMode
import EggTextureCollection
import EggTransform3d
import EventParameter
import EventQueue
import EventReceiver
import Extractor
import FILE
import Filename
import FontPool
import FrameBufferProperties
import FreetypeFont
import Frustum
import FrustumD
import Fstream
import GeomTransformer
import GlobPattern
import GraphicsEngine
import GraphicsPipeSelection
import GraphicsThreadingModel
import HTTPClient
import HTTPCookie
import HTTPDate
import HTTPEntityTag
import HTTPEnum
import HashVal
import Ifstream
import Istream
import KeyboardButton
import LinearIntegrator
import LoaderFileType
import MapPointerToEggMaterialPointerToEggMaterial
import MapPointerToEggTexturePointerToEggTexture
import Mat3
import Mat3D
import Mat4
import Mat4D
import MaterialPool
import MathNumbers
import Mersenne
import ModelPool
import ModifierButtons
import MouseButton
import MouseData
import MouseWatcherParameter
import MultitexReducer
import Namable
import NametagGlobals
import NametagGroup
import NodePath
import NodePathCollection
import NonlinearImager
import Notify
import NotifyCategory
import NurbsCurveInterface
import Ofstream
import Ostream
import PGFrameStyle
import PNMFileType
import PNMImageHeader
import PNMReader
import PNMWriter
import PStatClient
import PStatCollector
import PTADouble
import PTAInt
import PTAUshort
import ParticleSystemManager
import Patcher
import Patchfile
import PhysicsManager
import Pipeline
import PixelBuffer
import PointerToBaseRefCountObjvectorLPoint2f
import PointerToBaseRefCountObjvectorLPoint3f
import PointerToBaseRefCountObjvectorLVecBase4f
import PointerToBaseRefCountObjvectorLVector3f
import PointerToVoid
import PosHpr
import PreparedGraphicsObjects
import ProfileTimer
import Ramfile
import ReferenceCount
import SceneGraphReducer
import Settings
import SmoothMover
import StreamReader
import StreamWriter
import SuitLeg
import SuitLegList
import TextEncoder
import TextProperties
import TextPropertiesManager
import TextureCollection
import TexturePool
import TextureStageCollection
import TimeVal
import TypeHandle
import TypeRegistry
import TypedObject
import URLSpec
import UniqueIdAllocator
import UpdateSeq
import VBase2
import VBase2D
import VBase3
import VBase3D
import VBase4
import VBase4D
import VectorNodePath
import VectorURLSpec
import VectorbasicStringchar
import VirtualFileSystem
import WindowProperties
import WindowsRegistry
import Xel
import AngularEulerIntegrator
import AnimControl
import BaseParticleEmitter
import BaseParticleFactory
import BaseParticleRenderer
import CardMaker
import ChatBalloon
import CollisionTraverser
import ConfigVariableBase
import DCClass
import DCField
import DCSwitch
import DCTypedef
import Datagram
import DisplayRegion
import EventHandler
import ISocketStream
import Iostream
import Light
import LineSegs
import LineStream
import LinearEulerIntegrator
import MouseWatcherGroup
import Multifile
import MultiplexStream
import Nametag
import NurbsCurveEvaluator
import NurbsCurveResult
import NurbsSurfaceEvaluator
import NurbsSurfaceResult
import OSocketStream
import PNMImage
import PTAColorf
import PTANormalf
import PTATexCoordf
import PTAVertexf
import PandaLoader
import ParametricCurveCollection
import ParametricCurveDrawer
import Plane
import PlaneD
import Point2
import Point2D
import Point3
import Point3D
import Point4
import Point4D
import PointerToBaseRefCountObjvectorunsignedchar
import Quat
import QuatD
import RecorderBase
import TypedReferenceCount
import TypedWritable
import Vec2
import Vec2D
import Vec3
import Vec3D
import Vec4
import Vec4D
import VirtualFileList
import WeakPointerToVoid
import AudioManager
import AudioSound
import AutonomousLerp
import AuxSceneData
import BaseForce
import BoundingVolume
import BoxEmitter
import CImpulse
import CInterval
import CMover
import ClientBase
import CollisionHandler
import ConfigVariable
import ConfigVariableList
import ConfigVariableSearchPath
import DCAtomicField
import DCMolecularField
import DCParameter
import DNABattleCell
import DNAGroup
import DNASuitEdge
import DNASuitPath
import DNASuitPoint
import DiscEmitter
import EggObject
import EggUserData
import Event
import GeomParticleRenderer
import GraphicsDevice
import GraphicsPipe
import LOrientationd
import LOrientationf
import LRotationd
import LRotationf
import Lerp
import LerpBlendType
import LerpFunctor
import LineEmitter
import LineParticleRenderer
import NurbsCurveDrawer
import PTAUchar
import PandaNode
import Physical
import PhysicsObject
import PointEmitter
import PointParticleFactory
import PointParticleRenderer
import RecorderController
import RectangleEmitter
import RingEmitter
import SocketStream
import SocketStreamRecorder
import SparkleParticleRenderer
import SphereSurfaceEmitter
import SphereVolumeEmitter
import SpriteParticleRenderer
import TangentRingEmitter
import TextFont
import TypedWritableReferenceCount
import VirtualFile
import WritableConfigurable
import ZSpinParticleFactory
import AngularForce
import AnimBundleNode
import AnimGroup
import CLerpInterval
import CMetaInterval
import CPetChase
import CPetFlee
import CachedTypedWritableReferenceCount
import CollisionEntry
import CollisionHandlerEvent
import CollisionHandlerQueue
import CollisionNode
import CollisionSolid
import ConfigVariableBool
import ConfigVariableDouble
import ConfigVariableFilename
import ConfigVariableInt
import ConfigVariableString
import DCArrayParameter
import DCClassParameter
import DCSimpleParameter
import DCSwitchParameter
import DDrawable
import DNACornice
import DNAData
import DNADoor
import DNANode
import DNAVisGroup
import DNAWindows
import DataNode
import DynamicTextFont
import EaseInBlendType
import EaseInOutBlendType
import EaseOutBlendType
import EggBinMaker
import EggNameUniquifier
import EggNamedObject
import EggSwitchCondition
import EggVertex
import FloatLerpFunctor
import Fog
import ForceNode
import GeomNode
import GeometricBoundingVolume
import GraphicsOutput
import GraphicsStateGuardianBase
import HTTPChannel
import HideInterval
import HprScaleLerpFunctor
import ImageBuffer
import IntLerpFunctor
import LODNode
import Lens
import LensNode
import LightNode
import LinearForce
import MarginManager
import MarginPopup
import Material
import ModelNode
import MouseWatcherRegion
import MultiLerpFunctor
import Nametag3d
import NoBlendType
import PGItem
import PGMouseWatcherParameter
import PGTop
import ParametricCurve
import PartBundleNode
import PartGroup
import ParticleSystem
import PhysicalNode
import PlaneNode
import PolylightNode
import PortalNode
import PosHprLerpFunctor
import PosHprScaleLerpFunctor
import ProjectionScreen
import RenderAttrib
import RenderEffect
import RenderEffects
import RopeNode
import SelectiveChildNode
import SheetNode
import ShowInterval
import SimpleLerpFunctorLPoint2f
import SimpleLerpFunctorLPoint3f
import SimpleLerpFunctorLPoint4f
import SimpleLerpFunctorLVecBase2f
import SimpleLerpFunctorLVecBase3f
import SimpleLerpFunctorLVecBase4f
import SimpleLerpFunctorLVector2f
import SimpleLerpFunctorLVector3f
import SimpleLerpFunctorLVector4f
import StaticTextFont
import TexCoordName
import TextNode
import TextureStage
import VirtualFileComposite
import VirtualFileSimple
import WaitInterval
import ActorNode
import AlphaTestAttrib
import AmbientLight
import AnalogNode
import AngularVectorForce
import AnimBundle
import AnimChannelBase
import BillboardEffect
import BoundingLine
import ButtonNode
import ButtonThrower
import CLerpAnimEffectInterval
import CLerpNodePathInterval
import Camera
import Character
import ClipPlaneAttrib
import CollisionHandlerPhysical
import CollisionPlane
import CollisionRay
import CollisionSegment
import CollisionSphere
import CollisionTube
import ColorAttrib
import ColorBlendAttrib
import ColorLerpFunctor
import ColorScaleAttrib
import ColorScaleLerpFunctor
import ColorWriteAttrib
import CompassEffect
import CubicCurveseg
import CullBinAttrib
import CullFaceAttrib
import CylindricalLens
import DNAFlatBuilding
import DNAFlatDoor
import DNALandmarkBuilding
import DNAProp
import DNASign
import DNASignBaseline
import DNASignGraphic
import DNASignText
import DNAStreet
import DNAWall
import DecalEffect
import DepthOffsetAttrib
import DepthTestAttrib
import DepthWriteAttrib
import DialNode
import DirectionalLight
import EggGroupUniquifier
import EggNode
import EggPolysetMaker
import EggPoolUniquifier
import EggVertexUV
import FadeLODNode
import FiniteBoundingVolume
import FisheyeLens
import FloatQueryLerpFunctor
import FogAttrib
import FrameRateMeter
import Geom
import GraphicsBuffer
import GraphicsStateGuardian
import GraphicsWindow
import HprLerpFunctor
import IntQueryLerpFunctor
import LightAttrib
import LightLensNode
import LinearCylinderVortexForce
import LinearDistanceForce
import LinearFrictionForce
import LinearRandomForce
import LinearUserDefinedForce
import LinearVectorForce
import MaterialAttrib
import MatrixLens
import ModelRoot
import MouseAndKeyboard
import MouseInterfaceNode
import MouseRecorder
import MouseWatcher
import MovingPartBase
import Nametag2d
import NametagFloat2d
import NametagFloat3d
import OmniBoundingVolume
import OrthographicLens
import PGButton
import PGEntry
import PGMouseWatcherBackground
import PGSliderBar
import PGWaitBar
import PSphereLens
import ParasiteBuffer
import PartBundle
import PerspectiveLens
import PiecewiseCurve
import PointLight
import PolylightEffect
import PosLerpFunctor
import RenderModeAttrib
import RenderState
import RescaleNormalAttrib
import ScaleLerpFunctor
import SequenceNode
import ShowBoundsEffect
import SimpleQueryLerpFunctorLPoint2f
import SimpleQueryLerpFunctorLPoint3f
import SimpleQueryLerpFunctorLPoint4f
import SimpleQueryLerpFunctorLVecBase2f
import SimpleQueryLerpFunctorLVecBase3f
import SimpleQueryLerpFunctorLVecBase4f
import SimpleQueryLerpFunctorLVector2f
import SimpleQueryLerpFunctorLVector3f
import SimpleQueryLerpFunctorLVector4f
import SwitchNode
import TexGenAttrib
import TexMatrixAttrib
import TexProjectorEffect
import Texture
import TextureApplyAttrib
import TextureAttrib
import TrackerNode
import Transform2SG
import TransformState
import TransparencyAttrib
import VirtualMouse
import WhisperPopup
import AnimChannelACMatrixSwitchType
import AnimChannelACScalarSwitchType
import BoundingSphere
import CharacterJointBundle
import CollisionHandlerFloor
import CollisionHandlerGravity
import CollisionHandlerPusher
import CollisionInvSphere
import CollisionLine
import CollisionPolygon
import DriveInterface
import DynamicTextPage
import EggAnimData
import EggComment
import EggFilenameNode
import EggGroupNode
import EggMaterial
import EggPrimitive
import EggVertexPool
import GeomLine
import GeomLinestrip
import GeomPoint
import GeomPolygon
import GeomQuad
import GeomSphere
import GeomSprite
import GeomTri
import GeomTrifan
import GeomTristrip
import HermiteCurve
import LinearJitterForce
import LinearNoiseForce
import LinearSinkForce
import LinearSourceForce
import MovingPartACMatrixSwitchType
import NurbsCurve
import PGSliderButton
import Spotlight
import Trackball
import AnimChannelMatrixDynamic
import AnimChannelMatrixXfmTable
import AnimChannelScalarDynamic
import AnimChannelScalarTable
import EggCurve
import EggData
import EggExternalReference
import EggGroup
import EggLine
import EggPoint
import EggPolygon
import EggSAnimData
import EggSurface
import EggTable
import EggTexture
import EggXfmAnimData
import EggXfmSAnim
import GeomTextGlyph
import MovingPartMatrix
import PhysicsCollisionHandler
import CharacterJoint
import EggBin
import EggNurbsCurve
from libtoontownGlobals import *
AccumulatedAttribs = AccumulatedAttribs.AccumulatedAttribs
AngularIntegrator = AngularIntegrator.AngularIntegrator
AnimControlCollection = AnimControlCollection.AnimControlCollection
AsyncUtility = AsyncUtility.AsyncUtility
BamFile = BamFile.BamFile
BaseParticle = BaseParticle.BaseParticle
BitMask32 = BitMask32.BitMask32
BoundedObject = BoundedObject.BoundedObject
Buffer = Buffer.Buffer
ButtonHandle = ButtonHandle.ButtonHandle
ButtonRegistry = ButtonRegistry.ButtonRegistry
CConnectionRepository = CConnectionRepository.CConnectionRepository
CDistributedSmoothNodeBase = CDistributedSmoothNodeBase.CDistributedSmoothNodeBase
CIntervalManager = CIntervalManager.CIntervalManager
CPTAFloat = CPTAFloat.CPTAFloat
CPetBrain = CPetBrain.CPetBrain
CString = CString.CString
ClickablePopup = ClickablePopup.ClickablePopup
ClockObject = ClockObject.ClockObject
ComputedVertices = ComputedVertices.ComputedVertices
ConfigConfigureGetConfigConfigShowbase = ConfigConfigureGetConfigConfigShowbase.ConfigConfigureGetConfigConfigShowbase
ConfigDeclaration = ConfigDeclaration.ConfigDeclaration
ConfigExpress = ConfigExpress.ConfigExpress
ConfigFlags = ConfigFlags.ConfigFlags
ConfigPage = ConfigPage.ConfigPage
ConfigPageManager = ConfigPageManager.ConfigPageManager
ConfigVariableCore = ConfigVariableCore.ConfigVariableCore
ConfigVariableManager = ConfigVariableManager.ConfigVariableManager
CullBinManager = CullBinManager.CullBinManager
CullableObject = CullableObject.CullableObject
CurveFitter = CurveFitter.CurveFitter
DCDeclaration = DCDeclaration.DCDeclaration
DCFile = DCFile.DCFile
DCPackData = DCPackData.DCPackData
DCPacker = DCPacker.DCPacker
DCPackerInterface = DCPackerInterface.DCPackerInterface
DNALoader = DNALoader.DNALoader
DNAStorage = DNAStorage.DNAStorage
DSearchPath = DSearchPath.DSearchPath
DataGraphTraverser = DataGraphTraverser.DataGraphTraverser
DataNodeTransmit = DataNodeTransmit.DataNodeTransmit
DatagramIterator = DatagramIterator.DatagramIterator
Decompressor = Decompressor.Decompressor
DocumentSpec = DocumentSpec.DocumentSpec
DownloadDb = DownloadDb.DownloadDb
DrawableRegion = DrawableRegion.DrawableRegion
EggAttributes = EggAttributes.EggAttributes
EggMaterialCollection = EggMaterialCollection.EggMaterialCollection
EggRenderMode = EggRenderMode.EggRenderMode
EggTextureCollection = EggTextureCollection.EggTextureCollection
EggTransform3d = EggTransform3d.EggTransform3d
EventParameter = EventParameter.EventParameter
EventQueue = EventQueue.EventQueue
EventReceiver = EventReceiver.EventReceiver
Extractor = Extractor.Extractor
FILE = FILE.FILE
Filename = Filename.Filename
FontPool = FontPool.FontPool
FrameBufferProperties = FrameBufferProperties.FrameBufferProperties
FreetypeFont = FreetypeFont.FreetypeFont
Frustum = Frustum.Frustum
FrustumD = FrustumD.FrustumD
Fstream = Fstream.Fstream
GeomTransformer = GeomTransformer.GeomTransformer
GlobPattern = GlobPattern.GlobPattern
GraphicsEngine = GraphicsEngine.GraphicsEngine
GraphicsPipeSelection = GraphicsPipeSelection.GraphicsPipeSelection
GraphicsThreadingModel = GraphicsThreadingModel.GraphicsThreadingModel
HTTPClient = HTTPClient.HTTPClient
HTTPCookie = HTTPCookie.HTTPCookie
HTTPDate = HTTPDate.HTTPDate
HTTPEntityTag = HTTPEntityTag.HTTPEntityTag
HTTPEnum = HTTPEnum.HTTPEnum
HashVal = HashVal.HashVal
Ifstream = Ifstream.Ifstream
Istream = Istream.Istream
KeyboardButton = KeyboardButton.KeyboardButton
LinearIntegrator = LinearIntegrator.LinearIntegrator
LoaderFileType = LoaderFileType.LoaderFileType
MapPointerToEggMaterialPointerToEggMaterial = MapPointerToEggMaterialPointerToEggMaterial.MapPointerToEggMaterialPointerToEggMaterial
MapPointerToEggTexturePointerToEggTexture = MapPointerToEggTexturePointerToEggTexture.MapPointerToEggTexturePointerToEggTexture
Mat3 = Mat3.Mat3
Mat3D = Mat3D.Mat3D
Mat4 = Mat4.Mat4
Mat4D = Mat4D.Mat4D
MaterialPool = MaterialPool.MaterialPool
MathNumbers = MathNumbers.MathNumbers
Mersenne = Mersenne.Mersenne
ModelPool = ModelPool.ModelPool
ModifierButtons = ModifierButtons.ModifierButtons
MouseButton = MouseButton.MouseButton
MouseData = MouseData.MouseData
MouseWatcherParameter = MouseWatcherParameter.MouseWatcherParameter
MultitexReducer = MultitexReducer.MultitexReducer
Namable = Namable.Namable
NametagGlobals = NametagGlobals.NametagGlobals
NametagGroup = NametagGroup.NametagGroup
NodePath = NodePath.NodePath
NodePathCollection = NodePathCollection.NodePathCollection
NonlinearImager = NonlinearImager.NonlinearImager
Notify = Notify.Notify
NotifyCategory = NotifyCategory.NotifyCategory
NurbsCurveInterface = NurbsCurveInterface.NurbsCurveInterface
Ofstream = Ofstream.Ofstream
Ostream = Ostream.Ostream
PGFrameStyle = PGFrameStyle.PGFrameStyle
PNMFileType = PNMFileType.PNMFileType
PNMImageHeader = PNMImageHeader.PNMImageHeader
PNMReader = PNMReader.PNMReader
PNMWriter = PNMWriter.PNMWriter
PStatClient = PStatClient.PStatClient
PStatCollector = PStatCollector.PStatCollector
PTADouble = PTADouble.PTADouble
PTAInt = PTAInt.PTAInt
PTAUshort = PTAUshort.PTAUshort
ParticleSystemManager = ParticleSystemManager.ParticleSystemManager
Patcher = Patcher.Patcher
Patchfile = Patchfile.Patchfile
PhysicsManager = PhysicsManager.PhysicsManager
Pipeline = Pipeline.Pipeline
PixelBuffer = PixelBuffer.PixelBuffer
PointerToBaseRefCountObjvectorLPoint2f = PointerToBaseRefCountObjvectorLPoint2f.PointerToBaseRefCountObjvectorLPoint2f
PointerToBaseRefCountObjvectorLPoint3f = PointerToBaseRefCountObjvectorLPoint3f.PointerToBaseRefCountObjvectorLPoint3f
PointerToBaseRefCountObjvectorLVecBase4f = PointerToBaseRefCountObjvectorLVecBase4f.PointerToBaseRefCountObjvectorLVecBase4f
PointerToBaseRefCountObjvectorLVector3f = PointerToBaseRefCountObjvectorLVector3f.PointerToBaseRefCountObjvectorLVector3f
PointerToVoid = PointerToVoid.PointerToVoid
PosHpr = PosHpr.PosHpr
PreparedGraphicsObjects = PreparedGraphicsObjects.PreparedGraphicsObjects
ProfileTimer = ProfileTimer.ProfileTimer
Ramfile = Ramfile.Ramfile
ReferenceCount = ReferenceCount.ReferenceCount
SceneGraphReducer = SceneGraphReducer.SceneGraphReducer
Settings = Settings.Settings
SmoothMover = SmoothMover.SmoothMover
StreamReader = StreamReader.StreamReader
StreamWriter = StreamWriter.StreamWriter
SuitLeg = SuitLeg.SuitLeg
SuitLegList = SuitLegList.SuitLegList
TextEncoder = TextEncoder.TextEncoder
TextProperties = TextProperties.TextProperties
TextPropertiesManager = TextPropertiesManager.TextPropertiesManager
TextureCollection = TextureCollection.TextureCollection
TexturePool = TexturePool.TexturePool
TextureStageCollection = TextureStageCollection.TextureStageCollection
TimeVal = TimeVal.TimeVal
TypeHandle = TypeHandle.TypeHandle
TypeRegistry = TypeRegistry.TypeRegistry
TypedObject = TypedObject.TypedObject
URLSpec = URLSpec.URLSpec
UniqueIdAllocator = UniqueIdAllocator.UniqueIdAllocator
UpdateSeq = UpdateSeq.UpdateSeq
VBase2 = VBase2.VBase2
VBase2D = VBase2D.VBase2D
VBase3 = VBase3.VBase3
VBase3D = VBase3D.VBase3D
VBase4 = VBase4.VBase4
VBase4D = VBase4D.VBase4D
VectorNodePath = VectorNodePath.VectorNodePath
VectorURLSpec = VectorURLSpec.VectorURLSpec
VectorbasicStringchar = VectorbasicStringchar.VectorbasicStringchar
VirtualFileSystem = VirtualFileSystem.VirtualFileSystem
WindowProperties = WindowProperties.WindowProperties
WindowsRegistry = WindowsRegistry.WindowsRegistry
Xel = Xel.Xel
AngularEulerIntegrator = AngularEulerIntegrator.AngularEulerIntegrator
AnimControl = AnimControl.AnimControl
BaseParticleEmitter = BaseParticleEmitter.BaseParticleEmitter
BaseParticleFactory = BaseParticleFactory.BaseParticleFactory
BaseParticleRenderer = BaseParticleRenderer.BaseParticleRenderer
CardMaker = CardMaker.CardMaker
ChatBalloon = ChatBalloon.ChatBalloon
CollisionTraverser = CollisionTraverser.CollisionTraverser
ConfigVariableBase = ConfigVariableBase.ConfigVariableBase
DCClass = DCClass.DCClass
DCField = DCField.DCField
DCSwitch = DCSwitch.DCSwitch
DCTypedef = DCTypedef.DCTypedef
Datagram = Datagram.Datagram
DisplayRegion = DisplayRegion.DisplayRegion
EventHandler = EventHandler.EventHandler
ISocketStream = ISocketStream.ISocketStream
Iostream = Iostream.Iostream
Light = Light.Light
LineSegs = LineSegs.LineSegs
LineStream = LineStream.LineStream
LinearEulerIntegrator = LinearEulerIntegrator.LinearEulerIntegrator
MouseWatcherGroup = MouseWatcherGroup.MouseWatcherGroup
Multifile = Multifile.Multifile
MultiplexStream = MultiplexStream.MultiplexStream
Nametag = Nametag.Nametag
NurbsCurveEvaluator = NurbsCurveEvaluator.NurbsCurveEvaluator
NurbsCurveResult = NurbsCurveResult.NurbsCurveResult
NurbsSurfaceEvaluator = NurbsSurfaceEvaluator.NurbsSurfaceEvaluator
NurbsSurfaceResult = NurbsSurfaceResult.NurbsSurfaceResult
OSocketStream = OSocketStream.OSocketStream
PNMImage = PNMImage.PNMImage
PTAColorf = PTAColorf.PTAColorf
PTANormalf = PTANormalf.PTANormalf
PTATexCoordf = PTATexCoordf.PTATexCoordf
PTAVertexf = PTAVertexf.PTAVertexf
PandaLoader = PandaLoader.PandaLoader
ParametricCurveCollection = ParametricCurveCollection.ParametricCurveCollection
ParametricCurveDrawer = ParametricCurveDrawer.ParametricCurveDrawer
Plane = Plane.Plane
PlaneD = PlaneD.PlaneD
Point2 = Point2.Point2
Point2D = Point2D.Point2D
Point3 = Point3.Point3
Point3D = Point3D.Point3D
Point4 = Point4.Point4
Point4D = Point4D.Point4D
PointerToBaseRefCountObjvectorunsignedchar = PointerToBaseRefCountObjvectorunsignedchar.PointerToBaseRefCountObjvectorunsignedchar
Quat = Quat.Quat
QuatD = QuatD.QuatD
RecorderBase = RecorderBase.RecorderBase
TypedReferenceCount = TypedReferenceCount.TypedReferenceCount
TypedWritable = TypedWritable.TypedWritable
Vec2 = Vec2.Vec2
Vec2D = Vec2D.Vec2D
Vec3 = Vec3.Vec3
Vec3D = Vec3D.Vec3D
Vec4 = Vec4.Vec4
Vec4D = Vec4D.Vec4D
VirtualFileList = VirtualFileList.VirtualFileList
WeakPointerToVoid = WeakPointerToVoid.WeakPointerToVoid
AudioManager = AudioManager.AudioManager
AudioSound = AudioSound.AudioSound
AutonomousLerp = AutonomousLerp.AutonomousLerp
AuxSceneData = AuxSceneData.AuxSceneData
BaseForce = BaseForce.BaseForce
BoundingVolume = BoundingVolume.BoundingVolume
BoxEmitter = BoxEmitter.BoxEmitter
CImpulse = CImpulse.CImpulse
CInterval = CInterval.CInterval
CMover = CMover.CMover
ClientBase = ClientBase.ClientBase
CollisionHandler = CollisionHandler.CollisionHandler
ConfigVariable = ConfigVariable.ConfigVariable
ConfigVariableList = ConfigVariableList.ConfigVariableList
ConfigVariableSearchPath = ConfigVariableSearchPath.ConfigVariableSearchPath
DCAtomicField = DCAtomicField.DCAtomicField
DCMolecularField = DCMolecularField.DCMolecularField
DCParameter = DCParameter.DCParameter
DNABattleCell = DNABattleCell.DNABattleCell
DNAGroup = DNAGroup.DNAGroup
DNASuitEdge = DNASuitEdge.DNASuitEdge
DNASuitPath = DNASuitPath.DNASuitPath
DNASuitPoint = DNASuitPoint.DNASuitPoint
DiscEmitter = DiscEmitter.DiscEmitter
EggObject = EggObject.EggObject
EggUserData = EggUserData.EggUserData
Event = Event.Event
GeomParticleRenderer = GeomParticleRenderer.GeomParticleRenderer
GraphicsDevice = GraphicsDevice.GraphicsDevice
GraphicsPipe = GraphicsPipe.GraphicsPipe
LOrientationd = LOrientationd.LOrientationd
LOrientationf = LOrientationf.LOrientationf
LRotationd = LRotationd.LRotationd
LRotationf = LRotationf.LRotationf
Lerp = Lerp.Lerp
LerpBlendType = LerpBlendType.LerpBlendType
LerpFunctor = LerpFunctor.LerpFunctor
LineEmitter = LineEmitter.LineEmitter
LineParticleRenderer = LineParticleRenderer.LineParticleRenderer
NurbsCurveDrawer = NurbsCurveDrawer.NurbsCurveDrawer
PTAUchar = PTAUchar.PTAUchar
PandaNode = PandaNode.PandaNode
Physical = Physical.Physical
PhysicsObject = PhysicsObject.PhysicsObject
PointEmitter = PointEmitter.PointEmitter
PointParticleFactory = PointParticleFactory.PointParticleFactory
PointParticleRenderer = PointParticleRenderer.PointParticleRenderer
RecorderController = RecorderController.RecorderController
RectangleEmitter = RectangleEmitter.RectangleEmitter
RingEmitter = RingEmitter.RingEmitter
SocketStream = SocketStream.SocketStream
SocketStreamRecorder = SocketStreamRecorder.SocketStreamRecorder
SparkleParticleRenderer = SparkleParticleRenderer.SparkleParticleRenderer
SphereSurfaceEmitter = SphereSurfaceEmitter.SphereSurfaceEmitter
SphereVolumeEmitter = SphereVolumeEmitter.SphereVolumeEmitter
SpriteParticleRenderer = SpriteParticleRenderer.SpriteParticleRenderer
TangentRingEmitter = TangentRingEmitter.TangentRingEmitter
TextFont = TextFont.TextFont
TypedWritableReferenceCount = TypedWritableReferenceCount.TypedWritableReferenceCount
VirtualFile = VirtualFile.VirtualFile
WritableConfigurable = WritableConfigurable.WritableConfigurable
ZSpinParticleFactory = ZSpinParticleFactory.ZSpinParticleFactory
AngularForce = AngularForce.AngularForce
AnimBundleNode = AnimBundleNode.AnimBundleNode
AnimGroup = AnimGroup.AnimGroup
CLerpInterval = CLerpInterval.CLerpInterval
CMetaInterval = CMetaInterval.CMetaInterval
CPetChase = CPetChase.CPetChase
CPetFlee = CPetFlee.CPetFlee
CachedTypedWritableReferenceCount = CachedTypedWritableReferenceCount.CachedTypedWritableReferenceCount
CollisionEntry = CollisionEntry.CollisionEntry
CollisionHandlerEvent = CollisionHandlerEvent.CollisionHandlerEvent
CollisionHandlerQueue = CollisionHandlerQueue.CollisionHandlerQueue
CollisionNode = CollisionNode.CollisionNode
CollisionSolid = CollisionSolid.CollisionSolid
ConfigVariableBool = ConfigVariableBool.ConfigVariableBool
ConfigVariableDouble = ConfigVariableDouble.ConfigVariableDouble
ConfigVariableFilename = ConfigVariableFilename.ConfigVariableFilename
ConfigVariableInt = ConfigVariableInt.ConfigVariableInt
ConfigVariableString = ConfigVariableString.ConfigVariableString
DCArrayParameter = DCArrayParameter.DCArrayParameter
DCClassParameter = DCClassParameter.DCClassParameter
DCSimpleParameter = DCSimpleParameter.DCSimpleParameter
DCSwitchParameter = DCSwitchParameter.DCSwitchParameter
DDrawable = DDrawable.DDrawable
DNACornice = DNACornice.DNACornice
DNAData = DNAData.DNAData
DNADoor = DNADoor.DNADoor
DNANode = DNANode.DNANode
DNAVisGroup = DNAVisGroup.DNAVisGroup
DNAWindows = DNAWindows.DNAWindows
DataNode = DataNode.DataNode
DynamicTextFont = DynamicTextFont.DynamicTextFont
EaseInBlendType = EaseInBlendType.EaseInBlendType
EaseInOutBlendType = EaseInOutBlendType.EaseInOutBlendType
EaseOutBlendType = EaseOutBlendType.EaseOutBlendType
EggBinMaker = EggBinMaker.EggBinMaker
EggNameUniquifier = EggNameUniquifier.EggNameUniquifier
EggNamedObject = EggNamedObject.EggNamedObject
EggSwitchCondition = EggSwitchCondition.EggSwitchCondition
EggVertex = EggVertex.EggVertex
FloatLerpFunctor = FloatLerpFunctor.FloatLerpFunctor
Fog = Fog.Fog
ForceNode = ForceNode.ForceNode
GeomNode = GeomNode.GeomNode
GeometricBoundingVolume = GeometricBoundingVolume.GeometricBoundingVolume
GraphicsOutput = GraphicsOutput.GraphicsOutput
GraphicsStateGuardianBase = GraphicsStateGuardianBase.GraphicsStateGuardianBase
HTTPChannel = HTTPChannel.HTTPChannel
HideInterval = HideInterval.HideInterval
HprScaleLerpFunctor = HprScaleLerpFunctor.HprScaleLerpFunctor
ImageBuffer = ImageBuffer.ImageBuffer
IntLerpFunctor = IntLerpFunctor.IntLerpFunctor
LODNode = LODNode.LODNode
Lens = Lens.Lens
LensNode = LensNode.LensNode
LightNode = LightNode.LightNode
LinearForce = LinearForce.LinearForce
MarginManager = MarginManager.MarginManager
MarginPopup = MarginPopup.MarginPopup
Material = Material.Material
ModelNode = ModelNode.ModelNode
MouseWatcherRegion = MouseWatcherRegion.MouseWatcherRegion
MultiLerpFunctor = MultiLerpFunctor.MultiLerpFunctor
Nametag3d = Nametag3d.Nametag3d
NoBlendType = NoBlendType.NoBlendType
PGItem = PGItem.PGItem
PGMouseWatcherParameter = PGMouseWatcherParameter.PGMouseWatcherParameter
PGTop = PGTop.PGTop
ParametricCurve = ParametricCurve.ParametricCurve
PartBundleNode = PartBundleNode.PartBundleNode
PartGroup = PartGroup.PartGroup
ParticleSystem = ParticleSystem.ParticleSystem
PhysicalNode = PhysicalNode.PhysicalNode
PlaneNode = PlaneNode.PlaneNode
PolylightNode = PolylightNode.PolylightNode
PortalNode = PortalNode.PortalNode
PosHprLerpFunctor = PosHprLerpFunctor.PosHprLerpFunctor
PosHprScaleLerpFunctor = PosHprScaleLerpFunctor.PosHprScaleLerpFunctor
ProjectionScreen = ProjectionScreen.ProjectionScreen
RenderAttrib = RenderAttrib.RenderAttrib
RenderEffect = RenderEffect.RenderEffect
RenderEffects = RenderEffects.RenderEffects
RopeNode = RopeNode.RopeNode
SelectiveChildNode = SelectiveChildNode.SelectiveChildNode
SheetNode = SheetNode.SheetNode
ShowInterval = ShowInterval.ShowInterval
SimpleLerpFunctorLPoint2f = SimpleLerpFunctorLPoint2f.SimpleLerpFunctorLPoint2f
SimpleLerpFunctorLPoint3f = SimpleLerpFunctorLPoint3f.SimpleLerpFunctorLPoint3f
SimpleLerpFunctorLPoint4f = SimpleLerpFunctorLPoint4f.SimpleLerpFunctorLPoint4f
SimpleLerpFunctorLVecBase2f = SimpleLerpFunctorLVecBase2f.SimpleLerpFunctorLVecBase2f
SimpleLerpFunctorLVecBase3f = SimpleLerpFunctorLVecBase3f.SimpleLerpFunctorLVecBase3f
SimpleLerpFunctorLVecBase4f = SimpleLerpFunctorLVecBase4f.SimpleLerpFunctorLVecBase4f
SimpleLerpFunctorLVector2f = SimpleLerpFunctorLVector2f.SimpleLerpFunctorLVector2f
SimpleLerpFunctorLVector3f = SimpleLerpFunctorLVector3f.SimpleLerpFunctorLVector3f
SimpleLerpFunctorLVector4f = SimpleLerpFunctorLVector4f.SimpleLerpFunctorLVector4f
StaticTextFont = StaticTextFont.StaticTextFont
TexCoordName = TexCoordName.TexCoordName
TextNode = TextNode.TextNode
TextureStage = TextureStage.TextureStage
VirtualFileComposite = VirtualFileComposite.VirtualFileComposite
VirtualFileSimple = VirtualFileSimple.VirtualFileSimple
WaitInterval = WaitInterval.WaitInterval
ActorNode = ActorNode.ActorNode
AlphaTestAttrib = AlphaTestAttrib.AlphaTestAttrib
AmbientLight = AmbientLight.AmbientLight
AnalogNode = AnalogNode.AnalogNode
AngularVectorForce = AngularVectorForce.AngularVectorForce
AnimBundle = AnimBundle.AnimBundle
AnimChannelBase = AnimChannelBase.AnimChannelBase
BillboardEffect = BillboardEffect.BillboardEffect
BoundingLine = BoundingLine.BoundingLine
ButtonNode = ButtonNode.ButtonNode
ButtonThrower = ButtonThrower.ButtonThrower
CLerpAnimEffectInterval = CLerpAnimEffectInterval.CLerpAnimEffectInterval
CLerpNodePathInterval = CLerpNodePathInterval.CLerpNodePathInterval
Camera = Camera.Camera
Character = Character.Character
ClipPlaneAttrib = ClipPlaneAttrib.ClipPlaneAttrib
CollisionHandlerPhysical = CollisionHandlerPhysical.CollisionHandlerPhysical
CollisionPlane = CollisionPlane.CollisionPlane
CollisionRay = CollisionRay.CollisionRay
CollisionSegment = CollisionSegment.CollisionSegment
CollisionSphere = CollisionSphere.CollisionSphere
CollisionTube = CollisionTube.CollisionTube
ColorAttrib = ColorAttrib.ColorAttrib
ColorBlendAttrib = ColorBlendAttrib.ColorBlendAttrib
ColorLerpFunctor = ColorLerpFunctor.ColorLerpFunctor
ColorScaleAttrib = ColorScaleAttrib.ColorScaleAttrib
ColorScaleLerpFunctor = ColorScaleLerpFunctor.ColorScaleLerpFunctor
ColorWriteAttrib = ColorWriteAttrib.ColorWriteAttrib
CompassEffect = CompassEffect.CompassEffect
CubicCurveseg = CubicCurveseg.CubicCurveseg
CullBinAttrib = CullBinAttrib.CullBinAttrib
CullFaceAttrib = CullFaceAttrib.CullFaceAttrib
CylindricalLens = CylindricalLens.CylindricalLens
DNAFlatBuilding = DNAFlatBuilding.DNAFlatBuilding
DNAFlatDoor = DNAFlatDoor.DNAFlatDoor
DNALandmarkBuilding = DNALandmarkBuilding.DNALandmarkBuilding
DNAProp = DNAProp.DNAProp
DNASign = DNASign.DNASign
DNASignBaseline = DNASignBaseline.DNASignBaseline
DNASignGraphic = DNASignGraphic.DNASignGraphic
DNASignText = DNASignText.DNASignText
DNAStreet = DNAStreet.DNAStreet
DNAWall = DNAWall.DNAWall
DecalEffect = DecalEffect.DecalEffect
DepthOffsetAttrib = DepthOffsetAttrib.DepthOffsetAttrib
DepthTestAttrib = DepthTestAttrib.DepthTestAttrib
DepthWriteAttrib = DepthWriteAttrib.DepthWriteAttrib
DialNode = DialNode.DialNode
DirectionalLight = DirectionalLight.DirectionalLight
EggGroupUniquifier = EggGroupUniquifier.EggGroupUniquifier
EggNode = EggNode.EggNode
EggPolysetMaker = EggPolysetMaker.EggPolysetMaker
EggPoolUniquifier = EggPoolUniquifier.EggPoolUniquifier
EggVertexUV = EggVertexUV.EggVertexUV
FadeLODNode = FadeLODNode.FadeLODNode
FiniteBoundingVolume = FiniteBoundingVolume.FiniteBoundingVolume
FisheyeLens = FisheyeLens.FisheyeLens
FloatQueryLerpFunctor = FloatQueryLerpFunctor.FloatQueryLerpFunctor
FogAttrib = FogAttrib.FogAttrib
FrameRateMeter = FrameRateMeter.FrameRateMeter
Geom = Geom.Geom
GraphicsBuffer = GraphicsBuffer.GraphicsBuffer
GraphicsStateGuardian = GraphicsStateGuardian.GraphicsStateGuardian
GraphicsWindow = GraphicsWindow.GraphicsWindow
HprLerpFunctor = HprLerpFunctor.HprLerpFunctor
IntQueryLerpFunctor = IntQueryLerpFunctor.IntQueryLerpFunctor
LightAttrib = LightAttrib.LightAttrib
LightLensNode = LightLensNode.LightLensNode
LinearCylinderVortexForce = LinearCylinderVortexForce.LinearCylinderVortexForce
LinearDistanceForce = LinearDistanceForce.LinearDistanceForce
LinearFrictionForce = LinearFrictionForce.LinearFrictionForce
LinearRandomForce = LinearRandomForce.LinearRandomForce
LinearUserDefinedForce = LinearUserDefinedForce.LinearUserDefinedForce
LinearVectorForce = LinearVectorForce.LinearVectorForce
MaterialAttrib = MaterialAttrib.MaterialAttrib
MatrixLens = MatrixLens.MatrixLens
ModelRoot = ModelRoot.ModelRoot
MouseAndKeyboard = MouseAndKeyboard.MouseAndKeyboard
MouseInterfaceNode = MouseInterfaceNode.MouseInterfaceNode
MouseRecorder = MouseRecorder.MouseRecorder
MouseWatcher = MouseWatcher.MouseWatcher
MovingPartBase = MovingPartBase.MovingPartBase
Nametag2d = Nametag2d.Nametag2d
NametagFloat2d = NametagFloat2d.NametagFloat2d
NametagFloat3d = NametagFloat3d.NametagFloat3d
OmniBoundingVolume = OmniBoundingVolume.OmniBoundingVolume
OrthographicLens = OrthographicLens.OrthographicLens
PGButton = PGButton.PGButton
PGEntry = PGEntry.PGEntry
PGMouseWatcherBackground = PGMouseWatcherBackground.PGMouseWatcherBackground
PGSliderBar = PGSliderBar.PGSliderBar
PGWaitBar = PGWaitBar.PGWaitBar
PSphereLens = PSphereLens.PSphereLens
ParasiteBuffer = ParasiteBuffer.ParasiteBuffer
PartBundle = PartBundle.PartBundle
PerspectiveLens = PerspectiveLens.PerspectiveLens
PiecewiseCurve = PiecewiseCurve.PiecewiseCurve
PointLight = PointLight.PointLight
PolylightEffect = PolylightEffect.PolylightEffect
PosLerpFunctor = PosLerpFunctor.PosLerpFunctor
RenderModeAttrib = RenderModeAttrib.RenderModeAttrib
RenderState = RenderState.RenderState
RescaleNormalAttrib = RescaleNormalAttrib.RescaleNormalAttrib
ScaleLerpFunctor = ScaleLerpFunctor.ScaleLerpFunctor
SequenceNode = SequenceNode.SequenceNode
ShowBoundsEffect = ShowBoundsEffect.ShowBoundsEffect
SimpleQueryLerpFunctorLPoint2f = SimpleQueryLerpFunctorLPoint2f.SimpleQueryLerpFunctorLPoint2f
SimpleQueryLerpFunctorLPoint3f = SimpleQueryLerpFunctorLPoint3f.SimpleQueryLerpFunctorLPoint3f
SimpleQueryLerpFunctorLPoint4f = SimpleQueryLerpFunctorLPoint4f.SimpleQueryLerpFunctorLPoint4f
SimpleQueryLerpFunctorLVecBase2f = SimpleQueryLerpFunctorLVecBase2f.SimpleQueryLerpFunctorLVecBase2f
SimpleQueryLerpFunctorLVecBase3f = SimpleQueryLerpFunctorLVecBase3f.SimpleQueryLerpFunctorLVecBase3f
SimpleQueryLerpFunctorLVecBase4f = SimpleQueryLerpFunctorLVecBase4f.SimpleQueryLerpFunctorLVecBase4f
SimpleQueryLerpFunctorLVector2f = SimpleQueryLerpFunctorLVector2f.SimpleQueryLerpFunctorLVector2f
SimpleQueryLerpFunctorLVector3f = SimpleQueryLerpFunctorLVector3f.SimpleQueryLerpFunctorLVector3f
SimpleQueryLerpFunctorLVector4f = SimpleQueryLerpFunctorLVector4f.SimpleQueryLerpFunctorLVector4f
SwitchNode = SwitchNode.SwitchNode
TexGenAttrib = TexGenAttrib.TexGenAttrib
TexMatrixAttrib = TexMatrixAttrib.TexMatrixAttrib
TexProjectorEffect = TexProjectorEffect.TexProjectorEffect
Texture = Texture.Texture
TextureApplyAttrib = TextureApplyAttrib.TextureApplyAttrib
TextureAttrib = TextureAttrib.TextureAttrib
TrackerNode = TrackerNode.TrackerNode
Transform2SG = Transform2SG.Transform2SG
TransformState = TransformState.TransformState
TransparencyAttrib = TransparencyAttrib.TransparencyAttrib
VirtualMouse = VirtualMouse.VirtualMouse
WhisperPopup = WhisperPopup.WhisperPopup
AnimChannelACMatrixSwitchType = AnimChannelACMatrixSwitchType.AnimChannelACMatrixSwitchType
AnimChannelACScalarSwitchType = AnimChannelACScalarSwitchType.AnimChannelACScalarSwitchType
BoundingSphere = BoundingSphere.BoundingSphere
CharacterJointBundle = CharacterJointBundle.CharacterJointBundle
CollisionHandlerFloor = CollisionHandlerFloor.CollisionHandlerFloor
CollisionHandlerGravity = CollisionHandlerGravity.CollisionHandlerGravity
CollisionHandlerPusher = CollisionHandlerPusher.CollisionHandlerPusher
CollisionInvSphere = CollisionInvSphere.CollisionInvSphere
CollisionLine = CollisionLine.CollisionLine
CollisionPolygon = CollisionPolygon.CollisionPolygon
DriveInterface = DriveInterface.DriveInterface
DynamicTextPage = DynamicTextPage.DynamicTextPage
EggAnimData = EggAnimData.EggAnimData
EggComment = EggComment.EggComment
EggFilenameNode = EggFilenameNode.EggFilenameNode
EggGroupNode = EggGroupNode.EggGroupNode
EggMaterial = EggMaterial.EggMaterial
EggPrimitive = EggPrimitive.EggPrimitive
EggVertexPool = EggVertexPool.EggVertexPool
GeomLine = GeomLine.GeomLine
GeomLinestrip = GeomLinestrip.GeomLinestrip
GeomPoint = GeomPoint.GeomPoint
GeomPolygon = GeomPolygon.GeomPolygon
GeomQuad = GeomQuad.GeomQuad
GeomSphere = GeomSphere.GeomSphere
GeomSprite = GeomSprite.GeomSprite
GeomTri = GeomTri.GeomTri
GeomTrifan = GeomTrifan.GeomTrifan
GeomTristrip = GeomTristrip.GeomTristrip
HermiteCurve = HermiteCurve.HermiteCurve
LinearJitterForce = LinearJitterForce.LinearJitterForce
LinearNoiseForce = LinearNoiseForce.LinearNoiseForce
LinearSinkForce = LinearSinkForce.LinearSinkForce
LinearSourceForce = LinearSourceForce.LinearSourceForce
MovingPartACMatrixSwitchType = MovingPartACMatrixSwitchType.MovingPartACMatrixSwitchType
NurbsCurve = NurbsCurve.NurbsCurve
PGSliderButton = PGSliderButton.PGSliderButton
Spotlight = Spotlight.Spotlight
Trackball = Trackball.Trackball
AnimChannelMatrixDynamic = AnimChannelMatrixDynamic.AnimChannelMatrixDynamic
AnimChannelMatrixXfmTable = AnimChannelMatrixXfmTable.AnimChannelMatrixXfmTable
AnimChannelScalarDynamic = AnimChannelScalarDynamic.AnimChannelScalarDynamic
AnimChannelScalarTable = AnimChannelScalarTable.AnimChannelScalarTable
EggCurve = EggCurve.EggCurve
EggData = EggData.EggData
EggExternalReference = EggExternalReference.EggExternalReference
EggGroup = EggGroup.EggGroup
EggLine = EggLine.EggLine
EggPoint = EggPoint.EggPoint
EggPolygon = EggPolygon.EggPolygon
EggSAnimData = EggSAnimData.EggSAnimData
EggSurface = EggSurface.EggSurface
EggTable = EggTable.EggTable
EggTexture = EggTexture.EggTexture
EggXfmAnimData = EggXfmAnimData.EggXfmAnimData
EggXfmSAnim = EggXfmSAnim.EggXfmSAnim
GeomTextGlyph = GeomTextGlyph.GeomTextGlyph
MovingPartMatrix = MovingPartMatrix.MovingPartMatrix
PhysicsCollisionHandler = PhysicsCollisionHandler.PhysicsCollisionHandler
CharacterJoint = CharacterJoint.CharacterJoint
EggBin = EggBin.EggBin
EggNurbsCurve = EggNurbsCurve.EggNurbsCurve
from direct.ffi.FFIExternalObject import registerInTypeMap
registerInTypeMap(AccumulatedAttribs)
registerInTypeMap(AngularIntegrator)
registerInTypeMap(AnimControlCollection)
registerInTypeMap(AsyncUtility)
registerInTypeMap(BamFile)
registerInTypeMap(BaseParticle)
registerInTypeMap(BitMask32)
registerInTypeMap(BoundedObject)
registerInTypeMap(Buffer)
registerInTypeMap(ButtonHandle)
registerInTypeMap(ButtonRegistry)
registerInTypeMap(CConnectionRepository)
registerInTypeMap(CDistributedSmoothNodeBase)
registerInTypeMap(CIntervalManager)
registerInTypeMap(CPTAFloat)
registerInTypeMap(CPetBrain)
registerInTypeMap(CString)
registerInTypeMap(ClickablePopup)
registerInTypeMap(ClockObject)
registerInTypeMap(ComputedVertices)
registerInTypeMap(ConfigConfigureGetConfigConfigShowbase)
registerInTypeMap(ConfigDeclaration)
registerInTypeMap(ConfigExpress)
registerInTypeMap(ConfigFlags)
registerInTypeMap(ConfigPage)
registerInTypeMap(ConfigPageManager)
registerInTypeMap(ConfigVariableCore)
registerInTypeMap(ConfigVariableManager)
registerInTypeMap(CullBinManager)
registerInTypeMap(CullableObject)
registerInTypeMap(CurveFitter)
registerInTypeMap(DCDeclaration)
registerInTypeMap(DCFile)
registerInTypeMap(DCPackData)
registerInTypeMap(DCPacker)
registerInTypeMap(DCPackerInterface)
registerInTypeMap(DNALoader)
registerInTypeMap(DNAStorage)
registerInTypeMap(DSearchPath)
registerInTypeMap(DataGraphTraverser)
registerInTypeMap(DataNodeTransmit)
registerInTypeMap(DatagramIterator)
registerInTypeMap(Decompressor)
registerInTypeMap(DocumentSpec)
registerInTypeMap(DownloadDb)
registerInTypeMap(DrawableRegion)
registerInTypeMap(EggAttributes)
registerInTypeMap(EggMaterialCollection)
registerInTypeMap(EggRenderMode)
registerInTypeMap(EggTextureCollection)
registerInTypeMap(EggTransform3d)
registerInTypeMap(EventParameter)
registerInTypeMap(EventQueue)
registerInTypeMap(EventReceiver)
registerInTypeMap(Extractor)
registerInTypeMap(FILE)
registerInTypeMap(Filename)
registerInTypeMap(FontPool)
registerInTypeMap(FrameBufferProperties)
registerInTypeMap(FreetypeFont)
registerInTypeMap(Frustum)
registerInTypeMap(FrustumD)
registerInTypeMap(Fstream)
registerInTypeMap(GeomTransformer)
registerInTypeMap(GlobPattern)
registerInTypeMap(GraphicsEngine)
registerInTypeMap(GraphicsPipeSelection)
registerInTypeMap(GraphicsThreadingModel)
registerInTypeMap(HTTPClient)
registerInTypeMap(HTTPCookie)
registerInTypeMap(HTTPDate)
registerInTypeMap(HTTPEntityTag)
registerInTypeMap(HTTPEnum)
registerInTypeMap(HashVal)
registerInTypeMap(Ifstream)
registerInTypeMap(Istream)
registerInTypeMap(KeyboardButton)
registerInTypeMap(LinearIntegrator)
registerInTypeMap(LoaderFileType)
registerInTypeMap(MapPointerToEggMaterialPointerToEggMaterial)
registerInTypeMap(MapPointerToEggTexturePointerToEggTexture)
registerInTypeMap(Mat3)
registerInTypeMap(Mat3D)
registerInTypeMap(Mat4)
registerInTypeMap(Mat4D)
registerInTypeMap(MaterialPool)
registerInTypeMap(MathNumbers)
registerInTypeMap(Mersenne)
registerInTypeMap(ModelPool)
registerInTypeMap(ModifierButtons)
registerInTypeMap(MouseButton)
registerInTypeMap(MouseData)
registerInTypeMap(MouseWatcherParameter)
registerInTypeMap(MultitexReducer)
registerInTypeMap(Namable)
registerInTypeMap(NametagGlobals)
registerInTypeMap(NametagGroup)
registerInTypeMap(NodePath)
registerInTypeMap(NodePathCollection)
registerInTypeMap(NonlinearImager)
registerInTypeMap(Notify)
registerInTypeMap(NotifyCategory)
registerInTypeMap(NurbsCurveInterface)
registerInTypeMap(Ofstream)
registerInTypeMap(Ostream)
registerInTypeMap(PGFrameStyle)
registerInTypeMap(PNMFileType)
registerInTypeMap(PNMImageHeader)
registerInTypeMap(PNMReader)
registerInTypeMap(PNMWriter)
registerInTypeMap(PStatClient)
registerInTypeMap(PStatCollector)
registerInTypeMap(PTADouble)
registerInTypeMap(PTAInt)
registerInTypeMap(PTAUshort)
registerInTypeMap(ParticleSystemManager)
registerInTypeMap(Patcher)
registerInTypeMap(Patchfile)
registerInTypeMap(PhysicsManager)
registerInTypeMap(Pipeline)
registerInTypeMap(PixelBuffer)
registerInTypeMap(PointerToBaseRefCountObjvectorLPoint2f)
registerInTypeMap(PointerToBaseRefCountObjvectorLPoint3f)
registerInTypeMap(PointerToBaseRefCountObjvectorLVecBase4f)
registerInTypeMap(PointerToBaseRefCountObjvectorLVector3f)
registerInTypeMap(PointerToVoid)
registerInTypeMap(PosHpr)
registerInTypeMap(PreparedGraphicsObjects)
registerInTypeMap(ProfileTimer)
registerInTypeMap(Ramfile)
registerInTypeMap(ReferenceCount)
registerInTypeMap(SceneGraphReducer)
registerInTypeMap(Settings)
registerInTypeMap(SmoothMover)
registerInTypeMap(StreamReader)
registerInTypeMap(StreamWriter)
registerInTypeMap(SuitLeg)
registerInTypeMap(SuitLegList)
registerInTypeMap(TextEncoder)
registerInTypeMap(TextProperties)
registerInTypeMap(TextPropertiesManager)
registerInTypeMap(TextureCollection)
registerInTypeMap(TexturePool)
registerInTypeMap(TextureStageCollection)
registerInTypeMap(TimeVal)
registerInTypeMap(TypeHandle)
registerInTypeMap(TypeRegistry)
registerInTypeMap(TypedObject)
registerInTypeMap(URLSpec)
registerInTypeMap(UniqueIdAllocator)
registerInTypeMap(UpdateSeq)
registerInTypeMap(VBase2)
registerInTypeMap(VBase2D)
registerInTypeMap(VBase3)
registerInTypeMap(VBase3D)
registerInTypeMap(VBase4)
registerInTypeMap(VBase4D)
registerInTypeMap(VectorNodePath)
registerInTypeMap(VectorURLSpec)
registerInTypeMap(VectorbasicStringchar)
registerInTypeMap(VirtualFileSystem)
registerInTypeMap(WindowProperties)
registerInTypeMap(WindowsRegistry)
registerInTypeMap(Xel)
registerInTypeMap(AngularEulerIntegrator)
registerInTypeMap(AnimControl)
registerInTypeMap(BaseParticleEmitter)
registerInTypeMap(BaseParticleFactory)
registerInTypeMap(BaseParticleRenderer)
registerInTypeMap(CardMaker)
registerInTypeMap(ChatBalloon)
registerInTypeMap(CollisionTraverser)
registerInTypeMap(ConfigVariableBase)
registerInTypeMap(DCClass)
registerInTypeMap(DCField)
registerInTypeMap(DCSwitch)
registerInTypeMap(DCTypedef)
registerInTypeMap(Datagram)
registerInTypeMap(DisplayRegion)
registerInTypeMap(EventHandler)
registerInTypeMap(ISocketStream)
registerInTypeMap(Iostream)
registerInTypeMap(Light)
registerInTypeMap(LineSegs)
registerInTypeMap(LineStream)
registerInTypeMap(LinearEulerIntegrator)
registerInTypeMap(MouseWatcherGroup)
registerInTypeMap(Multifile)
registerInTypeMap(MultiplexStream)
registerInTypeMap(Nametag)
registerInTypeMap(NurbsCurveEvaluator)
registerInTypeMap(NurbsCurveResult)
registerInTypeMap(NurbsSurfaceEvaluator)
registerInTypeMap(NurbsSurfaceResult)
registerInTypeMap(OSocketStream)
registerInTypeMap(PNMImage)
registerInTypeMap(PTAColorf)
registerInTypeMap(PTANormalf)
registerInTypeMap(PTATexCoordf)
registerInTypeMap(PTAVertexf)
registerInTypeMap(PandaLoader)
registerInTypeMap(ParametricCurveCollection)
registerInTypeMap(ParametricCurveDrawer)
registerInTypeMap(Plane)
registerInTypeMap(PlaneD)
registerInTypeMap(Point2)
registerInTypeMap(Point2D)
registerInTypeMap(Point3)
registerInTypeMap(Point3D)
registerInTypeMap(Point4)
registerInTypeMap(Point4D)
registerInTypeMap(PointerToBaseRefCountObjvectorunsignedchar)
registerInTypeMap(Quat)
registerInTypeMap(QuatD)
registerInTypeMap(RecorderBase)
registerInTypeMap(TypedReferenceCount)
registerInTypeMap(TypedWritable)
registerInTypeMap(Vec2)
registerInTypeMap(Vec2D)
registerInTypeMap(Vec3)
registerInTypeMap(Vec3D)
registerInTypeMap(Vec4)
registerInTypeMap(Vec4D)
registerInTypeMap(VirtualFileList)
registerInTypeMap(WeakPointerToVoid)
registerInTypeMap(AudioManager)
registerInTypeMap(AudioSound)
registerInTypeMap(AutonomousLerp)
registerInTypeMap(AuxSceneData)
registerInTypeMap(BaseForce)
registerInTypeMap(BoundingVolume)
registerInTypeMap(BoxEmitter)
registerInTypeMap(CImpulse)
registerInTypeMap(CInterval)
registerInTypeMap(CMover)
registerInTypeMap(ClientBase)
registerInTypeMap(CollisionHandler)
registerInTypeMap(ConfigVariable)
registerInTypeMap(ConfigVariableList)
registerInTypeMap(ConfigVariableSearchPath)
registerInTypeMap(DCAtomicField)
registerInTypeMap(DCMolecularField)
registerInTypeMap(DCParameter)
registerInTypeMap(DNABattleCell)
registerInTypeMap(DNAGroup)
registerInTypeMap(DNASuitEdge)
registerInTypeMap(DNASuitPath)
registerInTypeMap(DNASuitPoint)
registerInTypeMap(DiscEmitter)
registerInTypeMap(EggObject)
registerInTypeMap(EggUserData)
registerInTypeMap(Event)
registerInTypeMap(GeomParticleRenderer)
registerInTypeMap(GraphicsDevice)
registerInTypeMap(GraphicsPipe)
registerInTypeMap(LOrientationd)
registerInTypeMap(LOrientationf)
registerInTypeMap(LRotationd)
registerInTypeMap(LRotationf)
registerInTypeMap(Lerp)
registerInTypeMap(LerpBlendType)
registerInTypeMap(LerpFunctor)
registerInTypeMap(LineEmitter)
registerInTypeMap(LineParticleRenderer)
registerInTypeMap(NurbsCurveDrawer)
registerInTypeMap(PTAUchar)
registerInTypeMap(PandaNode)
registerInTypeMap(Physical)
registerInTypeMap(PhysicsObject)
registerInTypeMap(PointEmitter)
registerInTypeMap(PointParticleFactory)
registerInTypeMap(PointParticleRenderer)
registerInTypeMap(RecorderController)
registerInTypeMap(RectangleEmitter)
registerInTypeMap(RingEmitter)
registerInTypeMap(SocketStream)
registerInTypeMap(SocketStreamRecorder)
registerInTypeMap(SparkleParticleRenderer)
registerInTypeMap(SphereSurfaceEmitter)
registerInTypeMap(SphereVolumeEmitter)
registerInTypeMap(SpriteParticleRenderer)
registerInTypeMap(TangentRingEmitter)
registerInTypeMap(TextFont)
registerInTypeMap(TypedWritableReferenceCount)
registerInTypeMap(VirtualFile)
registerInTypeMap(WritableConfigurable)
registerInTypeMap(ZSpinParticleFactory)
registerInTypeMap(AngularForce)
registerInTypeMap(AnimBundleNode)
registerInTypeMap(AnimGroup)
registerInTypeMap(CLerpInterval)
registerInTypeMap(CMetaInterval)
registerInTypeMap(CPetChase)
registerInTypeMap(CPetFlee)
registerInTypeMap(CachedTypedWritableReferenceCount)
registerInTypeMap(CollisionEntry)
registerInTypeMap(CollisionHandlerEvent)
registerInTypeMap(CollisionHandlerQueue)
registerInTypeMap(CollisionNode)
registerInTypeMap(CollisionSolid)
registerInTypeMap(ConfigVariableBool)
registerInTypeMap(ConfigVariableDouble)
registerInTypeMap(ConfigVariableFilename)
registerInTypeMap(ConfigVariableInt)
registerInTypeMap(ConfigVariableString)
registerInTypeMap(DCArrayParameter)
registerInTypeMap(DCClassParameter)
registerInTypeMap(DCSimpleParameter)
registerInTypeMap(DCSwitchParameter)
registerInTypeMap(DDrawable)
registerInTypeMap(DNACornice)
registerInTypeMap(DNAData)
registerInTypeMap(DNADoor)
registerInTypeMap(DNANode)
registerInTypeMap(DNAVisGroup)
registerInTypeMap(DNAWindows)
registerInTypeMap(DataNode)
registerInTypeMap(DynamicTextFont)
registerInTypeMap(EaseInBlendType)
registerInTypeMap(EaseInOutBlendType)
registerInTypeMap(EaseOutBlendType)
registerInTypeMap(EggBinMaker)
registerInTypeMap(EggNameUniquifier)
registerInTypeMap(EggNamedObject)
registerInTypeMap(EggSwitchCondition)
registerInTypeMap(EggVertex)
registerInTypeMap(FloatLerpFunctor)
registerInTypeMap(Fog)
registerInTypeMap(ForceNode)
registerInTypeMap(GeomNode)
registerInTypeMap(GeometricBoundingVolume)
registerInTypeMap(GraphicsOutput)
registerInTypeMap(GraphicsStateGuardianBase)
registerInTypeMap(HTTPChannel)
registerInTypeMap(HideInterval)
registerInTypeMap(HprScaleLerpFunctor)
registerInTypeMap(ImageBuffer)
registerInTypeMap(IntLerpFunctor)
registerInTypeMap(LODNode)
registerInTypeMap(Lens)
registerInTypeMap(LensNode)
registerInTypeMap(LightNode)
registerInTypeMap(LinearForce)
registerInTypeMap(MarginManager)
registerInTypeMap(MarginPopup)
registerInTypeMap(Material)
registerInTypeMap(ModelNode)
registerInTypeMap(MouseWatcherRegion)
registerInTypeMap(MultiLerpFunctor)
registerInTypeMap(Nametag3d)
registerInTypeMap(NoBlendType)
registerInTypeMap(PGItem)
registerInTypeMap(PGMouseWatcherParameter)
registerInTypeMap(PGTop)
registerInTypeMap(ParametricCurve)
registerInTypeMap(PartBundleNode)
registerInTypeMap(PartGroup)
registerInTypeMap(ParticleSystem)
registerInTypeMap(PhysicalNode)
registerInTypeMap(PlaneNode)
registerInTypeMap(PolylightNode)
registerInTypeMap(PortalNode)
registerInTypeMap(PosHprLerpFunctor)
registerInTypeMap(PosHprScaleLerpFunctor)
registerInTypeMap(ProjectionScreen)
registerInTypeMap(RenderAttrib)
registerInTypeMap(RenderEffect)
registerInTypeMap(RenderEffects)
registerInTypeMap(RopeNode)
registerInTypeMap(SelectiveChildNode)
registerInTypeMap(SheetNode)
registerInTypeMap(ShowInterval)
registerInTypeMap(SimpleLerpFunctorLPoint2f)
registerInTypeMap(SimpleLerpFunctorLPoint3f)
registerInTypeMap(SimpleLerpFunctorLPoint4f)
registerInTypeMap(SimpleLerpFunctorLVecBase2f)
registerInTypeMap(SimpleLerpFunctorLVecBase3f)
registerInTypeMap(SimpleLerpFunctorLVecBase4f)
registerInTypeMap(SimpleLerpFunctorLVector2f)
registerInTypeMap(SimpleLerpFunctorLVector3f)
registerInTypeMap(SimpleLerpFunctorLVector4f)
registerInTypeMap(StaticTextFont)
registerInTypeMap(TexCoordName)
registerInTypeMap(TextNode)
registerInTypeMap(TextureStage)
registerInTypeMap(VirtualFileComposite)
registerInTypeMap(VirtualFileSimple)
registerInTypeMap(WaitInterval)
registerInTypeMap(ActorNode)
registerInTypeMap(AlphaTestAttrib)
registerInTypeMap(AmbientLight)
registerInTypeMap(AnalogNode)
registerInTypeMap(AngularVectorForce)
registerInTypeMap(AnimBundle)
registerInTypeMap(AnimChannelBase)
registerInTypeMap(BillboardEffect)
registerInTypeMap(BoundingLine)
registerInTypeMap(ButtonNode)
registerInTypeMap(ButtonThrower)
registerInTypeMap(CLerpAnimEffectInterval)
registerInTypeMap(CLerpNodePathInterval)
registerInTypeMap(Camera)
registerInTypeMap(Character)
registerInTypeMap(ClipPlaneAttrib)
registerInTypeMap(CollisionHandlerPhysical)
registerInTypeMap(CollisionPlane)
registerInTypeMap(CollisionRay)
registerInTypeMap(CollisionSegment)
registerInTypeMap(CollisionSphere)
registerInTypeMap(CollisionTube)
registerInTypeMap(ColorAttrib)
registerInTypeMap(ColorBlendAttrib)
registerInTypeMap(ColorLerpFunctor)
registerInTypeMap(ColorScaleAttrib)
registerInTypeMap(ColorScaleLerpFunctor)
registerInTypeMap(ColorWriteAttrib)
registerInTypeMap(CompassEffect)
registerInTypeMap(CubicCurveseg)
registerInTypeMap(CullBinAttrib)
registerInTypeMap(CullFaceAttrib)
registerInTypeMap(CylindricalLens)
registerInTypeMap(DNAFlatBuilding)
registerInTypeMap(DNAFlatDoor)
registerInTypeMap(DNALandmarkBuilding)
registerInTypeMap(DNAProp)
registerInTypeMap(DNASign)
registerInTypeMap(DNASignBaseline)
registerInTypeMap(DNASignGraphic)
registerInTypeMap(DNASignText)
registerInTypeMap(DNAStreet)
registerInTypeMap(DNAWall)
registerInTypeMap(DecalEffect)
registerInTypeMap(DepthOffsetAttrib)
registerInTypeMap(DepthTestAttrib)
registerInTypeMap(DepthWriteAttrib)
registerInTypeMap(DialNode)
registerInTypeMap(DirectionalLight)
registerInTypeMap(EggGroupUniquifier)
registerInTypeMap(EggNode)
registerInTypeMap(EggPolysetMaker)
registerInTypeMap(EggPoolUniquifier)
registerInTypeMap(EggVertexUV)
registerInTypeMap(FadeLODNode)
registerInTypeMap(FiniteBoundingVolume)
registerInTypeMap(FisheyeLens)
registerInTypeMap(FloatQueryLerpFunctor)
registerInTypeMap(FogAttrib)
registerInTypeMap(FrameRateMeter)
registerInTypeMap(Geom)
registerInTypeMap(GraphicsBuffer)
registerInTypeMap(GraphicsStateGuardian)
registerInTypeMap(GraphicsWindow)
registerInTypeMap(HprLerpFunctor)
registerInTypeMap(IntQueryLerpFunctor)
registerInTypeMap(LightAttrib)
registerInTypeMap(LightLensNode)
registerInTypeMap(LinearCylinderVortexForce)
registerInTypeMap(LinearDistanceForce)
registerInTypeMap(LinearFrictionForce)
registerInTypeMap(LinearRandomForce)
registerInTypeMap(LinearUserDefinedForce)
registerInTypeMap(LinearVectorForce)
registerInTypeMap(MaterialAttrib)
registerInTypeMap(MatrixLens)
registerInTypeMap(ModelRoot)
registerInTypeMap(MouseAndKeyboard)
registerInTypeMap(MouseInterfaceNode)
registerInTypeMap(MouseRecorder)
registerInTypeMap(MouseWatcher)
registerInTypeMap(MovingPartBase)
registerInTypeMap(Nametag2d)
registerInTypeMap(NametagFloat2d)
registerInTypeMap(NametagFloat3d)
registerInTypeMap(OmniBoundingVolume)
registerInTypeMap(OrthographicLens)
registerInTypeMap(PGButton)
registerInTypeMap(PGEntry)
registerInTypeMap(PGMouseWatcherBackground)
registerInTypeMap(PGSliderBar)
registerInTypeMap(PGWaitBar)
registerInTypeMap(PSphereLens)
registerInTypeMap(ParasiteBuffer)
registerInTypeMap(PartBundle)
registerInTypeMap(PerspectiveLens)
registerInTypeMap(PiecewiseCurve)
registerInTypeMap(PointLight)
registerInTypeMap(PolylightEffect)
registerInTypeMap(PosLerpFunctor)
registerInTypeMap(RenderModeAttrib)
registerInTypeMap(RenderState)
registerInTypeMap(RescaleNormalAttrib)
registerInTypeMap(ScaleLerpFunctor)
registerInTypeMap(SequenceNode)
registerInTypeMap(ShowBoundsEffect)
registerInTypeMap(SimpleQueryLerpFunctorLPoint2f)
registerInTypeMap(SimpleQueryLerpFunctorLPoint3f)
registerInTypeMap(SimpleQueryLerpFunctorLPoint4f)
registerInTypeMap(SimpleQueryLerpFunctorLVecBase2f)
registerInTypeMap(SimpleQueryLerpFunctorLVecBase3f)
registerInTypeMap(SimpleQueryLerpFunctorLVecBase4f)
registerInTypeMap(SimpleQueryLerpFunctorLVector2f)
registerInTypeMap(SimpleQueryLerpFunctorLVector3f)
registerInTypeMap(SimpleQueryLerpFunctorLVector4f)
registerInTypeMap(SwitchNode)
registerInTypeMap(TexGenAttrib)
registerInTypeMap(TexMatrixAttrib)
registerInTypeMap(TexProjectorEffect)
registerInTypeMap(Texture)
registerInTypeMap(TextureApplyAttrib)
registerInTypeMap(TextureAttrib)
registerInTypeMap(TrackerNode)
registerInTypeMap(Transform2SG)
registerInTypeMap(TransformState)
registerInTypeMap(TransparencyAttrib)
registerInTypeMap(VirtualMouse)
registerInTypeMap(WhisperPopup)
registerInTypeMap(AnimChannelACMatrixSwitchType)
registerInTypeMap(AnimChannelACScalarSwitchType)
registerInTypeMap(BoundingSphere)
registerInTypeMap(CharacterJointBundle)
registerInTypeMap(CollisionHandlerFloor)
registerInTypeMap(CollisionHandlerGravity)
registerInTypeMap(CollisionHandlerPusher)
registerInTypeMap(CollisionInvSphere)
registerInTypeMap(CollisionLine)
registerInTypeMap(CollisionPolygon)
registerInTypeMap(DriveInterface)
registerInTypeMap(DynamicTextPage)
registerInTypeMap(EggAnimData)
registerInTypeMap(EggComment)
registerInTypeMap(EggFilenameNode)
registerInTypeMap(EggGroupNode)
registerInTypeMap(EggMaterial)
registerInTypeMap(EggPrimitive)
registerInTypeMap(EggVertexPool)
registerInTypeMap(GeomLine)
registerInTypeMap(GeomLinestrip)
registerInTypeMap(GeomPoint)
registerInTypeMap(GeomPolygon)
registerInTypeMap(GeomQuad)
registerInTypeMap(GeomSphere)
registerInTypeMap(GeomSprite)
registerInTypeMap(GeomTri)
registerInTypeMap(GeomTrifan)
registerInTypeMap(GeomTristrip)
registerInTypeMap(HermiteCurve)
registerInTypeMap(LinearJitterForce)
registerInTypeMap(LinearNoiseForce)
registerInTypeMap(LinearSinkForce)
registerInTypeMap(LinearSourceForce)
registerInTypeMap(MovingPartACMatrixSwitchType)
registerInTypeMap(NurbsCurve)
registerInTypeMap(PGSliderButton)
registerInTypeMap(Spotlight)
registerInTypeMap(Trackball)
registerInTypeMap(AnimChannelMatrixDynamic)
registerInTypeMap(AnimChannelMatrixXfmTable)
registerInTypeMap(AnimChannelScalarDynamic)
registerInTypeMap(AnimChannelScalarTable)
registerInTypeMap(EggCurve)
registerInTypeMap(EggData)
registerInTypeMap(EggExternalReference)
registerInTypeMap(EggGroup)
registerInTypeMap(EggLine)
registerInTypeMap(EggPoint)
registerInTypeMap(EggPolygon)
registerInTypeMap(EggSAnimData)
registerInTypeMap(EggSurface)
registerInTypeMap(EggTable)
registerInTypeMap(EggTexture)
registerInTypeMap(EggXfmAnimData)
registerInTypeMap(EggXfmSAnim)
registerInTypeMap(GeomTextGlyph)
registerInTypeMap(MovingPartMatrix)
registerInTypeMap(PhysicsCollisionHandler)
registerInTypeMap(CharacterJoint)
registerInTypeMap(EggBin)
registerInTypeMap(EggNurbsCurve)
