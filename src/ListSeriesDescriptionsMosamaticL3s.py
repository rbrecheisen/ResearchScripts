import os
import pydicom
import pydicom.errors

DATA_DIR = 'L:\\FHML_SURGERY\\Mosamatic\\Projects'


def load_dicom(f):
    try:
        p = pydicom.dcmread(f, stop_before_pixels=True)
        return p
    except pydicom.errors.InvalidDicomError:
        pass
    return None


def get_series_description(p):
    if 'SeriesDescription' in p:
        return p.SeriesDescription
    return None


def main():
    with open('series_descriptions.txt', 'w') as f_obj:
        for root, dirs, files in os.walk(DATA_DIR):
            for f in files:
                f_path = os.path.join(root, f)
                p = load_dicom(f_path)
                if p:
                    sd = get_series_description(p)
                    if sd:
                        x = f'{os.path.dirname(f_path)}/{f}: {sd}'
                        f_obj.write(x + '\n')
                        print(x)


if __name__ == '__main__':
    main()
