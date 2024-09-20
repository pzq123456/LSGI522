# 计算角度平均值 角度以度分秒形式给出 例如 45-30-15 表示45度30分15秒
# 144-52-31	89-48-48
# 324-47-47	270-10-32

# 35-01-55	89-20-36	
# 214-58-39	270-39-14

# 19-11-41	89-50-11
# 199-08-05	270-08-48

import math

def minus(angle_1, angle_2):
    angle_1 = angle_1.split('-')
    angle_2 = angle_2.split('-')
    angle_1 = int(angle_1[0]) + int(angle_1[1])/60 + int(angle_1[2])/3600
    angle_2 = int(angle_2[0]) + int(angle_2[1])/60 + int(angle_2[2])/3600
    return angle_1 - angle_2

def decimal_to_dms(decimal):
    degree = int(decimal)
    minute = int((decimal - degree) * 60)
    second = int(((decimal - degree) * 60 - minute) * 60)
    return str(degree) + '-' + str(minute) + '-' + str(second)

def mean_angle_HCR(angle_1, angle_2):
# FL HCR and FR HCR are opposite, so that the difference should be 180°. 
# Error = (FL HCR - FR HCR) - 180°.
# Correction = - Error/2. 
# Mean HCR = FL HCR + Correction E.g. 
# Error = (a -p)-180°. Mean HCR = a + Correction
    angle_1 = angle_1.split('-')
    angle_2 = angle_2.split('-')
    angle_1 = int(angle_1[0]) + int(angle_1[1])/60 + int(angle_1[2])/3600
    angle_2 = int(angle_2[0]) + int(angle_2[1])/60 + int(angle_2[2])/3600
    # # 第二个首先要减去180度
    # angle_2 = angle_2 - 180
    # # 取平均
    # mean_angle = (angle_1 + angle_2) / 2

    Error = (angle_1 - angle_2) + 180
    Correction = - Error / 2
    mean_angle = angle_1 + Correction

    return mean_angle



def mean_angle_VCR(angle_1, angle_2):
# A vertical circle is 360°. 
# FL VCR + FR VCR should be 360°. 
# Error = (FL VCR + FR VCR) - 360°. 
# Correction = - Error/2. 
# Mean VCR = FL VCR + Correction Error=(b+q)-360°. 
# Mean VCR= b + Correction
    angle_1 = angle_1.split('-')
    angle_2 = angle_2.split('-')
    angle_1 = int(angle_1[0]) + int(angle_1[1])/60 + int(angle_1[2])/3600
    angle_2 = int(angle_2[0]) + int(angle_2[1])/60 + int(angle_2[2])/3600

    Error = (angle_1 + angle_2) - 360
    Correction = - Error / 2
    mean_angle = angle_1 + Correction

    return mean_angle

# angles = [
#     ['144-52-31', '89-48-48'],
#     ['324-47-47', '270-10-32'], 
#     ['35-01-55', '89-20-36'],
#     ['214-58-39', '270-39-14'],
#     ['19-11-41', '89-50-11'],
#     ['199-08-05', '270-08-48']
# ]

angles = [
    ['144-43-34', '89-50-01'],
    ['324-46-39', '270-10-22'], 
    ['34-57-05', '89-20-41'],
    ['214-58-29', '270-39-04'],
    ['19-07-25', '89-50-07'],
    ['199-07-46', '270-08-41']
]

def mean(dis1, dis2):
    return (dis1 + dis2) / 2

# distances = [
#     [32.664, 32.665],
#     [17.186, 17.186],
#     [21.692, 21.692]
# ]

# distances = [
#     [32.665, 32.664],
#     [17.186, 17.186],
#     [21.691, 21.692]
# ]

def string_to_decimal(angle):
    angle = angle.split('-')
    return int(angle[0]) + int(angle[1])/60 + int(angle[2])/3600


# If Mean VCR <90°, 
# =cos(90°-Mean VCR) x Mean Slope Dist. 
# If Mean VCR > 90°, 
# =cos(Mean VCR - 90°) x Mean Slope Dist. 
# Or, (since VCR in the totalstation is set to 
# Zenth angle), 
# =sin(Mean VCR) x Mean Slope Dist. 

def mean_slope(mean_angle, mean_slope_dist):
    if mean_angle < 90:
        return math.cos(math.radians(90 - mean_angle)) * mean_slope_dist
    else:
        return math.cos(math.radians(mean_angle - 90)) * mean_slope_dist

VCRSlope = [
    ['89-49-8', 32.6645],
    ['89-20-41', 17.186],
    ['89-50-41', 21.692]
]


# VCRSlope = [
#     ['89-49-49', 32.6645],
#     ['89-20-48', 17.186],
#     ['89-50-42', 21.692]
# ]

if __name__ == '__main__':
    # mean distance
    # for i in range(0, 3):
    #     print(mean(distances[i][0], distances[i][1]))

    print('Mean HCR Slope')
    for i in range(0, 6, 2):
        print(decimal_to_dms(mean_angle_HCR(angles[i][0], angles[i+1][0])))
        
    print('Mean VCR Slope')
    for i in range(0, 6, 2):
        print(decimal_to_dms(mean_angle_VCR(angles[i][1], angles[i+1][1])))

    print('Mean Slope')
    for i in range(0, 3):
        print(mean_slope(string_to_decimal(VCRSlope[i][0]), VCRSlope[i][1]))

# 324-50-9
# 215-0-16
# 199-9-53

# 144-54-53
# 35-3-32
# 19-13-29
    # # 计算差值 角度
    # print(minus('144-54-53', '324-50-9'))
    # print(minus('35-3-32', '215-0-16'))
    # print(minus('19-13-29', '199-9-53'))

    # # 转化为度分秒
    # print(decimal_to_dms(minus('144-54-53', '324-50-9')))
    # print(decimal_to_dms(minus('35-3-32', '215-0-16')))
    # print(decimal_to_dms(minus('19-13-29', '199-9-53')))
