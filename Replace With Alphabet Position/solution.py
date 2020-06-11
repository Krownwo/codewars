def alphabet_position(text):
    text = text.upper().split()
    ans = ""

    for word in text:
        for letter in word:
            if ord(letter) >= 65 and ord(letter) <= 90:
                ans += str(ord(letter)-64) + " "
    
    return ans[:-1]