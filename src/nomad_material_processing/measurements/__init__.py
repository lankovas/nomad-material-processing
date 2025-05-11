from nomad.config.models.plugins import SchemaPackageEntryPoint


class MRO005SchemaPackageEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_material_processing.measurements.MRO005 import m_package

        return m_package


schema = MRO005SchemaPackageEntryPoint(
    name='experiment MRO005 schema',
    description='Schema tailored for experimnet MRO005.',
)