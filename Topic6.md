# Topic 6 Satellite Positioning

## Questions from exams
### 1. uestion 6 
- (a)  Explain the difference between the terms GPS and GNSS. (2 marks) 
- (b)  In the GPS system, the positioning codes are phase modulated onto the L1 and L2 carrier waves. Explain the principle of phase modulation. (2 marks) 


1. What are the three segments of GPS and what are their functions? Show how they interact with each other using a diagram. 

Space segment
• 24 Satellites (3 operational spares)
• 6 orbital planes (4 satellites per plane)
• 55° orbit inclination
• 20200 km above the Earth
• 12-hour orbits
• Ground repeat?

- Control segment
  - Master Control Station (MCS) :Schriever Air Force Base, Colorado
  - Monitor Stations (MS) : Provide global coverage via 16 sites: 6 from the Air Force (10 National Geospatial- Intelligence Agency (NGA))
- Master Control station
  - Provides command and control of the GPS constellation
  - Uses global monitor station data to compute the precise locations of the satellites
  - Generate navigation messages
  - Monitors satellite broadcasts and system integrity to ensure constellation health and accuracy
- Monitor stations
  - Track GPS satellites as they pass overhead
  - Collect navigation signals, range/carrier measurements, and atmospheric data
  - Feed observations to the master control station
- Ground Antennas
  - Send commands, navigation data uploads, and processor program loads to the satellites

User segment
• Hardware and software to convert satellite
signals to navigation information
 Precise time
 Three-dimensional position
 Three-dimensional velocity
• Both receiver and software technology
changing very quickly
• Combine at least 2 GNSS data streams
 GPS and GLONASS
• All GNSS data – Geodetic Receivers

User segment
• Receiver components
 Antenna & preamplifier
 Signal processor
 Microprocessor
 Terminal or control and display unit
 Recording device
 Power supply
• Generates a copy of the visible satellites’
signals

电离层误差：
    - 对于伪距减慢，对于载波相位加快。Delay for code,Advancement for carrier phase
    - 太阳光会加剧电离，所以这种误差是受时间影响的。下午两点往往是最大的误差。
    - Effects can be minimised by use of L1 and L2 carrier phase observations

Multipath errors
    - Low elevation angle signals are more susceptible to multipath effects than high elevation angles 因为低角度的信号更容易被建筑物反射
    - Choke ring antenna 可以减少这种误差，把地面反射的信号过滤