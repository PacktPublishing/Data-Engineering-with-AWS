from random import randint 
 
def lambda_handler(event, context):
    print('Processing')
    #Our ETL code would go here
    value = randint(0, 2)
    # We now divide 10 by our random number.
    # If the random numebr is 0, our function will fail
    newval = 10 / value
    print(f'New Value is: {newval}')
    return(newval)
