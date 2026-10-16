import sys

sys.dont_write_bytecode = True

# Este sistema es el sistema tradicional usando herencia de los 90s

if __name__ == "__main__":
    from src.engine.game_engine import GameEngine

    engine = GameEngine()
    engine.run()
