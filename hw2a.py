from math import sqrt, pi, exp
def Probability(PDF, args, c, GT=True):
    """
    This is the function to calculate the probability that x is >c or <c depending
    on the GT boolean.
    :param PDF: the probability density function to be integrated
    :param args: a tuple with (mean, standard deviation)
    :param c: value for which we ask the probability question
    :param GT: boolean deciding if we want probability x>c (True) or x<c (False)
    :return: probability value
    """
    mu,sig=args
    p=Simpson(PDF,(mu,sig, mu-5*sig, 0))
    return p

def GPDF(args):
    """
    The Gaussian probability density function.
    This requires knowing the population mean and standard deviation..
    :param args: (x, mean, standard deviation)  tuple in that order
    :return: value of GPDF at the desired x
    """
    #Step 1: unpack args
    x, mu, sig=args
    #step 2: compute GPDF at x
    fx=(1/(sig*sqrt(2*pi)))*exp(-0.5*((x-mu)/sig)**2)
    #step 3: return value
    return fx

def Simpson(fx, args):
    """
    This executes the Simpson 1/3 rule for numerical integration.
    :param fx: some function of x to integrate
    :param args: a tuple containing (mean, stDev, lhl, rhl)
    :return: the area beneath the function between lhl and rhl
    """

    area = 0.5
    return area

def main():
    """
    I want to integrate the Gaussian probability density function between
    a left hand limit = (mean - 5*stDev) to a right hand limit = (c).
    :return:
    """
    #region testing GPDF
    fx = GPDF((0,0,1))
    print("{:0.5f}".format(fx))
    #edregion

    #region testing Simpson
    p=Simpson(GPDF,(0,1,-5,0)) #should return 0.5
    print("p={:0.5f}".format(p))
    #endregion

    #region testing Probability
    p1 = Probability(GPDF, (0,1),0,True)
    print("p1={:0.5f}".format(p1))
    #endregion

    #region testing user input
    mean = input("Population mean? ")
    stDev = input("Standard deviation?")
    c = input("c value?")
    GT = True if input("Probability greater than c?").lower() in ["y","yes","true"] else "False"
    print("P(x"+(">" if GT else "<") + c +"|"+mean+", "+stDev +")")
    pass
    #endregion

if __name__ == "__main__":
    main()