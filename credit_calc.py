import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()
if not args.type:
    print("Incorrect parameters")
count = len(sys.argv)

if args.principal:
    credit_principal = float(args.principal)
else:
    credit_principal = -1

if args.periods:
    count_of_months = float(args.periods)
else:
    count_of_months = -1

if args.interest:
    credit_interest = float(args.interest)
else:
    credit_interest = -1

if args.payment:
    monthly_payment = float(args.payment)
else:
    monthly_payment = -1

if args.type == "annuity":
    if count < 4:
        print("Incorrect parameters")
    else:
        if not args.payment:
            if credit_interest >= 0 and credit_principal >= 0 and count_of_months >=0:
                i = credit_interest / (12 * 100)
                A = credit_principal * ((i * math.pow((1 + i), count_of_months))/(math.pow((1 + i), count_of_months) - 1))
                A = math.ceil(A)
                total = A * count_of_months
                print(f"Your annuity payment = {A}!")
                overpayment = int(total - credit_principal)
                print(f"Overpayment = {overpayment}")
            else:
                print("Incorrect parameters")
        if not args.periods:
            if credit_interest >= 0 and monthly_payment >= 0 and credit_principal >= 0:
                i = credit_interest / (12 * 100)
                z = monthly_payment / (monthly_payment - i * credit_principal)
                n = math.ceil(math.log(z, 1+i))
                months = n % 12
                years = round((n - months) / 12)
                total = monthly_payment * n
                if months > 0:
                    print(f"You need {years} years and {months} months to repay this credit!")
                else:
                    print(f"You need {years} years to repay this credit!")
                overpayment = total - credit_principal
                print(f"Overpayment = {overpayment}")
            else:
                print("Incorrect parameters")

        if not args.principal:

            if credit_interest >= 0 and monthly_payment >= 0 and count_of_months >= 0:
                i = credit_interest / (12 * 100)
                P = monthly_payment / (i * math.pow((1 + i), count_of_months) / (math.pow((1 + i), count_of_months) - 1))
                P = int(P)
                total = monthly_payment * count_of_months
                print(f"Your credit principal = {P}!")
                overpayment = total - P
                print(f"Overpayment = {overpayment}")
            else:
                print("Incorrect parameters")


if args.type == "diff":
    if args.payment or count < 4:
        print("Incorrect parameters")
    else:
        P = credit_principal
        n = count_of_months
        i = credit_interest
        i = i / (12 * 100)
        total = 0
        for j in range(1, int(n) + 1):
            m = j
            Dm = (P/n) + (i *(P - ((P*(m-1))/n)))
            Dm = math.ceil(Dm)
            total = total + Dm
            print(f"Month {j}: paid out {Dm}")
        Overpayment = int(total - P)
        print(f"\nOverpayment = {Overpayment}")
