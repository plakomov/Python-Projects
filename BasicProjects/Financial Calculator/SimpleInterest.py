# This is the simple interest object; the object is going to be static


class SimpleInterest:
    @staticmethod
    def rate(principal, time, amount):
        """Calculates rate"""
        return ((amount / principal) - 1) / time

    @staticmethod
    def time(principal, rate, amount):
        """Calculates time"""
        return ((amount / principal) - 1) / rate

    @staticmethod
    def principal(rate, time, amount):
        """Calculates principal"""
        return amount / (1 + rate * time)

    @staticmethod
    def amount(principal, rate, time):
        """Calculate amount"""
        return principal*(1 + rate*time)

    @staticmethod
    def effective_interval_rate(principal, rate, t1, t2):
        """Calculates the effective interest rate over a period"""
        a_1 = SimpleInterest.amount(principal, rate, t1)
        a_2 = SimpleInterest.amount(principal, rate, t2)
        if t1 > t2:
            return (a_1 - a_2)/a_2
        else:
            return (a_2 - a_1)/a_1

    @staticmethod
    def discount(rate, time):
        """Returns the discount value over the period"""
        return 1/(1 + rate * time)