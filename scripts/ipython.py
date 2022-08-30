#!/usr/bin/env python3
from bleanser.core.sqlite import SqliteNormaliser, Tool


class Normaliser(SqliteNormaliser):
    MULTIWAY = True
    PRUNE_DOMINATED = True

    def check(self, c) -> None:
        tables = Tool(c).get_tables()
        assert "history" in tables, tables
        assert "sessions" in tables, tables

    def cleanup(self, c) -> None:
        self.check(c)


if __name__ == "__main__":
    Normaliser.main()
