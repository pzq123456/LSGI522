# 计算向量夹角
import math
import numpy as np

def decimal_to_dms(decimal):
    degree = int(decimal)
    minute = int((decimal - degree) * 60)
    second = int(((decimal - degree) * 60 - minute) * 60)
    return str(degree) + '-' + str(minute) + '-' + str(second)

def string_to_decimal(angle, isRadian=True):
    angle = angle.split('-')
    angles = int(angle[0]) + int(angle[1])/60 + int(angle[2])/3600
    if isRadian:
        return math.radians(angles)
    return angles

def angle_between_vectors(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return math.acos(dot_product / (norm_v1 * norm_v2))

# 弧度转度分秒
def radian_to_dms(radian):
    degree = math.degrees(radian)
    return decimal_to_dms(degree)


# 324-50-9
# 215-0-16
# 199-9-53
round1 = [
    "324-50-9",
    "215-0-16",
    "199-9-53"
] # A B C


# 324-45-6
# 214-57-46
# 199-7-35
round2 =[
    "324-45-6",
    "214-57-46",
    "199-7-35"
] # A B C

def getACHelper(AaddC,a,c,x,y):
    sinAC = math.sin(AaddC)
    cosAC = math.cos(AaddC)
    sinx = math.sin(x)
    siny = math.sin(y)

    # 分子
    numerator = a * sinx * sinAC
    # 分母
    denominator = c * siny + a * sinx * cosAC

    return math.atan(numerator / denominator)


def getAC(AaddC,a,c,x,y):
    A = getACHelper(AaddC,a,c,x,y)
    C = getACHelper(AaddC,c,a,y,x)

    return A, C

# Station A: (836510.893 mE, 818629.171 mN) 
# Station B: (836551.654 mE, 818638.135 mN) 
# Station C: (836558.048 mE, 818640.893 mN)

# 解三角形辅助函数
def getAPHelper(A, X, c):
    alpha1 = np.pi - A - X
    # 求解AP
    # AP / alpha1 = c / sin(X)
    AP = c * math.sin(alpha1) / math.sin(X)
    BP = c * math.sin(A) / math.sin(X)
    return AP, BP

def getAzimuth(A,B):
    return math.atan2((B[1] - A[1]), (B[0] - A[0]))

def getDeltaEandDeltaN(AP, A, B, angle_A):
    azimuth = getAzimuth(A,B)
    print('azimuthAB:', radian_to_dms(azimuth))
    print('azimuthAP:', radian_to_dms(azimuth + angle_A))
    deltaE = AP * math.cos(azimuth + angle_A)
    deltaN = AP * math.sin(azimuth + angle_A)
    return deltaE, deltaN

def getAP(A, B, angle_A, X, c):
    AP, BP = getAPHelper(angle_A, X, c)
    print('AP:', AP)
    # print('BP:', BP)
    deltaE, deltaN = getDeltaEandDeltaN(AP, A, B, angle_A)
    return deltaE, deltaN

def resection(roundAngles):
    # 1. From the known coordinates of A, B, and C calculate lengths a and c, and angle α at station B.
    # 三个点
    A = np.array([836510.893, 818629.171])
    B = np.array([836551.654, 818638.135])
    C = np.array([836558.048, 818640.893])

    # 两个向量
    BA = A - B
    BC = C - B

    # 计算两个向量的夹角
    alpha = angle_between_vectors(BA, BC)

    # length
    c = np.linalg.norm(BA)
    a = np.linalg.norm(BC)

    print('c:', c)
    print('a:', a)
    # print('alpha:', alpha)
    print('alpha:', radian_to_dms(alpha))

    # 2. Subtract the sum of angles x, y, and α in figure ABCP from 360° to obtain the sum of angles A + C 
    X = string_to_decimal(roundAngles[0]) - string_to_decimal(roundAngles[1]) # angle A B
    Y = string_to_decimal(roundAngles[1]) - string_to_decimal(roundAngles[2]) # angle B C

    AaddC = 2 * np.pi - (alpha + X + Y) 

    print('A+C:', radian_to_dms(AaddC))

    angle_A, angle_C = getAC(AaddC,a,c,X,Y)
    print('X:', X)
    print('Y:', Y)
    # print('A:', angle_A)
    print('A:', radian_to_dms(angle_A))
    # print('C:', angle_C)
    print('C:', radian_to_dms(angle_C))


    # 4. From angle A and azimuth AB, calculate azimuth AP in triangle ABP. 
    # Then solve for length AP using the law of sines, 
    # where 𝛼𝛼1 = 180° - A - x. Calculate the ∆E and ∆N of AP followed by the coordinates of P.

    deltaE, deltaN = getAP(A, B, angle_A, X, c)
    # 也可以带入 C, Y, a 求解
    deltaE2, deltaN2 = getAP(C, B, angle_C, Y, a)
    print('deltaE:', deltaE, 'deltaN:', deltaN)
    print('AP:', deltaE + A[0], deltaN + A[1])
    print('deltaE2:', deltaE2, 'deltaN2:', deltaN2)
    print('AP2:', deltaE2 +C[0], deltaN2 + C[1])
    print('A+C+X+Y+alpha:', alpha + X + Y + angle_A + angle_C - 2*np.pi)

if __name__ == '__main__':
    resection(round1)

# 144-50-9 
# 35-0-16
# 19-9-53

# 32.665
# 17.185
# 21.691

# 144-45-6
# 34-57-47
# 19-7-35

# 32.665
# 17.185
# 21.692