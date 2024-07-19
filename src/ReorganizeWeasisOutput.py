import os
import shutil
import pydicom
import pydicom.errors

ROOTDIR = "D:\\Mosamatic\\ChenFei_LUNG3\\Output"
OUTPUTDIR = "D:\\Mosamatic\\ChenFei_LUNG3\\OutputReorg"


def is_dicom_file(dicom_file_path):
    try:
        if os.path.isfile(dicom_file_path):
            if os.path.split(dicom_file_path)[1] != 'DICOMDIR':
                pydicom.dcmread(dicom_file_path, stop_before_pixels=True)
                return True
        return False
    except pydicom.errors.InvalidDicomError:
        return False


def main():

    os.makedirs(OUTPUTDIR, exist_ok=False)
    
    for subject_dir_name in os.listdir(ROOTDIR):
        subject_dir_path = os.path.join(ROOTDIR, subject_dir_name)
        for root, dirs, files in os.walk(subject_dir_path):
            for dicom_file_name in files:
                dicom_file_path = os.path.join(root, dicom_file_name)
                if is_dicom_file(dicom_file_path):
                    output_dicom_file_path = os.path.join(OUTPUTDIR, subject_dir_name + '.dcm')
                    shutil.copyfile(dicom_file_path, output_dicom_file_path)
                    print(subject_dir_name)


if __name__ == '__main__':
    main()
