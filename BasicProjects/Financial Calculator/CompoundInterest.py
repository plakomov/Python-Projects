# Compound Interest Module
import math


class CompoundInterest:
    @staticmethod
    def nominal_rate(principal, time, amount, n_intervals=1):
        """Calculates nominal rate"""
        return (math.pow(amount / principal, 1 / (time * n_intervals)) - 1) * n_intervals

    @staticmethod
    def effective_interest_rate(principal, time, amount, n_intervals=1):
        """Calculates effective interest rate per interest period"""
        return math.pow(amount / principal, 1 / (time * n_intervals)) - 1

    @staticmethod
    def time(principal, rate, amount, n_intervals=1):
        """Calculates time per 1 unit of time"""
        a_1 = math.log(amount / principal)
        a_2 = math.log(1 + rate / n_intervals)
        return (a_1 / a_2) / n_intervals

    @staticmethod
    def time_n_intervals(principal, rate, amount, n_intervals=1):
        """Calculates number of interest periods"""
        a_1 = math.log(amount / principal)
        a_2 = math.log(1 + rate / n_intervals)
        return a_1 / a_2

    @staticmethod
    def principal(rate, time, amount, n_intervals=1):
        """Calculates principal"""
        return amount / math.pow(1 + rate/n_intervals, time * n_intervals)

    @staticmethod
    def amount(principal, rate, time, n_intervals=1):
        """Calculate amount"""
        return principal * math.pow(1 + (rate/n_intervals), time*n_intervals)

    @staticmethod
    def effective_interval_rate(principal, rate, t1, t2, n_intervals=1):
        """Calculates the effective interest rate over a period"""
        a_1 = CompoundInterest.amount(principal, rate, t1, n_intervals)
        a_2 = CompoundInterest.amount(principal, rate, t2, n_intervals)
        if t1 > t2:
            return (a_1 - a_2) / a_2
        else:
            return (a_2 - a_1) / a_1

    @staticmethod
    def discount(rate, time, n_intervals=1):
        """Returns the discount value over the period"""
        return 1 / CompoundInterest.amount(1, rate, time, n_intervals)

    @staticmethod
    def discount_amount(amount, rate, time, n_intervals=1):
        """ Returns the discounted amount over a period of time"""
        return amount * CompoundInterest.discount(rate, time, n_intervals)

    @staticmethod
    def nominal_discount_rate(rate, n_intervals=1):
        """ Returns nominal discount rate equivalent to effective interest rate"""
        return rate/(1+(rate/n_intervals))

    @staticmethod
    def effective_discount_rate(rate, n_intervals=1):
        """ Returns effective discount rate equivalent to effective interest rate"""
        i_m = rate/n_intervals
        return i_m/(1+i_m)

    @staticmethod
    def nom_discount_to_nom_interest(disc, n_intervals=1):
        """ Returns nominal interest rate equivalent to nominal discount rate"""
        return disc/(1-(disc/n_intervals))

    @staticmethod
    def nom_discount_to_nom_interest(disc, n_intervals=1):
        """ Returns nominal interest rate equivalent to nominal discount rate"""
        d_m = disc/n_intervals
        return d_m/(1-d_m)

    @staticmethod
    def force_of_interest(eff_rate):
        """Returns the force of interest based on the effective interest rate per 1 unit of time"""
        return math.log(1+eff_rate)

    @staticmethod
    def real_interest_rate(eff_rate, inf_rate):
        """Returns the real interest rate (inflation adjusted rate)
        based on the effective rate and inflation rate per 1 unit of time"""
        return (eff_rate-inf_rate)/(1+inf_rate)


# Still need to a couple of things related to the net-present values