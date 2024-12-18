## Topic 3 Projction
1. Evaluating distortion
   - In order to evaluate the distortion of a projection, five scales are important:
     - Scale along the meridian, h
     - Scale along the parallel, k
     - Maximum scale at a point, a
     - Minimum scale at a point, b
     - Scale along any arc, µ
   - These a and b are not the same as for the reference ellipsoid.
   - These quantities are used in Tissot’s Indicatrix or ellipse of distortion.




## Topic 4 Photogrammetry
1. **Photogrammetry** 
   - is the art, science, and technology of obtaining reliable information about the Earth, its environment, and other physical objects and processes through non-contact imaging and sensor systems. It involves recording, measuring, analyzing, and representing such information. According to the International Society for Photogrammetry and Remote Sensing (ISPRS), photogrammetry integrates photography and remote sensing to derive data through various techniques.
   - In photogrammetry, photographs serve as perspective projections, where 3D objects are transformed into 2D images via a perspective center. The appearance of these photographs depends on factors such as the location of the camera (the position of the perspective center), its orientation (the direction the camera is pointing), the principal distance of the lens, and the size of the image sensor.
   - Photogrammetry typically involves capturing two or more overlapping images from different locations. By measuring corresponding points on these images, the relationship between the object and the camera can be re-established. This process allows the creation of a 3D model of the object through "back projection."

2. | **Category**                   | **Subcategory**                       | **Description**                                                                 |
    |--------------------------------|---------------------------------------|---------------------------------------------------------------------------------|
    | **Type of Equipment Used**     | Analogue                              | Traditional, non-digital methods.                                              |
    |                                | Analytical                            | Uses computational tools for analysis.                                         |
    |                                | Digital                               | Fully digital processes and outputs.                                           |
    | **Type of Cameras Used**       | Metric                                | Stable geometry, designed specifically for photogrammetry.                     |
    |                                | Non-Metric                            | Unstable internal geometry, typically consumer-grade cameras.                  |
    | **Types of Photogrammetry**    | Aerial                                | Camera in the sky, pointing towards the ground.                                |
    |                                | Terrestrial                           | On or near the ground, pointing horizontally or obliquely (upwards/downwards). |
    | **Aerial Photogrammetry**      | Parallel Axis                         | Photographs taken from above the ground.                                       |
    |                                | Vertical                              | No tilt from the vertical axis.                                                |
    |                                | Near Vertical                         | Less than 3° tilt from the vertical axis.                                      |
    |                                | Low Oblique                           | Does not include the horizon.                                                  |
    |                                | High Oblique                          | Includes the horizon.                                                          |
    |                                | Overlapping Parallel Axis Geometry    | Organized in strips and blocks for overlap.                                    |
    |                                | Platforms                             | Examples: Kite, balloon, aeroplane, spacecraft.                                | 


2. | **Parameter**              | **Definition**                                                                                           | **Formula**                                                                                   | **Typical Values**                                                                                               | **Additional Notes**                                                                                                                                                        |
    |----------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **End Lap (E)**            | The amount by which photographs overlap along the flight strip.                                          | \( E\% = \frac{G - B}{G} \cdot 100\% \)                                                      | - Typical: 60%–80% of \( G \) (coverage). <br> - Camera base (\( B \)): 40%–20% of \( G \).                     | - Ensures stereoscopic viewing.<br>- 90% or 80% end lap is possible.<br>- Less than 50% end lap: incomplete coverage.<br>- More than 60% end lap: easier to view but reduces x-parallax and stereo model accuracy. |
    | **Stereo Model**           | 3D view created from a pair of stereo-viewable photographs.                                              | N/A                                                                                           | N/A                                                                                                           | Higher end lap produces poorer accuracy but is easier to view.                                                                                                               |
    | **Side Lap (S)**           | The overlap across adjacent flight lines (block).                                                       | \( S\% = \frac{G - W}{G} \cdot 100\% \)                                                      | - Typical: 30% of \( G \).<br>- Strip spacing (\( W \)): 70% of \( G \).                                      | Ensures sufficient overlap between strips for complete block coverage.                                                                                                      |

3. operations
- Before products can be created (在产品创建之前)
  - Recreate geometric relationship between images and object (重新创建图像和对象之间的几何关系)
- Exterior orientation (外部定向)
  - Define the internal geometry of the camera and stablish relationship between measuring system and images  (定义相机的内部几何，并建立测量系统与图像之间的关系)
  - Interior orientation (内部定向)
