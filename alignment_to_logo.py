
from __future__ import annotations
import weblogo
import os

CLUSTER_ALIGNMENT_DIR = '/home/biswas.99/euk_styk_project/clusters/pro_x_pro_multiple_alignments'
LOGO_OUTPUT_DIR = '/home/biswas.99/euk_styk_project/clusters/pro_x_pro_logos'


def create_logo(alignment_file_name: str):
    with open(f'{CLUSTER_ALIGNMENT_DIR}/{alignment_file_name}', 'r', encoding='UTF-8') as alignment:
        seqs = weblogo.read_seq_data(alignment)
        logodata = weblogo.LogoData.from_seqs(seqs)
        logooptions = weblogo.LogoOptions()
        logooptions.logo_title = f'{alignment_file_name.split(sep="/")[-1][:-6]}'
        logoformat = weblogo.LogoFormat(logodata, logooptions)
        svg = weblogo.svg_formatter(logodata, logoformat)
        return svg


def main() -> None:
    alignments = os.listdir(CLUSTER_ALIGNMENT_DIR)
    for alignment in alignments:
        svg = create_logo(alignment)
        with open(f'{LOGO_OUTPUT_DIR}/{alignment.split(sep="/")[-1][:-6]}_logo.svg', 'wb') as logo:
            logo.write(svg)
    return None


if __name__ == "__main__":
    main()
