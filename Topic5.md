# Topic5 Laser Scanning

1. List at least 5 differences between output usefulness of LiDAR and Photogrammetry as a data source for topographic mapping ?

| LiDAR | Photogrammetry |
| --- | --- |
| Day or night data acquisition | Day time collection only |
| Direct acquisition of 3D collection | Complicated and sometimes unreliable procedures |
| Vertical accuracy is better than planimetric | Planimetric accuracy is better than vertical |
| Point cloud difficult to derive semantic information; however, intensity values can be used to produce a visually rich image like product (example of an intensity image) | Rich in semantic information |
| Can penetrate vegetation | Cannot penetrate vegetation |

- 雷达
  - 立即就能获得地形数据，不需要复杂的数据处理
  - 可以在白天和黑夜进行数据采集
  - 3D数据直接采集
  - 垂直精度比平面精度好

2.Compared to survey
| + | - |
| --- | --- |
| Rapid data collection | Requires survey for control |
| High point density | Large data volumes |
| High accuracy | Requires processing expertise |
| Non-contact | |
| Immediate data use or analysis for terrain models | |

## Measurement principles
1. Active distance measurement: sensor-object-sensor. send-reflection-receive.
2. Possible for “none cooperative targets”, resp.reflectorless ranging (without prisms)
3. Study of an object by emitting a certain amount of laser energy and by the analysis of the backscattered energy (range, amplitude, etc.) 
4. What precision does the clock need for σt = 5 mm? c = 3 * 10^8 m/s 
    $$ σd = \sqrt{ {σc / 2}^2 + {σt * c / 2}^2 }$$
5. LiDAR Data Characteristics
   1. Raw return data are XYZ points
   2. High spatial resolution
       - Laser footprint on ground ≤ 0.50 meters
       - Typical density is 0.5 to 20+ pulses/m2
       - 2 to 3 returns/pulse in forest areas 发射一个激光脉冲，接收到的反射信号可能有多个
       - Surface/canopy models typically 1 to 5m grid 
   3. Large volume of data
       - 5,000 to 60,000+ pulses/hectare (10,000 m2 =100 m x 100 m)
       - 10 to 100+ thousands of returns/hectare
       - 0.4 to 5.4+ MB/hectare
   4. 反射回的的信号强度可用于区分不同地物
   5. Dust & Vapor can affect the signal 事前需要做相关测量实验
   6. 同一个型号（same pause）可能会有多个反射信号，例如首先收到树叶的反射（first return），然后收到地面的反射（last return）
6. IMU Inertial Measurement Unit
    - Combination of accelerometers and gyroscopes
    - Provides position and orientation via software
    - The main accelerometer error source is the drift，开的越远（运行时间越长），误差越大

## Geo-referencing
1. Direct : Integrate traversing with scanning 将雷达放在控制点上
2. Indirect : 扫描到控制点上
   - Use targets with known object-space coordinates
   - 3D conformal transformation


## Dust & Vapor
- Laser measurements can be weakened by interacting with dust and vapor particles, which scatter the laser beam and the signal returning from the target.
- Using last-pulse measurements can reduce or eliminate this interference.
- Systems that are expected to work in such conditions regularly can be optimized for these environments.

## Reflectivity
- Highly reflective objects may saturate some laser detectors, while the return signal from low-reflectivity objects may occasionally be too weak to register as valid.
- Minimum detectable object size depends on reflectivity.
- A strong sunlight reflection off a highly reflective target may "saturate" a receiver, producing an invalid or less accurate reading.
  * Most acquisition is done in a preferred range of angles to avoid this issue.

## Strip Adjustment
- Systematic Error (shifts & drifts): Wrong or inaccurate calibration of the entire measurement system (block specific), limited accuracy of exterior orientation (GPS- & IMU-related time- and location-specific).
- Result: Offset in planimetric view and height (10’s of cm).
- For removing these discrepancies, strip adjustment algorithms require quantification of these offsets at various locations.
  - Across-track flight lines and ground control are needed to fully adjust the systematic errors.
  - Automatic tie elements detection & 3D adjustments.
  - Improves planimetric accuracy by about 40% and height accuracy by about 25%.

## From point clouds to 3-D surface models
- Points are used to create 3D surface models for applications.
- Triangular Irregular Networks (TINs) are used to develop Digital Elevation Models (DEMs).
- Points must be classified: “bare earth” points hit the “ground”; other point categories include tree canopy and buildings.
- Correct identification of “bare earth” is critical for mapping applications.


## LiDAR compared to Survey
| + | - |
| --- | --- |
| Rapid data collection | Requires survey for control |
| High point density | Large data volumes |
| High accuracy | Requires processing expertise |
| Non-contact | |
| Immediate data use or analysis for terrain models | |

## Overview of operation
- Scan scene from different locations
- Join scans together
  - Targeted points
  - Object features
  - Cloud constraints
- Geo-referencing
  - Surveyed control points
- Modelling

## Geo-referencing
- Direct
  - Integrate traversing with scanning
- Indirect
  - Use targets with known object-space coordinates
  - 3D conformal transformation