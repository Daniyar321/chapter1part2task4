first_hours = int(input())
first_minutes = int(input())
first_seconds = int(input())
second_hours = int(input())
second_minutes = int(input())
second_seconds = int(input())
result1 = ((first_hours*60)*60)+(first_minutes*60)+first_seconds
result2 = ((second_hours*60)*60)+(second_minutes*60)+second_seconds
if result1 > result2:
    print(result1 - result2)
else:
    print(result2 - result1)