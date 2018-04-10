from .base import SectionBase

class ResourcesSection(SectionBase):
    def __init__(self, cpus=None, mem=None, tpus=0, gpus=0):
        self.cpus = cpus
        self.mem = mem
        self.gpus = gpus
        self.tpus = tpus