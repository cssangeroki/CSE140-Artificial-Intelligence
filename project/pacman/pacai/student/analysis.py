"""
Analysis question.
Change these default values to obtain the specified policies through value iteration.
If any question is not possible, return just the constant NOT_POSSIBLE:
```
return NOT_POSSIBLE
```
"""

NOT_POSSIBLE = None

def question2():
    """
    I removed the noise so that the agent is able to CERTAINLY
    get the best value (+10) without any risks.
    """

    answerDiscount = 0.9
    answerNoise = 0

    return answerDiscount, answerNoise

def question3a():
    """
    [Enter a description of what you did here.]
    """

    answerDiscount = 0.3
    answerNoise = 0.0
    answerLivingReward = -6

    return answerDiscount, answerNoise, answerLivingReward

def question3b():
    """
    [Enter a description of what you did here.]
    """

    answerDiscount = 0.1
    answerNoise = 0.1
    answerLivingReward = -2

    return answerDiscount, answerNoise, answerLivingReward

def question3c():
    """
    [Enter a description of what you did here.]
    """

    answerDiscount = 0.9
    answerNoise = 0.0
    answerLivingReward = 0.0

    return answerDiscount, answerNoise, answerLivingReward

def question3d():
    """
    [Enter a description of what you did here.]
    """

    answerDiscount = 0.9
    answerNoise = 0.5
    answerLivingReward = 0.0

    return answerDiscount, answerNoise, answerLivingReward

def question3e():
    """
    [Enter a description of what you did here.]
    """

    answerDiscount = 0.9
    answerNoise = 0.5
    answerLivingReward = 0.0

    return answerDiscount, answerNoise, answerLivingReward

def question6():
    """
    [Enter a description of what you did here.]
    """

    # answerEpsilon = 0.3
    # answerLearningRate = 0.5

    return NOT_POSSIBLE

if __name__ == '__main__':
    questions = [
        question2,
        question3a,
        question3b,
        question3c,
        question3d,
        question3e,
        question6,
    ]

    print('Answers to analysis questions:')
    for question in questions:
        response = question()
        print('    Question %-10s:\t%s' % (question.__name__, str(response)))
