try:
    from generator.recipe import Recipe
except ImportError:
    from flowcraft.generator.recipe import Recipe


class Denim(Recipe):
    """

    """

    def __init__(self):

        self.name = "denim"

        self.pipeline_str = "integrity_coverage " \
                            "fastqc_trimmomatic " \
                            "filter_poly " \
                            "remove_host " \
                            "bowtie " \
                            "retrieve_mapped " \
                            "viral_assembly " \
                            "assembly_mapping " \
                            "pilon " \
                            "split_assembly " \
                            "(dengue_typing | mafft raxml)"

        # Recipe parameters and directives
        self.directives = {
            "integrity_coverage": {
                "params": {"genomeSize": "0.012", "minCoverage": "15"}
            },
            "bowtie":{
                "directives": {"container": "flowcraft/bowtie_dengue", "version": "2-1"},
                "pararm": {"reference": "'/ref/1_GenotypesDENV_14-05-18.fasta'"}
            },
            "assembly_mapping": {
                "param": {"AMaxContigs": "1000", "genomeSize": "0.01"}
            },
            "split_assembly": {
                "param": {"size": "10000"}
            }
        }