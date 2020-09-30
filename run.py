from pathlib import Path

from src.loader import ScenarioLoader

scenario_path = Path('.') / 'data' / 'scenarios'

loader = ScenarioLoader(scenario_path, 1)

print(loader.graph_tail)
