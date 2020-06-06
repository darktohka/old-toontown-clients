# File: E (Python 2.2)

from pandac.PandaModules import *
ELEVATOR_NORMAL = 0
ELEVATOR_VP = 1
ELEVATOR_MINT = 2
ELEVATOR_CFO = 3
if __dev__:
    
    try:
        config = simbase.config
    except:
        config = base.config

    elevatorCountdown = config.GetFloat('elevator-countdown', -1)
    if elevatorCountdown != -1:
        bboard.post('elevatorCountdown', elevatorCountdown)
    

ElevatorData = {
    ELEVATOR_NORMAL: {
        'openTime': 2.0,
        'closeTime': 2.0,
        'width': 3.5,
        'countdown': bboard.get('elevatorCountdown', 15.0),
        'sfxVolume': 1.0,
        'collRadius': 5 },
    ELEVATOR_VP: {
        'openTime': 4.0,
        'closeTime': 4.0,
        'width': 11.5,
        'countdown': bboard.get('elevatorCountdown', 30.0),
        'sfxVolume': 0.69999999999999996,
        'collRadius': 7.5 },
    ELEVATOR_MINT: {
        'openTime': 2.0,
        'closeTime': 2.0,
        'width': 5.875,
        'countdown': bboard.get('elevatorCountdown', 15.0),
        'sfxVolume': 1.0,
        'collRadius': 5 },
    ELEVATOR_CFO: {
        'openTime': 3.0,
        'closeTime': 3.0,
        'width': 8.1660000000000004,
        'countdown': bboard.get('elevatorCountdown', 30.0),
        'sfxVolume': 0.69999999999999996,
        'collRadius': 7.5 } }
TOON_BOARD_ELEVATOR_TIME = 1.0
TOON_EXIT_ELEVATOR_TIME = 1.0
TOON_VICTORY_EXIT_TIME = 1.0
SUIT_HOLD_ELEVATOR_TIME = 1.0
SUIT_LEAVE_ELEVATOR_TIME = 2.0
INTERIOR_ELEVATOR_COUNTDOWN_TIME = 90
LIGHT_OFF_COLOR = Vec4(0.5, 0.5, 0.5, 1.0)
LIGHT_ON_COLOR = Vec4(1.0, 1.0, 1.0, 1.0)
ElevatorPoints = [
    [
        -1.5,
        5,
        0.10000000000000001],
    [
        1.5,
        5,
        0.10000000000000001],
    [
        -2.5,
        3,
        0.10000000000000001],
    [
        2.5,
        3,
        0.10000000000000001],
    [
        -3.5,
        5,
        0.10000000000000001],
    [
        3.5,
        5,
        0.10000000000000001],
    [
        -4,
        3,
        0.10000000000000001],
    [
        4,
        3,
        0.10000000000000001]]
BigElevatorPoints = [
    [
        -2.5,
        9,
        0.10000000000000001],
    [
        2.5,
        9,
        0.10000000000000001],
    [
        -8.0,
        9,
        0.10000000000000001],
    [
        8.0,
        9,
        0.10000000000000001],
    [
        -2.5,
        4,
        0.10000000000000001],
    [
        2.5,
        4,
        0.10000000000000001],
    [
        -8.0,
        4,
        0.10000000000000001],
    [
        8.0,
        4,
        0.10000000000000001]]
ElevatorOutPoints = [
    [
        -4.5999999999999996,
        -5.2000000000000002,
        0.10000000000000001],
    [
        4.5999999999999996,
        -5.2000000000000002,
        0.10000000000000001],
    [
        -1.6000000000000001,
        -6.2000000000000002,
        0.10000000000000001],
    [
        1.6000000000000001,
        -6.2000000000000002,
        0.10000000000000001]]
