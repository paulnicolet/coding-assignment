from pathlib import Path

from src.loader import ScenarioLoader
from src.database import Database

SCENARIOS_PATH = Path('.') / 'data' / 'scenarios'


def run(scenario_id):
    loader = ScenarioLoader(SCENARIOS_PATH, scenario_id)

    db = Database(loader.graph_root)
    db.add_nodes(loader.graph_tail)
    db.add_extract(loader.extract)
    db.add_nodes(loader.graph_edits)

    status = db.get_extract_status()

    print(status)


if __name__ == "__main__":
    run(1)
