import json

EXPECTED_STATUS_FNAME = 'expected_status.json'
GRAPH_BUILD_FNAME = 'graph_build.json'
GRAPH_EDITS_FNAME = 'graph_edits.json'
EXTRACT_FNAME = 'img_extract.json'


class ScenarioLoader(object):

    def __init__(self, base_path, scenario_id):
        paths = self._get_paths(base_path, scenario_id)
        attrs = ['_expected_status', '_graph_build',
                 '_graph_edits', '_extract']

        for path, attr in zip(paths, attrs):
            with path.open() as f:
                setattr(self, attr, json.load(f))

    @property
    def graph_root(self):
        return self._graph_build[0][0]

    @property
    def graph_tail(self):
        return self._graph_build[1:]

    @property
    def expected_status(self):
        return self._expected_status

    @property
    def extract(self):
        return self._extract

    def _get_paths(self, base_path, scenario_id):
        path = base_path / str(scenario_id)

        if not path.exists() or not path.is_dir():
            raise ValueError('Invalid path and scenario id')

        status_path = path / EXPECTED_STATUS_FNAME
        build_path = path / GRAPH_BUILD_FNAME
        edits_path = path / GRAPH_EDITS_FNAME
        extract_path = path / EXTRACT_FNAME

        for path in [status_path, build_path, edits_path, extract_path]:
            if not path.exists():
                raise ValueError('Scenario directory must contain the 4 files')

        return status_path, build_path, edits_path, extract_path
