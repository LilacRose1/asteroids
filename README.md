# Asteroids

A Python recreation of the classic *Asteroids* arcade game, built with [Pygame](https://www.pygame.org/). This was a guided project from [Boot.dev](https://www.boot.dev), extended with a couple of small features of my own (asteroids splitting into smaller ones on impact and a lightweight game-state/event logger).

## Controls

| Key | Action |
|-----|--------|
| `W` | Thrust forward |
| `S` | Thrust backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Fire |
| Close window | Quit |

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recommended) — or `pip`

## Running it

With [uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
git clone https://github.com/LilacRose1/asteroids.git
cd asteroids
uv run main.py
```

`uv run` will create a virtual environment and install the pinned dependency (`pygame==2.6.1`) automatically from `pyproject.toml`/`uv.lock`.

Without `uv`, using a plain virtual environment:

```bash
git clone https://github.com/LilacRose1/asteroids.git
cd asteroids
python3 -m venv .venv
source .venv/bin/activate
pip install pygame==2.6.1
python main.py
```

## Credit

Built while following the [Boot.dev](https://www.boot.dev) "Build a Video Game" guided project.
