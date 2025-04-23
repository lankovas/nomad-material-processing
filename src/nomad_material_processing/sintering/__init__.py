from nomad.config.models.plugins import SchemaPackageEntryPoint


class SinteringSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_material_processing.sintering.sintering import m_package

        return m_package


schema = SinteringSchemaPackageEntryPoint(
    name='Sintering Schema',
    description='Schema package containing classes for sintering from Tutorial 13.',
)