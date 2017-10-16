import os
import yaml
import datetime
import locus_processing
from snakemake import WorkflowError

# yaml representer for dumping config
from yaml.representer import Representer
import collections

class PipeHelper(object):
    def __init__(self, config, workflow_name=""):
        self._config = config
        self._workflow_name = workflow_name
        self._locus = None
        
        self._barcode_ids = yaml.load(config.get("BARCODE_IDS", "[]"))
        
        try:
            with open(config["BARCODES"], "r") as bc_file:
                self._all_barcodes = [line.strip()[1:] for line in bc_file if line.startswith(">")]
        except KeyError:
            self._all_barcodes = []
            #raise WorkflowError("Barcode file not specified")
        except IOError:
            raise WorkflowError("Could not load barcodes")
        
        if len(self._barcode_ids) and len(self._all_barcodes):
            assert all((x in self._all_barcodes for x in self._barcode_ids)), "barcode id not in barcode file"
        
        if len(self._barcode_ids) == 0:
            if len(self._all_barcodes) > 0:
                self._barcode_ids = self._all_barcodes
            else:
                raise WorkflowError("No valid barcodes provided")

    # handlers for workflow exit status
    def onsuccess(self):
        print("{} workflow completed successfully".format(self._workflow_name))
        yaml.add_representer(collections.OrderedDict, Representer.represent_dict)
        config_file = "config.{}.yaml".format("{:%Y-%m-%d_%H:%M:%S}".format(datetime.datetime.now()))
        with open(config_file, "w") as outfile:
            print(yaml.dump(self._config, default_flow_style=False), file=outfile)
    
    def onerror(self):
        print("Error encountered while executing workflow")
        shell("cat {log}")
  
    @property
    def barcode_ids(self):
        return self._barcode_ids

    def barcode_index(self, barcode_id):
        return self._all_barcodes.index(barcode_id)
    
    @property
    def loci(self):
        return self._config.get("LOCI", [])

    @property
    def outputs(self):
        raise NotImplementedError
   

