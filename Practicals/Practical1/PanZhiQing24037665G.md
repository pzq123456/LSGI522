# resection sheet
> - PanZhiQing 24037665g

## Three-point resection
1. From the known coordinates of A, B, and C calculate lengths a and c, and angle α at station B. 
    c: 41.7350262608734
    a: 6.963461782748601
    alpha: 169-4-12
2. Subtract the sum of angles x, y, and α in figure ABCP from 360° to obtain the sum of angles A + C 
   $$A + C = 360° - (α + x + y)$$ 
    - A + C: 65-14-23

3. Calculate angles A and C using the following: 
    - A: 22-49-31
    - C: 42-24-51

4. From angle A and azimuth AB, calculate azimuth AP in triangle ABP. Then solve for length AP using the law of sines, where 𝛼𝛼1 = 180° - A - x.Calculate the ∆E and ∆N of AP followed by the coordinates of P. 
   - Solve the triangle ABP(Round1):
    - AP: 32.62646401200535
    - azimuthAB: 12-24-10
    - azimuthAP: 35-13-52
    - deltaE: 26.65030422241778 deltaN: 18.82146218494358
    - **P: 836537.5433042224 818647.9924621849**
  - Solve the triangle ABP(Round2):
    - AP: 32.619147037426494
    - azimuthAB: 12-24-10
    - azimuthAP: 35-17-17
    - deltaE: 26.62555889420214 deltaN: 18.843788552746577
    - **P: 836537.5185588943 818648.0147885528**

5. In the manner outlined in step 4, use triangle BCP to calculate the coordinates of P to obtain a check. 
   - Solve the triangle BCP(Round1):
     - CP : 11.41923988409439
     - azimuthBC: 203-19-57
     - azimuthCP: 160-55-6
     - deltaE: -10.791793992092192 deltaN: 3.7331249594321028
     - **P : 836547.2562060079, 818644.6261249594**
     - Difference between P1 and P2: 9.717117445543408 3.3613701018039137
   - Solve the triangle BCP(Round2):
     - CP : 11.455825633046228
     - azimuthBC: 203-19-57
     - azimuthCP: 160-52-4
     - deltaE: -10.823076487008173 deltaN: 3.7545913614040383
     - **P : 836547.2249235129, 818644.6475913614**
     - Difference between P1 and P2: errorE 9.706364618614316 errorN 3.3671971913427114

6. Error between two rounds
    - For P1 only: errorE 0.020529668079689145 errorN 0.02729349152650684
## Leveling
- Given the (arbitrary) RL of BM11 as 25.362 mpd.
- Result : 25.362 + 0.171 = 25.533 mpd.

## Appendix

### Round1
<!-- | c | a | alpha | X | Y | A | C |
|---|---|-------|---|---|---|---|
| 41.7350262608734 | 6.963461782748601 | 169-4-12 | 1.9173459941888038 | 0.27635834264286885 | 22-49-31 | 42-24-51 |

| AP | azimuthAB | azimuthAP | P1 | deltaE | deltaN |
|----|-----------|-----------|----|--------|--------|
| 32.62015515078579 | 12-24-10 | 35-13-42 | [836537.5390885624, 818647.9874950612] | 26.646088562305245 | 18.816495061278612 |

| CP | azimuthBC | azimuthCP | P2 | deltaE | deltaN |
|----|-----------|-----------|----|--------|--------|
| 11.41923988409439 | 203-19-57 | 160-55-6 | [836547.2562060079, 818644.6261249594] | -10.791793992092192 | 3.7331249594321028 | -->

