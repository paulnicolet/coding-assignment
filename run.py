import argparse
from pathlib import Path

from src.database import Database
from src.eval import accuracy
from src.loader import ScenarioLoader

DEFAULT_SCENARIO = 3
SCENARIOS_PATH = Path('.') / 'data' / 'scenarios'


def run(scenario_id):
    # Load scenario
    loader = ScenarioLoader(SCENARIOS_PATH, scenario_id)

    # Execute database operations
    db = Database(loader.graph_root)
    db.add_nodes(loader.graph_tail)
    db.add_extract(loader.extract)
    db.add_nodes(loader.graph_edits)

    # Get result
    status = db.get_extract_status()
    acc = accuracy(loader.expected_status, status)
    print(f'Accuracy for scenario {scenario_id}: {acc}')


def _parse_scenario_id():
    parser = argparse.ArgumentParser(
        description='Foodvisor dynamic class structure'
    )

    parser.add_argument(
        '-sid',
        '--scenario_id',
        type=int,
        required=False,
        default=DEFAULT_SCENARIO,
        help=f'The scenario id to execute. Resources must be available under {SCENARIOS_PATH}'
    )

    return parser.parse_args().scenario_id


if __name__ == "__main__":
    run(_parse_scenario_id())
