sentencelist = list(input().strip().split())

vowels = 'aeiouAEIOU'
vowel_count = []

for i in sentencelist:
    count = 0
    for j in i:
        if j in vowels:
            count += 1
    vowel_count.append(f'[{i},{count}]')

print(vowel_count)
