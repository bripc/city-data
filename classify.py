import csv

import config
import util


def classify_as_native(urban_forest, ca_native_flora):
    total_native = 0
    total_nonnative = 0
    with open(config.LOCAL_PATH + '/output/classified_trees.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar="'", quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['common_name', 'scientific_name', 'flora_matched', 'address', 'is_native'])
        for tree in urban_forest:
            native_flora_found = util.binary_search(ca_native_flora, tree.get_scientific_name())
            if native_flora_found:
                tree.set_native(True)
                total_native += 1
            else:
                tree.set_native(False)
                total_nonnative += 1
            filewriter.writerow([tree.common_name, tree.scientific_name, native_flora_found, tree.address, tree.is_native])
        print("Trees:", len(urban_forest), "Native:", total_native, "Non-native:", total_nonnative,
              "% native:", (total_native / len(urban_forest)) * 100)
