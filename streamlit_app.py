import streamlit as st
import numpy as np

def extract(num):
    return [num // 1000, (num % 1000) // 100, (num % 100) // 10, num % 10]

def checkforRepeat(l):
    return l[0] == l[1] == l[2] == l[3]

def order(l):
    return [sorted(l, reverse=True), sorted(l)]

def dalist(olist):
    dnum = int("".join(map(str, olist[0])))
    anum = int("".join(map(str, olist[1])))
    return [dnum, anum]

def minus(danum):
    return danum[0] - danum[1]

def kaprekar_process(num):
    steps = []
    while num != 6174:
        l = extract(num)
        if checkforRepeat(l):
            steps.append(f"{num}: All digits are the same. Restart needed!")
            break
        
        olist = order(l)
        danum = dalist(olist)
        num = minus(danum)
        steps.append(f"Descending: {danum[0]}, Ascending: {danum[1]}, Subtract: {num}")
        
        if num == 6174:
            steps.append("Kaprekar's constant 6174 reached!")
            break
    return steps

def main():
    st.title("Kaprekar's Constant Finder")
    
    num = st.number_input("Enter a 4-digit number (or leave empty for random)", min_value=100, max_value=9999, step=1, format="%d")
    generate = st.button("Generate")
    
    if generate:
        if num == 0:
            num = np.random.randint(1000, 10000)
            st.write(f"Randomly chosen number: {num}")
        
        steps = kaprekar_process(num)
        
        for step in steps:
            st.write(step)

if __name__ == "__main__":
    main()