| Parameters | Value |
|------------|-------|
| c | 41.7350262608734 |
| a | 6.963461782748601 |
| alpha | 169-4-12 |
| X | 1.9173459941888038 |
| Y | 0.27635834264286885 |
| A | 22-49-31 |
| C | 42-24-51 |
| AP | 32.62015515078579 |
| azimuthAB | 12-24-10 |
| azimuthAP | 35-13-42 |
| P1 | [836537.5390885624, 818647.9874950612] |
| deltaE | 26.646088562305245 |
| deltaN | 18.816495061278612 |
| CP | 11.41923988409439 |
| azimuthBC | 203-19-57 |
| azimuthCP | 160-55-6 |
| P2 | [836547.2562060079, 818644.6261249594] |
| deltaE | -10.791793992092192 |
| deltaN | 3.7331249594321028 |

### Round2
<!-- | c | a | alpha | X | Y | A | C |
|---|---|-------|---|---|---|---|
| 41.7350262608734 | 6.963461782748601 | 169-4-12 | 1.9156830832625982 | 0.27609654325506955 | 22-53-7 | 42-27-52 |

| AP | azimuthAB | azimuthAP | P1 | deltaE | deltaN |
|----|-----------|-----------|----|--------|--------|
| 32.619147037426494 | 12-24-10 | 35-17-17 | [836537.5185588943, 818648.0147885528] | 26.62555889420214 | 18.843788552746577 |

| CP | azimuthBC | azimuthCP | P2 | deltaE | deltaN |
|----|-----------|-----------|----|--------|--------|
| 11.455825633046228 | 203-19-57 | 160-52-4 | [836547.2249235129, 818644.6475913614] | -10.823076487008173 | 3.7545913614040383 | -->

| Parameters | Value |
|------------|-------|
| c | 41.7350262608734 |
| a | 6.963461782748601 |
| alpha | 169-4-12 |
| X | 1.9156830832625982 |
| Y | 0.27609654325506955 |
| A | 22-53-7 |
| C | 42-27-52 |
| AP | 32.619147037426494 |
| azimuthAB | 12-24-10 |
| azimuthAP | 35-17-17 |
| P1 | [836537.5185588943, 818648.0147885528] |
| deltaE | 26.62555889420214 |
| deltaN | 18.843788552746577 |
| CP | 11.455825633046228 |
| azimuthBC | 203-19-57 |
| azimuthCP | 160-52-4 |
| P2 | [836547.2249235129, 818644.6475913614] |
| deltaE | -10.823076487008173 |
| deltaN | 3.7545913614040383 |


### Script Output
> source code: [resection.py](https://github.com/pzq123456/LSGI522/blob/main/Practicals/Practical1/resection.py)

```
### Round 1 ###
c: 41.7350262608734
a: 6.963461782748601
alpha: 169-4-12
A+C: 65-14-23
X: 1.9173459941888038
Y: 0.27635834264286885
A: 22-49-31
C: 42-24-51
AP: 32.62015515078579
azimuthAB: 12-24-10
azimuthAP: 35-13-42
AP: 11.41923988409439
azimuthAB: 203-19-57
azimuthAP: 160-55-6
P1: [836537.5390885624, 818647.9874950612] deltaE: 26.646088562305245 deltaN: 18.816495061278612
P2: [836547.2562060079, 818644.6261249594] deltaE: -10.791793992092192 deltaN: 3.7331249594321028
errorE 9.717117445543408 errorN 3.3613701018039137
### Round 2 ###
c: 41.7350262608734
a: 6.963461782748601
alpha: 169-4-12
A+C: 65-21-0
X: 1.9156830832625982
Y: 0.27609654325506955
A: 22-53-7
C: 42-27-52
AP: 32.619147037426494
azimuthAB: 12-24-10
azimuthAP: 35-17-17
AP: 11.455825633046228
azimuthAB: 203-19-57
azimuthAP: 160-52-4
P1: [836537.5185588943, 818648.0147885528] deltaE: 26.62555889420214 deltaN: 18.843788552746577
P2: [836547.2249235129, 818644.6475913614] deltaE: -10.823076487008173 deltaN: 3.7545913614040383
errorE 9.706364618614316 errorN 3.3671971913427114
### Between Round Error ###
errorE 0.020529668079689145 errorN 0.02729349152650684
```
