'''
Abstraction for Sacramento's tree data

Tree.geometry will be used in future development to map trees
'''
class Tree:

    def __init__(self, props, geometry):
        self.address = str.join(' ', ((props['ADDRESS_NUMBER'] or ''), (props['STREET'] or ''), 'SACRAMENTO, CA'))
        self.common_name = props['SPECIES'] or ''
        self.scientific_name = props['BOTANICAL'] or ''
        self.geometry = geometry
        self.is_native = None

    # format scientific name for easier comparison to flora database
    def get_scientific_name(self):
        return self.scientific_name.lower().replace('.', '').rstrip(' spp')

    def set_native(self, native):
        self.is_native = native

    # pretty print tree objects for debugging
    def __repr__(self):
        return "<Tree common_name:%s, scientific_name:%s, address:%s>" % (self.common_name, self.scientific_name, self.address)

    def __str__(self):
        return "<Tree common_name:%s, scientific_name:%s, address:%s>" % (self.common_name, self.scientific_name, self.address)



