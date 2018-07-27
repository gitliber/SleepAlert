# SleepAlert
## A real time Behavioral Drowsiness detector - for safety purpose alarm

## Context

In recent years, driver drowsiness has been one of the major causes of road accidents and can lead to severe physical injuries, deaths and significant economic losses. Statistics indicate the need of a reliable driver drowsiness detection system which could alert the driver before a mishap happens. 

A driver who falls asleep at the wheel loses control of the vehicle, an action which often results in a crash with either another vehicle or stationary objects. In order to prevent these devastating accidents, the state of drowsiness of the driver should be monitored.

Drowsy driving kills. According to the National Highway Traffic Safety Administration, drowsy driving caused 824 deaths in 2015, the last year for which figures are available.

Several manufacturers, including Audi, Mercedes and Volvo, currently offer drowsiness detection systems that monitor a vehicle’s movements, such as steering wheel angle, lane deviation, time driven and road conditions.

<img src="images/sleeprec.gif">

# Behavioral Measures

A drowsy person displays a number of characteristic facial movements, including rapid and constant blinking, nodding or swinging their head, and frequent yawning. Computerized, non-intrusive, behavioral approaches are widely used for determining the drowsiness level of drivers by measuring their abnormal behaviors. Most of the published studies on using behavioral approaches to determine drowsiness, focus on blinking. 

Some researchers used multiple facial actions, including inner brow rise, outer brow rise, lip stretch, jaw drop and eye blink, to detect drowsiness. However, research on using other behavioral measures, such as yawning and head or eye position orientation, to determine the level of drowsiness is ongoing.

## How does SleepAlert work?

If the users do close their eyes for longer than expected -- generally anything longer than 1.6 seconds -- an alarm message is shown, (it can be combined with a noise in future versions) and a log event is recorded.

Real-Time Sleep Detection and Warning Systems like this can be proposed and implemented to ensure the safety for the drivers and pilots, for example.

In critical environments this kind of system can help to estimate and measure the driver attention, the percentage of oxygen in the blood of the driver (when combined with an oxygen saturation sensor) and to check if driver is failing a sleep. In addition this kind of system can rely on a Real time vital signs monitoring system to measure the vital signs values (In critical environments). 

## Requirements 

Pre-trained Shape Predictor Dlib Model - shape_predictor_68_face_landmarks.dat (https://github.com/AKSHAYUBHAT/TensorFace/blob/master/openface/models/dlib/shape_predictor_68_face_landmarks.dat)

Python 
imutils 
dlib 
cv2 
numpy

## Future Improvements

The model will predict when critical impairment will occur.

The Model accuracy will be greater with behavioral (eye and head) indicators.

Driving time data will improve model detection and prediction performance.
    
The computer vision algorithms will track human eye and eyelid behaviour, looking for the frequency of blinking, duration of blinks and the velocity of the eyelid.
    
## References
Umesh Prabushitha Jayasinghe - https://github.com/prabushitha/Sleep-Recognition

Detecting Driver Drowsiness Based on Sensors: A Review - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3571819/

Eye-tracking system monitors driver fatigue, prevents sleeping at wheel - https://www.wired.co.uk/article/eye-tracking-mining-system

Detection and prediction of driver drowsiness using artificial neural network models - https://www.sciencedirect.com/science/article/pii/S0001457517304347 

Sleepy Behind the Wheel? Some Cars Can Tell - https://www.nytimes.com/2017/03/16/automobiles/wheels/drowsy-driving-technology.html



