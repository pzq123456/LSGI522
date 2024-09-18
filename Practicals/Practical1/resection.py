# 计算向量夹角
import numpy as np

def decimal_to_dms(decimal):
    degree = int(decimal)
    minute = int((decimal - degree) * 60)
    second = int(((decimal - degree) * 60 - minute) * 60)
    return str(degree) + '-' + str(minute) + '-' + str(second)

def string_to_decimal(angle):
    angle = angle.split('-')
    return int(angle[0]) + int(angle[1])/60 + int(angle[2])/3600

def angle_between_vectors(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return np.arccos(dot_product / (norm_v1 * norm_v2))

# Station A: (836510.893 mE, 818629.171 mN) 
# Station B: (836551.654 mE, 818638.135 mN) 
# Station C: (836558.048 mE, 818640.893 mN)
def resection():
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
    print('alpha:', alpha)

    # 2. Subtract the sum of angles x, y, and α in figure ABCP from 360° to obtain the sum of angles A + C 
    AaddC = 2 * np.pi - alpha

if __name__ == '__main__':
    resection()