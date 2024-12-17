在你的回答中，老师指出你在第三题的分析其实是针对第二题的内容。具体来说，第二题要求分析不同GNSS定位技术的差异，而第三题要求分析所用的测量和数据处理方法。

### 你的问题：
- 在**Q2**中，你已经比较了不同GNSS定位技术（如Stand-alone GPS, DGPS, RTK GPS等）之间的精度差异。
- **Q3**需要你分析**测量方法和数据处理方法**，即：
  1. 这些定位技术使用了什么样的测量方法（例如，伪距、载波相位等）？
  2. 数据处理方法是什么（例如，差分校正、载波相位解算、PPP后处理等）？
  
### 如何改进：
在**Q3**中，应该专注于以下几个方面：
1. **测量方法**：
   - **Stand-alone GPS**：使用伪距测量来计算位置。
   - **DGPS**：使用伪距测量，并依赖参考站的实时差分信息来修正误差。
   - **RTK GPS 和 RTK GNSS**：使用载波相位测量，RTK通过基站与移动接收机之间的实时信息传输来提供更高精度。
   - **PPP**：使用精确的卫星轨道和钟差数据，进行静态模式的后处理，以实现厘米级精度。

2. **数据处理方法**：
   - **Stand-alone GPS**：没有任何实时数据修正，单纯依赖卫星信号和本地接收机的时间戳。
   - **DGPS**：通过接收基站发送的修正信息，减少诸如电离层和对流层误差等影响。
   - **RTK GPS 和 RTK GNSS**：通过载波相位解算，进行基站和移动站之间的实时差分处理。
   - **PPP**：通过精确的卫星轨道和时钟差的后处理数据来提高定位精度。

你可以在第三题的答案中详细阐述每种技术的**测量和数据处理方法**，并且解释这些方法如何影响定位精度。

# Practical 3 Supplement Content
> - PANZhiqing 24037665G 18/12/2024
> - Supplement Content for 
>   - your answer in Q3 is actually for Q2, marks are given for Q2 here
>   - Q3: how about measurements and the data processing methodsused?

## Q3: how about measurements and the data processing methodsused? (Analyse the differences based on the theory of the five positioning techniques.)

### 1. Stand-alone GPS
#### 1.1 Obsevation (Measurements)

在Stand-alone GPS中，多于4个卫星的伪距观测值可以用来计算接收机的位置。

In Stand-alone GPS, pseudorange observations from more than 4 satellites can be used to calculate the position of the receiver.



GPS广播星历提供卫星钟差、开普勒轨道参数和轨道摄动修正量，但是不提供接收机钟差。因此，接收机需要通过接收多个卫星的信号（多于4个），计算出接收机钟差，然后计算出接收机的位置。接收机钟差的计算方法是通过多个卫星的伪距观测值进行解算，然后计算出接收机钟差。

The GPS broadcast ephemeris provides satellite clock error, Keplerian orbit parameters, and orbit perturbation correction, but does not provide receiver clock error. Therefore, the receiver needs to receive signals from multiple satellites (more than 4), calculate the receiver clock error, and then calculate the position of the receiver. The calculation method of the receiver clock error is to solve the pseudorange observation values of multiple satellites, and then calculate the receiver clock error.



#### 1.2 Data Processing Methods

If we consider the clock error correction $\delta_{ion}$, ionospheric correction $\delta_{tro}$, tropospheric correction $\delta_{tide}$, multipath effect correction $\delta_{mul}$, relativistic effect correction $\delta_{rel}$, and error $\epsilon$, then we have:

$$ R_r^s(t_r,t_e) = \rho^s_r(t_r,t_e) - c(\delta t_r - \delta t_s) + \delta_{ion} + \delta_{tro} + \delta_{tide} + \delta_{mul} + \delta_{rel} + \epsilon \tag{1.1} $$

