LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'
guessed = ['L', 'b', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
prizeMoney = 260

print([l for l in LETTERS if l not in guessed and (l not in VOWELS or prizeMoney >= 250)])