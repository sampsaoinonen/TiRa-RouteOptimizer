import unittest
from utils.osm_utils import get_nearest_node, download_osm_graph
from unittest.mock import patch


class TestOsmUtils(unittest.TestCase):

    def setUp(self):
        # Download a real OSM graph for testing (e.g., Helsinki)
        self.graph = download_osm_graph("Helsinki, Finland")

    def test_get_nearest_node_valid(self):
        # Test with valid coordinates in Helsinki
        lat, lon = 60.1699, 24.9384  
        nearest_node = get_nearest_node(self.graph, lat, lon)
        self.assertIsNotNone(nearest_node)
        self.assertIsInstance(nearest_node, int)

    def test_get_nearest_node_invalid(self):
        # Test with invalid coordinates (in the ocean)
        lat, lon = 0, 0
        nearest_node = get_nearest_node(self.graph, lat, lon)

        # Check that OSMnx still returns a valid node
        self.assertIsNotNone(nearest_node)
        self.assertIsInstance(nearest_node, int)


if __name__ == '__main__':
    unittest.main()
