# coding=utf-8
FA = 1

print(f"il Numero iniziale di Fibonacci è FA {FA}") 
print(f"il Numero successivo di Fibonacci è FA {FA}") 

FB = 1
FC = 1

while (FA < 100) or (FB < 100) or (FC < 100):
        FA = FB + FC
        print(f"il Numero successivo è FA {FA}")
        FC = FA + FB
        print(f"il Numero successivo è FC {FC}")
        FB = FC + FA
        print(f"il Numero successivo è FB {FB}")
