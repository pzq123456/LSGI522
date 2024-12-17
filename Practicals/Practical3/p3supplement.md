# Practical 3 Supplement Content
> - PANZhiqing 24037665G 18/12/2024
> - Supplement Content for 
>   - your answer in Q3 is actually for Q2, marks are given for Q2 here
>   - Q3: how about measurements and the data processing methodsused?

## Q3: how about measurements and the data processing methodsused? (Analyse the differences based on the theory of the five positioning techniques.)

### 1. Stand-alone GPS
#### 1.1 Obsevation (Measurements)

In Stand-alone GPS, pseudorange observations from more than 4 satellites can be used to calculate the position of the receiver.

The GPS broadcast ephemeris provides satellite clock error, Keplerian orbit parameters, and orbit perturbation correction, but does not provide receiver clock error. Therefore, the receiver needs to receive signals from multiple satellites (more than 4), calculate the receiver clock error, and then calculate the position of the receiver. The calculation method of the receiver clock error is to solve the pseudorange observation values of multiple satellites, and then calculate the receiver clock error.



#### 1.2 Data Processing Methods

If we consider the clock error correction $\delta_{ion}$, ionospheric correction $\delta_{tro}$, tropospheric correction $\delta_{tide}$, multipath effect correction $\delta_{mul}$, relativistic effect correction $\delta_{rel}$, and error $\epsilon$, then we have:

$$ R_r^s(t_r,t_e) = \rho^s_r(t_r,t_e) - c(\delta t_r - \delta t_s) + \delta_{ion} + \delta_{tro} + \delta_{tide} + \delta_{mul} + \delta_{rel} + \epsilon \tag{1.1} $$


It should be noted that in Stand-alone GPS, we cannot effectively eliminate error terms such as ionospheric delay, tropospheric delay, multipath effect, etc. Therefore, the positioning accuracy of Stand-alone GPS is affected by these error terms.


### 2. DGPS
#### 2.1 Obsevation (Measurements)

Using pseudorange measurements and relying on real-time differential information from reference stations to correct errors.

#### 2.2 Data Processing Methods

By referring to the information sent by the reference station, we can effectively eliminate error terms such as ionospheric delay, tropospheric delay, satellite clock error, satellite orbit error, etc.

### 3. RTK GPS
#### 3.1 Obsevation (Measurements)

By measuring the carrier phase, we can obtain better positioning accuracy. However, the carrier signal is a kind of periodic and discontinuous sine signal (modulated with the ranging code and navigation message), and measuring the carrier phase itself is not enough to determine the distance. We also need to determine how many complete cycles have passed. This introduces the concept of integer ambiguity (N). Essentially, the carrier phase observation is the difference between the phase of the local oscillator in the receiver at the time the signal is received $t_r$ and the phase of the signal transmitted by the satellite $\Phi^s$, plus an integer ambiguity:

$$ \Phi_r^s = \Phi_r - \Phi^s + N_r^s \tag{3.1} $$


If we consider the clock error and other errors in the above equation, we have:

$$ \Phi_r^s = \frac{\rho^s_r(t_r,t_e)}{\lambda} - f(\delta t_r - \delta t_s) + N_r^s - \frac{\delta_{ion}}{\lambda} + \frac{\delta_{tro}}{\lambda} + \frac{\delta_{tide}}{\lambda} + \frac{\delta_{mul}}{\lambda} + \frac{\delta_{rel}}{\lambda} + \frac{\epsilon}{\lambda} \tag{3.2} $$

where $\lambda$ is the wavelength of the carrier signal. Specifically, the ionosphere will accelerate the phase of the signal while other factors will decelerate it, and that is why the ionospheric correction is positive in the above equation(others are negative).

Another thing to note is that the integer ambiguity depends on the continuous observation of the receiver to the satellite. If the observation is interrupted, it will cause an integer jump, and only the phase observation values that are less than one week are correct.


#### 3.2 Data Processing Methods


By solving the carrier phase, real-time differential processing between the base station and the mobile station is performed. The reason why it can be done in real-time is that the base station also sends information about the ambiguity resolution, such as using On-the-fly (OTF) integer ambiguity resolution.


### 4. RTK GNSS
Same as RTK GPS but have more satellites to choose from. The number of satellites increased from a dozen to more than thirty if I remember correctly.

### 5. PPP
#### 5.1 Obsevation (Measurements)

Combined dual-frequency pseudoranges and/or carrier phase.

#### 5.2 Data Processing Methods

Using post-processing, based on more accurate satellite orbit and clock data (such as data provided by IGS) to achieve centimeter-level accuracy. These data include observed satellite orbits, satellite clock errors, dual-frequency pseudorange and carrier phase observations, and other factors (such as Earth tides, Sagnac effect, Polar motion, ocean loading, atmospheric loading, crustal motion, antenna phase centre locations, etc.). The PPP method is based on the least squares adjustment of these data to obtain the precise position of the receiver.
