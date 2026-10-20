"""Fixtures and test selection for the publicly distributed observable-only package.

The original project has additional tests using an intentionally unpublished
synthetic design oracle. Public tests must not silently reconstruct that oracle.
"""

from pathlib import Path

import pytest

from economic_graph.simulator.design import load_design
from economic_graph.simulator.project import project_observations

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_DESIGN = ROOT / "design-data" / "restricted"


@pytest.fixture(scope="session")
def approved_design():
    if not (PRIVATE_DESIGN / "companies_world_design.json").is_file():
        pytest.skip("Requires private synthetic design oracle; omitted from public portfolio")
    return load_design(PRIVATE_DESIGN)


@pytest.fixture
def projection(approved_design):
    return project_observations(approved_design["observations"])


def pytest_collection_modifyitems(items):
    if PRIVATE_DESIGN.exists():
        return
    for item in items:
        node = item.nodeid.replace("\\", "/")
        if (
            node.startswith("tests/test_design.py::")
            or node.startswith("tests/test_public_export.py::")
            or "test_graph_commands.py::test_build_dry_run_does_not_invoke_writer" in node
            or "test_observable.py::test_reader_rejects_raw_design_file" in node
        ):
            item.add_marker(
                pytest.mark.skip(reason="Requires omitted private design data or private exporter")
            )
