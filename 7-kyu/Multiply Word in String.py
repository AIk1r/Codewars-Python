def modify_multiply(st, loc, num):
    s = [i for i in st.split()]
    return(((s[loc]+'-')*num).rstrip('-'))
