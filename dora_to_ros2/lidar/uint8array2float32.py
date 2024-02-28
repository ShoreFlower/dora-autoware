# def uint8_2_float(uint8_array):
#     # transfrom the datatype from uint8 array to float32
    
#     # transfrom the element in uint8 array to binary ,then transform to string
#     bin_element_array = [str(bin(uint8_array[i]))[2:] for i in range(0, 4)]
#     for i in range(0, 4):
#         if len(bin_element_array[i]) < 8:
#             bin_element_array[i] = "0" * (8-len(bin_element_array[i])) + bin_element_array[i]  # the binary_element shoud have 8 bit

    
#     sign = int(bin_element_array[3][0]) # if 0, the number is non-negtive ,else the number is negtive
#     exp_bit = bin_element_array[3][1:] + bin_element_array[2][0]  # 8 bit for exponent
#     fraction_bit = bin_element_array[2][1:] + bin_element_array[1] + bin_element_array[0] # 23 bit for fraction
    
#     # compute the exponent
#     exp_num = 0
#     for i in range(0,8):
#         exp_num = exp_num + int(exp_bit[i]) * 2**(7-i)
#     exp_result = 2**(exp_num - 127)

#     # compute the fraction
#     fraction_num = 0
#     for i in range(0, 23):
#         fraction_num += int(fraction_bit[i]) * 2**(-1 * (i+1))
#     fraction_result = fraction_num + 1

#     return (-1)**(sign) * exp_result * fraction_result

import numpy as np
import math
def uint8_2_float(uint8_array):
    # 将uint8数组重新组织为uint32数组
    uint32_array = uint8_array.view(np.uint32)
    # (uint8_array[0] << 24) | (uint8_array[1] << 16) | (uint8_array[2] << 8) | uint8_array[3]
     # 将uint32数组解释为float32数组
    float32_array = uint32_array.view(np.float32)
    #float32_array1 = float32_array[0:(float32_array.size-1-float32_array.size%3)]
    # 重新形状为N*4的数组
    # float32_array = float32_array.reshape(float32_array.size//3,3)
    
    return float32_array