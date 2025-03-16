s = input().strip()
n = len(s)
max_len = 0
max_pals = []

for i in range(n):
    # Check for odd length palindromes
    l, r = i, i
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    substr = s[l+1:r]
    current_length = len(substr)
    if current_length > max_len:
        max_len = current_length
        max_pals = [substr]
    elif current_length == max_len:
        max_pals.append(substr)
    
    # Check for even length palindromes
    l, r = i, i + 1
    if r >= n:
        continue
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    substr = s[l+1:r]
    current_length = len(substr)
    if current_length > max_len:
        max_len = current_length
        max_pals = [substr]
    elif current_length == max_len:
        max_pals.append(substr)

print(max(max_pals))