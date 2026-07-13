#!/usr/bin/python3
"""Prime Game module."""


def isWinner(x, nums):
    """Return the player who wins the most Prime Game rounds."""
    # Vérifie qu'il existe au moins une manche valide
    if x <= 0 or not nums:
        return None

    # Ne conserve que les valeurs correspondant aux x manches
    rounds = nums[:x]

    if not rounds:
        return None

    # Récupère la plus grande valeur afin de créer un seul crible
    max_number = max(rounds)

    # Si toutes les valeurs sont inférieures à 2,
    # Maria ne peut jamais jouer et Ben gagne toutes les manches
    if max_number < 2:
        return "Ben"

    # Au départ, on considère tous les nombres comme premiers
    is_prime = [True] * (max_number + 1)

    # 0 et 1 ne sont pas des nombres premiers
    is_prime[0] = False
    is_prime[1] = False

    # Crible d'Ératosthène
    number = 2
    while number * number <= max_number:
        if is_prime[number]:
            # Les multiples précédents ont déjà été traités,
            # on commence donc à number * number
            multiple = number * number

            while multiple <= max_number:
                is_prime[multiple] = False
                multiple += number

        number += 1

    # Stocke le nombre de nombres premiers trouvés jusqu'à chaque valeur
    prime_counts = [0] * (max_number + 1)
    count = 0

    for number in range(max_number + 1):
        if is_prime[number]:
            count += 1

        prime_counts[number] = count

    # Compteurs des manches gagnées par chaque joueur
    maria_score = 0
    ben_score = 0

    # Détermine le gagnant de chaque manche grâce à la parité
    for number in rounds:
        if prime_counts[number] % 2 == 1:
            maria_score += 1
        else:
            ben_score += 1

    # Retourne le joueur ayant gagné le plus de manches
    if maria_score > ben_score:
        return "Maria"

    if ben_score > maria_score:
        return "Ben"

    return None
