import deck_of_cards as deck
import card_player as player
import blackjack as bj
import account


def main():
    username = input("Username: ")
    user = account.Account(username)
    bj.game_loop()


if __name__ == '__main__':
    main()