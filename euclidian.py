num_one = int(input('Enter First Number: '))
num_two = int(input('Enter Second Number: '))
step = 0

num_three = num_one % num_two

# print('\nStep:', step)
# print('R{}: {}'.format(step, num_one))
# print('R{}: {}'.format(step + 1, num_two))
# print('R{}: {}'.format(step + 2, num_three))
#
# print('\n')
# step += 1

while(num_one % num_two != 0):
    print('Step:', step)
    print('R{}: {}'.format(step, num_one))
    num_three = num_one % num_two
    num_one = num_two
    print('R{}: {}'.format(step + 1, num_two))
    print('R{}: {}'.format(step + 2, num_three))
    print('\n')

    num_two = num_three

    step += 1


print('The GCD is:', num_two)
