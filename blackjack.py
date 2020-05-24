import deck_of_cards
import card_player
import collections

PlayerReport = collections.namedtuple('PlayerReport', 'win, tie, loss')


def game_loop():
    players = create_players()
    deck = create_deck()
    deck.shuffle()
    deal(players, deck)

    for p in players[1:]:
        p.assign_score(player_hand_loop(p, deck))
    if len(players) > 0:
        players[0].score = dealer_hand_loop(players[0], deck)
    else:
        players[0].show_hand()

    report = compare_scores_against_dealer(players[1:], players[0])
    ui_results(report)


def create_players(count=1):
    players = []
    dealer = card_player.Player('Dealer')
    players.append(dealer)
    for i in range(0, count):
        name = input("Enter player name:   ")
        new_player = card_player.Player(str(name))
        players.append(new_player)
    return players


def create_deck():
    bj_deck = deck_of_cards.Deck()
    return bj_deck


def deal(players, deck):
    for p in players:
        p.draw(deck)
        p.draw(deck)
        hand_ui(players[players.index(p)])


def hand_ui(player, reveal=False):
    if player.name != 'Dealer':
        print("{}'s hand:".format(player.name))
        for card in player.hand:
            print(card.name)
    else:
        print("Dealer`s hand:")
        for card in player.hand:
            print(card.name) if reveal or player.hand.index(card) == 0 else print("face down card")
    print()


def sum_player_hand(player):
    sum_of_hand = 0
    for c in player.hand:
        sum_of_hand += c.num_val
    for c in player.hand:
        if c.num_val == 1 and sum_of_hand <= 11:
            sum_of_hand += 10
    return sum_of_hand


def player_hand_loop(player, deck):
    choice = None
    hand_score = sum_player_hand(player)

    while choice != 's' and hand_score <= 21:
        choice = input("You are at {}. (H)it or (S)tand?   ".format(hand_score))
        if choice == 'h':
            player.draw(deck)
            print("You drew: {}".format(player.hand[-1].name))
            hand_score = sum_player_hand(player)

    if hand_score > 21:
        print("{} busted at {}!".format(player.name, sum_player_hand(player)))
        print()
        return 0
    else:
        print("{} stands at {}.".format(player.name, hand_score))
        print()
        return hand_score


def dealer_hand_loop(dealer, deck):
    dealer_sum = sum_player_hand(dealer)
    print("The dealer flips his second card over.")
    print()
    dealer.show_hand()
    print()

    while dealer_sum < 17:
        dealer.draw(deck)
        print("The dealer draws: {}".format(dealer.hand[-1].name))
        dealer_sum = sum_player_hand(dealer)
        print("The dealer now has {}".format(dealer_sum))
    if dealer_sum > 21:
        print("{} busted at {}!".format(dealer.name, sum_player_hand(dealer)))
        return 0
    else:
        print("Dealer stands at {}".format(dealer_sum))
        return dealer_sum


def compare_scores_against_dealer(players, dealer):
    winners = []
    tied_dealer = []
    losers = []
    for p in players:
        if p.score > dealer.score:
            winners.append(p)
        if p.score == dealer.score:
            tied_dealer.append(p)
        if p.score < dealer.score:
            losers.append(p)
    report = PlayerReport(win=winners, tie=tied_dealer, loss=losers)
    return report


def ui_results(report):
    print()
    print("Winners:")
    for p in report.win:
        print("* {}".format(p.name))
    print("Tied:")
    for p in report.tie:
        print("* {}".format(p.name))
    print("Losers:")
    for p in report.loss:
        print("* {}".format(p.name))


if __name__ == '__main__':
    game_loop()
