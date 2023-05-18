""" Задача про банкомат с логированием ошибок """
import logging
import argparse

parser = argparse.ArgumentParser(description='ATM seanse with client')
parser.add_argument('taxes', metavar='take_off_tax every_third_operation_tax wealth_tax min_take_off_tax max_take_off_tax', type=float, nargs=5, help='enter a b c separated by a space')
args = parser.parse_args()

logging.basicConfig(filename="ATMLog.log", encoding="utf-8", level=logging.INFO)
logger = logging.getLogger('__main__')

#TAKE_OFF_TAX = 0.015
#EVERY_THIRD_OPERATION_TAX = 0.03
#WEALTH_TAX = 0.1
#MIN_TAKE_OFF_TAX = 30
#MAX_TAKE_OFF_TAX = 600

TAKE_OFF_TAX, EVERY_THIRD_OPERATION_TAX, WEALTH_TAX, MIN_TAKE_OFF_TAX, MAX_TAKE_OFF_TAX = args.taxes
WEALTH = 5_000_000
START = 0
MULTIPLICITY = 50

sum_ = START
operation_count = 0

while True:
    
    choice = int(input('Choose an action: '
                       '\n1 - Put money'
                       '\n2 - Take off money'
                       '\n3 - Exit\n'))
    match choice:

        case 1:
            if sum_ > WEALTH:
                sum_ -= (sum_ - WEALTH) * WEALTH_TAX
                logger.info('Client want to put money and the wealth tax was substracted')
                print(f'Since you have more than {WEALTH} on your account, we take off wealth tax {WEALTH_TAX}')
            while True:
                number = int(input('Enter sum you want to PUT: '))
                if number % 50 == 0 and number > 0:
                    sum_ += number
                    print(f'Operation completed successfully, you have {sum_} on your account')
                    logger.info(f'Operation completed successfully, client put on {number} and now have {sum_} on his account')
                    operation_count += 1
                    if operation_count % 3 == 0:
                        sum_ += number * EVERY_THIRD_OPERATION_TAX
                        print(f'And since it was the third operation, we add you {EVERY_THIRD_OPERATION_TAX} and now there is {sum_} on your account')
                        logger.info(f'Since it was the third operation, {EVERY_THIRD_OPERATION_TAX} was added and now there is {sum_} on clients account')
                    break
                else:
                    print(f'Enter a summ multiples in {MULTIPLICITY} and not null')
                    logger.error(f'sum not multiples in {MULTIPLICITY} or null was entered')

        case 2:
            if sum_ == 0:
                print('You have no money at all')
                logger.info('Client have 0 on his account')

            elif sum_ > 0:
                if sum_ > WEALTH:
                    sum_ -= (sum_ - WEALTH) * WEALTH_TAX
                    logger.info('Client want to put money and the wealth tax was substracted')
                    print(f'Since you have more than {WEALTH} on your account, we take off wealth tax {WEALTH_TAX}')

            while True:
                number = int(input('Enter sum you want to TAKE OFF: '))

                if number <= 0 or number % MULTIPLICITY != 0:
                    logger.error(f'sum not multiples in {MULTIPLICITY} or null was entered')
                    print(f'Enter a summ multiples in {MULTIPLICITY} and not null')    
                else:
                    if number < MIN_TAKE_OFF_TAX / TAKE_OFF_TAX:
                        tax_sum = MIN_TAKE_OFF_TAX
                    elif number > MAX_TAKE_OFF_TAX / TAKE_OFF_TAX:
                        tax_sum = MAX_TAKE_OFF_TAX
                    else:
                        tax_sum = number * TAKE_OFF_TAX

                    if sum_< number + tax_sum:
                        logger.error(f'account sum not enough to take off {number}')
                        print(f'You have not enough money on your account for this operation')                 
                    else:
                        sum_ -= number + tax_sum
                        logger.info(f'Operation completed successfully. Client take off {number}, tax summ was {tax_sum} and summ on his account now is {sum_}')
                        print(f'Operation completed successfully. Summ on your account now is {sum_}')
                        operation_count += 1
                        if operation_count % 3 == 0:
                            sum_ += number * EVERY_THIRD_OPERATION_TAX
                            logger.info(f'Since it was the third operation, {EVERY_THIRD_OPERATION_TAX} was added and now there is {sum_} on clients account')
                            print(f'And since it was the third operation, we add you {EVERY_THIRD_OPERATION_TAX} and now there is {sum_} on your account')
                        break
                
        case 3:
            logger.info('Client exit the session')
            break

        case _:
            logger.warning('Error of user choice.')
            print('Your choice is not in list')

  