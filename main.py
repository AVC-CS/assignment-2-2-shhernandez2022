def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celsius = int(input('Enter your temperature in Celsius: '))
    fahrenheit = 9/5 * celsius + 32
    
    print (f'The converted temperature is {fahrenheit:.2f}')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
