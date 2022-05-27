import lottery

target = lottery.generate_lottery()

count = 0
while True:
    count += 1
    if lottery.generate_lottery() == target:
        break
print(count)
