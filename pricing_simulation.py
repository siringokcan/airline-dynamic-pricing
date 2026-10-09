"""Illustrative airline ticket pricing simulation (synthetic parameters)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

BASE_PRICE = 1000.0
TOTAL_DAYS = 30
CAPACITY = 180
TIME_EFFECT = 500.0
SEAT_EFFECT = 800.0


def ticket_price(days_left: int, empty_seats: int) -> float:
    """Compute illustrative price; days and seats must be in valid ranges."""
    if not 0 <= days_left <= TOTAL_DAYS:
        raise ValueError(f'days_left must be between 0 and {TOTAL_DAYS}')
    if not 0 <= empty_seats <= CAPACITY:
        raise ValueError(f'empty_seats must be between 0 and {CAPACITY}')
    return round(BASE_PRICE + TIME_EFFECT * (1 - days_left / TOTAL_DAYS)
                 + SEAT_EFFECT * (1 - empty_seats / CAPACITY), 2)


def main():
    scenarios = [(30, 180), (20, 140), (10, 80), (3, 20)]
    print('Illustrative airline ticket prices (TRY):')
    for days, seats in scenarios:
        print(f'Days left: {days:2d} | Empty seats: {seats:3d} | Price: {ticket_price(days, seats):.2f} TRY')

    output = Path(__file__).resolve().parent / 'figures'
    output.mkdir(exist_ok=True)

    days = list(range(TOTAL_DAYS + 1))
    plt.figure(figsize=(8, 5))
    plt.plot(days, [ticket_price(day, 90) for day in days])
    plt.xlabel('Days remaining until departure')
    plt.ylabel('Ticket price (TRY)')
    plt.title('Price vs. Time (90 Empty Seats)')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(output / 'price_vs_time.png', dpi=160)
    plt.close()

    seats = list(range(CAPACITY + 1))
    plt.figure(figsize=(8, 5))
    plt.plot(seats, [ticket_price(10, seat) for seat in seats])
    plt.xlabel('Empty seats')
    plt.ylabel('Ticket price (TRY)')
    plt.title('Price vs. Seat Availability (10 Days Left)')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(output / 'price_vs_seats.png', dpi=160)
    plt.close()
    print('Saved two plots to figures/.')


if __name__ == '__main__':
    main()
