import sys

sys.dont_write_bytecode = True

# Este sistema es muy parecido a comp funciona un
# motor de juegos como Unity o Unreal

if __name__ == "__main__":
    from src.engine.game_engine import GameEngine

    engine = GameEngine()
    engine.run()
