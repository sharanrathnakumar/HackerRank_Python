'''Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of K members per group where K ≠ 1.

The Captain was given a separate room, and the rest were given one room per group.
Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear
K times per group except for the Captain's room.
Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of K and the room number list.'''


grp_mbrs_no = int(input())
room_no = map(int, input().split())
room_no = sorted(room_no)

for i in range(len(room_no)):
    if(i != len(room_no)-1):
        if(room_no[i]!=room_no[i-1] and room_no[i]!=room_no[i+1]):
            print(room_no[i])
            break;
    else:
        print(room_no[i])
        
        
'''
Not Working for Test Case 0 to Test case 5

# Enter your code here. Read input from STDIN. Print output to STDOUT
grp_mbrs_no = int(input())
room_nos = set(map(int, input().split()))
room_list = list(room_nos)
for no in room_list:
    f = 0
    for no2 in room_list:
        if no == no2:
            f += 1
            if f>=grp_mbrs_no:
                room_list.remove(no)
print(no)

'''
