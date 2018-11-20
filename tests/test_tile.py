# -*- coding: utf-8 -*-
import json
import unittest
from py3dtiles import BoundingVolume, HelperTest, TileForReal


class Test_Tile(unittest.TestCase):

    def test_basics(self):
        helper = HelperTest(lambda x: TileForReal().validate(x))
        helper.sample_file_names.append(
                              'Tile_box_bounding_volume_sample.json')
        if not helper.check():
            self.fail()

    def build_sample(self):
        """
        Programmatically define a tile (which illustrates the API).
        """
        bv = BoundingVolume()
        bv.add_property_from_array('box',
                                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        tile = TileForReal()
        tile.set_bounding_volume(bv)
        tile.set_geometric_error(3.14159)
        return tile

    def test_json_encoding(self):
        self.build_sample().to_json()

    def test_build_sample_and_validate(self):
        if not self.build_sample().validate():
            self.fail()

if __name__ == "__main__":
    unittest.main()