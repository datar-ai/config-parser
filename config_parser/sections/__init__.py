from .deploy import DeploySection
from .train import TrainSection
from .repository import RepositoryConfig
from .resources import ResourcesSection

__all__ = ['RepositoryConfig', 'DeploySection', 'TrainSection', 'job_section_classes', 'get_job_section',
           'ResourcesSection' ]


def get_job_section(kind):
    return job_section_classes.get(kind)

job_section_classes = {
    'deploy': DeploySection,
    'train': TrainSection
}