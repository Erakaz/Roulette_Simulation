import random
import matplotlib.pyplot as plt

def simulate_martingale_markov(initial_capital=1000, initial_bet=1, max_losses=10, max_steps=1000):
    capital = initial_capital
    losses = 0  # nombre de pertes consécutives
    capital_history = [capital]

    for step in range(max_steps):
        bet = initial_bet * (2 ** losses)

        # Si la mise dépasse le capital, on arrête (ruine)
        if bet > capital:
            print(f"Ruine à l'étape {step} (mise {bet} > capital {capital})")
            break

        # Simulation du résultat de la roulette européenne (18/37 chance de gagner)
        win = random.random() < 18/37

        if win:
            capital += bet
            losses = 0  # reset pertes consécutives
        else:
            capital -= bet
            losses += 1
            if losses > max_losses:
                # Pour limiter la taille des pertes consécutives (stratégie pratique)
                losses = max_losses

        capital_history.append(capital)

    return capital_history

# Simulation
history = simulate_martingale_markov()

# Affichage du capital au fil du temps
plt.plot(history)
plt.title("Simulation Martingale - Chaîne de Markov augmentée")
plt.xlabel("Nombre de mises")
plt.ylabel("Capital")
plt.grid(True)
plt.savefig("markov_martingale_plot.png")
