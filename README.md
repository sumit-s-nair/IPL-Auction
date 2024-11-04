# IPL Auction Program

## Overview
The **IPL Auction Program** simulates or manages the auction process for the Indian Premier League (IPL). It allows users to bid for players, manage teams, and track budgets, providing a detailed breakdown of the entire auction process.

## Features
- Auction simulation for IPL players.
- Bid tracking for each team.
- Team budget management.
- Database support for player information and auction results.
- (Add any other relevant features here)

## Prerequisites
Before running the program, ensure you have the following installed:

- Python 3.x
- Required Python modules (listed in `requirements.txt` or as follows):
  - `sqlite3` (for database management)
  - `custom tkinter`(for ui)

To install the necessary dependencies, you can run:
```bash
pip install -r requirements.txt
```

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/sumit-s-nair/IPL-Auction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd IPL-Auction
   cd ipl-auction
   ```

3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the `ipl_auction.py` file to start the program:
   ```bash
   python ipl_auction.py
   ```

2. Follow the on-screen instructions to simulate the auction process or manage an auction event.

3. If the program uses a database (`ipl_auction.db`), ensure that it is correctly placed in the working directory.

## Program Structure
- `ipl_auction.py`: Main Python script that runs the auction simulation.
- `ipl_auction.db`: (If applicable) SQLite database containing player information and auction data.
- Other assets or resources such as images, data files, or configs should be placed in their respective folders.

## Future Improvements
- Integrate real-time bidding using web sockets.
- Add player stats and team history.
- Improve error handling and input validation.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.
