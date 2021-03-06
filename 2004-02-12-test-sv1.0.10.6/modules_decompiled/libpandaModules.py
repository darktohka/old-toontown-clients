# File: l (Python 2.2)

import libdtoolconfig
import libpanda
from GeomBindType import *
from CoordinateSystem import *
from NotifySeverity import *
from ErrorUtilCode import *
from libpandaDowncasts import *
import AccumulatedAttribs
import AnimControlCollection
import AsyncUtility
import BamFile
import BitMask32
import BoundedObject
import Buffer
import ButtonHandle
import ButtonRegistry
import CPTAFloat
import CString
import ChanCfgOverrides
import ChanConfig
import ClearableRegion
import ClockObject
import ComputedVertices
import ConfigExpress
import CullBinManager
import CullableObject
import CurveFitter
import DSearchPath
import DataGraphTraverser
import DataNodeTransmit
import DatagramIterator
import Decompressor
import DocumentSpec
import DownloadDb
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
import GraphicsEngine
import GraphicsPipeSelection
import GraphicsThreadingModel
import HTTPClient
import HTTPDate
import HTTPEntityTag
import HTTPEnum
import HashVal
import Ifstream
import Istream
import KeyboardButton
import LOD
import LoaderFileType
import Mat3
import Mat3D
import Mat4
import Mat4D
import MaterialPool
import MathNumbers
import ModelPool
import ModifierButtons
import MouseButton
import MouseData
import MouseWatcherParameter
import Multifile
import Namable
import NodePath
import NodePathCollection
import Notify
import NotifyCategory
import NurbsCurveInterface
import Ofstream
import Ostream
import PGFrameStyle
import PStatClient
import PStatCollector
import PTAUshort
import Patcher
import Patchfile
import Pipeline
import PointerToBaseRefCountObjvectorLPoint2f
import PointerToBaseRefCountObjvectorLPoint3f
import PointerToBaseRefCountObjvectorLVecBase4f
import PointerToBaseRefCountObjvectorLVector3f
import PointerToBaseRefCountObjvectorunsignedchar
import ProfileTimer
import Ramfile
import ReferenceCount
import SceneGraphReducer
import StreamReader
import StreamWriter
import TextEncoder
import TextureCollection
import TexturePool
import TimeVal
import TypeHandle
import TypeRegistry
import TypedObject
import URLSpec
import UniqueIdAllocator
import VBase2
import VBase2D
import VBase3
import VBase3D
import VBase4
import VBase4D
import VectorURLSpec
import VectorbasicStringchar
import VirtualFileSystem
import WindowProperties
import WindowsRegistry
import AnimControl
import CardMaker
import CollisionTraverser
import Datagram
import DisplayRegion
import EventHandler
import ISocketStream
import Iostream
import Light
import LineSegs
import LineStream
import MouseWatcherGroup
import MultiplexStream
import NurbsCurveEvaluator
import NurbsCurveResult
import NurbsSurfaceEvaluator
import NurbsSurfaceResult
import OSocketStream
import PTAColorf
import PTANormalf
import PTATexCoordf
import PTAUchar
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
import AudioManager
import AudioSound
import AutonomousLerp
import BoundingVolume
import ClientBase
import CollisionHandler
import Event
import GraphicsChannel
import GraphicsDevice
import GraphicsLayer
import GraphicsPipe
import GraphicsStateGuardianBase
import LOrientationd
import LOrientationf
import LRotationd
import LRotationf
import Lerp
import LerpBlendType
import LerpFunctor
import NurbsCurveDrawer
import PandaNode
import RecorderController
import SocketStream
import SocketStreamRecorder
import TextFont
import TypedWritableReferenceCount
import VirtualFile
import WritableConfigurable
import AnimBundleNode
import AnimGroup
import CollisionEntry
import CollisionHandlerEvent
import CollisionHandlerQueue
import CollisionNode
import CollisionSolid
import DDrawable
import DataNode
import DynamicTextFont
import EaseInBlendType
import EaseInOutBlendType
import EaseOutBlendType
import FloatLerpFunctor
import Fog
import GeomNode
import GeometricBoundingVolume
import GraphicsStateGuardian
import GraphicsWindow
import HTTPChannel
import HprScaleLerpFunctor
import ImageBuffer
import IntLerpFunctor
import Lens
import LensNode
import LightNode
import Material
import ModelNode
import MouseWatcherRegion
import MultiLerpFunctor
import NoBlendType
import PGItem
import PGMouseWatcherParameter
import PGTop
import ParametricCurve
import PartBundleNode
import PartGroup
import PlaneNode
import PosHprLerpFunctor
import PosHprScaleLerpFunctor
import RenderAttrib
import RenderEffect
import RenderEffects
import RenderState
import RopeNode
import SelectiveChildNode
import SheetNode
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
import TextNode
import TransformState
import VirtualFileComposite
import VirtualFileSimple
import AlphaTestAttrib
import AmbientLight
import AnalogNode
import AnimBundle
import AnimChannelBase
import BillboardEffect
import BoundingLine
import ButtonNode
import ButtonThrower
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
import DecalEffect
import DepthOffsetAttrib
import DepthTestAttrib
import DepthWriteAttrib
import DialNode
import DirectionalLight
import DriveInterface
import FiniteBoundingVolume
import FloatQueryLerpFunctor
import FogAttrib
import FrameRateMeter
import Geom
import HprLerpFunctor
import IntQueryLerpFunctor
import LODNode
import LightAttrib
import LightLensNode
import MaterialAttrib
import MatrixLens
import ModelRoot
import MouseAndKeyboard
import MouseRecorder
import MouseWatcher
import MovingPartBase
import OmniBoundingVolume
import OrthographicLens
import PGButton
import PGEntry
import PGMouseWatcherBackground
import PGWaitBar
import PartBundle
import PerspectiveLens
import PiecewiseCurve
import PointLight
import PosLerpFunctor
import RenderModeAttrib
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
import TexMatrixAttrib
import Texture
import TextureApplyAttrib
import TextureAttrib
import Trackball
import TrackerNode
import Transform2SG
import TransparencyAttrib
import VirtualMouse
import AnimChannelACMatrixSwitchType
import AnimChannelACScalarSwitchType
import BoundingSphere
import CharacterJointBundle
import CollisionHandlerFloor
import CollisionHandlerGravity
import CollisionHandlerPusher
import CollisionPolygon
import DynamicTextPage
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
import MovingPartACMatrixSwitchType
import NurbsCurve
import Spotlight
import AnimChannelMatrixDynamic
import AnimChannelMatrixXfmTable
import AnimChannelScalarDynamic
import AnimChannelScalarTable
import GeomTextGlyph
import MovingPartMatrix
import CharacterJoint
from libpandaGlobals import *
AccumulatedAttribs = AccumulatedAttribs.AccumulatedAttribs
AnimControlCollection = AnimControlCollection.AnimControlCollection
AsyncUtility = AsyncUtility.AsyncUtility
BamFile = BamFile.BamFile
BitMask32 = BitMask32.BitMask32
BoundedObject = BoundedObject.BoundedObject
Buffer = Buffer.Buffer
ButtonHandle = ButtonHandle.ButtonHandle
ButtonRegistry = ButtonRegistry.ButtonRegistry
CPTAFloat = CPTAFloat.CPTAFloat
CString = CString.CString
ChanCfgOverrides = ChanCfgOverrides.ChanCfgOverrides
ChanConfig = ChanConfig.ChanConfig
ClearableRegion = ClearableRegion.ClearableRegion
ClockObject = ClockObject.ClockObject
ComputedVertices = ComputedVertices.ComputedVertices
ConfigExpress = ConfigExpress.ConfigExpress
CullBinManager = CullBinManager.CullBinManager
CullableObject = CullableObject.CullableObject
CurveFitter = CurveFitter.CurveFitter
DSearchPath = DSearchPath.DSearchPath
DataGraphTraverser = DataGraphTraverser.DataGraphTraverser
DataNodeTransmit = DataNodeTransmit.DataNodeTransmit
DatagramIterator = DatagramIterator.DatagramIterator
Decompressor = Decompressor.Decompressor
DocumentSpec = DocumentSpec.DocumentSpec
DownloadDb = DownloadDb.DownloadDb
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
GraphicsEngine = GraphicsEngine.GraphicsEngine
GraphicsPipeSelection = GraphicsPipeSelection.GraphicsPipeSelection
GraphicsThreadingModel = GraphicsThreadingModel.GraphicsThreadingModel
HTTPClient = HTTPClient.HTTPClient
HTTPDate = HTTPDate.HTTPDate
HTTPEntityTag = HTTPEntityTag.HTTPEntityTag
HTTPEnum = HTTPEnum.HTTPEnum
HashVal = HashVal.HashVal
Ifstream = Ifstream.Ifstream
Istream = Istream.Istream
KeyboardButton = KeyboardButton.KeyboardButton
LOD = LOD.LOD
LoaderFileType = LoaderFileType.LoaderFileType
Mat3 = Mat3.Mat3
Mat3D = Mat3D.Mat3D
Mat4 = Mat4.Mat4
Mat4D = Mat4D.Mat4D
MaterialPool = MaterialPool.MaterialPool
MathNumbers = MathNumbers.MathNumbers
ModelPool = ModelPool.ModelPool
ModifierButtons = ModifierButtons.ModifierButtons
MouseButton = MouseButton.MouseButton
MouseData = MouseData.MouseData
MouseWatcherParameter = MouseWatcherParameter.MouseWatcherParameter
Multifile = Multifile.Multifile
Namable = Namable.Namable
NodePath = NodePath.NodePath
NodePathCollection = NodePathCollection.NodePathCollection
Notify = Notify.Notify
NotifyCategory = NotifyCategory.NotifyCategory
NurbsCurveInterface = NurbsCurveInterface.NurbsCurveInterface
Ofstream = Ofstream.Ofstream
Ostream = Ostream.Ostream
PGFrameStyle = PGFrameStyle.PGFrameStyle
PStatClient = PStatClient.PStatClient
PStatCollector = PStatCollector.PStatCollector
PTAUshort = PTAUshort.PTAUshort
Patcher = Patcher.Patcher
Patchfile = Patchfile.Patchfile
Pipeline = Pipeline.Pipeline
PointerToBaseRefCountObjvectorLPoint2f = PointerToBaseRefCountObjvectorLPoint2f.PointerToBaseRefCountObjvectorLPoint2f
PointerToBaseRefCountObjvectorLPoint3f = PointerToBaseRefCountObjvectorLPoint3f.PointerToBaseRefCountObjvectorLPoint3f
PointerToBaseRefCountObjvectorLVecBase4f = PointerToBaseRefCountObjvectorLVecBase4f.PointerToBaseRefCountObjvectorLVecBase4f
PointerToBaseRefCountObjvectorLVector3f = PointerToBaseRefCountObjvectorLVector3f.PointerToBaseRefCountObjvectorLVector3f
PointerToBaseRefCountObjvectorunsignedchar = PointerToBaseRefCountObjvectorunsignedchar.PointerToBaseRefCountObjvectorunsignedchar
ProfileTimer = ProfileTimer.ProfileTimer
Ramfile = Ramfile.Ramfile
ReferenceCount = ReferenceCount.ReferenceCount
SceneGraphReducer = SceneGraphReducer.SceneGraphReducer
StreamReader = StreamReader.StreamReader
StreamWriter = StreamWriter.StreamWriter
TextEncoder = TextEncoder.TextEncoder
TextureCollection = TextureCollection.TextureCollection
TexturePool = TexturePool.TexturePool
TimeVal = TimeVal.TimeVal
TypeHandle = TypeHandle.TypeHandle
TypeRegistry = TypeRegistry.TypeRegistry
TypedObject = TypedObject.TypedObject
URLSpec = URLSpec.URLSpec
UniqueIdAllocator = UniqueIdAllocator.UniqueIdAllocator
VBase2 = VBase2.VBase2
VBase2D = VBase2D.VBase2D
VBase3 = VBase3.VBase3
VBase3D = VBase3D.VBase3D
VBase4 = VBase4.VBase4
VBase4D = VBase4D.VBase4D
VectorURLSpec = VectorURLSpec.VectorURLSpec
VectorbasicStringchar = VectorbasicStringchar.VectorbasicStringchar
VirtualFileSystem = VirtualFileSystem.VirtualFileSystem
WindowProperties = WindowProperties.WindowProperties
WindowsRegistry = WindowsRegistry.WindowsRegistry
AnimControl = AnimControl.AnimControl
CardMaker = CardMaker.CardMaker
CollisionTraverser = CollisionTraverser.CollisionTraverser
Datagram = Datagram.Datagram
DisplayRegion = DisplayRegion.DisplayRegion
EventHandler = EventHandler.EventHandler
ISocketStream = ISocketStream.ISocketStream
Iostream = Iostream.Iostream
Light = Light.Light
LineSegs = LineSegs.LineSegs
LineStream = LineStream.LineStream
MouseWatcherGroup = MouseWatcherGroup.MouseWatcherGroup
MultiplexStream = MultiplexStream.MultiplexStream
NurbsCurveEvaluator = NurbsCurveEvaluator.NurbsCurveEvaluator
NurbsCurveResult = NurbsCurveResult.NurbsCurveResult
NurbsSurfaceEvaluator = NurbsSurfaceEvaluator.NurbsSurfaceEvaluator
NurbsSurfaceResult = NurbsSurfaceResult.NurbsSurfaceResult
OSocketStream = OSocketStream.OSocketStream
PTAColorf = PTAColorf.PTAColorf
PTANormalf = PTANormalf.PTANormalf
PTATexCoordf = PTATexCoordf.PTATexCoordf
PTAUchar = PTAUchar.PTAUchar
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
AudioManager = AudioManager.AudioManager
AudioSound = AudioSound.AudioSound
AutonomousLerp = AutonomousLerp.AutonomousLerp
BoundingVolume = BoundingVolume.BoundingVolume
ClientBase = ClientBase.ClientBase
CollisionHandler = CollisionHandler.CollisionHandler
Event = Event.Event
GraphicsChannel = GraphicsChannel.GraphicsChannel
GraphicsDevice = GraphicsDevice.GraphicsDevice
GraphicsLayer = GraphicsLayer.GraphicsLayer
GraphicsPipe = GraphicsPipe.GraphicsPipe
GraphicsStateGuardianBase = GraphicsStateGuardianBase.GraphicsStateGuardianBase
LOrientationd = LOrientationd.LOrientationd
LOrientationf = LOrientationf.LOrientationf
LRotationd = LRotationd.LRotationd
LRotationf = LRotationf.LRotationf
Lerp = Lerp.Lerp
LerpBlendType = LerpBlendType.LerpBlendType
LerpFunctor = LerpFunctor.LerpFunctor
NurbsCurveDrawer = NurbsCurveDrawer.NurbsCurveDrawer
PandaNode = PandaNode.PandaNode
RecorderController = RecorderController.RecorderController
SocketStream = SocketStream.SocketStream
SocketStreamRecorder = SocketStreamRecorder.SocketStreamRecorder
TextFont = TextFont.TextFont
TypedWritableReferenceCount = TypedWritableReferenceCount.TypedWritableReferenceCount
VirtualFile = VirtualFile.VirtualFile
WritableConfigurable = WritableConfigurable.WritableConfigurable
AnimBundleNode = AnimBundleNode.AnimBundleNode
AnimGroup = AnimGroup.AnimGroup
CollisionEntry = CollisionEntry.CollisionEntry
CollisionHandlerEvent = CollisionHandlerEvent.CollisionHandlerEvent
CollisionHandlerQueue = CollisionHandlerQueue.CollisionHandlerQueue
CollisionNode = CollisionNode.CollisionNode
CollisionSolid = CollisionSolid.CollisionSolid
DDrawable = DDrawable.DDrawable
DataNode = DataNode.DataNode
DynamicTextFont = DynamicTextFont.DynamicTextFont
EaseInBlendType = EaseInBlendType.EaseInBlendType
EaseInOutBlendType = EaseInOutBlendType.EaseInOutBlendType
EaseOutBlendType = EaseOutBlendType.EaseOutBlendType
FloatLerpFunctor = FloatLerpFunctor.FloatLerpFunctor
Fog = Fog.Fog
GeomNode = GeomNode.GeomNode
GeometricBoundingVolume = GeometricBoundingVolume.GeometricBoundingVolume
GraphicsStateGuardian = GraphicsStateGuardian.GraphicsStateGuardian
GraphicsWindow = GraphicsWindow.GraphicsWindow
HTTPChannel = HTTPChannel.HTTPChannel
HprScaleLerpFunctor = HprScaleLerpFunctor.HprScaleLerpFunctor
ImageBuffer = ImageBuffer.ImageBuffer
IntLerpFunctor = IntLerpFunctor.IntLerpFunctor
Lens = Lens.Lens
LensNode = LensNode.LensNode
LightNode = LightNode.LightNode
Material = Material.Material
ModelNode = ModelNode.ModelNode
MouseWatcherRegion = MouseWatcherRegion.MouseWatcherRegion
MultiLerpFunctor = MultiLerpFunctor.MultiLerpFunctor
NoBlendType = NoBlendType.NoBlendType
PGItem = PGItem.PGItem
PGMouseWatcherParameter = PGMouseWatcherParameter.PGMouseWatcherParameter
PGTop = PGTop.PGTop
ParametricCurve = ParametricCurve.ParametricCurve
PartBundleNode = PartBundleNode.PartBundleNode
PartGroup = PartGroup.PartGroup
PlaneNode = PlaneNode.PlaneNode
PosHprLerpFunctor = PosHprLerpFunctor.PosHprLerpFunctor
PosHprScaleLerpFunctor = PosHprScaleLerpFunctor.PosHprScaleLerpFunctor
RenderAttrib = RenderAttrib.RenderAttrib
RenderEffect = RenderEffect.RenderEffect
RenderEffects = RenderEffects.RenderEffects
RenderState = RenderState.RenderState
RopeNode = RopeNode.RopeNode
SelectiveChildNode = SelectiveChildNode.SelectiveChildNode
SheetNode = SheetNode.SheetNode
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
TextNode = TextNode.TextNode
TransformState = TransformState.TransformState
VirtualFileComposite = VirtualFileComposite.VirtualFileComposite
VirtualFileSimple = VirtualFileSimple.VirtualFileSimple
AlphaTestAttrib = AlphaTestAttrib.AlphaTestAttrib
AmbientLight = AmbientLight.AmbientLight
AnalogNode = AnalogNode.AnalogNode
AnimBundle = AnimBundle.AnimBundle
AnimChannelBase = AnimChannelBase.AnimChannelBase
BillboardEffect = BillboardEffect.BillboardEffect
BoundingLine = BoundingLine.BoundingLine
ButtonNode = ButtonNode.ButtonNode
ButtonThrower = ButtonThrower.ButtonThrower
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
DecalEffect = DecalEffect.DecalEffect
DepthOffsetAttrib = DepthOffsetAttrib.DepthOffsetAttrib
DepthTestAttrib = DepthTestAttrib.DepthTestAttrib
DepthWriteAttrib = DepthWriteAttrib.DepthWriteAttrib
DialNode = DialNode.DialNode
DirectionalLight = DirectionalLight.DirectionalLight
DriveInterface = DriveInterface.DriveInterface
FiniteBoundingVolume = FiniteBoundingVolume.FiniteBoundingVolume
FloatQueryLerpFunctor = FloatQueryLerpFunctor.FloatQueryLerpFunctor
FogAttrib = FogAttrib.FogAttrib
FrameRateMeter = FrameRateMeter.FrameRateMeter
Geom = Geom.Geom
HprLerpFunctor = HprLerpFunctor.HprLerpFunctor
IntQueryLerpFunctor = IntQueryLerpFunctor.IntQueryLerpFunctor
LODNode = LODNode.LODNode
LightAttrib = LightAttrib.LightAttrib
LightLensNode = LightLensNode.LightLensNode
MaterialAttrib = MaterialAttrib.MaterialAttrib
MatrixLens = MatrixLens.MatrixLens
ModelRoot = ModelRoot.ModelRoot
MouseAndKeyboard = MouseAndKeyboard.MouseAndKeyboard
MouseRecorder = MouseRecorder.MouseRecorder
MouseWatcher = MouseWatcher.MouseWatcher
MovingPartBase = MovingPartBase.MovingPartBase
OmniBoundingVolume = OmniBoundingVolume.OmniBoundingVolume
OrthographicLens = OrthographicLens.OrthographicLens
PGButton = PGButton.PGButton
PGEntry = PGEntry.PGEntry
PGMouseWatcherBackground = PGMouseWatcherBackground.PGMouseWatcherBackground
PGWaitBar = PGWaitBar.PGWaitBar
PartBundle = PartBundle.PartBundle
PerspectiveLens = PerspectiveLens.PerspectiveLens
PiecewiseCurve = PiecewiseCurve.PiecewiseCurve
PointLight = PointLight.PointLight
PosLerpFunctor = PosLerpFunctor.PosLerpFunctor
RenderModeAttrib = RenderModeAttrib.RenderModeAttrib
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
TexMatrixAttrib = TexMatrixAttrib.TexMatrixAttrib
Texture = Texture.Texture
TextureApplyAttrib = TextureApplyAttrib.TextureApplyAttrib
TextureAttrib = TextureAttrib.TextureAttrib
Trackball = Trackball.Trackball
TrackerNode = TrackerNode.TrackerNode
Transform2SG = Transform2SG.Transform2SG
TransparencyAttrib = TransparencyAttrib.TransparencyAttrib
VirtualMouse = VirtualMouse.VirtualMouse
AnimChannelACMatrixSwitchType = AnimChannelACMatrixSwitchType.AnimChannelACMatrixSwitchType
AnimChannelACScalarSwitchType = AnimChannelACScalarSwitchType.AnimChannelACScalarSwitchType
BoundingSphere = BoundingSphere.BoundingSphere
CharacterJointBundle = CharacterJointBundle.CharacterJointBundle
CollisionHandlerFloor = CollisionHandlerFloor.CollisionHandlerFloor
CollisionHandlerGravity = CollisionHandlerGravity.CollisionHandlerGravity
CollisionHandlerPusher = CollisionHandlerPusher.CollisionHandlerPusher
CollisionPolygon = CollisionPolygon.CollisionPolygon
DynamicTextPage = DynamicTextPage.DynamicTextPage
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
MovingPartACMatrixSwitchType = MovingPartACMatrixSwitchType.MovingPartACMatrixSwitchType
NurbsCurve = NurbsCurve.NurbsCurve
Spotlight = Spotlight.Spotlight
AnimChannelMatrixDynamic = AnimChannelMatrixDynamic.AnimChannelMatrixDynamic
AnimChannelMatrixXfmTable = AnimChannelMatrixXfmTable.AnimChannelMatrixXfmTable
AnimChannelScalarDynamic = AnimChannelScalarDynamic.AnimChannelScalarDynamic
AnimChannelScalarTable = AnimChannelScalarTable.AnimChannelScalarTable
GeomTextGlyph = GeomTextGlyph.GeomTextGlyph
MovingPartMatrix = MovingPartMatrix.MovingPartMatrix
CharacterJoint = CharacterJoint.CharacterJoint
from FFIExternalObject import registerInTypeMap
registerInTypeMap(AccumulatedAttribs)
registerInTypeMap(AnimControlCollection)
registerInTypeMap(AsyncUtility)
registerInTypeMap(BamFile)
registerInTypeMap(BitMask32)
registerInTypeMap(BoundedObject)
registerInTypeMap(Buffer)
registerInTypeMap(ButtonHandle)
registerInTypeMap(ButtonRegistry)
registerInTypeMap(CPTAFloat)
registerInTypeMap(CString)
registerInTypeMap(ChanCfgOverrides)
registerInTypeMap(ChanConfig)
registerInTypeMap(ClearableRegion)
registerInTypeMap(ClockObject)
registerInTypeMap(ComputedVertices)
registerInTypeMap(ConfigExpress)
registerInTypeMap(CullBinManager)
registerInTypeMap(CullableObject)
registerInTypeMap(CurveFitter)
registerInTypeMap(DSearchPath)
registerInTypeMap(DataGraphTraverser)
registerInTypeMap(DataNodeTransmit)
registerInTypeMap(DatagramIterator)
registerInTypeMap(Decompressor)
registerInTypeMap(DocumentSpec)
registerInTypeMap(DownloadDb)
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
registerInTypeMap(GraphicsEngine)
registerInTypeMap(GraphicsPipeSelection)
registerInTypeMap(GraphicsThreadingModel)
registerInTypeMap(HTTPClient)
registerInTypeMap(HTTPDate)
registerInTypeMap(HTTPEntityTag)
registerInTypeMap(HTTPEnum)
registerInTypeMap(HashVal)
registerInTypeMap(Ifstream)
registerInTypeMap(Istream)
registerInTypeMap(KeyboardButton)
registerInTypeMap(LOD)
registerInTypeMap(LoaderFileType)
registerInTypeMap(Mat3)
registerInTypeMap(Mat3D)
registerInTypeMap(Mat4)
registerInTypeMap(Mat4D)
registerInTypeMap(MaterialPool)
registerInTypeMap(MathNumbers)
registerInTypeMap(ModelPool)
registerInTypeMap(ModifierButtons)
registerInTypeMap(MouseButton)
registerInTypeMap(MouseData)
registerInTypeMap(MouseWatcherParameter)
registerInTypeMap(Multifile)
registerInTypeMap(Namable)
registerInTypeMap(NodePath)
registerInTypeMap(NodePathCollection)
registerInTypeMap(Notify)
registerInTypeMap(NotifyCategory)
registerInTypeMap(NurbsCurveInterface)
registerInTypeMap(Ofstream)
registerInTypeMap(Ostream)
registerInTypeMap(PGFrameStyle)
registerInTypeMap(PStatClient)
registerInTypeMap(PStatCollector)
registerInTypeMap(PTAUshort)
registerInTypeMap(Patcher)
registerInTypeMap(Patchfile)
registerInTypeMap(Pipeline)
registerInTypeMap(PointerToBaseRefCountObjvectorLPoint2f)
registerInTypeMap(PointerToBaseRefCountObjvectorLPoint3f)
registerInTypeMap(PointerToBaseRefCountObjvectorLVecBase4f)
registerInTypeMap(PointerToBaseRefCountObjvectorLVector3f)
registerInTypeMap(PointerToBaseRefCountObjvectorunsignedchar)
registerInTypeMap(ProfileTimer)
registerInTypeMap(Ramfile)
registerInTypeMap(ReferenceCount)
registerInTypeMap(SceneGraphReducer)
registerInTypeMap(StreamReader)
registerInTypeMap(StreamWriter)
registerInTypeMap(TextEncoder)
registerInTypeMap(TextureCollection)
registerInTypeMap(TexturePool)
registerInTypeMap(TimeVal)
registerInTypeMap(TypeHandle)
registerInTypeMap(TypeRegistry)
registerInTypeMap(TypedObject)
registerInTypeMap(URLSpec)
registerInTypeMap(UniqueIdAllocator)
registerInTypeMap(VBase2)
registerInTypeMap(VBase2D)
registerInTypeMap(VBase3)
registerInTypeMap(VBase3D)
registerInTypeMap(VBase4)
registerInTypeMap(VBase4D)
registerInTypeMap(VectorURLSpec)
registerInTypeMap(VectorbasicStringchar)
registerInTypeMap(VirtualFileSystem)
registerInTypeMap(WindowProperties)
registerInTypeMap(WindowsRegistry)
registerInTypeMap(AnimControl)
registerInTypeMap(CardMaker)
registerInTypeMap(CollisionTraverser)
registerInTypeMap(Datagram)
registerInTypeMap(DisplayRegion)
registerInTypeMap(EventHandler)
registerInTypeMap(ISocketStream)
registerInTypeMap(Iostream)
registerInTypeMap(Light)
registerInTypeMap(LineSegs)
registerInTypeMap(LineStream)
registerInTypeMap(MouseWatcherGroup)
registerInTypeMap(MultiplexStream)
registerInTypeMap(NurbsCurveEvaluator)
registerInTypeMap(NurbsCurveResult)
registerInTypeMap(NurbsSurfaceEvaluator)
registerInTypeMap(NurbsSurfaceResult)
registerInTypeMap(OSocketStream)
registerInTypeMap(PTAColorf)
registerInTypeMap(PTANormalf)
registerInTypeMap(PTATexCoordf)
registerInTypeMap(PTAUchar)
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
registerInTypeMap(AudioManager)
registerInTypeMap(AudioSound)
registerInTypeMap(AutonomousLerp)
registerInTypeMap(BoundingVolume)
registerInTypeMap(ClientBase)
registerInTypeMap(CollisionHandler)
registerInTypeMap(Event)
registerInTypeMap(GraphicsChannel)
registerInTypeMap(GraphicsDevice)
registerInTypeMap(GraphicsLayer)
registerInTypeMap(GraphicsPipe)
registerInTypeMap(GraphicsStateGuardianBase)
registerInTypeMap(LOrientationd)
registerInTypeMap(LOrientationf)
registerInTypeMap(LRotationd)
registerInTypeMap(LRotationf)
registerInTypeMap(Lerp)
registerInTypeMap(LerpBlendType)
registerInTypeMap(LerpFunctor)
registerInTypeMap(NurbsCurveDrawer)
registerInTypeMap(PandaNode)
registerInTypeMap(RecorderController)
registerInTypeMap(SocketStream)
registerInTypeMap(SocketStreamRecorder)
registerInTypeMap(TextFont)
registerInTypeMap(TypedWritableReferenceCount)
registerInTypeMap(VirtualFile)
registerInTypeMap(WritableConfigurable)
registerInTypeMap(AnimBundleNode)
registerInTypeMap(AnimGroup)
registerInTypeMap(CollisionEntry)
registerInTypeMap(CollisionHandlerEvent)
registerInTypeMap(CollisionHandlerQueue)
registerInTypeMap(CollisionNode)
registerInTypeMap(CollisionSolid)
registerInTypeMap(DDrawable)
registerInTypeMap(DataNode)
registerInTypeMap(DynamicTextFont)
registerInTypeMap(EaseInBlendType)
registerInTypeMap(EaseInOutBlendType)
registerInTypeMap(EaseOutBlendType)
registerInTypeMap(FloatLerpFunctor)
registerInTypeMap(Fog)
registerInTypeMap(GeomNode)
registerInTypeMap(GeometricBoundingVolume)
registerInTypeMap(GraphicsStateGuardian)
registerInTypeMap(GraphicsWindow)
registerInTypeMap(HTTPChannel)
registerInTypeMap(HprScaleLerpFunctor)
registerInTypeMap(ImageBuffer)
registerInTypeMap(IntLerpFunctor)
registerInTypeMap(Lens)
registerInTypeMap(LensNode)
registerInTypeMap(LightNode)
registerInTypeMap(Material)
registerInTypeMap(ModelNode)
registerInTypeMap(MouseWatcherRegion)
registerInTypeMap(MultiLerpFunctor)
registerInTypeMap(NoBlendType)
registerInTypeMap(PGItem)
registerInTypeMap(PGMouseWatcherParameter)
registerInTypeMap(PGTop)
registerInTypeMap(ParametricCurve)
registerInTypeMap(PartBundleNode)
registerInTypeMap(PartGroup)
registerInTypeMap(PlaneNode)
registerInTypeMap(PosHprLerpFunctor)
registerInTypeMap(PosHprScaleLerpFunctor)
registerInTypeMap(RenderAttrib)
registerInTypeMap(RenderEffect)
registerInTypeMap(RenderEffects)
registerInTypeMap(RenderState)
registerInTypeMap(RopeNode)
registerInTypeMap(SelectiveChildNode)
registerInTypeMap(SheetNode)
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
registerInTypeMap(TextNode)
registerInTypeMap(TransformState)
registerInTypeMap(VirtualFileComposite)
registerInTypeMap(VirtualFileSimple)
registerInTypeMap(AlphaTestAttrib)
registerInTypeMap(AmbientLight)
registerInTypeMap(AnalogNode)
registerInTypeMap(AnimBundle)
registerInTypeMap(AnimChannelBase)
registerInTypeMap(BillboardEffect)
registerInTypeMap(BoundingLine)
registerInTypeMap(ButtonNode)
registerInTypeMap(ButtonThrower)
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
registerInTypeMap(DecalEffect)
registerInTypeMap(DepthOffsetAttrib)
registerInTypeMap(DepthTestAttrib)
registerInTypeMap(DepthWriteAttrib)
registerInTypeMap(DialNode)
registerInTypeMap(DirectionalLight)
registerInTypeMap(DriveInterface)
registerInTypeMap(FiniteBoundingVolume)
registerInTypeMap(FloatQueryLerpFunctor)
registerInTypeMap(FogAttrib)
registerInTypeMap(FrameRateMeter)
registerInTypeMap(Geom)
registerInTypeMap(HprLerpFunctor)
registerInTypeMap(IntQueryLerpFunctor)
registerInTypeMap(LODNode)
registerInTypeMap(LightAttrib)
registerInTypeMap(LightLensNode)
registerInTypeMap(MaterialAttrib)
registerInTypeMap(MatrixLens)
registerInTypeMap(ModelRoot)
registerInTypeMap(MouseAndKeyboard)
registerInTypeMap(MouseRecorder)
registerInTypeMap(MouseWatcher)
registerInTypeMap(MovingPartBase)
registerInTypeMap(OmniBoundingVolume)
registerInTypeMap(OrthographicLens)
registerInTypeMap(PGButton)
registerInTypeMap(PGEntry)
registerInTypeMap(PGMouseWatcherBackground)
registerInTypeMap(PGWaitBar)
registerInTypeMap(PartBundle)
registerInTypeMap(PerspectiveLens)
registerInTypeMap(PiecewiseCurve)
registerInTypeMap(PointLight)
registerInTypeMap(PosLerpFunctor)
registerInTypeMap(RenderModeAttrib)
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
registerInTypeMap(TexMatrixAttrib)
registerInTypeMap(Texture)
registerInTypeMap(TextureApplyAttrib)
registerInTypeMap(TextureAttrib)
registerInTypeMap(Trackball)
registerInTypeMap(TrackerNode)
registerInTypeMap(Transform2SG)
registerInTypeMap(TransparencyAttrib)
registerInTypeMap(VirtualMouse)
registerInTypeMap(AnimChannelACMatrixSwitchType)
registerInTypeMap(AnimChannelACScalarSwitchType)
registerInTypeMap(BoundingSphere)
registerInTypeMap(CharacterJointBundle)
registerInTypeMap(CollisionHandlerFloor)
registerInTypeMap(CollisionHandlerGravity)
registerInTypeMap(CollisionHandlerPusher)
registerInTypeMap(CollisionPolygon)
registerInTypeMap(DynamicTextPage)
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
registerInTypeMap(MovingPartACMatrixSwitchType)
registerInTypeMap(NurbsCurve)
registerInTypeMap(Spotlight)
registerInTypeMap(AnimChannelMatrixDynamic)
registerInTypeMap(AnimChannelMatrixXfmTable)
registerInTypeMap(AnimChannelScalarDynamic)
registerInTypeMap(AnimChannelScalarTable)
registerInTypeMap(GeomTextGlyph)
registerInTypeMap(MovingPartMatrix)
registerInTypeMap(CharacterJoint)
