from sqlite3 import Connection

from bleanser.core.sqlite import SqliteNormaliser, Tool


class Normaliser(SqliteNormaliser):
    MULTIWAY = True
    PRUNE_DOMINATED = True

    def check(self, c: Connection) -> None:
        tables = Tool(c).get_tables()
        assert "history" in tables, tables
        assert "sessions" in tables, tables

    def cleanup(self, c: Connection) -> None:
        self.check(c)


if __name__ == "__main__":
    Normaliser.main()
