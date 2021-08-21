# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
no_Eng_std=input()
roll_no_eng=set(map(int,input().split()))
no_Frn_std=input()
roll_no_Frn=set(map(int,input().split()))

eng_set=set(roll_no_eng)
atleast_one=eng_set.symmetric_difference(roll_no_Frn)
num=len(atleast_one)
print(num)
