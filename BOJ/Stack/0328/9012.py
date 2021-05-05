for _ in range(int(input())):
    st = input()

    st1 = st.replace("()","")

    if st1.count("(") == st1.count(")") and  st1 == "()" : print("YES")
    else: print("NO")