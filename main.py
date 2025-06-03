import numpy as np
import matplotlib.pyplot as plt

# === Paramètres ===
n_simulations = 1000       # Nombre de mises par essai
n_trials = 10000           # Nombre de simulations indépendantes
initial_bankroll = 100     # Capital de départ (€)
initial_bet = 1            # Mise initiale (€)
max_bet = 512              # Limite de mise maximale (€)
win_prob = 18 / 37         # Probabilité de gagner (roulette européenne)

# === Simulation Martingale pour une seule partie ===
def simulate_martingale():
    bankroll = initial_bankroll
    bet = initial_bet
    bankroll_history = [bankroll]
    for _ in range(n_simulations):
        if bankroll < bet or bet > max_bet:
            # Ruine ou dépassement limite
            bankroll_history.append(0)
            break
        outcome = np.random.rand() < win_prob
        if outcome:
            bankroll += bet
            bet = initial_bet
        else:
            bankroll -= bet
            bet *= 2
        bankroll_history.append(bankroll)
    else:
        # Si pas de ruine, garder la dernière valeur
        bankroll_history.append(bankroll)
    return bankroll_history

# === Lancer toutes les simulations et stocker résultats ===
all_histories = []
final_bankrolls = []
ruin_count = 0

for _ in range(n_trials):
    history = simulate_martingale()
    all_histories.append(history)
    final_capital = history[-1]
    final_bankrolls.append(final_capital)
    if final_capital == 0:
        ruin_count += 1

final_bankrolls = np.array(final_bankrolls)

# === Statistiques ===
mean_final = np.mean(final_bankrolls)
std_final = np.std(final_bankrolls)
ruin_probability = ruin_count / n_trials

print(f"Espérance (capital final moyen) : {mean_final:.2f} €")
print(f"Écart-type : {std_final:.2f} €")
print(f"Probabilité de ruine : {ruin_probability * 100:.2f} %")

# === Graphique 1 : Trajectoires Monte Carlo (20 premières) ===
plt.figure(figsize=(12, 6))
for history in all_histories[:20]:
    plt.plot(history, alpha=0.4)
plt.title("Trajectoires du capital (20 simulations) – Stratégie Martingale")
plt.xlabel("Nombre de mises")
plt.ylabel("Capital (€)")
plt.grid(True)
plt.axhline(initial_bankroll, color='black', linestyle='--', label='Capital initial')
plt.legend()
plt.tight_layout()
plt.savefig("martingale_monte_carlo_trajectories.png")

# === Graphique 2 : Histogramme capital final ===
plt.figure(figsize=(10, 6))
plt.hist(final_bankrolls, bins=50, color='skyblue', edgecolor='black')
plt.title("Distribution du capital final après 10 000 simulations")
plt.xlabel("Capital final (€)")
plt.ylabel("Nombre de simulations")
plt.grid(True)
plt.tight_layout()
plt.savefig("martingale_final_capital_histogram.png")
