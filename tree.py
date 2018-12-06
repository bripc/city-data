class Tree:

    def __init__(self, props, geometry):
        self.address = str.join(' ', ((props['ADDRESS_NUMBER'] or ''), (props['STREET'] or ''), 'SACRAMENTO, CA'))
        self.species = props['SPECIES']
        self.botanical = props['BOTANICAL']
        self.geometry = geometry

    def __repr__(self):
        return "<Tree species:%s, botanical:%s, address:%s>" % (self.species, self.botanical, self.address)

    def __str__(self):
        return "<Tree species:%s, botanical:%s, address:%s>" % (self.species, self.botanical, self.address)


