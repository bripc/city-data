import csv

import config
import util


def classify_as_native(urban_forest, ca_native_flora):
    total_native = 0
    total_nonnative = 0
    total_unclassified = 0
    with open(config.LOCAL_PATH + '/output/classified_trees.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar="'", quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['common_name', 'scientific_name', 'flora_matched', 'address', 'is_native'])
        for tree in urban_forest:
            if tree.scientific_name == '':
                total_unclassified += 1
                continue
            native_flora_found = util.binary_search(ca_native_flora, tree.get_scientific_name())
            if native_flora_found:
                tree.set_native(True)
                total_native += 1
            else:
                tree.set_native(False)
                total_nonnative += 1
            filewriter.writerow([tree.common_name, tree.scientific_name, native_flora_found, tree.address, tree.is_native])
    total_trees = len(urban_forest) - total_unclassified
    print('-'*80)
    print('Native:', total_native)
    print('Non-native:', total_nonnative)
    print('Total classified trees:', total_trees)
    print('Unclassified trees:', total_unclassified)
    percNative = float("{0:.2f}".format((total_native / total_trees) * 100))
    print('% total that are native:', percNative, '%')
