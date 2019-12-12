nmr_assay_MTBLS_dict = OrderedDict([
    ('measurement_type', OntologyAnnotation(term='metabolite profiling')),
    ('technology_type', OntologyAnnotation(term='nmr spectroscopy')),
            ('extraction', {}),
            ('extract', [
                {
                    'node_type': EXTRACT,
                    'characteristics_category':  OntologyAnnotation(term='extract type'),
                    'characteristics_value': OntologyAnnotation(term='supernatant'),
                    'size': 1,
                    'technical_replicates': None,
                    'is_input_to_next_protocols': True
                },
                {
                    'node_type': EXTRACT,
                    'characteristics_category':  OntologyAnnotation(term='extract type'),
                    'characteristics_value': OntologyAnnotation(term='pellet'),
                    'size': 1,
                    'technical_replicates': None,
                    'is_input_to_next_protocols': True
                }
            ]),
            ('nmr_spectroscopy', {
                OntologyAnnotation(term='Instrument'): [OntologyAnnotation(term='1.7 mm SampleJet')],
                OntologyAnnotation(term='Instrument'): [OntologyAnnotation(term='Bruker AvanceII 1 GHz')],
                OntologyAnnotation(term='Solvent'): [OntologyAnnotation(term='0.05 mM phosphate buffered D2O'),OntologyAnnotation(term='0.01 M phosphate buffered D2O')],
                OntologyAnnotation(term='Acquisition mode'): [OntologyAnnotation(term='1D 13C NMR')],
                OntologyAnnotation(term='NMR Probe'): [OntologyAnnotation(term='CPMG'),OntologyAnnotation(term='1.7 mm CPTCI 1H-13C/15N/D Z-GRD')],
                OntologyAnnotation(term='Pulse sequence name'): [OntologyAnnotation(term='CPMG'),OntologyAnnotation(term='1D 1H spectrum (zg)')],
                OntologyAnnotation(term='Magnetic field strength'): [OntologyAnnotation(term="400 Mhz"), OntologyAnnotation(term='600 MHz')]
                OntologyAnnotation(term='Pulse sequence name'): [OntologyAnnotation(term='CPMG'),OntologyAnnotation(term='1D 1H spectrum (zg)')]
            }),
            ('raw_spectral_data_file', [
                {
                    'node_type': DATA_FILE,
                    'size': 1,
                    'technical_replicates': 2,
                    'is_input_to_next_protocols': False
                }
            ])
        ])