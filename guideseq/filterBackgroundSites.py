import subprocess
import os


def filterBackgroundSites(bedtools_path, sample_path, control_path, outfile):
    bedtools_filter_command = '{0} intersect -a {1} -b {2}'.format(bedtools_path, sample_path, control_path)

    with open(outfile, 'w') as outfile:
        subprocess.call(bedtools_filter_command.split(), stdout=outfile)
