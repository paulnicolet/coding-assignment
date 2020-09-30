import json

EXPECTED_STATUS_FNAME = 'expected_status.json'
GRAPH_BUILD_FNAME = 'graph_build.json'
GRAPH_EDITS_FNAME = 'graph_edits.json'
EXTRACT_FNAME = 'img_extract.json'


class ScenarioLoader(object):

    def __init__(self, base_path, scenario_id):
        """Load scenario files and init scenario.
        The directory structure should look like this:
        base_path/
            1/
                expected_status.json
                graph_build.json
                graph_edits.json
                img_extract.json
            2/ ...
            3/ ...

        Args:
            base_path (Path): A pathlib path representing the root of scenarios.
            scenario_id (int): A scenario id.
        """
        paths = self._get_paths(base_path, scenario_id)
        attrs = ['_expected_status', '_graph_build',
                 '_graph_edits', '_extract']

        for path, attr in zip(paths, attrs):
            with path.open() as f:
                setattr(self, attr, json.load(f))

    @property
    def graph_root(self):
        """Returns the graph root name.

        Returns:
            str: The graph root name.
        """
        return self._graph_build[0][0]

    @property
    def graph_tail(self):
        """Returns the graph build tail, i.e. everything except the root.

        Returns:
            List[Tuple[str, str]]: The graph build tail.
        """
        return self._graph_build[1:]

    @property
    def expected_status(self):
        """Returns the expected extract status.

        Returns:
            Dict[str, str]: The expected extract status.
        """
        return self._expected_status

    @property
    def extract(self):
        """Returns the extract.

        Returns:
            Dict[str, List[str]]: The scenario extract.
        """
        return self._extract

    def _get_paths(self, base_path, scenario_id):
        """Get the scenario resource paths.

        Args:
            base_path (Path): The base pathlib path.
            scenario_id (int): The scenario id.

        Raises:
            ValueError: If paths does not exists.

        Returns:
            Tuple[Path, Path, Path, Path]: The status path, build path, 
            edits path and extract path in this order.
        """
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
