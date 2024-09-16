# 计算角度平均值 角度以度分秒形式给出 例如 45-30-15 表示45度30分15秒
# 144-52-31	89-48-48
# 324-47-47	270-10-32

# 35-01-55	89-20-36	
# 214-58-39	270-39-14

# 19-11-41	89-50-11
# 199-08-05	270-08-48

import math


def decimal_to_dms(decimal):
    degree = int(decimal)
    minute = int((decimal - degree) * 60)
    second = int(((decimal - degree) * 60 - minute) * 60)
    return str(degree) + '-' + str(minute) + '-' + str(second)

def mean_angle(angle_1, angle_2):
    angle_1 = angle_1.split('-')
    angle_2 = angle_2.split('-')
    angle_1 = int(angle_1[0]) + int(angle_1[1])/60 + int(angle_1[2])/3600
    angle_2 = int(angle_2[0]) + int(angle_2[1])/60 + int(angle_2[2])/3600
    # 第二个首先要减去180度
    angle_2 = angle_2 - 180
    # 取平均
    mean_angle = (angle_1 + angle_2) / 2
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

# konwn Mean VCR Mean Slope Dist 	
# get Horizontal  Dist
def get_horizontal_dist(vcr, slope_dist):
    angle = string_to_decimal(vcr)
    return slope_dist * math.cos(math.radians(angle))

# 144-50-9 89-59-39 32.664500000000004
# 35-0-16 89-59-54 17.186
# 19-9-53 89-59-29 21.692

# VCRSlope = [
#     ['89-59-39', 32.6645],
#     ['89-59-54', 17.186],
#     ['89-59-29', 21.692]
# ]

# 144-45-6 90-0-11 32.665
# 34-57-47 89-59-52 17.186
# 19-7-35 89-59-24 21.692

VCRSlope = [
    ['89-50-01', 32.6645],
    ['89-59-52', 17.186],
    ['89-50-07', 21.692]
]

if __name__ == '__main__':
    for i in range(0, 3):
        print(get_horizontal_dist(VCRSlope[i][0], VCRSlope[i][1]))
    # mean distance
    # for i in range(0, 3):
    #     print(mean(distances[i][0], distances[i][1]))

    # for i in range(0, 6, 2):
    #     print(decimal_to_dms(mean_angle(angles[i][0], angles[i+1][0])))
    #     print(decimal_to_dms(mean_angle(angles[i][1], angles[i+1][1])))

# Round 1
# 144-50-9 89-59-39 32.664500000000004
# 35-0-16 89-59-54 17.186
# 19-9-53 89-59-29 21.692

# 0.003325601256438242
# 0.0004999204753421562
# 0.00326013928261994

# Round 2
# 144-45-6 90-0-11 32.665
# 34-57-47 89-59-52 17.186
# 19-7-35 89-59-24 21.692

# 0.09485868362420538
# 0.0006665606337135336
# 0.062363223829185584