- Data then created by 3D digitising either manually or automatically (数据然后通过3D手动或自动数字化创建)

1. Exterior orientation : Recreate the geometric relationship between the image coordinates and the object coordinates. Two approaches to EO : 
   1. Two-step solution (两步解决方案)
       - Relative orientation (RO) (相对定向)
       - Absolute orientation (AO) (绝对定向)
       - A stereopair at one time (一次一个立体对)
   2. Direct solution (直接解决方案) 需要构造共线性方程
        - Collinearity (space resection) (共线性)
        - 1 or more photos at a time (一次一个或多个照片)
        - Simultaneous computation of EO and object coordinates (同时计算EO和对象坐标)
          - Bundle or block adjustment (BA) (捆绑或块调整)
            - Collinearity equations (共线性方程) 同样的点在同一条直线上（物体点，像点，光束点在同一条直线上）

2. Interior orientation (IO)
- EO requires measurement on images in the image coordinate system (EO需要在图像坐标系中测量图像)
- Instruments have own coordinate system (仪器有自己的坐标系)
- IO relates the two coordinate systems (IO将两个坐标系相关联)
  - 2D coordinate transformations (2D坐标变换)
- Rigid body, conformal, affine, projective (刚体，保角，仿射，投影)
  - Allows for distortion correction (允许畸变校正)
    - Camera calibration parameters to be applied (相机校准参数应用)
    - Corrections for image deformation to be applied (应用图像变形校正)
  
1. Image space coordinates
   - 3D origin is perspective centre
   - 2D origin is the principal point
   - x axis is in direction of travel (to the right) Defined by fiducial marks x
   - Conformal transformation 
     - When there is no change in shape
   - Affine transformation
     - When there is a change in shape between the times Of photography and measurement

2. Exterior orientation
3. Relative orientation
   - Establish the relative relationship between a pair of images
   - Use an arbitrary coordinate system based on left image perspective centre and set xr = 1
   - Solve for ω,φ,κ,YL,ZL. Require 5 conjugate point pairs
   - Typically observe von Gruber points

## Topic 5 LiDAR

### Dust & Vapor
- Laser measurements can be weakened by interacting with dust and vapor particles, which scatter the laser beam and the signal returning from the target.
- Using last-pulse measurements can reduce or eliminate this interference.
- Systems that are expected to work in such conditions regularly can be optimized for these environments.

### Reflectivity
- Highly reflective objects may saturate some laser detectors, while the return signal from low-reflectivity objects may occasionally be too weak to register as valid.
- Minimum detectable object size depends on reflectivity.
- A strong sunlight reflection off a highly reflective target may "saturate" a receiver, producing an invalid or less accurate reading.
  * Most acquisition is done in a preferred range of angles to avoid this issue.

### Strip Adjustment
- Systematic Error (shifts & drifts): Wrong or inaccurate calibration of the entire measurement system (block specific), limited accuracy of exterior orientation (GPS- & IMU-related time- and location-specific).
- Result: Offset in planimetric view and height (10’s of cm).
- For removing these discrepancies, strip adjustment algorithms require quantification of these offsets at various locations.
  - Across-track flight lines and ground control are needed to fully adjust the systematic errors.
  - Automatic tie elements detection & 3D adjustments.
  - Improves planimetric accuracy by about 40% and height accuracy by about 25%.

### From point clouds to 3-D surface models
- Points are used to create 3D surface models for applications.
- Triangular Irregular Networks (TINs) are used to develop Digital Elevation Models (DEMs).
- Points must be classified: “bare earth” points hit the “ground”; other point categories include tree canopy and buildings.
- Correct identification of “bare earth” is critical for mapping applications.


### LiDAR compared to Survey
| + | - |
| --- | --- |
| Rapid data collection | Requires survey for control |
| High point density | Large data volumes |
| High accuracy | Requires processing expertise |
| Non-contact | |
| Immediate data use or analysis for terrain models | |

### Overview of operation
- Scan scene from different locations
- Join scans together
  - Targeted points
  - Object features
  - Cloud constraints
- Geo-referencing
  - Surveyed control points
- Modelling

### Geo-referencing
- Direct
  - Integrate traversing with scanning
- Indirect
  - Use targets with known object-space coordinates
  - 3D conformal transformation