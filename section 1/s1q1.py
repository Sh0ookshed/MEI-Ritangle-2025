#SECTION 1 , QUESTION 1
left = [1,2,3,4,5,6,7,8]

middle = [10,11,12,13,14,15,16,17,18,19,20]

right = [1,2,3,4,5,6,7,8,9]


def get_s(l,m,r):
    #locals
    total_s = 0
    l_index = 0
    m_index = 0
    r_index = 0
    
    for x in range (792):

        if l_index > 7:
            l_index = 0

        if m_index > 10:
            m_index = 0

        if r_index > 8:
            r_index = 0

        add = str(l[l_index]) + str(m[m_index]) + str(r[r_index])
        total_s += int(add)
        l_index += 1
        m_index += 1
        r_index += 1
    return total_s

def get_t(l,m,r):
    #locals
    total_t = 0
    l_index = 0
    m_index = 0
    r_index = 0
    
    for x in range (792):

        if l_index > 7:
            l_index = 0

        if m_index > 10:
            m_index = 0

        if r_index > 8:
            r_index = 0

        mul = (l[l_index]) * (m[m_index]) *(r[r_index])
        total_t += mul
        l_index += 1
        m_index += 1
        r_index += 1
    return total_t
    



answer = get_s(left,middle,right) / get_t(left,middle,right)

print(f"{answer:.4g}")