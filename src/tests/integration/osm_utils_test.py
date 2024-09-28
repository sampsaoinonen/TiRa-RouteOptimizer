import unittest
from unittest.mock import patch
from utils.osm_utils import get_nearest_node, download_osm_graph

class TestOsmUtils(unittest.TestCase):
    """Unit tests for OSM utilities including node retrieval and OSM graph download."""

    def setUp(self):
        """Downloads a real OSM graph for testing, specifically for Helsinki, Finland."""
        self.graph = download_osm_graph("Helsinki, Finland")

    def test_get_nearest_node_valid(self):
        """Tests get_nearest_node with valid coordinates in Helsinki."""
        lat, lon = 60.1699, 24.9384  # Valid coordinates in Helsinki
        nearest_node = get_nearest_node(self.graph, lat, lon)
        self.assertIsNotNone(nearest_node)
        self.assertIsInstance(nearest_node, int)

    def test_get_nearest_node_invalid(self):
        """Tests get_nearest_node with invalid coordinates (e.g., in the ocean)."""
        lat, lon = 0, 0  # Invalid coordinates
        nearest_node = get_nearest_node(self.graph, lat, lon)

        # Check that OSMnx still returns a valid node even with invalid coordinates
        self.assertIsNotNone(nearest_node)
        self.assertIsInstance(nearest_node, int)

if __name__ == '__main__':
    unittest.main()
