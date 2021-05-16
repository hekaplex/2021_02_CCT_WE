def calculateFutureValue(monthlyInvestment, monthlyRate, months):
# iterator for length of calculation cycle
    futureValue = 0.0
    for i in range(months):
#business logic
        futureValue = (
                futureValue
                + monthlyInvestment
            ) \
            * \
            ( \
                1 
                + monthlyRate/100
            )
#output of function
    return str(round(futureValue,2))