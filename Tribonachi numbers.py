n_t = 1
m_t = 1
o_t = 1
a = int(input())
while a > 0:
    print(n_t)
    new_t = n_t + m_t + o_t
    n_t = m_t
    m_t = o_t
    o_t = new_t
    a -= 1


#old_f = 1
#cur_f = 1
#limit = int(input())
#while old_f <= limit:
    #print(old_f)
    #new_f = old_f + cur_f
    #old_f = cur_f
    #cur_f = new_f