def getHint( secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    secret_dict = {}
    guess_dict = {}

    A = 0
    B = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
           A += 1
        else:
            if secret[i] in secret_dict:
                secret_dict[secret[i]] = secret_dict[secret[i]] + 1
            else:
                secret_dict[secret[i]]=1
            if guess[i] in guess_dict:
                guess_dict[guess[i]] = guess_dict[guess[i]] + 1
            else:
                guess_dict[guess[i]]=1
    for digit in secret_dict:
        if digit in guess_dict:
            B += min(secret_dict[digit], guess_dict[digit])
    return str(A)+"A"+str(B)+"B"