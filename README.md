# MT5 Flask Backend API

This API bridges your Flutter app and MT5 trading EA.

## Endpoints
- `/` – Check API status
- `/account` – Account info
- `/positions` – Open trades
- `/orders` – Pending trades
- `/symbols` – Visible symbols
- `/trade` – Save trade instructions
- `/toggle-ea` – Turn EA on/off
- `/status` – Get EA status

## Setup
```bash
pip install -r requirements.txt
python3 server.py