应当注意到，在 Stand-alone GPS 中，我们无法有效消除误差项，如电离层延迟、对流层延迟、多路径效应等。因此，Stand-alone GPS 的定位精度受到这些误差项的影响。

It should be noted that in Stand-alone GPS, we cannot effectively eliminate error terms such as ionospheric delay, tropospheric delay, multipath effect, etc. Therefore, the positioning accuracy of Stand-alone GPS is affected by these error terms.


### 2. DGPS
#### 2.1 Obsevation (Measurements)
使用伪距测量，并依赖参考站的实时差分信息来修正误差。

Using pseudorange measurements and relying on real-time differential information from reference stations to correct errors.

#### 2.2 Data Processing Methods
通过参考参考站发来的信息，我们可以有效消除误差项，如电离层延迟、对流层延迟、卫星钟差、卫星轨道误差等。

By referring to the information sent by the reference station, we can effectively eliminate error terms such as ionospheric delay, tropospheric delay, satellite clock error, satellite orbit error, etc.

### 3. RTK GPS
#### 3.1 Obsevation (Measurements)
使用载波相位测量，RTK通过基站与移动接收机之间的实时信息传输来提供更高精度。

By measuring the carrier phase, we can obtain better positioning accuracy. However, the carrier signal is a kind of periodic and discontinuous sine signal (modulated with the ranging code and navigation message), and measuring the carrier phase itself is not enough to determine the distance. We also need to determine how many complete cycles have passed. This introduces the concept of integer ambiguity (N). Essentially, the carrier phase observation is the difference between the phase of the local oscillator in the receiver at the time the signal is received $t_r$ and the phase of the signal transmitted by the satellite $\Phi^s$, plus an integer ambiguity:

$$ \Phi_r^s = \Phi_r - \Phi^s + N_r^s \tag{3.1} $$


If we consider the clock error and other errors in the above equation, we have:

$$ \Phi_r^s = \frac{\rho^s_r(t_r,t_e)}{\lambda} - f(\delta t_r - \delta t_s) + N_r^s - \frac{\delta_{ion}}{\lambda} + \frac{\delta_{tro}}{\lambda} + \frac{\delta_{tide}}{\lambda} + \frac{\delta_{mul}}{\lambda} + \frac{\delta_{rel}}{\lambda} + \frac{\epsilon}{\lambda} \tag{3.2} $$

where $\lambda$ is the wavelength of the carrier signal. Specifically, the ionosphere will accelerate the phase of the signal while other factors will decelerate it, and that is why the ionospheric correction is positive in the above equation(others are negative).

Another thing to note is that the integer ambiguity depends on the continuous observation of the receiver to the satellite. If the observation is interrupted, it will cause an integer jump, and only the phase observation values that are less than one week are correct.


#### 3.2 Data Processing Methods

通过载波相位解算，进行基站和移动站之间的实时差分处理。之所以能够做到实时，是因为基站同时还发送了模糊度解算的信息，例如使用On-the-fly (OTF) integer ambiguity resolution。

By solving the carrier phase, real-time differential processing between the base station and the mobile station is performed. The reason why it can be done in real-time is that the base station also sends information about the ambiguity resolution, such as using On-the-fly (OTF) integer ambiguity resolution.


### 4. RTK GNSS
Same as RTK GPS but have more satellites to choose from. The number of satellites increased from a dozen to more than thirty if I remember correctly.

### 5. PPP
#### 5.1 Obsevation (Measurements)

Combined dual-frequency pseudoranges and/or carrier phase.

#### 5.2 Data Processing Methods

Using post-processing, based on more accurate satellite orbit and clock data (such as data provided by IGS) to achieve centimeter-level accuracy. These data include observed satellite orbits, satellite clock errors, dual-frequency pseudorange and carrier phase observations, and other factors (such as Earth tides, Sagnac effect, Polar motion, ocean loading, atmospheric loading, crustal motion, antenna phase centre locations, etc.). The PPP method is based on the least squares adjustment of these data to obtain the precise position of the receiver.
