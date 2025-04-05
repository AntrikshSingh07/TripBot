
# TripBot

TripBot is a simple and efficient Discord bot that helps manage shared expenses during group trips. With real-time tracking of transactions and a built-in optimized settlement algorithm, TripBot eliminates the stress of post-trip calculations.

## Features

- Add friends to the trip list
- Record payments for individuals or for everyone
- List all added trip members
- View the optimal settlement with minimum number of transactions
- Private help support and commands via DM

## How It Works

1. **Add members:** Users are added to the trip list via commands.
2. **Record expenses:** Payments are logged, dividing amounts between recipients.
3. **Balance settlement:** The bot calculates minimal transactions to settle all debts using a greedy approach.

## Commands

| Command | Description |
|--------|-------------|
| `!add[name]` | Adds a user to the trip. |
| `!list` | Lists all added members. |
| `!paid[name,person1,person2,...,amount]` | Logs a payment from `name` to listed persons. |
| `!paid[name,everyone,amount]` | Logs a payment made for everyone in the trip. |
| `!balance` | Displays the optimized transaction settlement. |
| `!help` | Displays usage guide. |
| `?!command` | Sends the bot response to your DM instead of the channel. |

### Example

```bash
!addAlice
!addBob
!addCharlie
!paidAlice,Bob,Charlie,120
!paidBob,everyone,60
!balance
```

Expected output:
```
Bob pays Alice 40
Charlie pays Alice 40
```

## Installation

### Requirements

- Python 3.8+
- `discord.py`
- `python-dotenv`

### Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/TripBot.git
cd TripBot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Discord bot token:

```env
DISCORD_TOKEN=your_token_here
```

4. Run the bot:

```bash
python main.py
```

