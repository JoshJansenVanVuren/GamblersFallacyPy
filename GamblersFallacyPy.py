import random
import sys

num_trails = 100000000
gambler_memory = [0,1,0,1,0,1,0,1,0,1]
num_heads = 0
num_tails = 0
heads_to_tails_ratio = 0
num_correct = 0
num_incorrect = 0
progress_counter = 1

print("Simluating " + str(num_trails) + " trails.")

for i in range(1,num_trails + 1):
    # show progress bar (adapted from: https://stackoverflow.com/a/3002100/10109587)
    if (((i)*100)/(num_trails) % 5 == 0):
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%" % ('='*progress_counter, 5*progress_counter))
        sys.stdout.flush()
        progress_counter += 1

    # toss a coin (0: tails , 1:heads)
    result = random.randint(0,1)

    # gambler makes the ill informed guess based off past n events
    # (+ a tiny bit of noise for good measure)
    guess_heads = random.gauss(0,0.001)
    for i in gambler_memory:
        if i == 1:
            guess_heads += 1
    
    # vote on the least seen item in the past few draws
    if guess_heads/len(gambler_memory) > 0.5:
        guess = 0
    else:
        guess = 1

    if guess == result:
        num_correct += 1
    else:
        num_incorrect += 1

    if result == 1:
        num_heads += 1
    else:
        num_tails += 1

    # update gambler memory
    gambler_memory[:-1] = gambler_memory[1:]
    gambler_memory[len(gambler_memory) - 1]
    gambler_memory[-1] = guess
    #print(gambler_memory)

# track the head to tail ratio
if num_heads > 0 and num_tails > 0:
    print("\nHead and tail Percentages: " + 
            str(round(num_heads*100.0/(num_heads + num_tails),2)) + ":" + 
            str(round(num_tails*100.0/(num_tails + num_heads),2)))
    
# track the correct percentage
print("Gambler Correct Percentage: " + \
            str(round(num_correct*100.0/(num_correct + num_incorrect),2)))
