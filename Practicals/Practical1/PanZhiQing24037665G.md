# resection sheet
> - PanZhiQing 24037665g

## Three-point resection
0. Get the mean angle of two rounds: 
    - A: 144-47-37
    - B: 34-59-1
    - C: 19-8-43
1. From the known coordinates of A, B, and C calculate lengths a and c, and angle α at station B. 
   - c: 41.7350262608734
   - a: 6.963461782748601
   - alpha: 169-4-12
2. Subtract the sum of angles x, y, and α in figure ABCP from 360° to obtain the sum of angles A + C 
   - A+C: 65-16-53

3. Calculate angles A and C using the following: 
   - A: 22-50-21
   - C: 42-26-31

4. From angle A and azimuth AB, calculate azimuth AP in triangle ABP. Then solve for length AP using the law of sines, where 𝛼𝛼1 = 180° - A - x.Calculate the ∆E and ∆N of AP followed by the coordinates of P. 
   - AP: 32.627620918129494
   - azimuthAB: 12-24-10
   - azimuthAP: 35-14-31
   - azimuthAP: 160-53-25
   - **P1: [836537.5406955964, 818647.9981603324]** 
   - deltaE: 26.647695596272634 deltaN: 18.827160332497133

5. In the manner outlined in step 4, use triangle BCP to calculate the coordinates of P to obtain a check. 
   - CP : 21.70329093140128
   - azimuthBC: 203-19-57
   - azimuthCP: 160-55-6
   - **P2: [836537.5406955964, 818647.9981603324]** 
   - deltaE: -20.507304403638898 deltaN: 7.1051603324300645

## Leveling
- Given the (arbitrary) RL of BM11 as 25.362 mpd.
- Result : 25.362 + 0.171 = 25.533 mpd.

## Appendix

| Parameter | Value |
| --- | --- |
| meanAngleA | 144-47-37 |
| meanAngleB | 34-59-1 |
| meanAngleC | 19-8-43 |
| c | 41.7350262608734 |
| a | 6.963461782748601 |
| alpha | 169-4-12 |
| A+C | 65-16-53 |
| X | 1.9165460516149735 |
| Y | 0.2764310646950353 |
| A | 22-50-21 |
| C | 42-26-31 |
| AP | 32.627620918129494 |
| azimuthAB | 12-24-10 |
| azimuthAP | 35-14-31 |
| AP | 21.70329093140128 |
| azimuthAB | 203-19-57 |
| azimuthAP | 160-53-25 |
| P1 | [836537.5406955964, 818647.9981603324] |
| deltaE | 26.647695596272634 |
| deltaN | 18.827160332497133 |
| P2 | [836537.5406955964, 818647.9981603324] |
| deltaE | -20.507304403638898 |
| deltaN | 7.1051603324300645 |
| errorE | 0.0 |
| errorN | 0.0 |


### Script Output
> source code: [resection.py](https://github.com/pzq123456/LSGI522/blob/main/Practicals/Practical1/resection.py)

```
meanangle: 144-47-37
meanangle: 34-59-1
meanangle: 19-8-43
c: 41.7350262608734
a: 6.963461782748601
alpha: 169-4-12
A+C: 65-16-53
X: 1.9165460516149735
Y: 0.2764310646950353
A: 22-50-21
C: 42-26-31
AP: 32.627620918129494
azimuthAB: 12-24-10
azimuthAP: 35-14-31
AP: 21.70329093140128
azimuthAB: 203-19-57
azimuthAP: 160-53-25
P1: [836537.5406955964, 818647.9981603324] deltaE: 26.647695596272634 deltaN: 18.827160332497133
P2: [836537.5406955964, 818647.9981603324] deltaE: -20.507304403638898 deltaN: 7.1051603324300645
errorE 0.0 errorN 0.0
```
