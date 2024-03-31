import matplotlib.pyplot as plt
import numpy as np
import math
import subprocess, os, re
import pandas as pd


def success_probability(q, z):
    """
    Calculate the expected success probability of a DS attack
    :param q: probability the attacker finds the next block
    :param z: number of blocks linked after the transaction
    :return:
    """
    p = 1 - q
    lam = z*(q/p)
    sum = 1.0
    for k in range(0, z+1):
        poisson = math.exp(-lam)
        for i in range(1, k+1):
            poisson *= lam/i
        sum -= poisson * (1 - math.pow(q/p, z-k))
    return sum

def fix_z_vary_q():
    x = np.arange(0, 0.51, 0.01)
    for z in range(1, 7):
        y = [success_probability(q, z) for q in x]
        plt.plot(x, y, label="$z$ = {}".format(z))
    plt.xlabel("$q$ = hashing power of Attacker")
    plt.ylabel("Probability of successful attack")
    plt.title("Double-Spend Success Probability vs. Attacker Hashing Power")
    plt.legend(loc="upper left")
    plt.savefig("figures/double_spend_success_prob.png", dpi=300)


def get_sim_results(q, z, blocks=100, iterations=10):
    cmd_string = "bash run_double_spend.sh {} {} {} {}".format(iterations, q, z, blocks)
    num_success = 0.0
    num_runs = 0
    for i in range(0, iterations):
        result = subprocess.run(cmd_string, capture_output=True, shell=True)
        flag = re.search(r'There were ([0-9]+) successful double-spending attacks', result.stdout.decode('utf-8'))
        if flag is not None:
            num_success += 1 if flag.group(1) != "0" else 0
            num_runs += 1
        else:
            print(f"command crashed: {cmd_string}")
            print(result.stderr)

    return num_success/num_runs # iterations TODO fix later
def simulate_double_spend():
    colours = ['b', 'c', 'g', 'r', 'y']
    x_prob = np.arange(0, 0.51, 0.01)
    x_sim = [0.001, 0.1, 0.2, 0.3, 0.4, 0.5]
    for colour, z in zip(colours, range(2, 7)): # z=1 causes a crash at iterations=10, q=0.05, z=1, noBlocks=100
        y_prob = [success_probability(q, z) for q in x_prob]
        y_sim = [get_sim_results(q, z, iterations=20) for q in x_sim]
        plt.plot(x_prob, y_prob, f'{colour}', label="$z$ = {}".format(z))
        plt.plot(x_sim, y_sim, f'+{colour}', label="_$z$ = {}".format(z))
        print(z, y_sim)

    plt.xlabel("$q$ = hashing power of Attacker")
    plt.ylabel("Probability of successful attack")
    plt.title("Double-Spend Success Probability vs. Attacker Hashing Power")
    plt.legend(loc="upper left")
    plt.savefig("figures/double_spend_success_sim.png", dpi=300)

def draw_only(*iters):
    dfs = [pd.read_csv(i, index_col="z") for i in iters]
    df0 = dfs[0]
    df1 = dfs[1]
    a = float(2/6)
    b = float(4/6)
    df0['q0'] = df0['q0']*a + df1['q0']*b
    df0['q1'] = df0['q1']*a + df1['q1']*b
    df0['q2'] = df0['q2']*a + df1['q2']*b
    df0['q3'] = df0['q3']*a + df1['q3']*b
    df0['q4'] = df0['q4']*a + df1['q4']*b
    df0['q5'] = df0['q5']*a + df1['q5']*b

    def get_csv_results(q, z):
        return df0.iloc[z-2][f"q{q}"]

    colours = ['b', 'c', 'g', 'r', 'y']
    x_prob = np.arange(0, 0.51, 0.01)
    x_names = [0, 1, 2, 3, 4, 5]
    x_sim = [0.001, 0.1, 0.2, 0.3, 0.4, 0.5]
    for colour, z in zip(colours, range(2, 7)): # z=1 causes a crash at iterations=10, q=0.05, z=1, noBlocks=100
        y_prob = [success_probability(q, z) for q in x_prob]
        y_sim = [get_csv_results(q, z) for q in x_names]
        # plt.plot(x_prob, y_prob, f'{colour}', label="$z$ = {}".format(z))
        plt.plot(x_sim, y_sim, f'+{colour}', label="$z$ = {}".format(z))
        plt.plot(x_sim, y_sim, f'--{colour}', label="_$z$ = {}".format(z))
        print(z, y_sim)

    plt.xlabel("$q$ = hashing power of Attacker")
    plt.ylabel("Probability of successful attack")
    plt.title("Double-Spend Success Probability vs. Attacker Hashing Power")
    plt.legend(loc="upper left")
    plt.savefig("figures/double_spend_success_sim_csv.png", dpi=300)


# simulate_double_spend()
draw_only('run_ten_iter.txt', 'run_20_iter.txt')